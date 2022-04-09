import React, { useState } from "react";
import "../styles/navbar.css";

const NavBar = () => {
  const [loggedIn, setLoggedIn] = useState(false);
  const [mode, setMode] = useState(true);
  const name = "Guest";

  function theme() {
    // mode = true -> dark theme
    // mode = false -> light theme
    //mode?setMode(false):setMode(true)

    let ele = document.getElementById("navBar");
    let elem = document.getElementById("btn");

    if (mode) {
      setMode(false);
      ele.classList.add("lightNav");
      elem.classList.add("lightNav")
    } else {
      setMode(true);
      ele.classList.remove("lightNav");
      document.getElementById("btn").classList.remove("lightBtn");
      
    }
  }

  return (
    <div className="navLayout" id="navBar">
      <a href="/">
        <h3 className="logo">Use-Less</h3>
      </a>
      <div className="button">
        <button className="theme dummy" id="btn" onClick={()=>theme()}>Dark</button>
        {!loggedIn ? (
          <>
            <a href="/login">
              <button className="loginButton dummy" id="b" >Login</button>
            </a>
            <a href="/signup">
              <button className="signupButton dummy" id="b" >SignUp</button>
            </a>
          </>
        ) : (
          <button className="signupButton dummy" id="b" >Welcome {name}</button>
        )}
      </div>
    </div>
  );
};

export default NavBar;
