import React, { useEffect } from 'react';
import usePropietarios from '@/hooks/usePropietarios';
import './Propietarios.css';

export default function PropietariosList() {
  const {
    items,
    total,
    page,
    perPage,
    loading,
    error,
    setPage,
    setPerPage,
    fetchPropietarios,
    remove
  } = usePropietarios({ initialPage: 1, initialPerPage: 10 });

  useEffect(() => {
    fetchPropietarios({ page, perPage });
  }, [page, perPage, fetchPropietarios]);

  if (loading) return <div>Cargando propietarios...</div>;
  if (error) return <div>Error cargando propietarios</div>;

  return (
    <div className="propietarios-list">
      <h2>Propietarios ({total})</h2>
      <table>
        <thead>
          <tr>
            <th>Nombre</th>
            <th>Teléfono</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          {items?.map((p) => (
            <tr key={p.id}>
              <td>{p.nombre || `${p.first_name ?? ''} ${p.last_name ?? ''}`}</td>
              <td>{p.telefono ?? p.phone}</td>
              <td>
                <button onClick={() => {/* navegar a editar */}}>Editar</button>
                <button onClick={() => { if (confirm('Eliminar propietario?')) remove(p.id); }}>Eliminar</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>

      <div className="pagination">
        <button disabled={page <= 1} onClick={() => setPage(page - 1)}>Prev</button>
        <span>Page {page}</span>
        <button onClick={() => setPage(page + 1)}>Next</button>

        <select value={perPage} onChange={(e) => setPerPage(Number(e.target.value))}>
          <option value={10}>10</option>
          <option value={25}>25</option>
          <option value={50}>50</option>
        </select>
      </div>
    </div>
  );
}