import React from "react";
import "../styles/global.css";
const Nav = () => {
  return (
    <div>
        <div className="nav-bar">
            <div className="left">
                <h2>Logo</h2>
            </div>
            <div className="right">
                <h2>Signup</h2>
                <h2>Login</h2>
            </div>
        </div>
    </div>
  );
};
export default Nav;