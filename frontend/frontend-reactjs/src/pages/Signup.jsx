import React, { useState, useEffect } from "react";

import "../styles/auth.css";
import { Register } from "../api/authAPI";
const Signup = () => {
  const [state, setState] = useState({
    firstName: "",
    lastName: "",
    email: "",
    password: "",
    confirmPassword: "",
  });

  useEffect(() => {
    document.title = "SignUp";
  }, []);
  // console.log("hi there")
  return (
    <div className="loginBox">
      <form
        id="signUpForm"
        data-testid="logInForm"
        onSubmit={() =>
          Register(
            `${state.firstName} ${state.lastName}`,
            state.email,
            state.password
          )
        }
      >
        <h2 id="logInTitle">SignUp</h2>
        <input
          type="text"
          name="firstName"
          id="firstName"
          className="inputBox"
          placeholder="First Name"
          data-testid="firstName"
          value={state.firstName}
          onChange={(event) =>
            setState({ ...state, firstName: event.target.value })
          }
        />
        <input
          type="text"
          name="lastName"
          id="lastName"
          className="inputBox"
          placeholder="Last Name"
          data-testid="lastName"
          value={state.lastName}
          onChange={(event) =>
            setState({ ...state, lastName: event.target.value })
          }
        />

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
        <input
          type="password"
          name="confirmPassword"
          id="confirmPassword"
          className="inputBox"
          placeholder="Confirm Password"
          data-testid="confirmPassword"
          value={state.confirmPassword}
          onChange={(event) =>
            setState({ ...state, confirmPassword: event.target.value })
          }
        />

        <button type="submit" id="logInButton" data-testid="logInButton">
          Register
        </button>
        <p>
          Have a Account?{" "}
          <a href="/login" id="signupRedirect">
            login
          </a>
        </p>
      </form>
    </div>
  );
};

export default Signup;
