$(document).ready(function () {
    $('.navbar-toggler').on('click', function() {
        console.log('clicked');
    });

    $('#navbar-content').on('shown.bs.collapse', function () {
        console.log('show');
        $('.navbar-toggler').removeClass('rotate-down').addClass('rotate-up');
    });

    $('#navbar-content').on('hidden.bs.collapse', function () {
        console.log('hide');
        $('.navbar-toggler').removeClass('rotate-up').addClass('rotate-down');
    });

    
});
