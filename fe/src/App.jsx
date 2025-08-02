import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import { createBrowserRouter, RouterProvider } from 'react-router-dom'

import WelcomePage from './pages/WelcomePage.jsx';
import Register from './pages/Register.jsx';
import Login from './pages/Login.jsx'

const router = createBrowserRouter([
  {path: "/", element: <WelcomePage />},
  {path: "/register", element: <Register />},
  {path: "/login", element: <Login />}
])

function App() {

  return (
    <>
      <RouterProvider router={router} />

    </>
  )
}

export default App
