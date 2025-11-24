import React, { useState } from 'react'

const RuseState = () => {
    // used to make a component remember a state
    //syntax : 
    const[count,setCount]=useState(0);

    function onclick(){
        setCount(count+1);
    }
  return (
    <div>
        <center>
            <p>useState</p>
            {count}<br/>
            <button onClick={onclick}>click me</button>
            <hr/>
        </center>
    </div>
  )
}

export default RuseState