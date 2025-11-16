import styles from './Header.module.css'
import { NavLink } from 'react-router-dom'
import logo from '@/assets/img/logo.jpg'

const Header = ()=> {

    return (
        <div className={styles.hero_area}>
            <header className={styles.header_section}>
                <div className={styles.container_fluid}>                    
                    <nav className={styles.navbar}>

                        <NavLink className={styles.navbar_brand}>
                            <img src={logo} alt="logo" />

                            <span>
                                apPET
                            </span>
                        </NavLink>

                        <NavLink className={styles.nav_link} to="/">Inicio</NavLink>
                        <NavLink className={styles.nav_link} to="/servicios">Servicios</NavLink>
                        <NavLink className={styles.nav_link} to="/galeria">Galería</NavLink>
                        <NavLink className={styles.nav_link} to="/contacto">Contacto</NavLink>
                        
                    </nav>
                </div>
            </header>
        </div>
    )


}

export default Header