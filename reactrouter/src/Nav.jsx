import React from 'react'
import './global.css'
import { Link } from 'react-router-dom'

const Nav = () => {
  return (
    <div>
        <div className="nav-bar">
            <div className="links"><Link to ='./profile'><h2>PROFILE</h2></Link></div>
            <div className="links"><Link to ='./dashboard'><h2>DASHBOARD</h2></Link></div>
            <div className="links"><Link to ='./settings'><h2>SETTINGS</h2></Link></div>
            <div className="links"><Link to ='./reels'><h2>REELS</h2></Link></div>
            
        </div>
    </div>
  )
}

export default Nav