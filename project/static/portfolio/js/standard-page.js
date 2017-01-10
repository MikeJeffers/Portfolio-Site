onResizeWindow();
$(window).smartresize(onResizeWindow);
$("body").css("overflow", "none");
function onResizeWindow(){
	var navBarHeight = $(".navbar").height();
	$("body").css("padding-top", navBarHeight+10);
}

$(".z-depth").hover(function() {
		$(this).addClass("hover");
	}, function() {
		$(this).removeClass("hover");
	}
);

