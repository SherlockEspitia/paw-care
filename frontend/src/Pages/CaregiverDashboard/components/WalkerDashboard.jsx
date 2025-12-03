import React, { useState } from 'react';
import useServicios from '@/hooks/useServicios';
import '../styles/SpecialtiesDashboard.css';

export default function WalkerDashboard() {
  const { items: servicios, create, remove } = useServicios();
  const [showForm, setShowForm] = useState(false);
  const [formData, setFormData] = useState({
    nombre: '',
    descripcion: '',
    precio: '',
    duracion: 30,
    distancia_aproximada: '',
    tamano_perro: 'todos',
    horarios_disponibles: ''
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await create(formData);
      setFormData({
        nombre: '',
        descripcion: '',
        precio: '',
        duracion: 30,
        distancia_aproximada: '',
        tamano_perro: 'todos',
        horarios_disponibles: ''
      });
      setShowForm(false);
      alert('¡Servicio de paseo creado!');
    } catch (err) {
      console.error('Error:', err);
    }
  };

  return (
    <div className="specialty-dashboard walker">
      <div className="dashboard-header">
        <h2>🐕 Mis Servicios de Paseo</h2>
        <button className="btn-add-service" onClick={() => setShowForm(true)}>
          + Nuevo Servicio
        </button>
      </div>

      {showForm && (
        <div className="service-form-container">
          <form className="service-form" onSubmit={handleSubmit}>
            <h3>Crear Servicio de Paseo</h3>

            <div className="form-group">
              <label>Nombre del Servicio</label>
              <input
                type="text"
                name="nombre"
                placeholder="ej: Paseo Matutino 30 minutos"
                value={formData.nombre}
                onChange={handleChange}
                required
              />
            </div>

            <div className="form-group">
              <label>Descripción</label>
              <textarea
                name="descripcion"
                placeholder="Describe tu servicio de paseo"
                value={formData.descripcion}
                onChange={handleChange}
                rows="3"
                required
              />
            </div>

            <div className="form-row">
              <div className="form-group">
                <label>Duración (minutos)</label>
                <select
                  name="duracion"
                  value={formData.duracion}
                  onChange={handleChange}
                >
                  <option value={15}>15 minutos</option>
                  <option value={30}>30 minutos</option>
                  <option value={45}>45 minutos</option>
                  <option value={60}>60 minutos</option>
                  <option value={90}>90 minutos</option>
                </select>
              </div>

              <div className="form-group">
                <label>Precio (€)</label>
                <input
                  type="number"
                  name="precio"
                  value={formData.precio}
                  onChange={handleChange}
                  required
                />
              </div>
            </div>

            <div className="form-row">
              <div className="form-group">
                <label>Tamaño de Perro</label>
                <select
                  name="tamano_perro"
                  value={formData.tamano_perro}
                  onChange={handleChange}
                >
                  <option value="pequeno">Pequeño (< 5kg)</option>
                  <option value="mediano">Mediano (5-15kg)</option>
                  <option value="grande">Grande (15-30kg)</option>
                  <option value="gigante">Gigante (> 30kg)</option>
                  <option value="todos">Todos los tamaños</option>
                </select>
              </div>

              <div className="form-group">
                <label>Distancia Aproximada (km)</label>
                <input
                  type="number"
                  name="distancia_aproximada"
                  placeholder="ej: 2 km"
                  value={formData.distancia_aproximada}
                  onChange={handleChange}
                />
              </div>
            </div>

            <div className="form-group">
              <label>Horarios Disponibles</label>
              <input
                type="text"
                name="horarios_disponibles"
                placeholder="ej: Mañana (8-12), Tarde (16-20)"
                value={formData.horarios_disponibles}
                onChange={handleChange}
              />
            </div>

            <div className="form-actions">
              <button type="submit" className="btn-save">
                Crear Servicio
              </button>
              <button
                type="button"
                className="btn-cancel"
                onClick={() => setShowForm(false)}
              >
                Cancelar
              </button>
            </div>
          </form>
        </div>
      )}

      <div className="services-list">
        {servicios && servicios.length > 0 ? (
          servicios.map(servicio => (
            <div key={servicio.id} className="service-item">
              <div className="service-info">
                <h3>{servicio.nombre}</h3>
                <p>{servicio.descripcion}</p>
                <div className="service-details">
                  <span>💰 €{servicio.precio}</span>
                  <span>⏱️ {servicio.duracion || 30} minutos</span>
                  {servicio.distancia_aproximada && (
                    <span>📍 ~{servicio.distancia_aproximada} km</span>
                  )}
                </div>
                {servicio.horarios_disponibles && (
                  <p className="service-schedule">📅 {servicio.horarios_disponibles}</p>
                )}
              </div>
              <div className="service-actions">
                <button className="btn-edit">Editar</button>
                <button className="btn-delete" onClick={() => remove(servicio.id)}>
                  Eliminar
                </button>
              </div>
            </div>
          ))
        ) : (
          <div className="no-services">
            <p>Aún no tienes servicios de paseo</p>
            <button className="btn-add-service" onClick={() => setShowForm(true)}>
              Crear Primer Servicio
            </button>
          </div>
        )}
      </div>
    </div>
  );
}