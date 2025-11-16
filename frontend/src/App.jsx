import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { Header, Registro, Footer, Cuidadores, Propietarios, InicioSesion } from '@/components';
//import Footer from '@/components/Footer';
//import InicioSesion from './components/InicioSesion';
//import {Registro} from './components/Registro';
//import Propietarios from './components/FormPropietarios';
//import Cuidadores from './components/FormCuidadores';

import {Contacto, Home, Galeria, Servicios} from '@/Pages';
//import Home from './Pages/Home';
//import Galeria from './Pages/Galeria/Galeria';
//import Servicios from './Pages/Servicios/Servicios';


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
