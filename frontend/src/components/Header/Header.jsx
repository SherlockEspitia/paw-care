import React from 'react'
import './Header.css'
import logo from '../../img/logo.jpg'

function Header() {

    return (
        <div className="hero_area">
            <header className="header_section">
                <div className="container-fluid">
                    <nav>
                        <div className="navbar">

                            <a className="navbar-brand">
                                <img src={logo} alt="logo" />
                                <span>
                                    apPET
                                </span>
                            </a>

                            <a className="nav-link" href="index.html">Inicio</a>
                            <a className="nav-link" href="servicios.html">Servicios</a>
                            <a className="nav-link" href="galeria.html">Galería</a>
                            <a className="nav-link" href="contacto.html">Contacto</a>
                        </div>
                    </nav>
                </div>
            </header>
        </div>
    )


}

export default Header