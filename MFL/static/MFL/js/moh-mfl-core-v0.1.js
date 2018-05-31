$(function () {
    $(document).ready(function () {
        $("#search_frm_div").toggleClass('left-col-hidden');
        //$("#search-toggle-btn").removeClass("fa-chevron-circle-left");
        //$("#search-toggle-btn").addClass("fa-chevron-circle-right");
         $("#search-toggle-btn").toggleClass("fa-chevron-circle-left");
         $("#search-toggle-btn").toggleClass("fa-chevron-circle-right");
    });
     $("#search-toggle-btn").click(function(e) {
        e.preventDefault();
        $("#search_frm_div").toggleClass('left-col-hidden');
        //$("#search-toggle-btn").removeClass("fa-chevron-circle-left");
        //$("#search-toggle-btn").addClass("fa-chevron-circle-right");
         $("#search-toggle-btn").toggleClass("fa-chevron-circle-left");
         $("#search-toggle-btn").toggleClass("fa-chevron-circle-right");
     });

});

var map;

function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: -34.397, lng: 150.644},
        zoom: 10,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    });
}

