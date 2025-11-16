import { NavLink } from 'react-router-dom';
import './Footer.css'

function Footer(){
    return(
        <footer className="footer_section">
            <p>&copy; 2025 Todos los derechos reservados por apPET
                <NavLink to="#">apPET</NavLink>
            </p>
        </footer>
    )
}

export default Footer;
