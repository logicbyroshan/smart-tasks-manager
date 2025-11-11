# todo/context_processors.py
from .forms import TaskForm

def add_task_form_to_context(request):
    """
    Makes the TaskForm available in the context of every template,
    but only if the user is logged in.
    """
    if request.user.is_authenticated:
        # We must pass the user to the form so it can filter categories correctly
        form = TaskForm(user=request.user)
        return {'task_create_form': form}
    return {}