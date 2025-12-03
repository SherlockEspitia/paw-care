import React from 'react';
import '../styles/OwnerProfile.css';

export default function OwnerProfile() {
  const [profile, setProfile] = React.useState({
    nombre: 'Juan Pérez',
    email: 'juan@example.com',
    telefono: '555-1234',
    direccion: 'Calle Principal 123',
    ciudad: 'Madrid'
  });

  const [isEditing, setIsEditing] = React.useState(false);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setProfile(prev => ({ ...prev, [name]: value }));
  };

  const handleSave = () => {
    // API call aquí
    setIsEditing(false);
  };

  return (
    <div className="owner-profile">
      <div className="profile-card">
        <h2>Mi Perfil</h2>
        
        <div className="profile-content">
          {!isEditing ? (
            <div className="profile-view">
              <p><strong>Nombre:</strong> {profile.nombre}</p>
              <p><strong>Email:</strong> {profile.email}</p>
              <p><strong>Teléfono:</strong> {profile.telefono}</p>
              <p><strong>Dirección:</strong> {profile.direccion}</p>
              <p><strong>Ciudad:</strong> {profile.ciudad}</p>
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