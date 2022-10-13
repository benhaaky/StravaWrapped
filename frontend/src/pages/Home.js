import React from 'react';
import stravaLogo from '../stravalogo.png'


function Home(props) {
  return(
    <div className="Home">
      <header className="App-header">
        <img src={stravaLogo} className="App" alt="../logo" />
        <p>
          Welcome to Stava Wrapped
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >

        </a>
        <div>
            <button onClick={handleLogin}>Connect with Strava</button>
          </div>
      </header>
    </div>
  )
  };

const { REACT_APP_CLIENT_ID } = process.env;
const clientId = "94320"
const redirectUrl = "http://localhost:3000/Redirect";
const responseType = "code";
const approvalPrompt = "auto";
const scope = "activity:read_all";

const handleLogin = () => {
    window.location = `http://www.strava.com/oauth/authorize?client_id=${clientId}&response_type=${responseType}&redirect_uri=${redirectUrl}/exchange_token&approval_prompt=auto&scope=${scope}`;
};

export default Home;
