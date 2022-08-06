function removePlaylist(playlistid){
	window.location.assign('/remove/playlist/'+playlistid)
}

function setDeletionCSS(id__){
	if(document.getElementById(id__).className == "list-group-item"){
		document.getElementById(id__).className = "list-group-item remove";
		document.getElementById("btn_"+id__).style.display="";
	}
	else{
		document.getElementById(id__).className = "list-group-item";
		document.getElementById("btn_"+id__).style.display="none";
	}
	
}


var pressTimer;

function mouseup(telement){
  clearTimeout(pressTimer);
  // Clear timeout
  return false;
}
function mousedown(telement){
  // Set timeout
  pressTimer = window.setTimeout(function() { setDeletionCSS(telement.id)},1000);
  return false; 
}
function touchmove(telement){
	document.getElementById(telement.id).className = "list-group-item";
  	document.getElementById("btn_"+telement.id).style.display="none";
}
function touchup(telement){
  
  clearTimeout(pressTimer);

  return false;
}
function touchdown(telement){

  pressTimer = window.setTimeout(function() { setDeletionCSS(telement.id)},1000);
  return false; 
}
function leavemouse(telement){
  document.getElementById(telement.id).className = "list-group-item";
  document.getElementById("btn_"+telement.id).style.display="none";
}