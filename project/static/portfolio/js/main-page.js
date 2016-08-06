

onResizeWindow();
$(window).smartresize(onResizeWindow);
title();
$("body").css("overflow", "none");
function onResizeWindow(){
	var navBarHeight = $(".navbar").height();
	$("body").css("padding-top", navBarHeight+10);
	console.log(navBarHeight);
}



function title(){
	var titles  = {"GET REKT": "",
					"Terrible Work": "By a Terrible Person",
					"You miss all the shots you don't take": "And the ones you do",
					"Existence is futile": "",
					"Look at this Garbage": "Awful",
					"Everything matters": "A lot less than you would think",
					"Hard work": "Goes largely unnoticed",
					"Give up": "",
					"Leave a comment": "Don't",
					"It could be worse": "It is",
					"Only death is certain": "and bugs",
					}
	var index = Math.floor(Math.random()*Object.keys(titles).length);
	var key = Object.keys(titles)[index];
	$("#title").text(key);
	$("#subtitle").text(titles[key]);
}