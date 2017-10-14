$(document).ready(function () {
    $('.menu-mapa li:has(ul)').click(function (e) {
        e.preventDefault();

        if ($(this).hasClass('activado')){
            $(this).removeClass('activado');
            $(this).children('ul').slideUp();
        } else {
            $('.menu-mapa li ul').slideUp();
            $('.menu-mapa li').removeClass('activado');
            $(this).addClass('activado');
            $(this).children('ul').slideDown();
        }

    });

});