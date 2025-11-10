import React,{useState} from 'react'
import './styles.css'

const App = () => {
  const[counter,setCounter]=useState(0);

    function increment(){
      setCounter(counter+1);
    }

    function decrement(){
      setCounter(counter-1);
    }

    function reset(){
      setCounter(0);
    }
  return (
    
    <div>
      <center><h1>COUNTER APP</h1></center>
      <div className="cn1">
      <button onClick={decrement}>-</button>
      <span>{counter}</span>
      <button onClick={increment}>+</button></div>
      
      <div className="cn2"><button onClick={reset}>Reset</button>  </div>
      
      
    </div>
  )
}

export default App