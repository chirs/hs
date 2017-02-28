function initialize() {

  var currentTime = new Date();
  updateTime(currentTime);
  

  function updateTime(t){
    var ts = t.getHours() + ":" + t.getMinutes();
    $("#subway_time").html(ts)
  };

  function adjustDate(d, minutes){
    return new Date(d.getTime() + minutes * 60000);
  };

  function incrementTime(){
    currentTime = adjustDate(currentTime, 1);
    updateTime(currentTime);
  };

  setInterval(incrementTime, 1000);

  var map = L.map('map_canvas').setView([51.505, -0.09], 13);
  L.tileLayer('http://{s}.tile.cloudmade.com/API-key/997/256/{z}/{x}/{y}.png', {
    attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://cloudmade.com">CloudMade</a>',
    key: '51e36637bc4e4dcca5d8f67640e55bdb',
    styleId: '4BW Color 2',
    maxZoom: 18,
  }).addTo(map);


}


$(document).ready(function () {
    initialize();
});



