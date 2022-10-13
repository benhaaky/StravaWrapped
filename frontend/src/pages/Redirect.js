import React, { useRef, useState, useEffect } from "react";
import axios from 'axios'
import polyline from '@mapbox/polyline'
import 'mapbox-gl/dist/mapbox-gl.css';
import mapboxgl from 'mapbox-gl';
import MapBox from '../components/MapBox'
import {
  BrowserRouter as Router,
  Link,
  Route,
  Routes,
  useSearchParams,

} from "react-router-dom";

function Redirect(props)  {
  const [searchParams, setSearchParams] = useSearchParams();
  const [stravaResponse, setStravaResponse] = useState();
  const [routeResponse, setRouteResponse] = useState();

  const headers = {
    'Content-Type': 'application/json',
    //'X-CSRFToken': csrftoken
  }

  const token = {
    'code': searchParams.get("code"),
  };

  const athleteData = {
    'athlete_id': '0',
  };

  async function getStrava(){

    var athlete = null
    console.log(token)
    const reply = await axios.post("http://127.0.0.1:8000/stravaAPI/authcode/", token, {
          headers: headers
        })
        .then((response) => {
          athlete = response.data.athlete_id;

        })
        .catch();
    athleteData['athlete_id'] = '' + athlete;
    console.log(athleteData)
    const route = await axios.get("http://127.0.0.1:8000/stravaAPI/activity/", {params: {athlete_id:athlete}},
        {
          headers: headers
        })
        .then((response) => {
          setRouteResponse(response.data)
        })
        .catch();







  };
  useEffect(() =>{
    getStrava();

  },[])




  return(
     <div>
     <link href="https://api.mapbox.com/mapbox-gl-js/v2.10.0/mapbox-gl.css" rel="stylesheet"/>
     {searchParams.get("code")}
     {routeResponse ? <MapBox props={routeResponse} />:null}
      <p>Hello youve been redirected{stravaResponse}</p>
     </div>
   );
};

export default Redirect;
