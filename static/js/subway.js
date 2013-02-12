function initialize() {


  var currentTime = new Date();
  //alert(startTime.getHours() + ":" + startTime.getMinutes());
  updateTime(currentTime);
  

  var markers = [];
  var latlng = new google.maps.LatLng(40.734, -74.0064)
  var myOptions = {
	zoom: 12,
	center: latlng,
	mapTypeId: google.maps.MapTypeId.ROADMAP
    };
  var map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);
  var infowindow = new google.maps.InfoWindow({content: "" });

  
  function create_marker(lat, lng, content){
	var l = new google.maps.LatLng(lat, lng);
	var marker = new google.maps.Marker({
	  position: l,
	  map: map,
	});
	
	google.maps.event.addListener(marker, 'click', function(){
	  infowindow.setContent(content);
	  infowindow.open(map, marker);
	});
	markers.push(marker);
	marker.setMap(map);
    };

  function create_route(latlngx){
    var path = []
    for (var i=0; i < latlngx.length; i++){
      var ll = new google.maps.LatLng(latlngx[i][0], latlngx[i][1]);
      path.push(ll);
    };
    var poly = new google.maps.Polyline({
      path: path,
      strokeColor: '#FF0000',
      strokeOpacity: 1.0,
      strokeWeight: 2
    });
    poly.setMap(map);

  };

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


  function get_stops(){
	$.getJSON("/subway/stations", function(data){
      stations = data.stations;
  	  for (var i = 0; i < stations.length; i++){
		var e = stations[i];
		create_marker(e.lat, e.lng, e.station); 
	    };
    });
  };


  function get_routes(){
	$.getJSON("/subway/routeshapes", function(data){
      var shapes = data.routeshapes;
      alert(shapes.length);
      //var shapes2 = shapes.slice(1, 40);
      //alert(shapes2.length);
  	  for (var i = 0; i < shapes.length; i++){
		var e = shapes[i];
        create_route(shapes[i])
		//create_marker(e.lat, e.lng, e.station); 
	    };
    });
  };

    function clear_all_listings(){
	for (var i = 0; i < markers.length; i++){
	    var m = markers[i];
	    m.setMap(null);
	};
    };

  //get_stops();

  //get_tweets();
  //create_marker(41.9, 12.5, "I quit. - Pope");
  //create_route([[41.9, 12.5], [50.9, 40.2]]);
  get_routes();
  setInterval(incrementTime, 1000)

}


$(document).ready(function () {
    initialize();
});



