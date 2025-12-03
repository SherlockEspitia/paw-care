import { useEffect } from 'react';
import useMascotas from '@/hooks/useMascotas';
import './MascotasList.css';

export default function MascotasList() {
  const {
    items,
    total,
    page,
    perPage,
    loading,
    error,
    setPage,
    setPerPage,
    fetchMascotas,
    remove
  } = useMascotas({ initialPage: 1, initialPerPage: 10 });

  useEffect(() => {
    fetchMascotas({ page, perPage });
  }, [page, perPage, fetchMascotas]);

  if (loading) return <div>Cargando mascotas...</div>;
  if (error) return <div>Error cargando mascotas</div>;

  return (
    <div className="mascotas-list">
      <h2>Mascotas ({total})</h2>
      <table>
        <thead>
          <tr>
            <th>Nombre</th>
            <th>Especie</th>
            <th>Raza</th>
            <th>Propietario</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          {items?.map((m) => (
            <tr key={m.id}>
              <td>{m.nombre}</td>
              <td>{m.especie}</td>
              <td>{m.raza}</td>
              <td>{m.propietario?.nombre || m.propietario_id}</td>
              <td>
                <button onClick={() => {/* navegar a editar */}}>Editar</button>
                <button onClick={() => { if (confirm('Eliminar mascota?')) remove(m.id); }}>Eliminar</button>
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