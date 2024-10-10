import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App'
import "../src/assets/css/base.css"
import { BrowserRouter as Router } from 'react-router-dom';

ReactDOM.createRoot(document.getElementById('root')).render(
  // <React.StrictMode>
  // {/* </React.StrictMode> */}
  <Router>
    <App />
  </Router>
)
