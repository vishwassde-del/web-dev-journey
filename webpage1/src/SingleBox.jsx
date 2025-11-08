import React from 'react'
import './golbal.css'
export default function SingleBox() {
  return (
    <div className="box">
      <div className="box-image">
        <img 
          src="https://help.goabstract.com/hc/theming_assets/01HZH4D3G4S2K93BN3WJPT8600" 
          alt="Abstract support"
        />
      </div>

      <div className="box-content">
        <h3>Abstract support</h3>
        <p>Get in touch with a human.</p>
        <a href="#">Learn More →</a>
      </div>
    </div>
  );
}
