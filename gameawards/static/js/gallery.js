$(document).ready(function() {
    $('.screen-gallery .screen-img').click(function() {
        console.log('click');
        var $that = $(this),
            $hidden = $('#hidden-div'),
            $sibs,
            $img = $that.children('img');

        if ($that.hasClass("screen-img-focus")) {

            $hidden.hide();
            $img.addClass("screen-in-list");
            $that.removeClass("screen-img-focus");
        }
        else {

            $hidden.show();
                
            $sibs = $that.siblings();
            $sibs.removeClass("screen-img-focus");
            $sibs.children('img').addClass("screen-in-list");

            $img.removeClass("screen-in-list");
            $that.addClass("screen-img-focus");

            $hidden.height($that.height()+10);
        }
    });
});
