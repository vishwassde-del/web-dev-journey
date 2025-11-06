import React from 'react'
import '../global.css'
import { Link } from 'react-router-dom'

const Nav = () => {
  return (
    <div>
        <div className="nav-bar">
            <div className="left"><h2>LOGO</h2></div>
            <div className="right">
                <Link to='/signup' className='link'><h2>SIGNUP</h2></Link>
                <Link to='/login' className='link'><h2>LOGIN</h2></Link>
            </div>
        </div>
    </div>
  )
}

export default Nav