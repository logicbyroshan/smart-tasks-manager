# 📁 Project Structure

Complete file and folder structure of the TaskMitra project.

---

## 🗂️ Directory Overview

```
To-Do/
├── 📁 config/                      # Django project settings
│   ├── __init__.py
│   ├── asgi.py                     # ASGI configuration
│   ├── settings.py                 # Django settings
│   ├── urls.py                     # Main URL configuration
│   └── wsgi.py                     # WSGI configuration
├── 📁 todo/                        # Main Django application
│   ├── 📁 migrations/              # Database migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_remove_profile...
│   │   └── ...
│   ├── 📁 static/todo/             # Static files
│   │   ├── 📁 css/
│   │   │   ├── base.css            # Base styles & theme
│   │   │   ├── style.css           # Main stylesheet
│   │   │   ├── my-tasks.css        # My Tasks page styles
│   │   │   ├── task-categories.css # Categories page styles
│   │   │   └── settings.css        # Settings page styles
│   │   ├── 📁 js/
│   │   │   └── script.js           # Main JavaScript functionality
│   │   └── 📁 images/
│   │       └── logo.png            # TaskMitra logo
│   ├── 📁 templates/todo/          # HTML templates
│   │   ├── 📁 partials/
│   │   │   └── sidebar.html        # Sidebar navigation
│   │   ├── base.html               # Base template with modals
│   │   ├── index.html              # Dashboard
│   │   ├── my-tasks.html           # All tasks page
│   │   ├── task-categories.html    # Categories management
│   │   └── settings.html           # Settings page
│   ├── api_auth.py                 # API endpoints for external auth
│   ├── apps.py                     # App configuration
│   ├── context_processors.py       # Template context processors
│   ├── forms.py                    # Django forms
│   ├── middleware.py               # Demo authentication middleware
│   ├── models.py                   # Database models (Task, Category)
│   ├── urls.py                     # App URL patterns
│   └── views.py                    # View functions
├── 📁 templates/                   # Project-level templates
│   └── 404.html                    # Custom 404 page
├── 📁 static/                      # Project-level static files
├── 📁 media/                       # User uploaded files (future use)
├── 📁 stock/                       # Screenshots & demo assets
│   ├── TaskMitra Thumb.png         # Cover image
│   ├── Dashbored.png               # Dashboard screenshot
│   ├── MyTask.png                  # My Tasks screenshot
│   ├── Category.png                # Categories screenshot
│   └── settings.png                # Settings screenshot
├── 📄 manage.py                    # Django management script
├── 📄 requirements.txt             # Python dependencies
├── 📄 db.sqlite3                   # SQLite database
├── 📄 .gitignore                   # Git ignore rules
├── 📄 README.md                    # Main documentation
├── 📄 ABOUT.md                     # About project
├── 📄 SETUP.md                     # Detailed setup guide
├── 📄 SECURITY.md                  # Security documentation
├── 📄 STRUCTURE.md                 # Project structure (this file)
├── 📄 API.md                       # API documentation
└── 📄 CONTRIBUTING.md              # Contributing guidelines
```

---

## 📂 Detailed File Descriptions

### **config/** - Project Configuration

#### `settings.py`
Main Django configuration file containing:
- **INSTALLED_APPS**: Registered Django apps
- **MIDDLEWARE**: Request/response processing pipeline
- **DATABASES**: Database configuration (SQLite by default)
- **STATIC_URL & STATICFILES_DIRS**: Static file settings
- **MEDIA_URL & MEDIA_ROOT**: Media file settings
- **AUTH_PASSWORD_VALIDATORS**: Password validation rules
- **LANGUAGE_CODE & TIME_ZONE**: Localization settings

Key settings:
```python
DEBUG = True  # Development mode
ALLOWED_HOSTS = []  # Localhost only
SECRET_KEY = 'django-insecure-...'  # Change in production
```

#### `urls.py`
Main URL routing configuration:
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo.urls')),  # Todo app URLs
]
```

#### `asgi.py` & `wsgi.py`
- **ASGI**: Asynchronous Server Gateway Interface for async support
- **WSGI**: Web Server Gateway Interface for traditional deployment

---

### **todo/** - Main Application

#### **Models** (`models.py`)

##### `Task` Model
```python
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    due_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

##### `Category` Model
```python
class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=7, default='#2e86de')
    created_at = models.DateTimeField(auto_now_add=True)
```

#### **Views** (`views.py`)

- **index**: Dashboard with recent tasks and statistics
- **my_tasks**: All tasks view with filtering
- **task_categories**: Category management
- **settings**: User settings page
- **add_task**: AJAX create task endpoint
- **update_task**: AJAX update task endpoint
- **delete_task**: AJAX delete task endpoint
- **add_category**: AJAX create category endpoint
- **update_category**: AJAX update category endpoint
- **delete_category**: AJAX delete category endpoint

#### **Forms** (`forms.py`)

```python
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'category', 'priority', 'status', 'due_date']
        
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'color']
```

#### **Middleware** (`middleware.py`)

##### `DemoAuthMiddleware`
Auto-login middleware for development:
```python
class DemoAuthMiddleware:
    def __call__(self, request):
        if not request.user.is_authenticated:
            user, created = User.objects.get_or_create(
                username='demo_user',
                defaults={'email': 'demo@taskmitra.com', ...}
            )
            login(request, user)
        return self.get_response(request)
```

#### **Context Processors** (`context_processors.py`)

