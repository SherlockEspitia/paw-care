import './Registro.css';
import { Link } from 'react-router-dom';

export const Registro = () => {
    return (
        <section className="registro_section">
            <div className="registro_container">
                <h2>Elige tu tipo de cuenta</h2>
                <div className="registro_buttons">
                    <Link className="btn-reg propietario" to="/registro/propietario">
                        Soy Propietario
                    </Link>
                    <Link className="btn-reg cuidador" to="/registro/cuidador">
                        Soy Cuidador
                    </Link>
                </div>
            </div>
        </section>
    );
};

export default Registro;