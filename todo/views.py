# ----------------- Django Core Imports -----------------
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

# ----------------- Django Contrib Imports -----------------
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm,  PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

# ----------------- Database and Querying Imports -----------------
from django.db.models import Count, Q

# ----------------- Local Application Imports -----------------
from .models import Task, Category
from .forms import (
    TaskForm, 
    CategoryForm, 
    RegistrationForm, 
    UserUpdateForm, 
    ProfileUpdateForm
)


# ==============================================================================
#  LANDING PAGE & AUTHENTICATION VIEWS
# ==============================================================================

def landing_page_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'todo/landing.html')


def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('dashboard')
    else:
        form = RegistrationForm()
        
    return render(request, 'todo/register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()

    return render(request, 'todo/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


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
def vital_tasks(request):
    """
    Displays tasks that are marked with 'High' priority and are not yet completed.
    This helps the user focus on their most critical to-dos.
    """
    vital_tasks = Task.objects.filter(
        user=request.user, 
        priority='high'
    ).exclude(status='completed').order_by('due_date')

    context = {
        'vital_tasks': vital_tasks,
        'active_page': 'vital_tasks',
    }
    return render(request, 'todo/vital-task.html', context)


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
    Handles the user settings page, which now manages two separate forms:
    1. Profile/User information update.
    2. Password change.
    """
    if request.method == 'POST':
        # Check which form was submitted by looking at the submit button's name
        if 'update_profile' in request.POST:
            u_form = UserUpdateForm(request.POST, instance=request.user)
            p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
            if u_form.is_valid() and p_form.is_valid():
                u_form.save()
                p_form.save()
                messages.success(request, 'Your profile has been updated successfully!')
                return redirect('settings')
        
        elif 'change_password' in request.POST:
            pass_form = PasswordChangeForm(request.user, request.POST)
            if pass_form.is_valid():
                user = pass_form.save()
                # IMPORTANT: This keeps the user logged in after changing their password.
                update_session_auth_hash(request, user)
                messages.success(request, 'Your password was successfully updated!')
                return redirect('settings')
            else:
                # If the password form has errors, we need to re-instantiate the other forms
                # so the page can render correctly with the password errors.
                u_form = UserUpdateForm(instance=request.user)
                p_form = ProfileUpdateForm(instance=request.user.profile)
                context = {'active_page': 'settings', 'u_form': u_form, 'p_form': p_form, 'pass_form': pass_form}
                return render(request, 'todo/settings.html', context)

    # For GET requests, instantiate all forms
    u_form = UserUpdateForm(instance=request.user)
    p_form = ProfileUpdateForm(instance=request.user.profile)
    pass_form = PasswordChangeForm(request.user)

    context = {
        'active_page': 'settings',
        'u_form': u_form,
        'p_form': p_form,
        'pass_form': pass_form  # Add the password form to the context
    }
    return render(request, 'todo/settings.html', context)

@login_required
def help_page(request):
    """
    Renders the static 'Help & Support' page.
    """
    context = {'active_page': 'help'}
    return render(request, 'todo/help.html', context)


# ==============================================================================
#  TASK CRUD (Create, Read, Update, Delete) VIEWS
# ==============================================================================

@login_required
def task_detail(request, pk):
    """
    Fetches details for a single task.
    This view is intended to be used by an AJAX/Fetch call to populate a modal
    with task details without a full page reload.
    """
    task = get_object_or_404(Task, pk=pk, user=request.user)
    # This renders a small HTML snippet, not a full page.
    return render(request, 'todo/partials/task_detail_modal.html', {'task': task})


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
    Handles updating an existing task.
    Finds the task by its primary key (pk) and renders a pre-filled form on GET.
    Processes the submitted form on POST.
    """
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, f'Task "{task.title}" updated successfully!')
            return redirect('my_tasks')
    else:
        form = TaskForm(instance=task, user=request.user)
        
    return render(request, 'todo/task_form.html', {'form': form, 'title': 'Update Task'})


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