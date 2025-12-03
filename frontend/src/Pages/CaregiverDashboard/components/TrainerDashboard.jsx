import React, { useState } from 'react';
import useServicios from '@/hooks/useServicios';
import '../styles/SpecialtiesDashboard.css';

export default function TrainerDashboard() {
  const { items: servicios, create, remove } = useServicios();
  const [showForm, setShowForm] = useState(false);
  const [formData, setFormData] = useState({
    nombre: '',
    descripcion: '',
    precio: '',
    tipo_entrenamiento: 'basico',
    duracion_sesion: 60,
    especializacion: ''
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
        tipo_entrenamiento: 'basico',
        duracion_sesion: 60,
        especializacion: ''
      });
      setShowForm(false);
      alert('¡Servicio de adiestramiento creado!');
    } catch (err) {
      console.error('Error:', err);
    }
  };

  return (
    <div className="specialty-dashboard trainer">
      <div className="dashboard-header">
        <h2>🎓 Mis Servicios de Adiestramiento</h2>
        <button className="btn-add-service" onClick={() => setShowForm(true)}>
          + Nuevo Servicio
        </button>
      </div>

      {showForm && (
        <div className="service-form-container">
          <form className="service-form" onSubmit={handleSubmit}>
            <h3>Crear Servicio de Adiestramiento</h3>

            <div className="form-group">
              <label>Nombre del Servicio</label>
              <input
                type="text"
                name="nombre"
                placeholder="ej: Entrenamiento de Obediencia Básica"
                value={formData.nombre}
                onChange={handleChange}
                required
              />
            </div>

            <div className="form-group">
              <label>Descripción</label>
              <textarea
                name="descripcion"
                placeholder="Describe tu servicio de adiestramiento"
                value={formData.descripcion}
                onChange={handleChange}
                rows="3"
                required
              />
            </div>

            <div className="form-row">
              <div className="form-group">
                <label>Tipo de Entrenamiento</label>
                <select
                  name="tipo_entrenamiento"
                  value={formData.tipo_entrenamiento}
                  onChange={handleChange}
                >
                  <option value="basico">Obediencia Básica</option>
                  <option value="avanzado">Entrenamiento Avanzado</option>
                  <option value="comportamiento">Corrección de Comportamiento</option>
                  <option value="socializacion">Socialización</option>
                  <option value="especial">Entrenamiento Especial</option>
                </select>
              </div>

              <div className="form-group">
                <label>Duración de Sesión (minutos)</label>
                <input
                  type="number"
                  name="duracion_sesion"
                  value={formData.duracion_sesion}
                  onChange={handleChange}
                />
              </div>
            </div>

            <div className="form-row">
              <div className="form-group">
                <label>Precio por Sesión (€)</label>
                <input
                  type="number"
                  name="precio"
                  value={formData.precio}
                  onChange={handleChange}
                  required
                />
              </div>

              <div className="form-group">
                <label>Especialización</label>
                <input
                  type="text"
                  name="especializacion"
                  placeholder="ej: Perros Agresivos, Cachorros"
                  value={formData.especializacion}
                  onChange={handleChange}
                />
              </div>
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
                  <span>💰 €{servicio.precio}/sesión</span>
                  <span>⏱️ {servicio.duracion_sesion || 60} minutos</span>
                  {servicio.especializacion && (
                    <span>🎯 {servicio.especializacion}</span>
                  )}
                </div>
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
            <p>Aún no tienes servicios de adiestramiento</p>
            <button className="btn-add-service" onClick={() => setShowForm(true)}>
              Crear Primer Servicio
            </button>
          </div>
        )}
      </div>
    </div>
  );
}