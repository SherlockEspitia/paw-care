import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import App from './App.jsx'
import './index.css'
import Propietarios from './Propietarios.jsx'
import './Propietarios.css'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App/> 
    <Propietarios></Propietarios>
  </StrictMode>,
)
