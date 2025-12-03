import React from 'react';
import '../styles/CaregiverProfile.css';

export default function CaregiverProfile({ caregiverType }) {
  const [profile, setProfile] = React.useState({
    nombre: 'María García',
    email: 'maria@example.com',
    telefono: '555-5678',
    direccion: 'Calle Secundaria 456',
    ciudad: 'Barcelona',
    tipo: caregiverType,
    calificacion: 4.8,
    experiencia: '5 años',
    descripcion: 'Profesional dedicada al cuidado de mascotas'
  });

  const [isEditing, setIsEditing] = React.useState(false);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setProfile(prev => ({ ...prev, [name]: value }));
  };

  const handleSave = () => {
    setIsEditing(false);
  };

  const getTypeLabel = (type) => {
    const labels = {
      guarderia: 'Guardería',
      adiestrador: 'Adiestrador',
      paseador: 'Paseador'
    };
    return labels[type] || type;
  };

  return (
    <div className="caregiver-profile">
      <div className="profile-card">
        <div className="profile-header">
          <h2>{profile.nombre}</h2>
          <span className="profile-type">{getTypeLabel(profile.tipo)}</span>
        </div>

        <div className="profile-stats">
          <div className="stat">
            <span className="stat-value">⭐ {profile.calificacion}</span>
            <span className="stat-label">Calificación</span>
          </div>
          <div className="stat">
            <span className="stat-value">{profile.experiencia}</span>
            <span className="stat-label">Experiencia</span>
          </div>
        </div>

        <div className="profile-content">
          {!isEditing ? (
            <div className="profile-view">
              <p><strong>Email:</strong> {profile.email}</p>
              <p><strong>Teléfono:</strong> {profile.telefono}</p>
              <p><strong>Dirección:</strong> {profile.direccion}</p>
              <p><strong>Ciudad:</strong> {profile.ciudad}</p>
              <p><strong>Descripción:</strong> {profile.descripcion}</p>
              <button className="btn-edit" onClick={() => setIsEditing(true)}>
                Editar Perfil
              </button>
            </div>
          ) : (
            <form className="profile-form">
              <div className="form-group">
                <label>Nombre</label>
                <input
                  type="text"
                  name="nombre"
                  value={profile.nombre}
                  onChange={handleChange}
                />
              </div>
              <div className="form-group">
                <label>Email</label>
                <input
                  type="email"
                  name="email"
                  value={profile.email}
                  onChange={handleChange}
                />
              </div>
              <div className="form-group">
                <label>Teléfono</label>
                <input
                  type="tel"
                  name="telefono"
                  value={profile.telefono}
                  onChange={handleChange}
                />
              </div>
              <div className="form-group">
                <label>Dirección</label>
                <input
                  type="text"
                  name="direccion"
                  value={profile.direccion}
                  onChange={handleChange}
                />
              </div>
              <div className="form-group">
                <label>Ciudad</label>
                <input
                  type="text"
                  name="ciudad"
                  value={profile.ciudad}
                  onChange={handleChange}
                />
              </div>
              <div className="form-group">
                <label>Descripción</label>
                <textarea
                  name="descripcion"
                  value={profile.descripcion}
                  onChange={handleChange}
                  rows="4"
                />
              </div>
              <div className="form-actions">
                <button
                  type="button"
                  className="btn-save"
                  onClick={handleSave}
                >
                  Guardar
                </button>
                <button
                  type="button"
                  className="btn-cancel"
                  onClick={() => setIsEditing(false)}
                >
                  Cancelar
                </button>
              </div>
            </form>
          )}
        </div>
      </div>
    </div>
  );
}