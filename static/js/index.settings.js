//FOR THE HOME SLIDER
jQuery(document).ready(function($) {
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
    autoScaleSliderHeight: 660, 

    numImagesToPreload: 0,
    controlNavigation: 'bullets',
    thumbsFitInViewport: false,
    navigateByClick: true,
    startSlideId: 0,
    autoPlay: {
    		// autoplay options go gere
    		enabled: true,
    		pauseOnHover: true,
    		delay: 8000
    	},
    transitionType:'move',
    globalCaption: true
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
  
//FOR THE GET STARTED SLIDER
$('#get-started-slider').royalSlider({
    arrowsNav: true,
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

//FOR THE AWESOME LOGO    
function moveLogo(){
	var contentwidth = $('.nga-logo-container').width();
 	
	var d = contentwidth - 330 + 15;
	$('.nga-logo').css('left', d+'px');
	$('.nt-logo').css('left', (d+200)+'px');
	$('.arm-logo').css('left', (d+188)+'px');
	$('.start-logo').css('left', (d+176)+'px');
	var d2 = contentwidth;
	$('.bg-behind-logo').css('left', d2-1+'px');
	var d3 = contentwidth+780;
	var d4 = contentwidth;
	$('.side-home-right').css('left', d3+'px');
	$('.side-events-right').css('left', d3+'px');
	$('.side-events-left').css('left', d4+'px');
	$('.side-get-started-right').css('left', d3+'px');
	$('.side-get-started-left').css('left', d4+'px');
	$('.side-participants-right').css('left', d3+'px');
	$('.side-participants-left').css('left', d4+'px');
	$('.side-contact-us-right').css('left', d3+'px');
	$('.side-contact-us-left').css('left', d4+'px');

}
moveLogo();
$(window).bind("resize", function(){//Adjusts image when browser resized  
 	moveLogo();
 }); 
 
});
