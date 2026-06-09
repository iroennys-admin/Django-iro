// Scripts personalizados para la web del curso de Django

// Dark Mode Toggle
document.addEventListener('DOMContentLoaded', function() {
    const darkModeToggle = document.createElement('button');
    darkModeToggle.innerHTML = '🌙';
    darkModeToggle.className = 'btn btn-sm btn-outline-light position-fixed bottom-0 end-0 m-3';
    darkModeToggle.id = 'darkModeToggle';
    document.body.appendChild(darkModeToggle);

    darkModeToggle.addEventListener('click', function() {
        document.body.classList.toggle('dark-mode');
        const isDark = document.body.classList.contains('dark-mode');
        localStorage.setItem('darkMode', isDark);
        this.innerHTML = isDark ? '☀️' : '🌙';
    });

    // Cargar preferencia de dark mode
    if (localStorage.getItem('darkMode') === 'true') {
        document.body.classList.add('dark-mode');
        darkModeToggle.innerHTML = '☀️';
    }
});

// Animaciones adicionales
AOS.init({
    duration: 1000,
    once: true
});