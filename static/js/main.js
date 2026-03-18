document.addEventListener('DOMContentLoaded', function() {
    const navLinks = document.querySelectorAll('nav a');
    const currentPath = window.location.pathname;

    navLinks.forEach(link => {
        if (link.getAttribute('href') === currentPath) {
            link.classList.add('active');
        }
    });

    const form = document.querySelector('form');
    if (form) {
        form.addEventListener('submit', function(event) {
            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;
            if (!username || !password) {
                event.preventDefault();
                alert('Please fill in all fields.');
            }
        });
    }

    const smoothScrollLinks = document.querySelectorAll('a[href^="#"]');
    smoothScrollLinks.forEach(link => {
        link.addEventListener('click', function(event) {
            event.preventDefault();
            const targetId = link.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);
            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop,
                    behavior: 'smooth'
                });
            }
        });
    });

    // Example of dynamic content loading
    const loadAppointmentsButton = document.querySelector('.btn-primary');
    if (loadAppointmentsButton) {
        loadAppointmentsButton.addEventListener('click', function() {
            fetch('/api/appointments')
                .then(response => response.json())
                .then(data => {
                    console.log(data);
                    // Process and display data
                });
        });
    }
});