Provides global template variables:
```python
def categories(request):
    """Make categories available in all templates"""
    return {
        'categories': Category.objects.filter(user=request.user)
    }
```

#### **API Authentication** (`api_auth.py`)

Prepared endpoints for external authentication:
- `verify_token()`: Verify JWT tokens
- `get_user_info()`: Retrieve user information

---

### **static/todo/** - Static Assets

#### **CSS Files**

##### `base.css`
- CSS variables for theme colors
- Base styles and resets
- Typography definitions
- Utility classes

##### `style.css`
- Main layout styles
- Navbar styling (36px height)
- Content area (15px padding)
- Modal styles
- Card components
- Button styles
- Form controls
- Custom scrollbars (6px thin)

##### `my-tasks.css`
- Task grid layout
- Filter options styling
- Task card specific styles

##### `task-categories.css`
- Category grid layout
- Category card styles
- Color picker styling

##### `settings.css`
- Settings grid layout
- Settings section styles

#### **JavaScript** (`script.js`)

Features:
- Modal management (open/close)
- AJAX task operations (create, update, delete)
- AJAX category operations
- Form handling and validation
- CSRF token management
- Dynamic UI updates
- Event listeners

Key functions:
```javascript
function getCookie(name)           // Get CSRF token
function openModal(modalId)        // Open modal
function closeModal(modalId)       // Close modal
function addTask()                 // Create new task
function updateTask(taskId)        // Update existing task
function deleteTask(taskId)        // Delete task
function addCategory()             // Create category
```

---

### **templates/todo/** - HTML Templates

#### `base.html`
Base template with:
- DOCTYPE and HTML structure
- Meta tags and viewport
- CSS imports
- Navbar with logo, search, date, user profile
- Main content container
- Modals (Add Task, Edit Task, Add Category)
- JavaScript imports

#### `index.html` (Dashboard)
```django
{% extends 'todo/base.html' %}
{% block content %}
    <!-- Recent tasks -->
    <!-- Task statistics -->
    <!-- Quick actions -->
{% endblock %}
```

#### `my-tasks.html`
```django
{% extends 'todo/base.html' %}
{% block content %}
    <!-- Filter options -->
    <!-- Task grid -->
    <!-- Add task button -->
{% endblock %}
```

#### `task-categories.html`
```django
{% extends 'todo/base.html' %}
{% block content %}
    <!-- Category header -->
    <!-- Category grid -->
    <!-- Add category button -->
{% endblock %}
```

#### `settings.html`
```django
{% extends 'todo/base.html' %}
{% block content %}
    <!-- Settings sections -->
{% endblock %}
```

#### `partials/sidebar.html`
Sidebar navigation component:
```django
<aside class="sidebar">
    <a href="{% url 'index' %}">Dashboard</a>
    <a href="{% url 'my_tasks' %}">My Tasks</a>
    <a href="{% url 'task_categories' %}">Categories</a>
    <a href="{% url 'settings' %}">Settings</a>
</aside>
```

---

## 🔧 Configuration Files

### `requirements.txt`
Python package dependencies:
```
Django==5.2.6
djangorestframework==3.14.0
python-dotenv==1.0.0
```

### `.gitignore`
Files/folders excluded from Git:
```
# Python
*.pyc
__pycache__/
*.py[cod]
venv/
env/

# Django
*.log
db.sqlite3
/media
/staticfiles

# IDE
.vscode/
.idea/
*.swp

# OS
.DS_Store
Thumbs.db
```

---

## 📊 Database Schema

### **Task Table**
```sql
CREATE TABLE todo_task (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    title VARCHAR(200) NOT NULL,
    description TEXT,
    category_id INTEGER,
    priority VARCHAR(10) NOT NULL,
    status VARCHAR(20) NOT NULL,
    due_date DATETIME,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,
    FOREIGN KEY (user_id) REFERENCES auth_user(id),
    FOREIGN KEY (category_id) REFERENCES todo_category(id)
);
```

### **Category Table**
```sql
CREATE TABLE todo_category (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    name VARCHAR(100) NOT NULL,
    color VARCHAR(7) NOT NULL,
    created_at DATETIME NOT NULL,
    FOREIGN KEY (user_id) REFERENCES auth_user(id)
);
```

---

## 🎨 Asset Organization

### **Images** (`static/todo/images/`)
- `logo.png` - TaskMitra logo (displayed in navbar)

### **Screenshots** (`stock/`)
- `TaskMitra Thumb.png` - Cover/thumbnail image (1200x630 recommended)
- `Dashbored.png` - Dashboard screenshot
- `MyTask.png` - My Tasks page screenshot
- `Category.png` - Categories page screenshot
- `settings.png` - Settings page screenshot

---

## 📝 URL Routing Structure

```python
# config/urls.py
'/' → include('todo.urls')

# todo/urls.py
'/'                        → index (Dashboard)
'/my-tasks/'              → my_tasks
'/task-categories/'       → task_categories
'/settings/'              → settings
'/task/add/'              → add_task (AJAX)
'/task/update/<id>/'      → update_task (AJAX)
'/task/delete/<id>/'      → delete_task (AJAX)
'/category/add/'          → add_category (AJAX)
'/category/update/<id>/'  → update_category (AJAX)
'/category/delete/<id>/'  → delete_category (AJAX)
'/api/auth/verify/'       → verify_token (API)
'/api/auth/user-info/'    → get_user_info (API)
```

---

<div align="center">
  <p>📁 For more details, see <a href="README.md">README</a> and <a href="ABOUT.md">ABOUT</a></p>
</div>
