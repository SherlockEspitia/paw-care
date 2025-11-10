import React from 'react'
import './Servicios.css'
import paseos from '../../img/imgPaseos.png'
import guarderia from '../../img/imgGuarderia.png'
import adiestramiento from '../../img/imgAdiestramiento.png'
import servicio from '../../img/imgServicio.jpg'
import { Link } from 'react-router-dom'

export const Servicios = () => {
    return (
        <section className="service_section layout_padding">
            <div className="container-fluid">
                <div className="service_row">
                    <div className="service_text_column">
                        <h2 className="custom_heading">Nuestros <span>Servicios</span></h2>
                        <div className="services_wrapper layout_padding2">

                            <div className="service_card">
                                <div className="img_box">
                                    <img src={paseos} alt="paseos" />
                                </div>
                                <div className="detail_box">
                                    <h6>Paseos</h6>
                                    <p>
                                        Tu peludo merece una aventura cada día. ¡Dale momentos felices con nuestros paseos diarios!
                                    </p>
                                </div>
                            </div>

                            <div className="service_card">
                                <div className="img_box">
                                    <img src={guarderia} alt="guarderia" />
                                </div>
                                <div className="detail_box">
                                    <h6>Guardería</h6>
                                    <p>
                                        Un segundo hogar para tu peludo. ¡Reserva su cupo en nuestra guardería!
                                    </p>
                                </div>
                            </div>

                            <div className="service_card">
                                <div className="img_box">
                                    <img src={adiestramiento} alt="adiestramiento" />
                                </div>
                                <div className="detail_box">
                                    <h6>Adiestramiento</h6>
                                    <p>
                                        Transforma travesuras en buenos modales. ¡Entrena a tu mascota con cariño y profesionalismo!
                                    </p>
                                </div>
                            </div>
                        </div>

                        <div className="agendar_btn_container">
                            <Link to="/agendar" className="agendar_general_btn">
                                Agendar una cita
                            </Link>
                        </div>
                    </div>

                    <div className="service_image_column">
                        <img src={servicio} alt="servicio" className="full_width_image" />
                    </div>
                </div>
            </div>
        </section>
    )
}
