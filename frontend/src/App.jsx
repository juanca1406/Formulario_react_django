import React from 'react';
import './App.css';
import BasicTable from './tabla';
function App() {
  return (
    <div>
      <nav className="navbar">
        <div className="navbar-brand">Logo</div>
        <ul className="navbar-nav">
          <li className="nav-item">Item 1</li>
          <li className="nav-item">Item 2</li>
          <li className="nav-item">Item 3</li>
        </ul>

      </nav>
      <br />
      <BasicTable />
    </div>
  );
}

export default App;
