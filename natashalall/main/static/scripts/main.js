// A $( document ).ready() block.
$(document).ready(function () {
    console.log('hello');

    $(".nav-link").off("mouseover").on("mouseover", function () {
        console.log('hello');
    });

});
