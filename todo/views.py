# ----------------- Django Core Imports -----------------
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import JsonResponse

# ----------------- Django Contrib Imports -----------------
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# ----------------- Database and Querying Imports -----------------
from django.db.models import Count, Q

# ----------------- Local Application Imports -----------------
from .models import Task, Category
from .forms import TaskForm, CategoryForm, UserUpdateForm


# ==============================================================================
#  CORE PAGE VIEWS
# ==============================================================================

@login_required
def dashboard(request):
    """
    Displays the main dashboard for an authenticated user.
    It gathers various statistics (task counts) and lists of recent tasks
    to provide a summary of the user's activity.
    """
    tasks = Task.objects.filter(user=request.user)

    # Calculate counts for the "Task Status" overview card
    completed_count = tasks.filter(status='completed').count()
    in_progress_count = tasks.filter(status='in-progress').count()
    not_started_count = tasks.filter(status='not-started').count()

    # Get the 5 most recent tasks that are not yet completed
    recent_tasks = tasks.exclude(status='completed').order_by('-created_at')[:5]

    # Get the 3 most recently completed tasks
    recently_completed_tasks = tasks.filter(status='completed').order_by('-completed_at')[:3]

    context = {
        'completed_count': completed_count,
        'in_progress_count': in_progress_count,
        'not_started_count': not_started_count,
        'recent_tasks': recent_tasks,
        'recently_completed_tasks': recently_completed_tasks,
        'active_page': 'dashboard',
    }
    return render(request, 'todo/index.html', context)


@login_required
def my_tasks(request):
    """
    Displays a grid of all tasks belonging to the current user.
    This view provides a comprehensive list for managing all tasks.
    """
    tasks = Task.objects.filter(user=request.user).order_by('-created_at')
    context = {
        'tasks': tasks,
        'active_page': 'my_tasks',
    }
    return render(request, 'todo/my-tasks.html', context)


@login_required
def task_categories(request):
    """
    Displays all categories created by the user.
    It calculates and shows the total task count and completion percentage for each category.
    Also provides a form for creating a new category (used in a modal).
    """
    categories = Category.objects.filter(user=request.user).annotate(
        task_count=Count('tasks'),
        completed_count=Count('tasks', filter=Q(tasks__status='completed'))
    )

    # Calculate progress percentage in the view for clarity
    for category in categories:
        if category.task_count > 0:
            category.progress = int((category.completed_count / category.task_count) * 100)
        else:
            category.progress = 0
            
    form = CategoryForm()
    context = {
        'categories': categories,
        'form': form,
        'active_page': 'task_categories',
    }
    return render(request, 'todo/task-categories.html', context)


@login_required
def settings_page(request):
    """
    Handles the user settings page for profile updates only.
    Password change removed as auth will be handled by another app.
    """
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('settings')

    # For GET requests
    u_form = UserUpdateForm(instance=request.user)

    context = {
        'active_page': 'settings',
        'u_form': u_form,
    }
    return render(request, 'todo/settings.html', context)


# ==============================================================================
#  TASK CRUD (Create, Read, Update, Delete) VIEWS
# ==============================================================================

@login_required
def task_detail(request, pk):
    """
    Displays full task details on a dedicated page.
    Shows all task information including rich text description.
    """
    task = get_object_or_404(Task, pk=pk, user=request.user)
    context = {
        'task': task,
        'active_page': 'my_tasks',
    }
    return render(request, 'todo/task_detail.html', context)


@login_required
def task_create(request):
    """
    Handles the creation of a new task via an AJAX POST request from a modal.
    Returns a JSON response indicating success or failure.
    """
    # This view should only accept POST requests now
    if request.method == 'POST':
        form = TaskForm(request.POST, user=request.user)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return JsonResponse({'success': True, 'message': 'Task created successfully!'})
        else:
            # If the form is invalid, return the errors as JSON
            return JsonResponse({'success': False, 'errors': form.errors})
    
    # If it's a GET request, it's not a valid way to use this endpoint anymore
    return JsonResponse({'success': False, 'message': 'Invalid request method.'}, status=405)


@login_required
def task_update(request, pk):
    """
    Handles updating an existing task via AJAX POST request.
    Returns a JSON response indicating success or failure.
    """
    task = get_object_or_404(Task, pk=pk, user=request.user)
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task, user=request.user)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'message': 'Task updated successfully!'})
        else:
            # If the form is invalid, return the errors as JSON
            return JsonResponse({'success': False, 'errors': form.errors})
    
    # If it's a GET request, return task data as JSON for populating the edit form
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        task_data = {
            'title': task.title,
            'description': task.description,
            'category': task.category.id if task.category else '',
            'priority': task.priority,
            'status': task.status,
            'due_date': task.due_date.strftime('%Y-%m-%d') if task.due_date else '',
        }
        return JsonResponse({'success': True, 'task': task_data})
    
    # Fallback for non-AJAX GET requests
    return JsonResponse({'success': False, 'message': 'Invalid request method.'}, status=405)


@login_required
def task_delete(request, pk):
    """
    Handles the deletion of a task.
    On GET, it shows a confirmation page.
    On POST, it deletes the task and redirects to the task list.
    """
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        task_title = task.title
        task.delete()
        messages.success(request, f'Task "{task_title}" has been deleted.')
        return redirect('my_tasks')
        
    return render(request, 'todo/confirm_delete.html', {'object': task})


# ==============================================================================
#  CATEGORY CRUD (Create, Read, Update, Delete) VIEWS
# ==============================================================================

@login_required
def category_create(request):
    """
    Handles the creation of a new category via a POST request,
    typically from a modal form. Redirects back to the categories page.
    """
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            messages.success(request, f'Category "{category.name}" created.')
    
    return redirect('task_categories')


@login_required
def category_update(request, pk):
    """
    Handles updating an existing category via a POST request.
    This would be used if you implement an "edit category" modal.
    """
    category = get_object_or_404(Category, pk=pk, user=request.user)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, f'Category "{category.name}" updated.')
            
    return redirect('task_categories')


@login_required
def category_delete(request, pk):
    """
    Handles the deletion of a category.
    It's recommended to handle this with a POST request for security.
    """
    category = get_object_or_404(Category, pk=pk, user=request.user)
    if request.method == 'POST':
        category_name = category.name
        category.delete()
        messages.success(request, f'Category "{category_name}" has been deleted.')
        return redirect('task_categories')
        
    return render(request, 'todo/confirm_delete.html', {'object': category})