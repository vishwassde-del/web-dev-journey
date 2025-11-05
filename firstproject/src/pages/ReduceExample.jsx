import React from 'react'

export const ReduceExample = () => {
    let data=[5,10,15,20,25];
    let sum=data.reduce((accumulator,currentValue)=>{
        return accumulator+currentValue;
    },0);
  return (
    <div><h1>Reduce Example</h1>
        <center>
                    <h2>{sum}</h2></center>
    </div>
    
  )
}
export default ReduceExample;
