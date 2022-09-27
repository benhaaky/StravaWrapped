import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
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
  );
}
const { REACT_APP_CLIENT_ID } = process.env;
const clientId = "94320"
const redirectUrl = "http://localhost:3000/redirect";
const responseType = "code";
const approvalPrompt = "auto";
const scope = "activity:read_all";

const handleLogin = () => {
    window.location = `http://www.strava.com/oauth/authorize?client_id=${clientId}&response_type=${responseType}&redirect_uri=${redirectUrl}/exchange_token&approval_prompt=auto&scope=${scope}`;
};
export default App;
