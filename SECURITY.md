# 🛡️ TaskMitra - Security Documentation

Security features, best practices, and guidelines for TaskMitra Task Management System.

---

## 📋 Table of Contents

- [Security Overview](#security-overview)
- [Current Security Features](#current-security-features)
- [Development vs Production](#development-vs-production)
- [Authentication & Authorization](#authentication--authorization)
- [Data Protection](#data-protection)
- [Security Best Practices](#security-best-practices)
- [Production Deployment Security](#production-deployment-security)
- [Security Checklist](#security-checklist)
- [Reporting Security Issues](#reporting-security-issues)

---

## 🔒 Security Overview

TaskMitra implements multiple layers of security to protect user data and prevent common web vulnerabilities. This document outlines implemented security features and recommended practices.

---

## ✅ Current Security Features

### **1. CSRF Protection**

Django's built-in Cross-Site Request Forgery protection is enabled.

```python
# config/settings.py
MIDDLEWARE = [
    # ...
    'django.middleware.csrf.CsrfViewMiddleware',
]
```

**Implementation:**
- All forms include `{% csrf_token %}`
- AJAX requests include CSRF token in headers
- Protection against forged requests

**Usage in Templates:**
```django
<form method="post">
    {% csrf_token %}
    <!-- form fields -->
</form>
```

**Usage in AJAX:**
```javascript
fetch(url, {
    method: 'POST',
    headers: {
        'X-CSRFToken': getCookie('csrftoken'),
        'Content-Type': 'application/json',
    },
    body: JSON.stringify(data)
})
```

### **2. XSS Prevention**

Cross-Site Scripting protection through template auto-escaping.

```django
{# Automatically escaped #}
{{ task.title }}

{# Manual escaping when needed #}
{{ task.description|escape }}

{# Trust HTML only when safe #}
{{ trusted_content|safe }}
```

**Protection Measures:**
- Automatic HTML escaping in templates
- Input sanitization in forms
- Content Security Policy headers (recommended for production)

### **3. SQL Injection Protection**

Django ORM provides automatic protection against SQL injection.

```python
# SAFE - Parameterized queries
Task.objects.filter(title=user_input)

# SAFE - ORM methods
Task.objects.get(id=task_id)

# AVOID - Raw SQL (if needed, use parameterization)
from django.db import connection
cursor = connection.cursor()
cursor.execute("SELECT * FROM todo_task WHERE id = %s", [task_id])
```

### **4. Clickjacking Protection**

X-Frame-Options header prevents clickjacking attacks.

```python
# config/settings.py
MIDDLEWARE = [
    # ...
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Default: DENY (prevents framing entirely)
X_FRAME_OPTIONS = 'DENY'

# Or use SAMEORIGIN to allow same-domain framing
# X_FRAME_OPTIONS = 'SAMEORIGIN'
```

### **5. Secure Cookies**

Cookie security settings for production.

```python
# config/settings.py

# HTTPS-only cookies (production)
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Prevent JavaScript access to session cookies
SESSION_COOKIE_HTTPONLY = True

# Restrict cookie domain
SESSION_COOKIE_SAMESITE = 'Lax'
CSRF_COOKIE_SAMESITE = 'Lax'
```

### **6. Password Security**

Django's password hashing and validation.

```python
# config/settings.py

# Password hashers (PBKDF2 by default)
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
]

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {'min_length': 8,}
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
```

---

## 🔄 Development vs Production

### **Development Settings (Current)**

```python
# config/settings.py

DEBUG = True  # Shows detailed error pages
SECRET_KEY = 'django-insecure-...'  # Hardcoded (NOT for production)
ALLOWED_HOSTS = []  # Allows localhost only

# Demo Authentication
MIDDLEWARE = [
    # ...
    'todo.middleware.DemoAuthMiddleware',  # Auto-login for testing
]
```

**Development Features:**
- ✅ Detailed error pages for debugging
- ✅ Auto-login demo user
- ✅ SQLite database
- ✅ Static files served by Django

### **Production Settings (Recommended)**

```python
# config/settings.py

DEBUG = False  # Hide error details
SECRET_KEY = os.environ.get('SECRET_KEY')  # From environment variable
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']

# Remove demo auth middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'todo.middleware.DemoAuthMiddleware',  # REMOVE THIS
]

# Security headers
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
```

---

## 🔐 Authentication & Authorization

### **Current Implementation**

#### **Demo Authentication Middleware**

```python
# todo/middleware.py

class DemoAuthMiddleware:
    """Auto-login middleware for development/testing"""
    
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        if not request.user.is_authenticated:
            user, created = User.objects.get_or_create(
                username='demo_user',
                defaults={
                    'email': 'demo@taskmitra.com',
                    'first_name': 'Demo',
                    'last_name': 'User',
                }
            )
            login(request, user)
        return self.get_response(request)
```

**⚠️ Security Warning:**
- This is **ONLY** for development/testing
- **NEVER** use in production
- Automatically logs in users without credentials

### **Production Authentication Options**

#### **Option 1: Django Built-in Authentication**

```python
# Enable Django's auth views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
```

#### **Option 2: External Authentication (Prepared)**

```python
# todo/api_auth.py

# Token verification endpoint
@api_view(['POST'])
def verify_token(request):
    """Verify JWT token from external auth service"""
    token = request.data.get('token')
    # Implement token verification logic
    pass

# User info endpoint
@api_view(['GET'])
def get_user_info(request):
    """Get authenticated user information"""
    # Return user data
    pass
```

#### **Option 3: OAuth/Social Authentication**

```bash
pip install django-allauth
```

```python
# Support for Google, GitHub, Facebook, etc.
INSTALLED_APPS = [
    # ...
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
]
```

---

## 🔐 Data Protection

### **Input Validation**

```python
# todo/forms.py

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'category', 'priority', 'status', 'due_date']
        
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 3:
            raise ValidationError('Title must be at least 3 characters long')
        return title
```

### **Database Security**

```python
# Prevent mass assignment vulnerabilities
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', ...]  # Explicitly list allowed fields
        # Don't use fields = '__all__'
```

### **File Upload Security** (Future Feature)

```python
# Validate file types
ALLOWED_EXTENSIONS = ['jpg', 'jpeg', 'png', 'pdf']

def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]
    if ext.lower() not in ALLOWED_EXTENSIONS:
        raise ValidationError('Unsupported file extension.')

# Limit file size
FILE_UPLOAD_MAX_MEMORY_SIZE = 5242880  # 5MB
```

---

## 🛡️ Security Best Practices

### **1. Secret Key Management**

**Development:**
```python
# Hardcoded (current)
SECRET_KEY = 'django-insecure-development-key'
```

**Production:**
```python
# Use environment variables
import os
SECRET_KEY = os.environ.get('SECRET_KEY')

# Or use python-dotenv
from dotenv import load_dotenv
load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')
```

**Generate Secure Key:**
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

### **2. Environment Variables**

Create `.env` file (never commit to Git):

```env
SECRET_KEY=your-super-secret-key-here
DEBUG=False
DATABASE_URL=postgresql://user:password@localhost/dbname
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
```

Load in settings:

```python
from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG', 'False') == 'True'
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')
```

### **3. Database Credentials**

**Never hardcode credentials:**

```python
# BAD
DATABASES = {
    'default': {
        'PASSWORD': 'mypassword123',
    }
}

# GOOD
DATABASES = {
    'default': {
        'PASSWORD': os.getenv('DB_PASSWORD'),
    }
}
```

### **4. HTTPS Enforcement**

```python
# config/settings.py (production)

SECURE_SSL_REDIRECT = True  # Redirect HTTP to HTTPS
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
```

### **5. Security Headers**

```python
# Additional security headers
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# HTTP Strict Transport Security
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
```

### **6. Content Security Policy**

```bash
pip install django-csp
```

```python
# config/settings.py
MIDDLEWARE = [
    # ...
    'csp.middleware.CSPMiddleware',
]

CSP_DEFAULT_SRC = ("'self'",)
CSP_SCRIPT_SRC = ("'self'", 'cdnjs.cloudflare.com')
CSP_STYLE_SRC = ("'self'", 'fonts.googleapis.com')
```

---

## 🚀 Production Deployment Security

### **Pre-Deployment Checklist**

```bash
# Run Django security check
python manage.py check --deploy
```

This command checks for:
- DEBUG = False
- SECRET_KEY not hardcoded
- ALLOWED_HOSTS configured
- Security middleware enabled
- HTTPS settings
- Cookie security

### **Server Configuration**

#### **Nginx Configuration Example**

```nginx
server {
    listen 443 ssl http2;
    server_name yourdomain.com;
    
    # SSL Configuration
    ssl_certificate /path/to/cert.pem;
    ssl_certificate_key /path/to/key.pem;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;
    
    # Security Headers
    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload";
    add_header X-Frame-Options "DENY";
    add_header X-Content-Type-Options "nosniff";
    add_header X-XSS-Protection "1; mode=block";
    
    # Static files
    location /static/ {
        alias /path/to/staticfiles/;
    }
    
    # Proxy to Django
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

### **Database Security**

```python
# Use PostgreSQL or MySQL in production
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT', '5432'),
        'OPTIONS': {
            'sslmode': 'require',  # Require SSL connection
        }
    }
}
```

### **Logging & Monitoring**

```python
# config/settings.py

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': '/var/log/taskmitra/django.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'WARNING',
            'propagate': True,
        },
        'django.security': {
            'handlers': ['file'],
            'level': 'WARNING',
            'propagate': False,
        },
    },
}
```

---

## ✅ Security Checklist

### **Development**
- [x] CSRF protection enabled
- [x] XSS protection via template escaping
- [x] SQL injection protection via ORM
- [x] Clickjacking protection
- [x] Input validation in forms
- [ ] Regular dependency updates

### **Production Deployment**
- [ ] DEBUG = False
- [ ] SECRET_KEY from environment variable
- [ ] ALLOWED_HOSTS configured
- [ ] Remove DemoAuthMiddleware
- [ ] Implement proper authentication
- [ ] HTTPS enabled
- [ ] Security headers configured
- [ ] Database over SSL
- [ ] Static files served by Nginx/CDN
- [ ] Regular security updates
- [ ] Monitoring and logging
- [ ] Backup strategy
- [ ] Rate limiting
- [ ] Firewall configuration

---

## 🚨 Reporting Security Issues

If you discover a security vulnerability:

1. **DO NOT** open a public GitHub issue
2. Email security concerns to: security@yourdomain.com
3. Include:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if any)

We will respond within 48 hours and work on a fix.

---

## 📚 Additional Resources

- [Django Security Documentation](https://docs.djangoproject.com/en/stable/topics/security/)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Django Deployment Checklist](https://docs.djangoproject.com/en/stable/howto/deployment/checklist/)
- [Mozilla Web Security Guidelines](https://infosec.mozilla.org/guidelines/web_security)

---

## 🔄 Security Updates

This project uses:
- Django 5.2.6 (check for updates regularly)
- Python 3.13.5 (check for security patches)

**Update regularly:**
```bash
pip list --outdated
pip install --upgrade django
```

---

<div align="center">
  <p>🛡️ Security is an ongoing process, not a one-time task.</p>
  <p>Stay vigilant and keep dependencies updated!</p>
</div>
