import React, { useEffect } from 'react';
import useServicios from '@/hooks/useServicios';
import useAgenda from '@/hooks/useAgenda';
import useMascotas from '@/hooks/useMascotas';
import '../styles/ServiceBooking.css';

export default function ServiceBooking() {
  const { items: servicios, loading: loadingServicios } = useServicios();
  const { items: agendas, create: createAgenda, loading: loadingAgenda } = useAgenda();
  const { items: mascotas } = useMascotas();

  const [showForm, setShowForm] = React.useState(false);
  const [selectedServicio, setSelectedServicio] = React.useState(null);
  const [formData, setFormData] = React.useState({
    mascota_id: '',
    cuidador_id: '',
    fecha: '',
    hora: '',
    notas: ''
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await createAgenda(formData);
      setFormData({
        mascota_id: '',
        cuidador_id: '',
        fecha: '',
        hora: '',
        notas: ''
      });
      setShowForm(false);
      alert('¡Servicio agendado exitosamente!');
    } catch (err) {
      console.error('Error agendando servicio:', err);
    }
  };

  if (loadingServicios) return <div className="loading">Cargando servicios...</div>;

  return (
    <div className="service-booking">
      <div className="booking-header">
        <h2>Agendar Servicios</h2>
        <p>Selecciona un servicio y agenda una cita con un cuidador</p>
      </div>

      <div className="services-grid">
        {servicios && servicios.length > 0 ? (
          servicios.map(servicio => (
            <div key={servicio.id} className="service-card">
              <div className="service-card-header">
                <h3>{servicio.nombre}</h3>
                <span className="service-price">${servicio.precio}</span>
              </div>
              <div className="service-card-body">
                <p>{servicio.descripcion}</p>
                <button
                  className="btn-book"
                  onClick={() => {
                    setSelectedServicio(servicio);
                    setShowForm(true);
                  }}
                >
                  Agendar
                </button>
              </div>
            </div>
          ))
        ) : (
          <p className="no-services">No hay servicios disponibles en este momento</p>
        )}
      </div>

      {showForm && selectedServicio && (
        <div className="booking-form-overlay">
          <div className="booking-form-container">
            <form className="booking-form" onSubmit={handleSubmit}>
              <h3>Agendar: {selectedServicio.nombre}</h3>

              <div className="form-group">
                <label>Mascota</label>
                <select
                  name="mascota_id"
                  value={formData.mascota_id}
                  onChange={handleChange}
                  required
                >
                  <option value="">Selecciona una mascota</option>
                  {mascotas && mascotas.map(m => (
                    <option key={m.id} value={m.id}>
                      {m.nombre}
                    </option>
                  ))}
                </select>
              </div>

              <div className="form-group">
                <label>Fecha</label>
                <input
                  type="date"
                  name="fecha"
                  value={formData.fecha}
                  onChange={handleChange}
                  required
                />
              </div>

              <div className="form-group">
                <label>Hora</label>
                <input
                  type="time"
                  name="hora"
                  value={formData.hora}
                  onChange={handleChange}
                  required
                />
              </div>

              <div className="form-group">
                <label>Notas adicionales</label>
                <textarea
                  name="notas"
                  value={formData.notas}
                  onChange={handleChange}
                  rows="3"
                  placeholder="Información adicional sobre la cita"
                />
              </div>

              <div className="form-actions">
                <button type="submit" className="btn-save" disabled={loadingAgenda}>
                  {loadingAgenda ? 'Agendando...' : 'Confirmar Cita'}
                </button>
                <button
                  type="button"
                  className="btn-cancel"
                  onClick={() => {
                    setShowForm(false);
                    setSelectedServicio(null);
                  }}
                >
                  Cancelar
                </button>
              </div>
            </form>
          </div>
        </div>
      )}

      <div className="upcoming-bookings">
        <h3>Próximas Citas</h3>
        {agendas && agendas.length > 0 ? (
          <div className="bookings-list">
            {agendas.map(agenda => (
              <div key={agenda.id} className="booking-item">
                <div className="booking-date">
                  <p className="date">{new Date(agenda.fecha).toLocaleDateString()}</p>
                  <p className="time">{agenda.hora}</p>
                </div>
                <div className="booking-details">
                  <p><strong>Mascota:</strong> {agenda.mascota?.nombre}</p>
                  <p><strong>Cuidador:</strong> {agenda.cuidador?.nombre}</p>
                  <p><strong>Estado:</strong> <span className="status-pending">{agenda.estado || 'Pendiente'}</span></p>
                </div>
              </div>
            ))}
          </div>
        ) : (
          <p className="no-bookings">No tienes citas agendadas</p>
        )}
      </div>
    </div>
  );
}