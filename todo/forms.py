from django import forms
from .models import Task, Category
from django.contrib.auth.models import User


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'category', 'priority', 'status', 'due_date']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Enter task title...',
                'class': 'form-control'
            }),
            'description': forms.Textarea(attrs={
                'id': 'task-description-editor',
                'placeholder': 'Enter task description...',
                'class': 'form-control'
            }),
            'due_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'priority': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }
        
    def __init__(self, *args, **kwargs):
        # Get the user from the kwargs
        user = kwargs.pop('user', None)
        super(TaskForm, self).__init__(*args, **kwargs)
        if user:
            # Filter the category queryset to only show categories belonging to the current user
            self.fields['category'].queryset = Category.objects.filter(user=user)
            self.fields['category'].empty_label = "No Category"


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'color']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'e.g., Work, Personal, Health',
                'class': 'form-control'
            }),
            'color': forms.TextInput(attrs={
                'type': 'color',
                'class': 'form-control'
            }),
        }


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


# Removed: Profile, RegistrationForm (auth handled by another app)