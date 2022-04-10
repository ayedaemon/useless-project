import React, { useState, useEffect } from "react";
import "../styles/navbar.css";

const NavBar = (props) => {
  const [loggedIn, setLoggedIn] = useState(false);
  const [mode, setMode] = useState({
    state: true,
    text: "Dark",
  });
  const name = "Guest";

  // useEffect(() => {
  //   let data = localStorage.getItem("theme");
  //   if (data === null) {
  //     localStorage.setItem("theme", true);
  //     setMode({ text: "Dark", state: true });
  //   } else {
  //     localStorage.setItem("theme", mode.state);
  //   }
  // }, [mode.state]);

  function theme() {
    // mode = true -> dark theme
    // mode = false -> light theme
    //mode?setMode(false):setMode(true)

    let ele = document.getElementById("navBar");
    let elems = document.querySelectorAll("button.dummy");

    if (mode.state === true) {
      setMode({ text: "Light", state: false });
      ele.classList.add("lightNav");
      document.getElementById("logo").style.color = "black";
      elems.forEach((item) => item.classList.add("lightBtn"));
      props.bcc(false);
    } else {
      setMode({ text: "Dark", state: true });
      document.getElementById("logo").style.color = "white";
      ele.classList.remove("lightNav");
      elems.forEach((item) => item.classList.remove("lightBtn"));
      props.bcc(true);
    }
  }

  return (
    <div className="navLayout" id="navBar">
      <a href="/">
        <h3 className="logo" id="logo">
          Use-Less
        </h3>
      </a>
      <div className="button">
        <button className="theme dummy" id="btn" onClick={() => theme()}>
          {mode.text}
        </button>
        {!loggedIn ? (
          <>
            <a href="/login">
              <button className="loginButton dummy" id="loginbtn">
                Login
              </button>
            </a>
            <a href="/signup">
              <button className="signupButton dummy" id="signupbtn">
                SignUp
              </button>
            </a>
          </>
        ) : (
          <button className="signupButton dummy" id="welcomebtn">
            Welcome {name}
          </button>
        )}
      </div>
    </div>
  );
};

export default NavBar;
