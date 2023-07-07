import React from "react";
import { BrowserRouter, Route, Routes, Link } from "react-router-dom";
import UserInfo from "./components/UserInfo";
import Buying from "./components/Buying";
import Selling from "./components/Selling";

function App() {
  return (
    <BrowserRouter>
      <div>
        <h1>Stock Trading App</h1>
        <nav>
          <ul>
            <li>
              <Link to="/user/info">User Info</Link>
            </li>
            <li>
              <Link to="/transaction/buying">Buying</Link>
            </li>
            <li>
              <Link to="/transaction/selling">Selling</Link>
            </li>
          </ul>
        </nav>

        <Routes>
          <Route path="/user/info" element={<UserInfo />} />
          <Route path="/transaction/buying" element={<Buying />} />
          <Route path="/transaction/selling" element={<Selling />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
