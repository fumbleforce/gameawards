$(function() {
    $('li a').bind('click',function(event){
        var $anchor = $(this);
        
        $('html, body').stop().animate({
            scrollTop: $($anchor.attr('href')).offset().top - 45
        }, 1000,'easeInOutExpo');
        event.preventDefault();
    });
});
