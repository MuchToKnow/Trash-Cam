//var urlGarbage = "35.163.191.108/api/getGarbage";
//var urlRecycle = "35.163.191.108/api/getRecycle";
//var urlCompost = "35.163.191.108/api/getCompost";

var urlGarbage = "localhost:3000/api/getGarbage";
var urlRecycle = "localhost:3000/api/getRecycle";
var urlCompost = "localhost:3000/api/getCompost";


function getGarbage(url) {

  var xmlHttp = new XMLHttpRequest();
  xmlHttp.open( "GET", url, false ); // false for synchronous request
  xmlHttp.send( null );
  return xmlHttp.responseText;
}

function getRecycle(url) {
  var xmlHttp = new XMLHttpRequest();
  xmlHttp.open( "GET", url, false ); // false for synchronous request
  xmlHttp.send( null );
  return xmlHttp.responseText;
}

function getCompost(url) {
  var xmlHttp = new XMLHttpRequest();
  xmlHttp.open( "GET", url, false ); // false for synchronous request
  xmlHttp.send( null );
  return xmlHttp.responseText;
}
