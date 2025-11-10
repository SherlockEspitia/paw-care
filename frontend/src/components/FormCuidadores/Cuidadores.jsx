import  { useState } from "react";
import './Cuidadores.css'

function Cuidadores() {
    const [formData, setFormData] = useState({
        nombres: '',
        apellidos: '',
        email: '',
        telefono: '',
        direccion: '',
        ciudad: ''
    });

    const [errors, setErrors] = useState({});

    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value,
        });

    };

    const validate = () => {
        let formErrors = {};
        if (!formData.nombres.trim()) formErrors.nombres = 'Nombre es requerido';
        if (!formData.apellidos.trim()) formErrors.apellidos = 'Apellidos son requeridos';
        if (!formData.email.trim() || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(formData.email))
            formErrors.email = 'Correo electrónico no es válido';
        if (!formData.telefono.trim() || !/^\d{10}$/.test(formData.telefono))
            formErrors.telefono = 'Teléfono debe tener 10 dígitos';
        if (!formData.direccion.trim()) formErrors.direccion = 'Dirección es requerida';
        if (!formData.ciudad.trim()) formErrors.ciudad = 'Ciudad es requerida';

        return formErrors;
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        
        const validationErrors = validate();
        if (Object.keys(validationErrors).length > 0) {
            setErrors(validationErrors);
        } else {
            alert('Formulario enviado con éxito');
            setErrors({});

            setFormData({
                nombres: '',
                apellidos: '',
                email: '',
                telefono: '',
                direccion: '',
                ciudad: ''
            });
        }
    };

    return (
        <div className="form-container">
            <div className="form-wrapper">
                <h2>Registro Cuidadores</h2>
                <form onSubmit={handleSubmit}>
                    <div className="form-group">
                        <label htmlFor="nombres">Nombres</label>
                        <input
                            type="text"
                            id="nombres"
                            name="nombres"
                            value={formData.nombres}
                            onChange={handleChange}
                        />
                        {errors.nombres && <span className="error">{errors.nombres}</span>}
                    </div>

                    <div className="form-group">
                        <label htmlFor="apellidos">Apellidos</label>
                        <input
                            type="text"
                            id="apellidos"
                            name="apellidos"
                            value={formData.apellidos}
                            onChange={handleChange}
                        />
                        {errors.apellidos && <span className="error">{errors.apellidos}</span>}
                    </div>

                    <div className="form-group">
                        <label htmlFor="email">Correo Electrónico</label>
                        <input
                            type="text"
                            id="email"
                            name="email"
                            value={formData.email}
                            onChange={handleChange}
                        />
                        {errors.email && <span className="error">{errors.email}</span>}
                    </div>

                    <div className="form-group">
                        <label htmlFor="telefono">Teléfono</label>
                        <input
                            type="text"
                            id="telefono"
                            name="telefono"
                            value={formData.telefono}
                            onChange={handleChange}
                        />
                        {errors.telefono && <span className="error">{errors.telefono}</span>}
                    </div>

                    <div className="form-group">
                        <label htmlFor="direccion">Dirección</label>
                        <input
                            type="text"
                            id="direccion"
                            name="direccion"
                            value={formData.direccion}
                            onChange={handleChange}
                        />
                        {errors.direccion && <span className="error">{errors.direccion}</span>}
                    </div>

                    <div className="form-group">
                        <label htmlFor="ciudad">Ciudad</label>
                        <input
                            type="text"
                            id="ciudad"
                            name="ciudad"
                            value={formData.ciudad}
                            onChange={handleChange}
                        />
                        {errors.ciudad && <span className="error">{errors.ciudad}</span>}
                    </div>

                    <button type="submit" className="btn-submit">Enviar</button>
                </form>
            </div>
        </div>
    );
}

export default Cuidadores