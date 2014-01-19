



﻿$(function() {
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




﻿(function ($) {
    $.fn.showHide = function (options) {
 
    //default vars for the plugin
        var defaults = {
            speed: 1000,
            easing: '',
            changeText: 0,
            showText: 'Show',
            hideText: 'Hide'
 
        };
        var options = $.extend(defaults, options);
 
        $(this).click(function () {
// optionally add the class .toggleDiv to each div you want to automatically close
                      $('.toggleDiv').slideUp(options.speed, options.easing);
             // this var stores which button you've clicked
             var toggleClick = $(this);
             // this reads the rel attribute of the button to determine which div id to toggle
             var toggleDiv = $(this).attr('rel');
             $(toggleDiv).css('height', 343);
             // here we toggle show/hide the correct div at the right speed and using which easing effect
             $(toggleDiv).slideToggle(options.speed, options.easing);
 
          return false;
 
        });
 
    };
})(jQuery);




