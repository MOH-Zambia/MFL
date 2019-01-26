$(document).ready(function () {
    $('#search-toggle-btn').on('click', function () {
        $('#sidebar').toggleClass('active');
        $("#search-toggle-btn").toggleClass("fa-chevron-circle-left");
        $("#search-toggle-btn").toggleClass("fa-chevron-circle-right");
    });
});

