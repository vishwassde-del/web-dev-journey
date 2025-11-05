import React from "react";

const MapExample = () => {
    let cartoons=["Tom and Jerry","Mickey Mouse","Doraemon","Shinchan","Chota Bheem"];
    console.log(cartoons);
    
    return (
        <>
        <h1>List of Popular Cartoons</h1>
        {
            cartoons.map((y)=>{
                return <div><center>
                    <h2>{y}</h2></center>
                </div>
            })
        }
        
        </>
        
    )
}
export default MapExample;