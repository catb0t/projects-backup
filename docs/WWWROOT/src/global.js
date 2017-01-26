/*jslint node:true */
"use strict";
var btnA = document.getElementById("lbA").href; //buttons
var btnB = document.getElementById("lbB").href; //cntd
var h1 = ".html"; //programmers are inherently lazy people
function iframeHref() {
    var d = document.getElementsByName("iframe_a").location.pathname;
    window.alert(d);
    return d;
}
function parsePathName() { //parse the pathname currently loaded into iframe_a
    var cS = iframeHref.slice(iframeHref.lastIndexOf("/") + 1, iframeHref.len).split(".", 1);
    window.alert("2day we r going 2 load an iframe from page " + cS + ".html"); //debugging; alert the dev
}
function writeiframe() {
	if (parsePathName.charAt(0) === 1) { //remember, the format is 1_2 where 1 = charAt(0) and 2 = charAt(2)
		if (!parsePathName.charAt(2)) {
			btnA = "1_1" + h1; //continue
			btnB = "z/1" + h1; //this is an ending point
		}
	}
}
function toggleshow(which) {
	if (!document.getElementById) {return; }
	if (which.style.display === "block") {
		which.style.display = "none";
	} else {
		which.style.display = "block";
	}
}

btnA.addEventListener('click', writeiframe(), true); //make the "buttons" function
btnB.addEventListener('click', writeiframe(), true); //
iframeHref();
window.onload(window.alert(iframeHref.slice(iframeHref.lastIndexOf("/") + 1, iframeHref.len).split(".", 1)));