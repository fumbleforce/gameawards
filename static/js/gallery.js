$(document).ready(function() {
    $('.screen-gallery .screen-img').click(function() {
        var $that = $(this);
        var $hidden = $('#hidden-div');
        var $img = $that.children('img');
        if ($that.hasClass("screen-img-focus")){
            $hidden.hide()
            $img.addClass("screen-in-list");
            $that.removeClass("screen-img-focus");
        }
        else{
            $hidden.show()
            $img.removeClass("screen-in-list");
            $that.addClass("screen-img-focus");
            $hidden.height($that.height()+10);
        }
    });
});
