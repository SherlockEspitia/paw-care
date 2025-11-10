import React from 'react';
import './App.css';
import Header from '@/components/Header/Header';
import Footer from '@/components/Footer/Footer';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import InicioSesion from './components/InicioSesion/InicioSesion';
import Registro from './components/Registro/Registro';
import Propietarios from './components/FormPropietarios/Propietarios';
import Cuidadores from './components/FormCuidadores/Cuidadores';

import Home from './Pages/Home';
import Servicios from './Pages/Servicios';
import Galeria from './Pages/Galeria';
import Contacto from './Pages/Contacto';


function App() {
  return (
    <Router>
      <Header />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/servicios" element={<Servicios />} />
        <Route path="/galeria" element={<Galeria />} />
        <Route path="/contacto" element={<Contacto/>} />
        <Route path="/login" element={<InicioSesion />} />
        <Route path="/registro" element={<Registro />} />
        <Route path="/registro/propietario" element={<Propietarios />} /> 
        <Route path="/registro/cuidador" element={<Cuidadores />} />
      </Routes>
      <Footer />
    </Router>    
  );
}

export default App;
