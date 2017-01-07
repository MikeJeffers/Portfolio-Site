onResizeWindow();
$(window).smartresize(onResizeWindow);
$("body").css("overflow", "none");
function onResizeWindow(){
	var navBarHeight = $(".navbar").height();
	$("body").css("padding-top", navBarHeight+10);
	console.log(navBarHeight);
}
