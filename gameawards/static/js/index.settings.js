//FOR THE HOME SLIDER
$(function($) {

    
    var set_logo = function() {
        var $logo = $('.nga-logo');
        var left = $('.navbar-right').offset().left - $logo.width() - 10;
        if (left < 0) left = $('.navbar-right li').last().offset().right + 12;
        $logo.css('left', left);
        
    };
    set_logo();
    $(window).resize(set_logo);

    $('.carousel').carousel({
      interval: 6000
    });
    $('.carousel-inner').each(function() {
        $(this).find('.item').first().addClass("active");
    });

    
});

//GET STARTED CONTROL
function getStartedSliderPrev()
{
        var getStartedSlider = $("#get-started-slider").data('royalSlider');
        getStartedSlider.prev();

}

function getStartedSliderNext()
{
        var getStartedSlider = $("#get-started-slider").data('royalSlider');
        getStartedSlider.next();

}

function getStartedSliderTo(id)
{
        var getStartedSlider = $("#get-started-slider").data('royalSlider');
        getStartedSlider.goTo(id);

}
/*
  $('#home-slider').royalSlider({
    arrowsNav: true,
    loop: true,
    keyboardNavEnabled: true,
    controlsInside: true,
    imageScaleMode: 'fill',
    arrowsNav: true,
    arrowsNavAutoHide: false,
    autoScaleSlider: true,
    autoScaleSliderWidth: 800,     
    autoScaleSliderHeight: 550, 
    numImagesToPreload: 3,
    controlNavigation: 'bullets',
    thumbsFitInViewport: false,
    navigateByClick: false,
    startSlideId: 0,
    transitionType:'move',
    globalCaption: true,
    autoPlay: {
    		// autoplay options go gere
    		enabled: true,
    		pauseOnHover: true,
    		delay: 8000
    	},
  });

//FOR THE EVENTSLIDER  
$('#events-slider').royalSlider({
    arrowsNav: true,
    loop: true,
    keyboardNavEnabled: true,
    controlsInside: true,
    imageScaleMode: 'fill',
    arrowsNav: true,
    arrowsNavAutoHide: false,
    autoScaleSlider: true,
    autoScaleSliderWidth: 800,     
    autoScaleSliderHeight: 550, 
    numImagesToPreload: 3,
    controlNavigation: 'bullets',
    thumbsFitInViewport: false,
    navigateByClick: false,
    startSlideId: 0,
    autoPlay: false,
    transitionType:'move',
    globalCaption: true
  });
  */
//FOR THE GET STARTED SLIDER
$('#get-started-slider').royalSlider({
    loop: false,
    keyboardNavEnabled: false,
    controlsInside: true,
    imageScaleMode: 'fill',
    arrowsNav: true,
    arrowsNavAutoHide: false,
    autoScaleSlider: true,
    autoScaleSliderWidth: 800,
    autoScaleSliderHeight: 600,
    numImagesToPreload: 4,
    controlNavigation: 'bullets',
    thumbsFitInViewport: false,
    navigateByClick: false,
    startSlideId: 3,
    minSlideOffset: 0,
    autoPlay: false,
    transitionType:'move',
    globalCaption: true
  });
/*
//FOR THE PARTICIPANTS SLIDER
$('#participants-slider').royalSlider({
    arrowsNav: true,
    loop: true,
    keyboardNavEnabled: false,
    controlsInside: true,
    imageScaleMode: 'fill',
    arrowsNav: true,
    arrowsNavAutoHide: false,
    autoScaleSlider: true,
    autoScaleSliderWidth: 800,     
    autoScaleSliderHeight: 400, 
    numImagesToPreload: 0,
    controlNavigation: 'bullets',
    thumbsFitInViewport: false,
    navigateByClick: false,
    startSlideId: 0,
    autoPlay: false,
    transitionType:'move',
    globalCaption: true
  });
  


//FOR THE CONTACT US SLIDER
$('#contact-us-slider').royalSlider({
    arrowsNav: true,
    loop: true,
    keyboardNavEnabled: false,
    controlsInside: true,
    imageScaleMode: 'fill',
    arrowsNav: true,
    arrowsNavAutoHide: false,
    autoScaleSlider: true,
    autoScaleSliderWidth: 800,     
    autoScaleSliderHeight: 400, 
    numImagesToPreload: 0,
    controlNavigation: 'bullets',
    thumbsFitInViewport: false,
    navigateByClick: false,
    startSlideId: 0,
    autoPlay: false,
    transitionType:'move',
    globalCaption: true
  });


//FOR THE HIDDEN UPLOAD DIV

$('.show-hide-button').showHide({
        speed: 400,  // speed you want the toggle to happen
        easing: '',  // the animation effect you want. Remove this line if you dont want an effect and if you haven't included jQuery UI
        changeText: 0, // if you dont want the button text to change, set this to 0 
    });
*/
 

