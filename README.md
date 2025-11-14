<div align="center">

  <img src="stock/TaskMitra Thumb.png" 
       alt="TaskMitra Cover" 
       width="100%" 
       style="border-radius: 15px; box-shadow: 0 8px 30px rgba(0,0,0,0.3);" />

  <h1 style="margin-top: 20px;">✅ TaskMitra — Smart Task Management</h1>

  <h3>
    🚀 A Modern Task Management System
  </h3>

  <p>
    <img src="https://img.shields.io/badge/Django-5.2.6-092E20?style=for-the-badge&logo=django&logoColor=white" />
    <img src="https://img.shields.io/badge/Python-3.13.5-3776AB?style=for-the-badge&logo=python&logoColor=white" />
    <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" />
    <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" />
    <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" />
    <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" />
  </p>

  <p><strong>
    A sleek, fully responsive task management application built with Django featuring 
    dynamic task organization, category management, and an intuitive user interface.
  </strong></p>

</div>

---

## 📱 Screenshots

<div align="center">
  <table>
    <tr>
      <td width="50%">
        <img src="./stock/Dashbored.png" alt="Dashboard" style="border-radius: 8px;"/>
        <p align="center"><b>Dashboard - Task Overview</b></p>
      </td>
      <td width="50%">
        <img src="./stock/MyTask.png" alt="My Tasks" style="border-radius: 8px;"/>
        <p align="center"><b>My Tasks - Grid View</b></p>
      </td>
    </tr>
    <tr>
      <td width="50%">
        <img src="./stock/Category.png" alt="Categories" style="border-radius: 8px;"/>
        <p align="center"><b>Task Categories</b></p>
      </td>
      <td width="50%">
        <img src="./stock/settings.png" alt="Settings" style="border-radius: 8px;"/>
        <p align="center"><b>Settings Panel</b></p>
      </td>
    </tr>
  </table>
</div>

---

## ✨ Features

### 🎨 **Frontend Features**
- **Fully Responsive Design** - Mobile-first approach optimized for all devices
- **Modern Dark Theme UI** - Sleek dark interface with blue accent colors
- **Interactive Modals** - AJAX-powered add/edit task modals
- **Custom Scrollbars** - Thin, stylish scrollbars matching the design
- **Fixed Height Layout** - Optimized viewport management for better UX
- **Smooth Animations** - Hover effects and transitions throughout
- **Touch Optimized** - Mobile-friendly interactions and gestures

### 🔧 **Backend Features**
- **Django 5.2.6 Framework** - Latest Django with enhanced features
- **SQLite Database** - Lightweight and efficient data storage
- **Demo Authentication** - Auto-login middleware for quick testing
- **API Endpoints Ready** - Prepared for external authentication integration
- **AJAX Operations** - Real-time task updates without page refresh
- **Category Management** - Organize tasks with custom categories
- **Task CRUD** - Complete create, read, update, delete functionality

### 🛡️ **Security Features**
- **CSRF Protection** - Cross-site request forgery protection enabled
- **XSS Prevention** - Sanitized inputs and secure template rendering
- **Middleware Authentication** - Demo auth middleware for development
- **Secure Headers** - Security headers configured
- **Input Validation** - Comprehensive form validation
- **Prepared for External Auth** - API endpoints ready for integration

### 📊 **Task Management**
- **Task Organization** - Organize tasks by priority, status, and category
- **Priority Levels** - High, Medium, Low priority classification
- **Status Tracking** - Not Started, In Progress, Completed states
- **Due Dates** - Set and track task deadlines
- **Categories** - Custom color-coded categories
- **Task Filtering** - Filter tasks by status, priority, and date
- **Search Functionality** - Quick task search capability
- **Recent Tasks View** - Dashboard with recent task overview
- **Task Statistics** - Visual task status breakdown

---

## 🚀 Quick Start

