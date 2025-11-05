import React from 'react'

const UserInfo = (props) => {
  return (
    <div>
    <center>
    <h1>User Information</h1>
    <h2>NAME : {props.name}</h2>
    <h2>AGE : {props.age}</h2>
    <h2>SKILLS : {props.skills.join(" , ")}</h2>
    <h2>ADDRESS : {props.address.city} , {props.address.state}</h2>
    <button onClick={props.greet}>CLICK HERE</button></center>
    </div>
  )
}

export default UserInfo