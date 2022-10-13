import ReactDOM from "react-dom";

import 'mapbox-gl/dist/mapbox-gl.css';
import mapboxgl from 'mapbox-gl';
import polyline from '@mapbox/polyline'
//import '../style/MapBox.css'
import React, { Component, useRef, useState, useEffect } from "react";



mapboxgl.accessToken = '';






function MapBox(props){
  const mapContainerRef = useRef(null);
  const [map, setMap] = useState(null);
  const [lng, setLng] = useState(-0.2);
  const [lat, setLat] = useState(52);
  const [zoom, setZoom] = useState(9);



  useEffect(() =>{

    if (map) return;

    async function loadMap(){
      console.log("loading map")
      const map = await new mapboxgl.Map({
        container: mapContainerRef.current,
        style: 'mapbox://styles/mapbox/streets-v11',
        center: [lng, lat],
        zoom: zoom
      });

      // const data = {
      //   'type': 'Feature',
      //
      //   'geometry': {
      //     'type': 'LineString',
      //     'coordinates': line
      //
      //     // 'type': 'LineString',
      //     // 'coordinates': line
      //   }
      // };
      console.log(props.props)



      var features = []
      for(var i=0; i<props.props.length; i++){
        var feature = {
          'type': 'Feature',
          'properties': {},
          'geometry': {}
        };
        var properties = {
          'type': '',
          'distance': 0,
          'avgPace': 0,
          'time': 0,
          //'kudos': 0
        };
        properties['type'] = props.props[i]['type'];
        properties['distance'] = props.props[i]['distance'];
        properties['avgPace'] = props.props[i]['Pace'];
        properties['time'] = props.props[i]['moving_time'];
        //properties['kudos'] = props.props[i]['kudos'];
        console.log(props.props[i])
        var line = polyline.toGeoJSON(props.props[i]['map']['summary_polyline']);
        feature['geometry'] = line;
        feature['properties'] = properties;
        features.push(feature);
      };

      console.log(features);
      map.on('load', () => {
        //for(var i=0; i<props.props.length; i++){
          map.addSource('routes', {
            'type': 'geojson',
            'data': {
              'type': 'FeatureCollection',
              'features': features

          }});

          map.addLayer({
            id: 'routes',
            type: 'line',
            source: 'routes',
            // {
            //   'type': 'geojson',
            //   'data': {
            //     'type': 'Feature',
            //
            //   'geometry': line
            // }},
            layout: {
              'line-join': 'round',
              'line-cap': 'round',
              'visibility': 'visible'
            },
            paint: {
              'line-color': '#007cbf',
              'line-width': 4
            }
          });
        //};
      });

      map.on('click', (event) => {
        const features = map.queryRenderedFeatures(event.point, {
        layers: ['routes']
        });
        console.log(event.point)
        if (!features.length) {
          return;
        }
        const feature = features[0];
        console.log(features)
        var html = '';
        for(var i=0; i<features.length; i++){
          html += `<h3>${feature.properties.type}</h3>
          <p>Distance: ${feature.properties.distance}M</p>
          <p>Time: ${feature.properties.time}s</p>`
        };
        new mapboxgl.Popup({ offset: [0, -15] })
          .setLngLat(event.lngLat)
          .setHTML(
            html
          ).addTo(map);
        });
    };
    const loading = loadMap();







  });

  useEffect(() => {
    if (!map) return; // wait for map to initialize
    map.on('move', () => {
    setLng(map.getCenter().lng.toFixed(4));
    setLat(map.getCenter().lat.toFixed(4));
    setZoom(map.getZoom().toFixed(2));
    });
  });

  return(
    <div>
    <div ref={mapContainerRef} className="map-container" />
    </div>
  )
}

export default MapBox;
