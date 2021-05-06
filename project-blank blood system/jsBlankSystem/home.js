$(document).ready(function () {
    $("#donate").hide();
    $(".close").hide();
    $(".mobile").hide();
    $("#link-donate").click(function (e) { 
        e.preventDefault();
        $("#donate").show();
    });
    $("#time-close").click(function (e) { 
        e.preventDefault();
        $("#donate").hide();
    });
    $(".fa-bars").click(function (e) { 
        e.preventDefault();
        $(".mobile").slideDown();
        $(".fa-bars").hide();
        $(".close").show();
    });
    $(".close").click(function (e) { 
        e.preventDefault();
        $(".mobile").slideUp();
    
        $(".fa-bars").show();
        $(".close").hide();
    });

    $(".nav_item").click(function (e) { 
        e.preventDefault();
        $(".mobile").slideUp();
        $(".fa-bars").show();
        $(".close").hide();
    });
});