import React,{useState} from 'react'


const Condition2 = () => {
    const[state,setState]=useState(false)
    function toggle(){
        setState(!state)
    }
  return (
    <div>
        <h1>{state?"Welcome Back": "Login again"}</h1>
        <button onClick={toggle}>{state?"logout":"login"}</button>
    </div>
  )
}

export default Condition2