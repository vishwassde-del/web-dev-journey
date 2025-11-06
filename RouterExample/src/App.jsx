import { useState } from 'react'
import { BrowserRouter as Router,Routes,Route} from 'react-router-dom'
import Signup from './pages/Signup'
import Login from './pages/Login'
import Nav from './pages/Nav'

function App() {

  return (
    <>
      <Router>
        <Nav/>
        <Routes>
          <Route path='/signup' element={<Signup/>}/>
          <Route path='/login' element={<Login/>}/>
        </Routes>
      </Router>
    </>
  )
}

export default App
