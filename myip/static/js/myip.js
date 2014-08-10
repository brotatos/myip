$(document).ready(function() {
    var $body = $(document.body);
    var $ip = $("#ip");
    var ip_height = $ip.height() / 2;
    var window_height = $ip.height() / 2;
    var middle = window_height - ip_height;
    var colors = $ip.text().split('.');
    var red = colors[0];
    var blue = colors[1];
    var green = colors[2];

    $ip.css("margin-top", middle + "px");
    $body.css("background-color",
              "rgb(" + red + "," + blue + "," + green + ")");
});
