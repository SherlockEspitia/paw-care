import styles from './Header.module.css'
import { Link } from 'react-router-dom'
import logo from '@/assets/img/logo.jpg'

function Header() {

    return (
        <div className={styles.hero_area}>
            <header className={styles.header_section}>
                <div className={styles.container_fluid}>
                    <nav>
                        <div className={styles.navbar}>

                            <Link className={styles.navbar_brand}>
                                <img src={logo} alt="logo" />

                                <span>
                                    apPET
                                </span>
                            </Link>

                            <Link className={styles.nav_link} to="/">Inicio</Link>
                            <Link className={styles.nav_link} to="/servicios">Servicios</Link>
                            <Link className={styles.nav_link} to="/galeria">Galería</Link>
                            <Link className={styles.nav_link} to="/contacto">Contacto</Link>


                        </div>
                    </nav>
                </div>
            </header>
        </div>
    )


}

export default Header