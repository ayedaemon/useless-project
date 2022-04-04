import "../styles/navbar.css";

const NavBar = () =>{
    return(
        <div className="navLayout">
            <h3 className="logo">Use-Less</h3>
            <div className="button">
                <button className="theme">
                    Dark
                </button>
                <button className="loginButton">
                    Login
                </button>
                <button className="signupButton">
                    SignUp
                </button>
            </div>
        </div>
    );

}

export default NavBar;