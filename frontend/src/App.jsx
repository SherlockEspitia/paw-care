import React from 'react';
import './App.css';
import Header from '@/components/Header/Header';
import Footer from '@/components/Footer/Footer';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import InicioSesion from './components/InicioSesion/InicioSesion';

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
      </Routes>
      <Footer />
    </Router>    
  );
}

export default App;
