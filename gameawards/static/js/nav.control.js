jQuery(function() {


    

    var $el, leftPos, newWidth, currLeft, currWidth;
        $mainNav2 = $("#example-two");
    
    /* Add Magic Line markup via JavaScript, because it ain't gonna work without */
    $(".nav-elements").append("<li id='magic-line'></li>");
    
    /* Cache it */
    var $magicLine = $("#magic-line");
    currLeft = $(".current_page_item a").position().left;
    currWidth = $(".current_page_item").width();	    
    
    $magicLine
        .width($(".current_page_item").width())
        .css("left", $(".current_page_item").position().left)
        .data("origLeft", $magicLine.position().left)
        .data("origWidth", $magicLine.width());
     
    //CLICK
   	$(".nav-elements li").find("a").click(function() {
   		allowScroll = false;
		setInterval(allowScroll = true, 300);
		
	   	$el = $(this);
		currLeft = $el.position().left;
        currWidth = $el.parent().width();

   	});
    
    //HOVER
    $(".nav-elements li").find("a").hover(function() {
        $el = $(this);

        leftPos = $el.position().left;
        newWidth = $el.parent().width();
                
        $magicLine.stop().animate({
            left: leftPos,
            width: newWidth
        });
    }, function() {
        $magicLine.stop().animate({
        	left: currLeft,
            width: currWidth
        });    
    });
    
    
    //SCROLL CONTROL
    var allowScroll = true;
    var executed = true;
    $(window).scroll(function() {
	    if (executed && allowScroll){
	    	executed = false
		    setInterval(moveSlider(),400); //TIME 
		} 
    });   
    
	function moveSlider(){
	        var pages = ['#second-container','#third-container','#fourth-container','#fifth-container'];
	    	windowPos = $(window).scrollTop();
	    	if (window.location.pathname === '/'){
			    pages = ['#first-container','#second-container','#third-container','#fourth-container','#fifth-container'];
			}
			
			var distances = [];
			for(var i = 0; i < pages.length; i++)
			{
				var offset = $(pages[i]).offset();
				var d = Math.abs(windowPos - offset.top);
				distances.push(d); 
			}
			shortest = 0;
			for (var j = 1; j < pages.length; j++)	{
			    if (distances[shortest] > distances[j]) shortest = j;
		    }
			navElem = $(".nav-elements li a");
			if (allowScroll){
				$('.nav-elements a').css('color', '#9ECE69');
			   	$(navElem[shortest]).css('color', '#DAE6CC');
			}
			
			currLeft = $(navElem[shortest]).offset().left - $('.nav-elements').offset().left;
	        currWidth = $(navElem[shortest]).width() + 20;
		    
		    executed = true;
		    $magicLine.stop().animate({
		        	left: currLeft,
		            width: currWidth
		        }); 
	    } 
});
