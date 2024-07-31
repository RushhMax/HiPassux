// scripts.js

document.addEventListener('DOMContentLoaded', function() {
    console.log('Document loaded and ready!');
    
    // Ejemplo de cómo agregar un evento a un botón
    const button = document.querySelector('button');
    if (button) {
        button.addEventListener('click', function() {
            alert('Button clicked!');
        });
    }
});
