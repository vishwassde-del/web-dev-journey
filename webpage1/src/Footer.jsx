import React from "react";
import "./golbal.css";

export default function Footer() {
  return (
    <footer className="footer">
      <div className="footer-section">
        <h3>Abstract</h3>
        <ul>
          <li><a href="#">Start Trial</a></li>
          <li><a href="#">Pricing</a></li>
          <li><a href="#">Download</a></li>
        </ul>
      </div>

      <div className="footer-section">
        <h3>Resources</h3>
        <ul>
          <li><a href="#">Blog</a></li>
          <li><a href="#">Help Center</a></li>
          <li><a href="#">Release Notes</a></li>
          <li><a href="#">Status</a></li>
        </ul>
      </div>

      <div className="footer-section">
        <h3>Community</h3>
        <ul>
          <li><a href="#">Twitter</a></li>
          <li><a href="#">LinkedIn</a></li>
          <li><a href="#">Facebook</a></li>
          <li><a href="#">Dribbble</a></li>
        </ul>
      </div>

      <div className="footer-section">
        <h3>Company</h3>
        <ul>
          <li><a href="#">About Us</a></li>
          <li><a href="#">Careers</a></li>
          <li><a href="#">Legal</a></li>
        </ul>
      </div>

      <div className="foo">
  <li className="foo-icon">🔥</li>
  <li>@Vishwas Html0.2</li>
  <li>Abstract Studio Design, Inc.</li>
  <li>All rights reserved</li>
</div>

    </footer>
  );
}
