function initialize() {
        var mapOptions = {
          center: new google.maps.LatLng(63.41639578136691, 10.409509688615799),
          zoom: 17,
          minZoom: 3,          
          maxZoom: 20,
          disableDefaultUI: true,
          scrollwheel: false,
          mapTypeId: google.maps.MapTypeId.ROADMAP          
        };
        var map = new google.maps.Map(document.getElementById("map_canvas"),
            mapOptions);
        

 var styledMapOptions = {
 map: map
 }

 var testmap =  new google.maps.StyledMapType(stylez,styledMapOptions);

 map.mapTypes.set('styled', testmap);
 map.setMapTypeId('styled');
 
   var marker = new google.maps.Marker({
      position: new google.maps.LatLng(63.41639578136691, 10.409509688615799),
      map: map,
      title:"Start NTNU, Richard Birkelandsvei 2B, 7491 Trondheim",
      icon: '/static/images/map-marker.png'
  });
  
  var marker2 = new google.maps.Marker({
      position: new google.maps.LatLng(63.41649270519487, 10.40325678884983),
      map: map,
      title:"Drivhuset, Sem Sælands Vei 7, 7034 Trondheim",
      icon: '/static/images/map-marker.png'
  });
  
  
	var marker3 = new google.maps.Marker({
      position: new google.maps.LatLng(63.43342803732703, 10.403802618384361),
      map: map,
      title:"Olavshallen, Kjøpmannsgata 44, 7010 Trondheim",
      icon: '/static/images/map-marker.png'
  });


var marker4 = new google.maps.Marker({
      position: new google.maps.LatLng(60.79297652836432, 11.101105213165283),
      map: map,
      title:"Vikingskipet, Hamar",
      icon: '/static/images/map-marker.png'
  });
  
var amundsen = new google.maps.Marker({
      position: new google.maps.LatLng(-85, 180),
      map: map,
      title:"Roald Amundsen was here",
      icon: '/static/images/map-marker.png'
  });


      }

 var stylez = [
  {
    featureType: "road.local",
    elementType: "geometry",
    stylers: [
      { "hue": "#00ff00" },
      { "weight": 1.3 },
      { "lightness": 42 }
    ]
  },{
    featureType: "road.arterial",
    stylers: [
      { "hue": "#08ff00" },
      { "saturation": -97 },
      { "lightness": 60 }
    ]
  },{
    featureType: "landscape",
    elementType: "geometry",
    stylers: [
      { "saturation": -100 },
      { "lightness": 100 }
    ]
  },{
    featureType: "poi",
    stylers: [
      { "visibility": "on" },
      { "hue": "#3bff00" },
      { "lightness": -16 },
      { "saturation": -14 }
    ]  },{
    featureType: "poi.business",
    stylers: [
      { "visibility": "off" }
    ]
  },{
    featureType: "road.highway",
    stylers: [
      { "hue": "#00ff00" },
      { "saturation": -62 },
      { "lightness": 17 }
    ]
  },{
    featureType: "water",
    stylers: [
      { "saturation": -11 },
      { "lightness": 23 }
    ]
  }
];



$(document).ready(function($) {initialize()});
