import React from 'react'
import './Header.css'
import { Link } from 'react-router-dom'
import logo from '../../img/logo.jpg'

function Header() {

    return (
        <div className="hero_area">
            <header className="header_section">
                <div className="container-fluid">
                    <nav>
                        <div className="navbar">

                            <Link className="navbar-brand">
                                <img src={logo} alt="logo" />

                                <span>
                                    apPET
                                </span>
                            </Link>

                            <Link className="nav-link" to="/">Inicio</Link>
                            <Link className="nav-link" to="/servicios">Servicios</Link>
                            <Link className="nav-link" to="/galeria">Galería</Link>
                            <Link className="nav-link" to="/contacto">Contacto</Link>


                        </div>
                    </nav>
                </div>
            </header>
        </div>
    )


}

export default Header