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
    autoScaleSliderHeight: 550, 
    numImagesToPreload: 3,
    controlNavigation: 'bullets',
    thumbsFitInViewport: false,
    navigateByClick: false,
    startSlideId: 0,
    transitionType:'move',
    globalCaption: true
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

 
});
