import React, { useState } from "react";
import "./AgendarCita.css";

export const AgendarCita = () => {
    const [selectedDate, setSelectedDate] = useState("");
    const [selectedService, setSelectedService] = useState("");
    const [name, setName] = useState("");
    const [phone, setPhone] = useState("");

    const handleSubmit = (e) => {
        e.preventDefault();
        if (!name || !phone || !selectedDate || !selectedService) {
            alert("Por favor completa todos los campos.");
            return;
        }
        alert(`✅ Cita agendada para ${name} el ${selectedDate} para ${selectedService}.`);
        setName("");
        setPhone("");
        setSelectedDate("");
        setSelectedService("");
    };

    return (
        <section className="agendar-section">
            <div className="agendar-container">
                <h2>Agendar una Cita</h2>
                <p>Selecciona el servicio y la fecha que mejor se ajusten a ti 🐾</p>

                <form className="agendar-form" onSubmit={handleSubmit}>
                    <label>Nombre del propietario:</label>
                    <input
                        type="text"
                        value={name}
                        onChange={(e) => setName(e.target.value)}
                        placeholder="Tu nombre completo"
                    />

                    <label>Teléfono de contacto:</label>
                    <input
                        type="tel"
                        value={phone}
                        onChange={(e) => setPhone(e.target.value)}
                        placeholder="Ej: 3001234567"
                    />

                    <label>Servicio:</label>
                    <select
                        value={selectedService}
                        onChange={(e) => setSelectedService(e.target.value)}
                    >
                        <option value="">Seleccionar servicio</option>
                        <option value="Paseo">Paseo</option>
                        <option value="Guardería">Guardería</option>
                        <option value="Adiestramiento">Adiestramiento</option>
                    </select>

                    <label>Fecha:</label>
                    <input
                        type="date"
                        value={selectedDate}
                        onChange={(e) => setSelectedDate(e.target.value)}
                    />

                    <button type="submit" className="btn-agendar">Agendar cita</button>
                </form>
            </div>
        </section>
    );
};
