
$(document).ready(function() {

    $('#page-button-container').click(function() {

        var top1 = $('#nav-page-container').position().top;
        var top2 = $('.nav-container').position().top;
        if (top1!==top2)
        {
	        $('#nav-page-container').animate({top: '0px'});
	        $('#page-nav-button').css('background-image', 'url(/static/images/pageNavigationArrowDown.png)');
	        
	    }
	    else
	    {
	        $('#nav-page-container').animate({top: $('.nav-container').height()});
	        $('#page-nav-button').css('background-image', 'url(/static/images/pageNavigationArrowUp.png)');
	    }
    });
    
});
