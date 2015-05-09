// nice script found at http://www.sitepoint.com/dynamically-load-jquery-library-javascript/

(function () {
	function loadScript(url, callback) {
		var script = document.createElement("script")
		script.type = "text/javascript";
 
		if (script.readyState) { //IE
			script.onreadystatechange = function () {
				if (script.readyState == "loaded" || script.readyState == "complete") {
					script.onreadystatechange = null;
					callback();
				}
			};
		} else { //Others
			script.onload = function ()	{
				callback();
			};
		}
 
		script.src = url;
		document.getElementsByTagName("head")[0].appendChild(script);
	}
 
	loadScript("https://code.jquery.com/jquery-2.1.4.min.js", function () {
		$("._s15").hide();
		/*loadScript("https://raw.githubusercontent.com/inuyaksa/jquery.nicescroll/master/jquery.nicescroll.min.js", function () {
			$(document).ready(function() {
				alert("nice pls");

				var page = $("._1wfr .uiScrollableArea"),
				scrollRange = 60,
				scrollSpeed = 200;

				page.on("mousewheel", function(event, delta, deltaX, deltaY) {
					if (delta < 0) {
						page.stop(true,true).animate({scrollTop: page.scrollTop()+scrollRange}, scrollSpeed);
					} else if (delta > 0) {
						page.stop(true,true).animate({scrollTop: page.scrollTop()-scrollRange}, scrollSpeed);
					}
					return false;
				});
			});
		});*/
	});
})();