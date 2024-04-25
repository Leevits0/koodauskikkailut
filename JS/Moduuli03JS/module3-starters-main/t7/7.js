
const triggerElement = document.getElementById('trigger');
const targetElement = document.getElementById('target');

const originalImageSrc = 'img/picA.jpg';
const hoverImageSrc = 'img/picB.jpg';

triggerElement.addEventListener('mouseenter', () => {
    targetElement.src = hoverImageSrc;
});

triggerElement.addEventListener('mouseleave', () => {
    targetElement.src = originalImageSrc;
});
