$(document).ready(function() {
  function filterPath(string) {
    return string
      .replace(/^\//,'')  
      .replace(/(index|default).[a-zA-Z]{3,4}$/,'')  
      .replace(/\/$/,'');
  }
  $('a[href*=#]').each(function() {
    if ( filterPath(location.pathname) == filterPath(this.pathname)
    && location.hostname == this.hostname
    && this.hash.replace(/#/,'') ) {
      var $targetId = $(this.hash), $targetAnchor = $('[name=' + this.hash.slice(1) +']');
      var $target = $targetId.length ? $targetId : $targetAnchor.length ? $targetAnchor : false;
       if ($target) {
         var targetOffset = $target.offset().top - 50;
         var offset = Math.abs(targetOffset);
         var timeMultipler = 1;
         if (offset < 600) timeMultipler = 2
         else if (offset < 1200) timeMultipler = 3
         else if (offset < 1800) timeMultipler = 4
         else if (offset < 2400) timeMultipler = 5
         else timeMultipler = 5
         
         $(this).click(function() {
           $('html, body').animate({scrollTop: targetOffset}, 100*timeMultipler);
           return false;
         });
      }
    }
  });
});