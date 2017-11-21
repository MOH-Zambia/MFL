$(function () {
     $("#search-toggle-btn").click(function(e) {
        e.preventDefault();
        $("#search_frm_div").toggleClass('left-col-hidden');
        //$("#search-toggle-btn").removeClass("fa-chevron-circle-left");
        //$("#search-toggle-btn").addClass("fa-chevron-circle-right");
         $("#search-toggle-btn").toggleClass("fa-chevron-circle-left");
         $("#search-toggle-btn").toggleClass("fa-chevron-circle-right");
     });
})

