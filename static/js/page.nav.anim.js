
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
    
    /*
    $('.game-in-list-container').click(function(event) {
        if ($(this).height() <= 220 && $(this).height() >= 180)
        {
            $(this).css('height', '100%');
            var max = $(this).height();
            $(this).css('height', '200px');
            $(this).animate({ height: max+'px' },max/1.5,'linear');
        }
        else
        {
            var h = $(this).height()
            $(this).animate({height:'200px'}, h/1.5, 'linear');
        }

    });*/
    
     
    $('.game-short-container').click(function(event) {
        
        var p = $(this).parent();
        
        if (p.height() <= 220 && p.height() >= 180)
        {
            p.children().show();
            p.css('height', '100%');
            var max = p.height();
            p.css('height', '200px');
            p.animate({ height: max+'px' },max/1.5,'linear');
        }
        else
        {   
            p.children('.game-long-container').hide('slow');
            var h = p.height()
            p.animate({height:'200px'}, h/1.5, 'linear');
        }

    });
    
    function alignNav(){

        var w = 0;
        $('.anav').each(function() {
            w = w + $(this).width() + 20;
        });
        $('.page-nav-group').css('width', w);
        $('.page-nav-group').css('margin-left', 'auto');
        $('.page-nav-group').css('margin-right', 'auto');
    }
    alignNav();
});
