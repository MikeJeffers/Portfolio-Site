
title();

function title(){
	var titles  = {"Profound Statements": "are hard to come up with",
					"Only death is certain": "and bugs",
					"Seeking employment": "jobs please!",
					"Professional Title": "snarky subtitle",
					}
	var index = Math.floor(Math.random()*Object.keys(titles).length);
	var key = Object.keys(titles)[index];
	$("#title").text(key);
	$("#subtitle").text(titles[key]);
}