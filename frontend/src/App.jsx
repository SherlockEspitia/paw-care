import React from 'react';
import './App.css';
import Header from '@/components/Header/Header';
import Footer from '@/components/Footer/Footer';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

import Home from './Pages/Home';
import Servicios from './Pages/Servicios';
import Galeria from './Pages/Galeria';

function App() {
  return (
    <Router>
      <Header />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/servicios" element={<Servicios />} />
        <Route path="/galeria" element={<Galeria />} />
      </Routes>
      <Footer />
    </Router>
  );
}

export default App;
