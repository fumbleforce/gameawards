$(function() {
    $('li a').bind('click',function(event){
        var $anchor = $(this);
        var time = 1000;
        var offset = $(window).scrollTop()-($($anchor.attr('href')).offset().top - 45);
        if(Math.abs(offset) < 300) time=500;
        else if(Math.abs(offset)> 1300) time=1500;
        
        $('html, body').stop().animate({
            scrollTop: $($anchor.attr('href')).offset().top - 45
        }, time,'easeInOutExpo');
        event.preventDefault();
    });
});
