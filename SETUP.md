# 🚀 TaskMitra - Setup Guide

Complete installation and configuration guide for TaskMitra Task Management System.

---

## 📋 Table of Contents

- [System Requirements](#system-requirements)
- [Installation Steps](#installation-steps)
  - [Windows Setup](#windows-setup)
  - [macOS/Linux Setup](#macoslinux-setup)
- [Database Configuration](#database-configuration)
- [Demo Authentication](#demo-authentication)
- [Static Files Configuration](#static-files-configuration)
- [Running the Application](#running-the-application)
- [Creating Sample Data](#creating-sample-data)
- [Troubleshooting](#troubleshooting)

---

## 📦 System Requirements

### **Minimum Requirements**
- **Python**: 3.13.5 or higher
- **pip**: Latest version
- **Git**: For cloning the repository
- **RAM**: 2GB minimum
- **Storage**: 500MB free space

### **Recommended**
- **Python**: 3.13.5
- **RAM**: 4GB or more
- **Storage**: 1GB free space
- **OS**: Windows 10/11, macOS 10.15+, Ubuntu 20.04+

---

## 🔧 Installation Steps

### Windows Setup

#### **1. Install Python**
```powershell
# Download Python from python.org
# During installation, check "Add Python to PATH"

# Verify installation
python --version
pip --version
```

#### **2. Install Git**
```powershell
# Download Git from git-scm.com
# Verify installation
git --version
```

#### **3. Clone Repository**
```powershell
# Navigate to desired directory
cd C:\Projects

# Clone the repository
git clone <repository-url>
cd To-Do
```

#### **4. Create Virtual Environment**
```powershell
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate

# You should see (venv) in your command prompt
```

#### **5. Install Dependencies**
```powershell
# Upgrade pip
python -m pip install --upgrade pip

# Install requirements
pip install -r requirements.txt
```

#### **6. Run Migrations**
```powershell
# Create database tables
python manage.py migrate
```

#### **7. Start Development Server**
```powershell
# Run server
python manage.py runserver

# Access at http://127.0.0.1:8000/
```

---

### macOS/Linux Setup

#### **1. Install Python**
```bash
# macOS (using Homebrew)
brew install python@3.13

# Ubuntu/Debian
sudo apt update
sudo apt install python3.13 python3-pip python3-venv

# Verify installation
python3 --version
pip3 --version
```

#### **2. Install Git**
```bash
# macOS
brew install git

# Ubuntu/Debian
sudo apt install git

# Verify installation
git --version
```

#### **3. Clone Repository**
```bash
# Navigate to desired directory
cd ~/Projects

# Clone the repository
git clone <repository-url>
cd To-Do
```

#### **4. Create Virtual Environment**
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# You should see (venv) in your terminal prompt
```

#### **5. Install Dependencies**
```bash
# Upgrade pip
python -m pip install --upgrade pip

# Install requirements
pip install -r requirements.txt
```

#### **6. Run Migrations**
```bash
# Create database tables
python manage.py migrate
```

#### **7. Start Development Server**
```bash
# Run server
python manage.py runserver

# Access at http://127.0.0.1:8000/
```

---

## 💾 Database Configuration

### **SQLite (Default)**

TaskMitra uses SQLite by default for ease of setup.

```python
# config/settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

**Advantages:**
- No additional setup required
- Perfect for development
- Lightweight and fast

**Database Location:** `To-Do/db.sqlite3`

### **Resetting Database**

If you need to reset the database:

```bash
# Stop the development server (Ctrl+C)

# Delete database file
# Windows
del db.sqlite3

# macOS/Linux
rm db.sqlite3

# Run migrations again
python manage.py migrate
```

---

## 🔐 Demo Authentication

TaskMitra includes a demo authentication middleware for easy testing.

### **How It Works**

1. **DemoAuthMiddleware** automatically logs you in as `demo_user`
2. No login required - immediate access to the application
3. User details:
   - Username: `demo_user`
   - Email: `demo@taskmitra.com`
   - Full Name: Demo User

### **Middleware Configuration**

```python
# config/settings.py
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'todo.middleware.DemoAuthMiddleware',  # Demo auto-login
]
```

### **For Production**

⚠️ **Important:** Remove `DemoAuthMiddleware` in production and implement proper authentication.

---

## 🎨 Static Files Configuration

### **Development**

Static files are served automatically in development:

```python
# config/settings.py
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
```

**Static files location:**
- `static/` - Project-level static files
- `todo/static/todo/` - App-level static files

### **Production**

For production, collect static files:

```bash
# Collect all static files
python manage.py collectstatic

# Files will be copied to STATIC_ROOT directory
```

---

## 🎯 Running the Application

### **Development Server**

```bash
# Standard port (8000)
python manage.py runserver

# Custom port
python manage.py runserver 8080

# Custom host and port
python manage.py runserver 0.0.0.0:8000
```

### **Accessing the Application**

- **Local**: http://127.0.0.1:8000/
- **Network**: http://<your-ip>:8000/ (if using 0.0.0.0)

### **Available Pages**

- **Dashboard**: `/` or `/dashboard/`
- **My Tasks**: `/my-tasks/`
- **Categories**: `/categories/`
- **Settings**: `/settings/`

---

## 📝 Creating Sample Data

### **Manual Creation**

1. **Visit Dashboard**: http://127.0.0.1:8000/
2. **Add Categories**:
   - Click "Categories" in sidebar
   - Click "Add Category"
   - Create categories (e.g., Work, Personal, Urgent)
3. **Add Tasks**:
   - Click "Add Task" button
   - Fill in task details
   - Select category, priority, status
   - Set due date

### **Python Shell Method**

```bash
# Open Django shell
python manage.py shell
```

```python
# Create categories
from todo.models import Category, Task
from django.contrib.auth.models import User
from datetime import date, timedelta

# Get demo user
user = User.objects.get(username='demo_user')

# Create categories
work = Category.objects.create(name='Work', color='#2e86de')
personal = Category.objects.create(name='Personal', color='#27ae60')
urgent = Category.objects.create(name='Urgent', color='#e74c3c')

# Create sample tasks
Task.objects.create(
    user=user,
    title='Complete Project Documentation',
    description='Write comprehensive documentation for the new feature',
    category=work,
    priority='high',
    status='in-progress',
    due_date=date.today() + timedelta(days=7)
)

Task.objects.create(
    user=user,
    title='Review Pull Requests',
    description='Review and merge pending pull requests',
    category=work,
    priority='medium',
    status='not-started',
    due_date=date.today() + timedelta(days=3)
)

Task.objects.create(
    user=user,
    title='Grocery Shopping',
    description='Buy groceries for the week',
    category=personal,
    priority='low',
    status='not-started',
    due_date=date.today() + timedelta(days=2)
)

print("Sample data created successfully!")
```

---

## 🔍 Troubleshooting

### **Common Issues**

#### **Issue 1: Module Not Found Error**
```
ModuleNotFoundError: No module named 'django'
```

**Solution:**
```bash
# Make sure virtual environment is activated
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

# Reinstall requirements
pip install -r requirements.txt
```

#### **Issue 2: Port Already in Use**
```
Error: That port is already in use.
```

**Solution:**
```bash
# Use a different port
python manage.py runserver 8080

# Or find and kill the process using port 8000
# Windows
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# macOS/Linux
lsof -ti:8000 | xargs kill -9
```

#### **Issue 3: Migration Errors**
```
django.db.migrations.exceptions.InconsistentMigrationHistory
```

**Solution:**
```bash
# Delete database and migrations
# Windows
del db.sqlite3
del todo\migrations\0*.py

# macOS/Linux
rm db.sqlite3
rm todo/migrations/0*.py

# Create fresh migrations
python manage.py makemigrations
python manage.py migrate
```

#### **Issue 4: Static Files Not Loading**
```
404 Error for static files
```

**Solution:**
```python
# Verify settings.py
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# In development, Django serves static files automatically
# Make sure DEBUG = True in settings.py
```

#### **Issue 5: Template Does Not Exist**
```
TemplateDoesNotExist at /
```

**Solution:**
```python
# Verify TEMPLATES configuration in settings.py
TEMPLATES = [
    {
        'DIRS': [BASE_DIR / 'templates'],
        # ...
    }
]

# Check template file paths match exactly
```

---

## 🔄 Updating the Application

### **Pull Latest Changes**

```bash
# Deactivate server (Ctrl+C)

# Pull updates
git pull origin main

# Activate virtual environment
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Update dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Restart server
python manage.py runserver
```

---

## 🛡️ Security Considerations

For development, the current setup is fine. For production:

1. **Remove Demo Auth**: Disable `DemoAuthMiddleware`
2. **Secret Key**: Generate a new `SECRET_KEY`
3. **Debug Mode**: Set `DEBUG = False`
4. **Allowed Hosts**: Configure `ALLOWED_HOSTS`
5. **Database**: Consider PostgreSQL or MySQL
6. **HTTPS**: Enable SSL/TLS

See [SECURITY.md](SECURITY.md) for detailed security configuration.

---

## 📞 Support

If you encounter issues not covered here:

1. Check the [GitHub Issues](https://github.com/yourusername/taskmitra/issues)
2. Review Django documentation
3. Contact: your.email@example.com

---

## ✅ Setup Checklist

- [ ] Python 3.13.5+ installed
- [ ] Git installed
- [ ] Repository cloned
- [ ] Virtual environment created and activated
- [ ] Dependencies installed
- [ ] Migrations applied
- [ ] Development server running
- [ ] Application accessible in browser
- [ ] Sample data created (optional)

---

<div align="center">
  <p>🎉 You're all set! Start managing your tasks with TaskMitra!</p>
</div>
