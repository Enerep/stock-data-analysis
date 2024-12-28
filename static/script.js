//js
document.addEventListener('DOMContentLoaded', function() {
    const hoverText = document.querySelector('.hover-text');
    const background = document.querySelector('.background');
    const mainContent = document.querySelector('.main-content');

    hoverText.addEventListener('mouseenter', function() {
        background.classList.add('darkened');
        mainContent.style.transform = 'scale(1.02)';

    });

    hoverText.addEventListener('mouseleave', function() {
        background.classList.remove('darkened');
        mainContent.style.transform = 'scale(1)';
    });

});