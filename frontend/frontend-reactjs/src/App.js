import React, { useEffect, useState } from "react";
import { Route, Routes, BrowserRouter as Router } from "react-router-dom";

import ResponsiveAppBar from "./components/navbar";
import Login from "./pages/Login";
import Signup from "./pages/Signup";
import Home from "./pages/Home";

import "./App.css";

function App() {
  function backgroundChange(arg) {
    if (arg) {
      document.getElementById("body").classList.remove("bodyLight");
    } else {
      document.getElementById("body").classList.add("bodyLight");
    }
  }
  return (
    <>
      <ResponsiveAppBar bcc={backgroundChange} />
      <div className="body" id="body">
        <Router>
          <Routes>
            <Route path="/" element={<Home bcc={backgroundChange} />} />
            <Route path="login" element={<Login />} />
            <Route path="signup" element={<Signup />} />
          </Routes>
        </Router>
        {/* <h1 className="front" id="title">
          Welcome to Useless-Project
        </h1> */}
      </div>
    </>
  );
}

export default App;
