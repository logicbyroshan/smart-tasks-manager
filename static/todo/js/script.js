// ==============================================================================
//  CORE APPLICATION JAVASCRIPT
//  This file is loaded on every page and handles global functionality.
// ==============================================================================

document.addEventListener('DOMContentLoaded', () => {
    // Initialize all global functionalities
    setupMobileMenu();
    updateDateTime();
    setupAddTaskModal();
    setupPWA();

    // Update the date/time display every minute
    setInterval(updateDateTime, 60000);
});

/**
 * Sets up the event listeners for the responsive mobile navigation menu (hamburger).
 */
function setupMobileMenu() {
    // This logic is dynamically creating the menu button and overlay, which is fine.
    const navbar = document.querySelector('.navbar-left');
    if (!navbar || document.querySelector('.mobile-menu-toggle')) return; // Don't run if it's already there

    const mobileMenuToggle = document.createElement('div');
    mobileMenuToggle.className = 'mobile-menu-toggle';
    mobileMenuToggle.innerHTML = '<i class="fas fa-bars"></i>';
    
    // Add the toggle button to the navbar
    navbar.appendChild(mobileMenuToggle);

    const sidebar = document.querySelector('.sidebar');
    
    // Create an overlay to close the menu when clicking outside
    const overlay = document.createElement('div');
    overlay.className = 'mobile-overlay';
    document.body.appendChild(overlay);

    const closeMenu = () => {
        if (sidebar) sidebar.classList.remove('mobile-open');
        overlay.classList.remove('active');
    };

    mobileMenuToggle.addEventListener('click', () => {
        if (sidebar) sidebar.classList.toggle('mobile-open');
        overlay.classList.toggle('active');
    });

    overlay.addEventListener('click', closeMenu);
}

/**
 * Updates the date and day display in the main navbar.
 */
function updateDateTime() {
    const now = new Date();
    const days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
    const dayName = days[now.getDay()];
    const dateString = now.toLocaleDateString('en-GB'); // Format: DD/MM/YYYY
    
    const dateElement = document.querySelector('.date-day');
    if (dateElement) {
        dateElement.innerHTML = `<span>${dayName}</span><span>${dateString}</span>`;
    }
}

/**
 * Sets up all event listeners for the global "Add Task" modal.
 * This includes opening, closing, and submitting the form via AJAX (Fetch).
 */
function setupAddTaskModal() {
    const taskModal = document.getElementById('add-task-modal');
    const addTaskForm = document.getElementById('add-task-form');
    const openModalButtons = document.querySelectorAll('.invite-btn'); // All "Add Task" buttons

    if (!taskModal || !addTaskForm) {
        // If the modal isn't on the page (e.g., user not logged in), do nothing.
        return;
    }

    const closeModal = () => {
        taskModal.style.display = 'none';
    };

    const openModal = () => {
        taskModal.style.display = 'flex';
        // Focus the first input field for a better user experience
        taskModal.querySelector('input[name="title"]').focus();
    };
    
    // Attach listener to all "Add Task" buttons on the page
    openModalButtons.forEach(btn => {
        btn.addEventListener('click', (event) => {
            event.preventDefault(); // Prevent any default link behavior
            openModal();
        });
    });

    // Listen for clicks to close the modal (on the 'x', cancel button, or background)
    taskModal.addEventListener('click', (event) => {
        if (event.target.classList.contains('close-modal') || 
            event.target.classList.contains('btn-cancel') ||
            event.target.classList.contains('modal-backdrop')) {
            closeModal();
        }
    });

    // Handle the form submission using the Fetch API for a smooth experience
    addTaskForm.addEventListener('submit', (event) => {
        event.preventDefault(); // Stop the default page reload

        const formData = new FormData(addTaskForm);
        const url = addTaskForm.action;

        fetch(url, {
            method: 'POST',
            body: formData,
            headers: {
                'X-Requested-With': 'XMLHttpRequest', // Important for Django to detect AJAX
            },
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // Easiest and most reliable way to show the new task is to reload.
                window.location.reload(); 
            } else {
                // If there are form errors, display them to the user.
                let errorMessages = 'Please correct the following errors:\n\n';
                for (const field in data.errors) {
                    // Capitalize the field name for readability
                    const fieldName = field.charAt(0).toUpperCase() + field.slice(1);
                    errorMessages += `- ${fieldName}: ${data.errors[field][0]}\n`;
                }
                alert(errorMessages);
            }
        })
        .catch(error => {
            console.error('Error submitting form:', error);
            alert('An unexpected error occurred. Please check the console and try again.');
        });
    });
}

/**
 * Sets up Progressive Web App (PWA) features like the service worker
 * and the "Add to Home Screen" install prompt.
 */
function setupPWA() {
    // 1. Register the Service Worker
    if ('serviceWorker' in navigator) {
        navigator.serviceWorker.register('/static/todo/js/sw.js') // Ensure this path is correct
            .then(registration => console.log('ServiceWorker registered successfully:', registration.scope))
            .catch(error => console.log('ServiceWorker registration failed:', error));
    }

    // 2. Handle the "Add to Home Screen" prompt
    let deferredPrompt;
    window.addEventListener('beforeinstallprompt', (e) => {
        e.preventDefault();
        deferredPrompt = e;
        // Here you could show a custom install button, but we'll keep it simple.
    });
}