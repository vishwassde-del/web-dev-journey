import React from "react";
import "./golbal.css";

export default function Main1() {
  return (
    <div id="main1">
      <div id="md1">How can we help?</div>

      <div id="md2">
        <input id="i1" type="text" placeholder="Search..." />
        <button className="searchBtn">→</button>
      </div>
    </div>
  );
}
