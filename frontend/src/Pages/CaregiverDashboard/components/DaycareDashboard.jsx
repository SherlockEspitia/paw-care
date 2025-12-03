import React, { useState } from 'react';
import useServicios from '@/hooks/useServicios';
import '../styles/SpecialtiesDashboard.css';

export default function DaycareDashboard() {
  const { items: servicios, create, update, remove, loading } = useServicios();
  const [showForm, setShowForm] = useState(false);
  const [formData, setFormData] = useState({
    nombre: '',
    descripcion: '',
    precio: '',
    capacidad: '',
    horario_inicio: '09:00',
    horario_fin: '18:00',
    edades_minimas: 'todas'
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
        capacidad: '',
        horario_inicio: '09:00',
        horario_fin: '18:00',
        edades_minimas: 'todas'
      });
      setShowForm(false);
      alert('¡Servicio de guardería creado!');
    } catch (err) {
      console.error('Error:', err);
    }
  };

  return (
    <div className="specialty-dashboard daycare">
      <div className="dashboard-header">
        <h2>🏠 Mis Servicios de Guardería</h2>
        <button className="btn-add-service" onClick={() => setShowForm(true)}>
          + Nuevo Servicio
        </button>
      </div>

      {showForm && (
        <div className="service-form-container">
          <form className="service-form" onSubmit={handleSubmit}>
            <h3>Crear Servicio de Guardería</h3>

            <div className="form-group">
              <label>Nombre del Servicio</label>
              <input
                type="text"
                name="nombre"
                placeholder="ej: Guardería Premium"
                value={formData.nombre}
                onChange={handleChange}
                required
              />
            </div>

            <div className="form-group">
              <label>Descripción</label>
              <textarea
                name="descripcion"
                placeholder="Describe tu servicio de guardería"
                value={formData.descripcion}
                onChange={handleChange}
                rows="3"
                required
              />
            </div>

            <div className="form-row">
              <div className="form-group">
                <label>Precio por día (€)</label>
                <input
                  type="number"
                  name="precio"
                  value={formData.precio}
                  onChange={handleChange}
                  required
                />
              </div>

              <div className="form-group">
                <label>Capacidad (mascotas)</label>
                <input
                  type="number"
                  name="capacidad"
                  value={formData.capacidad}
                  onChange={handleChange}
                  required
                />
              </div>
            </div>

            <div className="form-row">
              <div className="form-group">
                <label>Horario de Inicio</label>
                <input
                  type="time"
                  name="horario_inicio"
                  value={formData.horario_inicio}
                  onChange={handleChange}
                />
              </div>

              <div className="form-group">
                <label>Horario de Cierre</label>
                <input
                  type="time"
                  name="horario_fin"
                  value={formData.horario_fin}
                  onChange={handleChange}
                />
              </div>
            </div>

            <div className="form-group">
              <label>Edades Recomendadas</label>
              <select
                name="edades_minimas"
                value={formData.edades_minimas}
                onChange={handleChange}
              >
                <option value="todas">Todas las edades</option>
                <option value="cachorro">Cachorros (0-1 año)</option>
                <option value="adulto">Adultos (1-7 años)</option>
                <option value="senior">Seniors (7+ años)</option>
              </select>
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
                  <span>💰 €{servicio.precio}/día</span>
                  <span>🏠 Capacidad: {servicio.capacidad || 'N/A'}</span>
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
            <p>Aún no tienes servicios de guardería</p>
            <button className="btn-add-service" onClick={() => setShowForm(true)}>
              Crear Primer Servicio
            </button>
          </div>
        )}
      </div>
    </div>
  );
}