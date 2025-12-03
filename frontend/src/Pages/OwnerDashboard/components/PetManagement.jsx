import React, { useEffect } from 'react';
import useMascotas from '@/hooks/useMascotas';
import '../styles/PetManagement.css';

export default function PetManagement() {
  const {
    items: mascotas,
    loading,
    error,
    create,
    remove
  } = useMascotas();

  const [showForm, setShowForm] = React.useState(false);
  const [formData, setFormData] = React.useState({
    nombre: '',
    especie: 'perro',
    raza: '',
    edad: '',
    peso: '',
    descripcion: ''
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
        especie: 'perro',
        raza: '',
        edad: '',
        peso: '',
        descripcion: ''
      });
      setShowForm(false);
    } catch (err) {
      console.error('Error creando mascota:', err);
    }
  };

  if (loading) return <div className="loading">Cargando mascotas...</div>;
  if (error) return <div className="error">Error cargando mascotas</div>;

  return (
    <div className="pet-management">
      <div className="pet-header">
        <h2>Mis Mascotas</h2>
        <button className="btn-add-pet" onClick={() => setShowForm(true)}>
          + Agregar Mascota
        </button>
      </div>

      {showForm && (
        <div className="pet-form-container">
          <form className="pet-form" onSubmit={handleSubmit}>
            <h3>Nueva Mascota</h3>
            
            <div className="form-group">
              <label>Nombre</label>
              <input
                type="text"
                name="nombre"
                value={formData.nombre}
                onChange={handleChange}
                required
              />
            </div>

            <div className="form-row">
              <div className="form-group">
                <label>Especie</label>
                <select
                  name="especie"
                  value={formData.especie}
                  onChange={handleChange}
                >
                  <option value="perro">Perro</option>
                  <option value="gato">Gato</option>
                  <option value="conejo">Conejo</option>
                  <option value="pajaro">Pájaro</option>
                  <option value="otro">Otro</option>
                </select>
              </div>

              <div className="form-group">
                <label>Raza</label>
                <input
                  type="text"
                  name="raza"
                  value={formData.raza}
                  onChange={handleChange}
                />
              </div>
            </div>

            <div className="form-row">
              <div className="form-group">
                <label>Edad (años)</label>
                <input
                  type="number"
                  name="edad"
                  value={formData.edad}
                  onChange={handleChange}
                />
              </div>

              <div className="form-group">
                <label>Peso (kg)</label>
                <input
                  type="number"
                  name="peso"
                  value={formData.peso}
                  onChange={handleChange}
                />
              </div>
            </div>

            <div className="form-group">
              <label>Descripción</label>
              <textarea
                name="descripcion"
                value={formData.descripcion}
                onChange={handleChange}
                rows="3"
              />
            </div>

            <div className="form-actions">
              <button type="submit" className="btn-save">
                Guardar Mascota
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

      <div className="pets-grid">
        {mascotas && mascotas.length > 0 ? (
          mascotas.map(mascota => (
            <div key={mascota.id} className="pet-card">
              <div className="pet-card-header">
                <h3>{mascota.nombre}</h3>
                <button
                  className="btn-delete"
                  onClick={() => {
                    if (confirm('¿Eliminar esta mascota?')) {
                      remove(mascota.id);
                    }
                  }}
                >
                  ✕
                </button>
              </div>
              <div className="pet-card-body">
                <p><strong>Especie:</strong> {mascota.especie}</p>
                <p><strong>Raza:</strong> {mascota.raza}</p>
                <p><strong>Edad:</strong> {mascota.edad} años</p>
                <p><strong>Peso:</strong> {mascota.peso} kg</p>
                {mascota.descripcion && (
                  <p><strong>Notas:</strong> {mascota.descripcion}</p>
                )}
              </div>
            </div>
          ))
        ) : (
          <div className="no-pets">
            <p>Aún no tienes mascotas registradas.</p>
            <button className="btn-add-pet" onClick={() => setShowForm(true)}>
              Agregar Primera Mascota
            </button>
          </div>
        )}
      </div>
    </div>
  );
}