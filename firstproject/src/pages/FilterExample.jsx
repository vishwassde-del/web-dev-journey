import React from "react";

const FilterExample = () => {
    let arr=[10,20,30,40,50];
    let filteredArr=arr.filter((x)=>{
        return x>25;
    });
    
    return(
        <>
        <h1>filtered items</h1>
        {
            filteredArr.map((y)=>{
                return <div><center>
                    <h2>{y}</h2></center>
                </div>
            })
        }
        </>
    )
    
}
export default FilterExample;