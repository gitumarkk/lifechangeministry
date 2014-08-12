// Foundation JavaScript
// Documentation can be found at: http://foundation.zurb.com/docs
$(document).foundation();

// Replacing all spans with arial with calibri

$(document).ready(function() {
  var $tiny_mce = $(".tiny-mce");
  var $span = $tiny_mce.find("span");
  $span.css({"font-family":"calibri", "font-size": "16px", "line-height": "150%"});
});
