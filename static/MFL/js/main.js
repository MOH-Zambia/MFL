$(document).ready(function () {
    $('.nav.navbar-nav > li').on('click', function (e) {
        e.preventDefault();
        $('.nav.navbar-nav > li').removeClass('active');
        $(this).addClass('active');
    });

    $('#search-toggle-btn').on('click', function () {
        $('#sidebar').toggleClass('active');
        $("#search-toggle-btn").toggleClass("fa-chevron-circle-left");
        $("#search-toggle-btn").toggleClass("fa-chevron-circle-right");
    });
});

