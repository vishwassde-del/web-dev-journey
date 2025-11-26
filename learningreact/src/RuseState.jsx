import React, { useState } from 'react'

const RuseState = () => {
    // used to make a component remember a state
    //syntax : 
    const[count,setCount]=useState(0);
    const[view,setView]=useState(0);
    let message=""
    const[countchar,setcountchar]=useState(0);
    function execute1(){
        setCount(count+1);
    }
    function execute5(){
        setCount(count+5);
    }
    function viewmore(){
      setView(!view)
    }
    if(view){
      message=<h1>here are some more details .</h1>
    }
    else{
      message=<h1></h1>
    }
    function increment(){
      setcountchar(countchar+1)
    }
  return (
    <div>
        <center>
            <p>useState</p>
            {count}<br/>
            <button onClick={execute1}>increment by 1</button>
            <button onClick={execute5}>increment by 5</button>
            <h1>{message}</h1>
            <button onClick={viewmore}>{view?"hide details":"show details"}</button>
            <h1>you have entered {countchar} characters.</h1>
            <button onClick={increment}>click for a character</button>
            <hr/>
        </center>
    </div>
  )
}

export default RuseState