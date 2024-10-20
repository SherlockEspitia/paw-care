import React from 'react'
import './Header.css'

function Header(){

    return (
        <header>
            <img src="/src/img/Logo.svg" alt="AppCare" className='logo' height={120} width={120}/>
            <nav>
                <a href="/">Inicio</a>
                <a href="">Servicios</a>
                <a href="">Tienda</a>
                <a href="">Educativo</a>
                <a href="">Sobre Nosotros</a>
            </nav>
        </header>
    )

        
}

export default Header