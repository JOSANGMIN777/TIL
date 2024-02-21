import logo from './logo.svg';
import './App.css';

function App() {
  const name = '킹상민'
  
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <h2>
          {name} 님 안녕하세요
        </h2>
      </header>
    </div>
  );
}

export default App;
