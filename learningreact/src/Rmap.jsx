import React from 'react'

const Rmap = () => {
  
    let movies=["uhudah","uyue","wuekyf"]
    let players=["vk","msd","st"]
    let fruits=["ehbc","eueb","uybew"]
    let isLoggedIn=true
    return(
        <>
        <center><h2>(MAPPING):</h2>
        <ul style={{listStyle:"none"}}>
            {movies.map((movie,index)=>(<li key={index}>{movie}</li>))}
        </ul>
        <ul style={{listStyle:"none"}}>
            {players.map((player,index)=>(<li key={index}>{player}</li>))}
        </ul>
        <ul style={{listStyle:"none"}}>
            {fruits.map((fruit,index)=><li key={index}>{fruit}</li>)}
        </ul>
        <img src='/' alt='xyz' style={{width:"100px"}} className='images'></img>

        {/*ternary*/}
        {isLoggedIn?<h2>Welcome back</h2>:<h2>Please Log In</h2>}
        </center>

        </>
    )
  
}

export default Rmap