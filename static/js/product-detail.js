const primaryImage = document.querySelector('#primary-product-image');

const secondaryImages = document.querySelectorAll('.secondary-img');

const previousButton = document.querySelector('.pre-product-img-button');
const nextButton = document.querySelector('.next-product-img-button');

const images = [
    primaryImage.src,
    ...Array.from(secondaryImages, image => image.src)
];

let currentIndex = 0;
let isAnimating = false;


/*
========
Change Product Image
========
*/

function changeImage(index, direction) {

    if (isAnimating) return;

    currentIndex = (index + images.length) % images.length;

    isAnimating = true;

    const newImage = document.createElement('img');

    newImage.src = images[currentIndex];
    newImage.alt = primaryImage.alt;
    newImage.className = 'primary-img';

    newImage.style.position = 'absolute';
    newImage.style.top = '0';
    newImage.style.left = direction === 'next' ? '100%' : '-100%';

    const container = primaryImage.parentElement;

    container.style.position = 'relative';
    container.appendChild(newImage);

    newImage.style.transition = 'none';
    primaryImage.style.transition = 'none';

    requestAnimationFrame(() => {

        requestAnimationFrame(() => {

            newImage.style.transition = 'left 0.45s ease-in-out';
            primaryImage.style.transition = 'left 0.45s ease-in-out';

            primaryImage.style.position = 'relative';
            primaryImage.style.left = direction === 'next' ? '-100%' : '100%';

            newImage.style.left = '0';

        });

    });

    newImage.addEventListener('transitionend', function handler() {

        primaryImage.src = images[currentIndex];

        primaryImage.style.position = '';
        primaryImage.style.left = '';
        primaryImage.style.transition = '';

        newImage.remove();

        isAnimating = false;

    }, { once: true });

}


/*
========
Next Image
========
*/

nextButton.addEventListener('click', () => {

    changeImage(currentIndex + 1, 'next');

});


/*
========
Previous Image
========
*/

previousButton.addEventListener('click', () => {

    changeImage(currentIndex - 1, 'previous');

});




/*
========
Similar Products Carousel
========
*/

const similarList = document.querySelector('.similar-products-list');

const similarCards = document.querySelectorAll('.similar-products-list .product-card');

const similarPreviousButton = document.querySelector('.similar-previous-button');
const similarNextButton = document.querySelector('.similar-next-button');

let similarIndex = 0;

function showSimilarProducts(direction) {

    const cardWidth = similarCards[0].offsetWidth;
    const gap = parseFloat(getComputedStyle(similarList).gap);

    const visibleWidth = similarList.parentElement.offsetWidth;

    const maxIndex = Math.max(
        0,
        Math.ceil((similarCards.length * (cardWidth + gap) - gap - visibleWidth) / (cardWidth + gap))
    );

    similarIndex = Math.max(0, Math.min(similarIndex + direction, maxIndex));

    similarList.style.transform = `translateX(-${similarIndex * (cardWidth + gap)}px)`;

}

similarNextButton.addEventListener('click', () => showSimilarProducts(1));

similarPreviousButton.addEventListener('click', () => showSimilarProducts(-1));
