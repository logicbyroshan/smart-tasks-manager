# 🤝 Contributing to TaskMitra

Thank you for considering contributing to TaskMitra! We welcome contributions from everyone.

---

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)
- [Submission Guidelines](#submission-guidelines)
- [Commit Message Guidelines](#commit-message-guidelines)
- [Pull Request Process](#pull-request-process)

---

## 📜 Code of Conduct

### Our Pledge

We are committed to providing a welcoming and inspiring community for all. Please be respectful and constructive in your interactions.

### Expected Behavior

- **Be Respectful**: Treat everyone with respect and kindness
- **Be Collaborative**: Work together and help each other
- **Be Professional**: Keep discussions focused and constructive
- **Be Inclusive**: Welcome newcomers and diverse perspectives

### Unacceptable Behavior

- Harassment, discrimination, or offensive comments
- Trolling, insulting, or derogatory remarks
- Publishing others' private information
- Any conduct that could reasonably be considered inappropriate

---

## 🚀 How Can I Contribute?

### 🐛 Reporting Bugs

Before creating bug reports, please check existing issues to avoid duplicates.

**How to Submit a Bug Report:**

1. **Use a clear and descriptive title**
2. **Describe the exact steps to reproduce the problem**
3. **Provide specific examples** (screenshots, code snippets)
4. **Describe the behavior you observed** and what you expected
5. **Include your environment details:**
   - OS (Windows, macOS, Linux)
   - Python version
   - Django version
   - Browser (if frontend issue)

**Bug Report Template:**

```markdown
**Description:**
A clear description of the bug.

**Steps to Reproduce:**
1. Go to '...'
2. Click on '...'
3. See error

**Expected Behavior:**
What you expected to happen.

**Actual Behavior:**
What actually happened.

**Screenshots:**
If applicable, add screenshots.

**Environment:**
- OS: [e.g., Windows 11]
- Python: [e.g., 3.13.5]
- Django: [e.g., 5.2.6]
- Browser: [e.g., Chrome 120]

**Additional Context:**
Any other relevant information.
```

---

### 💡 Suggesting Enhancements

We love new ideas! Here's how to suggest enhancements:

1. **Check existing feature requests** to avoid duplicates
2. **Use a clear and descriptive title**
3. **Provide a detailed description** of the suggested enhancement
4. **Explain why this would be useful** to most users
5. **Provide examples** of how it would work

**Feature Request Template:**

```markdown
**Is your feature request related to a problem?**
A clear description of the problem.

**Describe the solution you'd like:**
A clear description of what you want to happen.

**Describe alternatives you've considered:**
Alternative solutions or features you've considered.

**Additional context:**
Any other context, screenshots, or mockups.
```

---

### 🔧 Contributing Code

#### **Areas We Need Help:**

- [ ] Rich text editor for task descriptions
- [ ] Task attachments and file uploads
- [ ] Email notifications
- [ ] Calendar view integration
- [ ] Mobile responsiveness improvements
- [ ] Performance optimizations
- [ ] Test coverage improvements
- [ ] Documentation improvements
- [ ] Accessibility enhancements
- [ ] Internationalization (i18n)

---

## 💻 Development Setup

### **1. Fork and Clone**

```bash
# Fork the repository on GitHub
# Then clone your fork
git clone https://github.com/YOUR_USERNAME/smart-tasks-manager.git
cd smart-tasks-manager
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

### **4. Setup Database**

```bash
python manage.py migrate
```

### **5. Create a Branch**

```bash
git checkout -b feature/your-feature-name
```

### **6. Make Your Changes**

Edit files and test your changes:

```bash
# Run development server
python manage.py runserver

# Run tests (when available)
python manage.py test
```

### **7. Commit Your Changes**

```bash
git add .
git commit -m "Add: your feature description"
```

### **8. Push to Your Fork**

```bash
git push origin feature/your-feature-name
```

### **9. Create Pull Request**

Go to GitHub and create a Pull Request from your fork.

---

## 📝 Coding Standards

### **Python Code Style**

Follow **PEP 8** guidelines:

```python
# Good
def calculate_total_tasks(user, status='all'):
    """Calculate total tasks for a user by status."""
    if status == 'all':
        return Task.objects.filter(user=user).count()
    return Task.objects.filter(user=user, status=status).count()

# Bad
def CalculateTotalTasks(user,status='all'):
    if status=='all':
        return Task.objects.filter(user=user).count()
    return Task.objects.filter(user=user,status=status).count()
```

**Key Points:**
- Use 4 spaces for indentation (no tabs)
- Maximum line length: 79 characters
- Use snake_case for functions and variables
- Use PascalCase for class names
- Add docstrings to functions and classes
- Import order: standard library → third-party → local

### **JavaScript Code Style**

```javascript
// Good
async function addTask() {
    const formData = {
        title: document.getElementById('task-title').value,
        description: document.getElementById('task-description').value
    };
    
    try {
        const response = await fetch('/task/add/', {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCookie('csrftoken'),
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        });
        
        const data = await response.json();
        if (data.success) {
            location.reload();
        }
    } catch (error) {
        console.error('Error:', error);
    }
}

// Bad
async function addTask(){
const formData={title:document.getElementById('task-title').value,description:document.getElementById('task-description').value};
const response=await fetch('/task/add/',{method:'POST',headers:{'X-CSRFToken':getCookie('csrftoken'),'Content-Type':'application/json'},body:JSON.stringify(formData)});
const data=await response.json();
if(data.success){location.reload();}
}
```

**Key Points:**
- Use 4 spaces for indentation
- Use camelCase for variables and functions
- Use meaningful variable names
- Add comments for complex logic
- Handle errors properly with try-catch

### **CSS Code Style**

```css
/* Good */
.task-card {
    background: var(--bg-secondary);
    border-radius: 8px;
    padding: 15px;
    margin-bottom: 15px;
}

.task-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 15px rgba(46, 134, 222, 0.3);
}

/* Bad */
.task-card{background:var(--bg-secondary);border-radius:8px;padding:15px;margin-bottom:15px;}
.task-card:hover{transform:translateY(-2px);box-shadow:0 4px 15px rgba(46,134,222,0.3);}
```

**Key Points:**
- Use 4 spaces for indentation
- One selector per line
- One property per line
- Use CSS variables for colors
- Alphabetize properties (optional but preferred)

### **HTML/Django Template Style**

```django
<!-- Good -->
{% extends 'todo/base.html' %}

{% block content %}
<div class="content-area">
    <h2>My Tasks</h2>
    
    {% for task in tasks %}
        <div class="task-card">
            <h3>{{ task.title }}</h3>
            <p>{{ task.description }}</p>
        </div>
    {% endfor %}
</div>
{% endblock %}

<!-- Bad -->
{% extends 'todo/base.html' %}
{% block content %}<div class="content-area"><h2>My Tasks</h2>{% for task in tasks %}<div class="task-card"><h3>{{ task.title }}</h3><p>{{ task.description }}</p></div>{% endfor %}</div>{% endblock %}
```

---

## 📤 Submission Guidelines

### **Before Submitting:**

- [ ] Test your changes thoroughly
- [ ] Update documentation if needed
- [ ] Follow coding standards
- [ ] Ensure no console errors
- [ ] Check for accessibility issues
- [ ] Verify responsive design
- [ ] Update CHANGELOG.md (if applicable)

### **What to Include:**

1. **Clear description** of changes
2. **Related issue number** (if applicable)
3. **Screenshots** (for UI changes)
4. **Testing steps** for reviewers
5. **Breaking changes** (if any)

---

## 💬 Commit Message Guidelines

### **Format:**

```
<type>: <subject>

<body>

<footer>
```

### **Types:**

- **feat**: New feature
- **fix**: Bug fix
- **docs**: Documentation changes
- **style**: Code style changes (formatting, no logic change)
- **refactor**: Code refactoring
- **test**: Adding or updating tests
- **chore**: Maintenance tasks

### **Examples:**

```bash
# Good
feat: Add rich text editor for task descriptions

Implemented Quill.js rich text editor for task descriptions.
Users can now format text with bold, italic, lists, etc.

Closes #42

# Good
fix: Resolve task deletion modal not closing

Fixed issue where delete confirmation modal remained
open after task deletion.

# Good
docs: Update API documentation with new endpoints

Added documentation for category filtering endpoints
and updated response examples.

# Bad
fixed stuff
update
changes
```

### **Subject Line Rules:**

- Use imperative mood ("Add" not "Added")
- Don't capitalize first letter
- No period at the end
- Maximum 50 characters

### **Body Rules:**

- Wrap at 72 characters
- Explain **what** and **why**, not **how**
- Separate from subject with blank line

---

## 🔄 Pull Request Process

### **1. Create Pull Request**

- **Title**: Clear and descriptive
- **Description**: Detailed explanation of changes
- **Link issues**: Reference related issues (#123)
- **Screenshots**: Include for UI changes

### **2. Pull Request Template:**

```markdown
## Description
Brief description of changes.

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Related Issues
Closes #123

## How Has This Been Tested?
Describe testing performed.

## Screenshots (if applicable)
Add screenshots here.

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review performed
- [ ] Comments added for complex code
- [ ] Documentation updated
- [ ] No new warnings generated
- [ ] Tests added/updated
```

### **3. Review Process**

- Maintainers will review your PR
- Address any requested changes
- Keep discussion respectful and constructive
- Update your branch if needed:

```bash
git fetch upstream
git rebase upstream/main
git push --force origin feature/your-feature-name
```

### **4. After Approval**

- PR will be merged by maintainers
- Your changes will be included in next release
- You'll be added to contributors list! 🎉

---

## 🧪 Testing Guidelines

### **Manual Testing:**

1. Test all affected functionality
2. Test on different browsers (Chrome, Firefox, Safari)
3. Test responsive design (mobile, tablet, desktop)
4. Test edge cases and error scenarios

### **Writing Tests (Future):**

```python
from django.test import TestCase
from todo.models import Task, Category

class TaskModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.category = Category.objects.create(
            user=self.user,
            name='Test Category',
            color='#2e86de'
        )
    
    def test_task_creation(self):
        """Test creating a new task"""
        task = Task.objects.create(
            user=self.user,
            title='Test Task',
            category=self.category,
            priority='high',
            status='not_started'
        )
        self.assertEqual(task.title, 'Test Task')
        self.assertEqual(task.priority, 'high')
```

---

## 📚 Additional Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [PEP 8 Style Guide](https://pep8.org/)
- [Git Branching Model](https://nvie.com/posts/a-successful-git-branching-model/)
- [Writing Good Commit Messages](https://chris.beams.io/posts/git-commit/)

---

## 🙏 Recognition

All contributors will be recognized in:
- README.md contributors section
- CHANGELOG.md for their contributions
- GitHub contributors graph

---

## ❓ Questions?

- Open an issue with the `question` label
- Reach out to maintainers
- Check existing discussions

---

<div align="center">
  <p>Thank you for contributing to TaskMitra! 🎉</p>
  <p>Together, we can build something amazing! 💪</p>
</div>
