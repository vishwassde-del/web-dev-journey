import React from "react";
import Nav from "./components/Nav.jsx";
import Home from "./pages/Home.jsx"
import MapExample from "./pages/MapExample.jsx";
import FilterExample from "./pages/FilterExample.jsx";
import ReduceExample from "./pages/ReduceExample.jsx";
import UserInfo from "./pages/UserInfo.jsx";

const App = () => {
  let name="VISHWAS"
  let age=22
  let skills=["HTML","CSS","JS","REACT"]
  let address={
    city:"BANGALURU",
    state:"KARNATAKA"
  }
  let greet=()=>{
    alert("Hello, Vishwas !!!")
  }
  return (
    <div>
    <MapExample/>
    <FilterExample/>
    <ReduceExample/>
    <UserInfo name={name} age={age} skills={skills} address={address} greet={greet}></UserInfo>
    </div>
  );
};

export default App;