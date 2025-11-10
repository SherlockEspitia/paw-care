import React from 'react'
import './Galeria.css'
import imgGaleria1 from '../../img/imgGaleria1.jpg'
import imgGaleria2 from '../../img/imgGaleria2.jpg'
import imgGaleria3 from '../../img/imgGaleria3.jpg'
import imgGaleria4 from '../../img/imgGaleria4.jpg'
import imgGaleria5 from '../../img/imgGaleria5.jpg'

export const Galeria = () => {
    return (
        <section className ="gallery-section layout_padding">
            <div className ="container">
                <h2>
                    Galeria
                </h2>
            </div>
            <div className ="container ">
                <div className ="img_box box-1">
                    <img src={imgGaleria3} alt="" />
                </div>
                <div className ="img_box box-2">
                    <img src={imgGaleria2} alt="" />
                </div>
                <div className ="img_box box-3">
                    <img src={imgGaleria1} alt="" />
                </div>
                <div className ="img_box box-4">
                    <img src={imgGaleria4} alt="" />
                </div>
                <div className ="img_box box-5">
                    <img src={imgGaleria5} alt="" />
                </div>
            </div>
        </section>

    )
}