### **Prerequisites**
```bash
- Python 3.13.5 or higher
- pip (Python package installer)
- Git
```

### **1. Clone Repository**
```bash
git clone <repository-url>
cd To-Do
```

### **2. Create Virtual Environment**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Run Migrations**
```bash
python manage.py migrate
```

### **5. Run Development Server**
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

> **Note:** The app uses demo authentication middleware. You'll be automatically logged in as `demo_user`.

For detailed setup instructions, see [SETUP.md](SETUP.md).

---

## 📁 Project Structure

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
├── 📄 README.md                    # Project documentation
├── 📄 SETUP.md                     # Detailed setup guide
└── 📄 SECURITY.md                  # Security documentation
```

---

## 🎯 Key Components

### **Models**
- **Task** - Main task model with title, description, category, priority, status, and due date
- **Category** - Custom categories with name and color

### **Views**
- **Dashboard** - Recent tasks overview with statistics
- **My Tasks** - Grid view of all tasks with filtering
- **Task Categories** - Category management interface
- **Settings** - Application settings (prepared for future features)
- **Task CRUD** - Create, update, delete operations via AJAX

### **Middleware**
- **DemoAuthMiddleware** - Auto-login for development/testing

### **API Endpoints** (Prepared)
- `/api/auth/verify/` - Token verification
- `/api/auth/user-info/` - User information retrieval

---

## 🔧 Configuration

### **Key Settings**
```python
# Demo Authentication
MIDDLEWARE = [
    # ...
    'todo.middleware.DemoAuthMiddleware',  # Auto-login
]

# Static Files
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Media Files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

---

## 🎨 Design Features

- **Color Scheme**: Dark theme (#1a1a1a, #202020) with blue accents (#2e86de)
- **Typography**: Segoe UI, clean and modern
- **Layout**: Fixed viewport height with scrollable content areas
- **Scrollbars**: Custom thin scrollbars (6px width)
- **Responsive**: Breakpoint at 768px for mobile devices
- **Components**: Modals, cards, filters, status badges

---

## 📝 Usage

### **Adding a Task**
1. Click "Add Task" button on Dashboard or My Tasks page
2. Fill in task details (title, description, category, priority, status, due date)
3. Click "Add Task" to save

### **Editing a Task**
1. Click on any task card
2. Edit task details in the modal
3. Click "Update Task" to save changes

### **Managing Categories**
1. Navigate to Categories page
2. Click "Add Category" to create new categories
3. Assign colors to categories for visual organization

### **Filtering Tasks**
1. Use the filter bar on My Tasks page
2. Filter by priority, status, or due date
3. Sort by various criteria

---

## 🛠️ Development

### **Adding New Features**
1. Update models in `todo/models.py`
2. Create migrations: `python manage.py makemigrations`
3. Apply migrations: `python manage.py migrate`
4. Update views in `todo/views.py`
5. Add templates in `templates/todo/`
6. Add styles in `static/todo/css/`

### **Customization**
- **Theme Colors**: Edit CSS variables in `base.css`
- **Layout**: Modify grid layouts in respective CSS files
- **Navbar**: Update `templates/todo/base.html`
- **Sidebar**: Edit `templates/todo/partials/sidebar.html`

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 Documentation

- [SETUP.md](SETUP.md) - Detailed installation and configuration guide
- [SECURITY.md](SECURITY.md) - Security features and best practices

---

## 📜 License

This project is licensed under the **MIT License** — see the LICENSE file for details.

---

## 👨‍💻 Author

**Developed with ❤️ by Your Name**

- GitHub: [@yourusername](https://github.com/yourusername)
- Email: your.email@example.com

---

## 🙏 Acknowledgments

- Django Framework
- Font Awesome for icons
- Google Fonts for typography
- Community contributors

---

<div align="center">
  <p>Made with ❤️ using Django</p>
  <p>⭐ Star this repository if you find it helpful!</p>
</div>
