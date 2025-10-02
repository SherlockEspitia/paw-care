import React from 'react'
import './Contacto.css'
import ubicacion from '../../img/location-white.png'
import imgTelefono from '../../img/telephone-white.png'
import imgEmail from '../../img/envelope-white.png'

export const Contacto = () => {
  return (
    <div className="sub_page">

      {/* map section */}
      <section className="map_section">
        <div id="map" className="map"></div>

        <div className="form_container">
          <form>
            <div className="text-center">
              <h3>Contáctanos</h3>
            </div>
            <div>
              <input type="text" placeholder="Nombre" className="input" />
            </div>
            <div>
              <input type="text" placeholder="Teléfono" className="input" />
            </div>
            <div>
              <input type="email" placeholder="Email" className="input" />
            </div>
            <div>
              <textarea className="message-box" placeholder="Mensaje"></textarea>
            </div>
            <div className="form-actions">
              <button type="submit">Enviar</button>
            </div>
          </form>
        </div>
      </section>

      {/* info section */}
      <section className="info_section">
        <div className="info_items">
          <a href="#">
            <div className="item">
              <div className="img-box">
                <img src={ ubicacion } alt="Ubicación" />
              </div>
              <div className="detail-box">
                <p>Ubicación</p>
              </div>
            </div>
          </a>
          <a href="#">
            <div className="item">
              <div className="img-box">
                <img src={ imgTelefono } alt="Teléfono" />
              </div>
              <div className="detail-box">
                <p>+57 1234567890</p>
              </div>
            </div>
          </a>
          <a href="#">
            <div className="item">
              <div className="img-box">
                <img src={ imgEmail } alt="Email" />
              </div>
              <div className="detail-box">
                <p>appet@gmail.com</p>
              </div>
            </div>
          </a>
        </div>
      </section>


      {/* end info_section */}
    </div>
  )
}
