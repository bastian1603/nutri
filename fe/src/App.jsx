import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import { createBrowserRouter, RouterProvider } from 'react-router-dom'

import WelcomePage from './pages/WelcomePage.jsx';
import Register from './pages/Register.jsx';

const router = createBrowserRouter([
  {path: "/", element: <WelcomePage />},
  {path: "/register", element: <Register/>}
])

function App() {

  return (
    <>
      <RouterProvider router={router} />

    </>
  )
}

export default App
