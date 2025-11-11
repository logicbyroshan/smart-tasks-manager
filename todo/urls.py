from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.landing_page_view, name='landing'),
    # Page Views
    path('dashboard/', views.dashboard, name='dashboard'),
    path('my-tasks/', views.my_tasks, name='my_tasks'),
    path('vital-tasks/', views.vital_tasks, name='vital_tasks'),
    path('categories/', views.task_categories, name='task_categories'),
    path('settings/', views.settings_page, name='settings'),
    path('help/', views.help_page, name='help'),
    
    # Task CRUD
    path('task/<int:pk>/', views.task_detail, name='task_detail'),
    path('task/create/', views.task_create, name='task_create'),
    path('task/<int:pk>/update/', views.task_update, name='task_update'),
    path('task/<int:pk>/delete/', views.task_delete, name='task_delete'),
    
    # Category CRUD
    path('category/create/', views.category_create, name='category_create'),
    path('category/<int:pk>/update/', views.category_update, name='category_update'),
    path('category/<int:pk>/delete/', views.category_delete, name='category_delete'),

    # Authentication
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # ==============================================================================
    #  PASSWORD RESET URLS (Add this entire block)
    # ==============================================================================
    path('password-reset/', 
         auth_views.PasswordResetView.as_view(
             template_name='todo/password_reset_form.html',
             email_template_name='todo/password_reset_email.html',
             html_email_template_name='todo/password_reset_html_email.html'
         ), 
         name='password_reset'),
         
    path('password-reset/done/', 
         auth_views.PasswordResetDoneView.as_view(template_name='todo/password_reset_sent.html'), 
         name='password_reset_done'),
         
    path('password-reset-confirm/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(template_name='todo/password_reset_confirm.html'), 
         name='password_reset_confirm'),
         
    path('password-reset-complete/', 
         auth_views.PasswordResetCompleteView.as_view(template_name='todo/password_reset_complete.html'), 
         name='password_reset_complete'),
]