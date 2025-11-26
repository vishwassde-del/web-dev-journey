import React, { useState } from "react";

const BgChanger = () => {
  const [color, setColor] = useState("white");

  return (
    <div style={{ backgroundColor: color, height: "200px", padding: "20px" }}>
      <button onClick={() => setColor("red")}>Red</button>
      <button onClick={() => setColor("green")}>Green</button>
      <button onClick={() => setColor("blue")}>Blue</button>
    </div>
  );
};

export default BgChanger;
