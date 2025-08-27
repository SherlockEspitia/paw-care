import React from "react";
import './SectionClient.css'
import client from '../../img/client.jpg'

export const SectionClient = () => {
    return (

        <section className="client_section">
            <h2> Nuestros <span>clientes</span> </h2>
            <p>Testimonios de quienes han confiado en nosotros:</p>


            <input type="radio" name="slider" id="client1" defaultChecked />
            <input type="radio" name="slider" id="client2" />
            <input type="radio" name="slider" id="client3" />

            <div className="carousel_wrapper">
                <div className="carousel">
                    <div className="client_container">
                        <img src={ client } alt="Cliente" />
                        <h5>Sandy Mark</h5>
                        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam sit amet tincidunt enim.</p>
                    </div>
                    <div className="client_container">
                        <img src={ client } alt="Cliente" />
                        <h5>Laura Smith</h5>
                        <p>Excelente servicio, muy profesionales y cariñosos con mi perro. ¡Recomiendo apPET!</p>
                    </div>
                    <div className="client_container">
                        <img src={ client } alt="Cliente" />
                        <h5>Pedro Gómez</h5>
                        <p>Muy contento con la guardería, mi mascota estuvo feliz. Atención 10/10.</p>
                    </div>
                </div>
            </div>

            <div className="carousel_controls">
                <label htmlFor="client1"></label>
                <label htmlFor="client2"></label>
                <label htmlFor="client3"></label>
            </div>
        </section>

        )
}

                    export default SectionClient

