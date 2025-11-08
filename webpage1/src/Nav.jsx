import React from "react";
import "./golbal.css";

export default function Nav() {
  return (
    <>
    <nav className="nav">
      <div className="navdiv left">🔥 Abstract | Help Center</div>

      <div className="navdiv right">
        <input className="search" placeholder="search" />
        <button className="btn">Submit a request</button>
        <button className="btn">Sign in</button>
      </div>
    </nav></>
  );
}