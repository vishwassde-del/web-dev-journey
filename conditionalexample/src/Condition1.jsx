import React,{useState} from 'react'


const Condition1 = () => {
    const[state,setState]=useState(false)
    function toggle(){
        setState(!state)
    }
    let message=""
    if(state){
        message="Welcome Back"
    }else{
        message="Login again"
    }
  return (
    <div>
        <h1>{message}</h1>
        <button onClick={toggle}>Click</button>
    </div>
  )
}

export default Condition1