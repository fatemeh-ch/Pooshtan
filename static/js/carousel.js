/*
========
Carousel
========
*/

const slides = document.querySelectorAll('.carousel-slide');
const indicators = document.querySelectorAll('.carousel-indicators button');

let currentSlide = 0;

function showSlide(index) {

    slides[currentSlide].classList.remove('active');
    indicators[currentSlide].classList.remove('active');

    currentSlide = index;

    slides[currentSlide].classList.add('active');
    indicators[currentSlide].classList.add('active');

}

/*
==========
Automatic Slide
==========
*/

setInterval(() => {

    const nextSlide = (currentSlide + 1) % slides.length;

    showSlide(nextSlide);

}, 5000);

/*
==========
Indicator Click
==========
*/

indicators.forEach((indicator, index) => {

    indicator.addEventListener('click', () => {
        showSlide(index);
    });

});