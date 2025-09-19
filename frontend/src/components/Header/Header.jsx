import React from 'react'
import './Header.css'
import { Link } from 'react-router-dom'
import logo from '../../img/logo.jpg'

function Header() {

    return (
        <div className="hero_area">
            <header className="header_section">
                <div className="container_fluid">
                    <nav>
                        <div className="navbar">

                            <Link className="navbar_brand">
                                <img src={logo} alt="logo" />

                                <span>
                                    apPET
                                </span>
                            </Link>

                            <Link className="nav_link" to="/">Inicio</Link>
                            <Link className="nav_link" to="/servicios">Servicios</Link>
                            <Link className="nav_link" to="/galeria">Galería</Link>
                            <Link className="nav_link" to="/contacto">Contacto</Link>


                        </div>
                    </nav>
                </div>
            </header>
        </div>
    )


}

export default Header