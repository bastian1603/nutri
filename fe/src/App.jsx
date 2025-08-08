import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import { createBrowserRouter, RouterProvider } from 'react-router-dom'

import { Navbar, NavbarToggle, NavbarLink, NavbarCollapse } from 'flowbite-react'

import WelcomePage from './pages/WelcomePage.jsx';
import Register from './pages/Register.jsx';
import Login from './pages/Login.jsx';
import Profile from './pages/Profile.jsx';
import Layout from './components/Layout.jsx';
import Home from './pages/Home.jsx'

import 'flowbite'
// import 'flowbite/dist/flowbite.css'

const router = createBrowserRouter([
  {path: "/", element: <WelcomePage />},
  {path: "/register", element: <Register />},
  {path: "/login", element: <Login />},
  {path: "/profile", element: <Profile />},
  {path: "/home", element: <Home />}
]);

function App() {

  return (
    <>

        <RouterProvider router={router} />
    
    </>
    
  )
}

export default App
