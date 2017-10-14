$(function () {
    var btnMenu = document.getElementById('btn-menu');
    var nav = document.getElementById('nav');
    btnMenu.addEventListener('click', function () {
        console.log('diana');
        nav.classList.toggle('mostrar');
    });
});