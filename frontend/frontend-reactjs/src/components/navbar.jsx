import "../styles/navbar.css";

const NavBar = () => {
  return (
    <div className="navLayout">
      <h3 className="logo">Use-Less</h3>
      <div className="button">
        <button className="theme">Dark</button>
        <a href="/login">
          <button className="loginButton">Login</button>
        </a>
        <a href="/signup">
          <button className="signupButton">SignUp</button>
        </a>
      </div>
    </div>
  );
};

export default NavBar;
