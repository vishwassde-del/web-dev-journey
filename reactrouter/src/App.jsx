import React from 'react'
import { BrowserRouter as Router,Routes,Route} from 'react-router-dom'
import Profile from './Profile'
import Settings from './Settings'
import Nav from './Nav'
import Dashboard from './Dashboard'
import Reels from './Reels'
import Home from './Home'
import Error from './Error'
import './global.css'

const App = () => {
  return (
    <div>
        <Router>
        <Nav/>
        <Routes>
          <Route path='/' element={<Home/>}/>
          <Route path='/profile' element={<Profile/>}/>
          <Route path='/dashboard' element={<Dashboard/>}/>
          <Route path='/settings' element={<Settings/>}/>
          <Route path='/reels' element={<Reels/>}/>
          <Route path='*' element={<Error/>}/>
        </Routes>
      </Router>
      </div>
  )
}

export default App