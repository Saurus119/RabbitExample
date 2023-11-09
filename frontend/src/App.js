import logo from './logo.svg';
import './css/App.css';
import DemoComponent from "./components/TestButton.tsx"
import DemoView from "./views/DemoView.tsx"

function App() {
  return (

    <div className="App">
      <DemoComponent/>
      <DemoView/>

      {/* <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header> */}
    </div>
  );
}

export default App;
