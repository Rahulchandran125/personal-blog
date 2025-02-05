const responsive = {
    0: {
        items: 1
    },
    320: {
        items: 1
    },
    560: {
        items: 2
    },
    960: {
        items: 3
    }
}

$(document).ready(function () {

    $nav = $('.nav');
    $toggleCollapse = $('.toggle-collapse');

    /** click event on toggle menu */
    $toggleCollapse.click(function () {
        $nav.toggleClass('collapse');
    })

    // owl-crousel for blog
    $('.owl-carousel').owlCarousel({
        loop: true,
        autoplay: false,
        autoplayTimeout: 3000,
        dots: false,
        nav: true,
        navText: [$('.owl-navigation .owl-nav-prev'), $('.owl-navigation .owl-nav-next')],
        responsive: responsive
    });



    // click to scroll top
    $('.move-up span').click(function () {
        $('body').animate({
            scrollTop: 0
        }, 1000);
    })

    // AOS Instance
    AOS.init();

});

//

// add post page navbar
// -----------------------

// const checkbox = document.getElementById("checkbox")
// checkbox.addEventListener("change", () => {
//   document.body.classList.toggle("darkmode")
// })


// DARKMODE

const toggle = document.getElementById('toggleDark');
const body = document.querySelector('body');

toggle.addEventListener('click', function(){
    this.classList.toggle('bi-moon');
    if(this.classList.toggle('bi-brightness-high-fill')){
        body.style.background = 'white';
        body.style.color = 'black';
        body.style.transition = '2s';
    }else{
        body.style.background = 'black';
        body.style.color = 'white';
        body.style.transition = '2s';
    }
});
// END

// SLIDER
"use strict";
// common idea: https://dribbble.com/shots/20364660-Nibble-Health-Identity-Social-Posting
// carousel animation: https://codepen.io/aija/details/xvXWoK
let CHECKED = false;
document.addEventListener("pointerdown", (e) => {
    CHECKED = !CHECKED;
    document.documentElement.style.setProperty("--light", CHECKED ? 1 : 0);
});
// END




