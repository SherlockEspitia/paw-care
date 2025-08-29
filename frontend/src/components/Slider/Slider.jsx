import './Slider.css'
import imgInicio from '../../img/imgInicio.png'

export const Slider = () => {
    return (
        <section className="slider_section">
            <div className="container">
                <div className="slider_content">

                    <div className="slider_detail-box">
                        <h1>apPET <span>Cuidado Canino</span></h1>
                        <p>
                            Deja el cuidado de tu mascota en manos de expertos. En apPET ofrecemos servicios de calidad.
                            Nuestro equipo de cuidadores está altamente capacitado para brindar la mejor atención
                            a tu mascota. Nos aseguramos de que cada perro reciba el amor y la atención que merece.
                        </p>
                        <div className="btn-box">
                            <a className="btn-1" href="">Regístrate</a>
                            <a className="btn-2" href="">Iniciar sesión</a>
                        </div>
                    </div>

                    <div className="slider_img-box">
                        <img src={imgInicio} alt="imgInicio"/>
                    </div>

                </div>
            </div>
        </section>
    )
}
