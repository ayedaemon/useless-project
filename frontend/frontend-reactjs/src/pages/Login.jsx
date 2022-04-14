import React, { useState, useEffect } from "react";

import {Signin} from "../api/authAPI";
import "../styles/auth.css";

const Login = () => {
  const [state, setState] = useState({
    email: "",
    password: "",
  });
  useEffect(() => {
    document.title = "Sign In";
  }, []);
  // console.log("hi there")
  return (
    <div className="loginBox">
      <form id="logInForm" data-testid="logInForm" onSubmit={()=> Signin(state.email,state.password)}>
        <h2 id="logInTitle">Sign In</h2>
        <input
          type="email"
          name="password"
          id="email"
          className="inputBox"
          placeholder="Enter email"
          data-testid="email"
          value={state.email}
          onChange={(event) =>
            setState({ ...state, email: event.target.value })
          }
        />
        <input
          type="password"
          name="password"
          id="password"
          className="inputBox"
          placeholder="Enter password"
          data-testid="password"
          value={state.password}
          onChange={(event) =>
            setState({ ...state, password: event.target.value })
          }
        />
        <a href="/reset" id="forgetPassword">
          Forgot your password?
        </a>

        <button type="submit" id="logInButton" data-testid="logInButton">
          Login
        </button>
        <p>
          Create New Account{" "}
          <a href="/signup" id="signupRedirect">
            SignUp
          </a>
        </p>
      </form>
    </div>
  );
};

export default Login;
