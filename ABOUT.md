# 📖 About TaskMitra

**TaskMitra** is a modern, feature-rich task management application built with Django that helps you organize, track, and manage your tasks efficiently. The name "TaskMitra" combines "Task" with "Mitra" (meaning "friend" in Sanskrit), symbolizing your friendly companion in task management.

---

## 🎯 Project Overview

TaskMitra provides a comprehensive solution for personal task management with an intuitive interface, powerful features, and a sleek dark theme design. Whether you're managing daily to-dos or complex projects, TaskMitra offers the flexibility and organization you need.

---

## ✨ Complete Feature Set

### 🎨 **Frontend Features**

#### **User Interface**
- **Fully Responsive Design** - Mobile-first approach optimized for all devices
- **Modern Dark Theme UI** - Sleek dark interface with blue accent colors (#2e86de)
- **Interactive Modals** - AJAX-powered add/edit task modals without page refresh
- **Custom Scrollbars** - Thin (6px), stylish scrollbars matching the design
- **Fixed Height Layout** - Optimized 100vh viewport management for better UX
- **Smooth Animations** - Hover effects, transitions, and micro-interactions throughout
- **Touch Optimized** - Mobile-friendly interactions and gestures

#### **Visual Design**
- **Color Scheme**: Consistent dark theme (#1a1a1a, #202020) with blue accents
- **Typography**: Clean Segoe UI font family for modern readability
- **Responsive Breakpoints**: Optimized for 768px and below mobile devices
- **Status Badges**: Color-coded priority and status indicators
- **Card-based Layout**: Modern card design for task display
- **Grid System**: Flexible CSS Grid layouts for content organization

### 🔧 **Backend Features**

#### **Framework & Database**
- **Django 5.2.6 Framework** - Latest Django with enhanced features and security
- **SQLite Database** - Lightweight and efficient data storage (upgradable to PostgreSQL)
- **ORM-based Queries** - Secure database interactions with SQL injection protection
- **Migration System** - Version-controlled database schema management

#### **Authentication & Security**
- **Demo Authentication** - Auto-login middleware for quick testing and development
- **API Endpoints Ready** - Prepared for external authentication integration
- **CSRF Protection** - Cross-site request forgery protection enabled
- **XSS Prevention** - Sanitized inputs and secure template rendering
- **Secure Headers** - Security headers configured for production readiness

#### **Task Operations**
- **AJAX Operations** - Real-time task updates without page refresh
- **Category Management** - Organize tasks with custom color-coded categories
- **Task CRUD** - Complete create, read, update, delete functionality
- **Bulk Operations** - Prepared for future batch task updates
- **Task Filtering** - Backend filtering by status, priority, and date ranges

### 📊 **Task Management Features**

#### **Task Organization**
- **Priority Levels** - High, Medium, Low priority classification with color coding
- **Status Tracking** - Not Started, In Progress, Completed states
- **Due Dates** - Set and track task deadlines with date pickers
- **Categories** - Custom color-coded categories for task grouping
- **Task Filtering** - Filter tasks by status, priority, category, and date
- **Search Functionality** - Quick task search by title and description
- **Sorting Options** - Sort by date, priority, status, or alphabetically

#### **Views & Pages**
- **Dashboard** - Recent tasks overview with statistics and quick actions
- **My Tasks** - Grid view of all tasks with comprehensive filtering
- **Task Categories** - Category management interface with CRUD operations
- **Settings** - Application settings and customization options
- **Task Details** - Detailed view with full task information

#### **Task Statistics**
- **Visual Status Breakdown** - Pie charts or progress bars for task completion
- **Category Distribution** - See task distribution across categories
- **Priority Analysis** - Understand task urgency distribution
- **Completion Tracking** - Monitor task completion rates over time

---

## 🎨 Design Philosophy

### **User Experience Principles**
1. **Simplicity First** - Clean, uncluttered interface focusing on essential features
2. **Speed & Performance** - Fast load times with optimized AJAX operations
3. **Accessibility** - Keyboard navigation and screen reader friendly
4. **Consistency** - Uniform design language across all pages
5. **Feedback** - Clear user feedback for all interactions

### **Visual Design**
- **Dark Theme**: Reduces eye strain for extended use
- **Blue Accents**: Professional color scheme with high contrast
- **Card-Based**: Modern card design patterns for content
- **Minimalist Icons**: Simple, recognizable iconography
- **Smooth Transitions**: Polished animations without performance impact

---

## 🔧 Key Components

### **Database Models**

#### **Task Model**
```python
class Task(models.Model):
    user = ForeignKey(User)              # Task owner
    title = CharField(max_length=200)    # Task title
    description = TextField()            # Detailed description
    category = ForeignKey(Category)      # Task category
    priority = CharField(choices=...)    # High/Medium/Low
    status = CharField(choices=...)      # Not Started/In Progress/Completed
    due_date = DateTimeField()           # Deadline
    created_at = DateTimeField()         # Creation timestamp
    updated_at = DateTimeField()         # Last update timestamp
```

#### **Category Model**
```python
class Category(models.Model):
    user = ForeignKey(User)              # Category owner
    name = CharField(max_length=100)     # Category name
    color = CharField(max_length=7)      # Hex color code (#RRGGBB)
    created_at = DateTimeField()         # Creation timestamp
```

### **View Functions**

- **index** - Dashboard with recent tasks and statistics
- **my_tasks** - All tasks view with filtering and search
- **task_categories** - Category management CRUD operations
- **settings** - User settings and preferences
- **add_task** - AJAX endpoint for creating tasks
- **update_task** - AJAX endpoint for updating tasks
- **delete_task** - AJAX endpoint for deleting tasks
- **add_category** - AJAX endpoint for creating categories

### **Middleware Components**

#### **DemoAuthMiddleware**
```python
class DemoAuthMiddleware:
    """Auto-login middleware for development/testing"""
    - Automatically logs in demo_user
    - Skips authentication for rapid testing
    - ⚠️ Should be disabled in production
```

### **API Endpoints** (Prepared for External Authentication)

- **POST** `/api/auth/verify/` - Verify JWT tokens from external auth service
- **GET** `/api/auth/user-info/` - Retrieve authenticated user information

---

## 📝 Usage Guide

### **Getting Started**

#### **1. First Login**
The application uses demo authentication middleware. When you first visit `http://127.0.0.1:8000/`, you'll be automatically logged in as `demo_user`.

#### **2. Dashboard Overview**
- View recent tasks at a glance
- Check task statistics (completion rate, priorities)
- Quick access to add new tasks
- Navigate to different sections via sidebar

### **Managing Tasks**

#### **Adding a New Task**
1. Click the "Add Task" button on Dashboard or My Tasks page
2. Fill in the task details:
   - **Title** (required) - Brief task name
   - **Description** (optional) - Detailed task information
   - **Category** - Select from existing categories
   - **Priority** - High, Medium, or Low
   - **Status** - Not Started, In Progress, or Completed
   - **Due Date** - Set task deadline
3. Click "Add Task" to save

#### **Editing a Task**
1. Click on any task card to open the edit modal
2. Modify task details as needed
3. Click "Update Task" to save changes
4. Changes are saved immediately via AJAX

#### **Deleting a Task**
1. Click on a task card to open the modal
2. Click the "Delete" button
3. Confirm deletion in the confirmation dialog
4. Task is removed immediately

#### **Filtering Tasks**
1. Navigate to "My Tasks" page
2. Use the filter options:
   - **Priority Filter** - High, Medium, Low
   - **Status Filter** - Not Started, In Progress, Completed
   - **Category Filter** - Select specific category
   - **Date Range** - Filter by due date
3. Use the search bar to find tasks by title/description
4. Sort results by date, priority, or status

### **Managing Categories**

#### **Creating Categories**
1. Navigate to "Task Categories" page
2. Click "Add Category" button
3. Enter category name
4. Choose a color (hex color picker)
5. Click "Save" to create

#### **Using Categories**
- Assign tasks to categories when creating/editing
- Color-coded visual organization
- Filter tasks by category on My Tasks page
- Edit or delete categories as needed

#### **Category Best Practices**
- Create categories for different areas (Work, Personal, Shopping, etc.)
- Use distinct colors for easy visual identification
- Keep category names short and descriptive

### **Application Settings**
1. Navigate to Settings page
2. Customize application preferences (future features):
   - Theme customization
   - Notification preferences
   - Default task settings
   - Account management

---

## 🛠️ Customization

### **Changing Theme Colors**

Edit CSS variables in `static/todo/css/base.css`:

```css
:root {
    --bg-primary: #1a1a1a;      /* Main background */
    --bg-secondary: #202020;     /* Card backgrounds */
    --text-primary: #fff;        /* Primary text */
    --text-secondary: #b0b0b0;   /* Secondary text */
    --accent: #2e86de;           /* Accent color (blue) */
    --accent-hover: #2475c7;     /* Accent hover state */
    --border-color: #2a2a2a;     /* Border color */
}
```

### **Modifying Layout**

#### **Grid Layouts**
Edit respective CSS files:
- **My Tasks Grid**: `static/todo/css/my-tasks.css`
- **Categories Grid**: `static/todo/css/task-categories.css`
- **Settings Grid**: `static/todo/css/settings.css`

#### **Navbar Customization**
Update `templates/todo/base.html`:
```django
<nav class="navbar">
    <!-- Customize logo, search, date, profile -->
</nav>
```

#### **Sidebar Navigation**
Edit `templates/todo/partials/sidebar.html`:
```django
<!-- Add/remove navigation items -->
<a href="{% url 'your_view' %}">
    <i class="icon"></i> Your Item
</a>
```

### **Adding Custom Functionality**

#### **New Model Fields**
1. Update model in `todo/models.py`
2. Create migration: `python manage.py makemigrations`
3. Apply migration: `python manage.py migrate`
4. Update forms in `todo/forms.py`
5. Update templates to display new fields

#### **Custom Views**
1. Add view function in `todo/views.py`
2. Create URL pattern in `todo/urls.py`
3. Create template in `templates/todo/`
4. Add navigation link in sidebar

---

## 🔄 Project Roadmap

### **Planned Features**
- [ ] Rich text editor for task descriptions
- [ ] Task attachments and file uploads
- [ ] Task comments and collaboration
- [ ] Recurring tasks support
- [ ] Email notifications for due dates
- [ ] Task sharing and team collaboration
- [ ] Mobile app (React Native)
- [ ] Calendar view integration
- [ ] Task templates
- [ ] Productivity analytics and reports
- [ ] Export tasks (PDF, CSV)
- [ ] Dark/Light theme toggle
- [ ] Custom task fields
- [ ] Subtasks and checklists
- [ ] Time tracking integration

---

## 📄 License

This project is licensed under the **MIT License**.

### MIT License

```
Copyright (c) 2025 TaskMitra

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

<div align="center">
  <p>📖 For more information, see the main <a href="README.md">README</a></p>
</div>
