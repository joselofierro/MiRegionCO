var didScroll;
var lastScrollTop = 0;
var delta = 5;
var navbarHeight = $('.header').outerHeight();

$(window).scroll(function(event){
    didScroll = true;
});

setInterval(function() {
    if (didScroll) {
        hasScrolled();
        didScroll = false;
    }
}, 250);

function hasScrolled() {
    var st = $(this).scrollTop();

// Asegúrese de que se desplacen más de delta
    if(Math.abs(lastScrollTop - st) <= delta)
        return;

    // Si se desplazaron hacia abajo y pasaron la barra de navegación, agregue la clase .nav-up.
     // Esto es necesario para que nunca veas lo que está "detrás" de la barra de navegación.
    if (st > lastScrollTop && st > navbarHeight){
        // Scroll Down
        $('.header').removeClass('nav-down').addClass('nav-up');
    } else {
        // Scroll Up
        if(st + $(window).height() < $(document).height()) {
            $('.header').removeClass('nav-up').addClass('nav-down');
        }
    }

    lastScrollTop = st;
}