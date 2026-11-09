/*
==========
Toast Messages
==========
*/

const toasts = document.querySelectorAll('.toast-message');

toasts.forEach((toast) => {

    setTimeout(() => {
        toast.classList.add('hide');

        setTimeout(() => {
            toast.remove();
        }, 300);

    }, 4000);

});