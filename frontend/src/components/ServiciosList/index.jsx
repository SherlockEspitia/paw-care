import { useEffect } from 'react';
import useServicios from '@/hooks/useServicios';
import './ServiciosList.css';

export default function ServiciosList() {
  const {
    items,
    total,
    page,
    perPage,
    loading,
    error,
    setPage,
    setPerPage,
    fetchServicios,
    remove
  } = useServicios({ initialPage: 1, initialPerPage: 10 });

  useEffect(() => {
    fetchServicios({ page, perPage });
  }, [page, perPage, fetchServicios]);

  if (loading) return <div>Cargando servicios...</div>;
  if (error) return <div>Error cargando servicios</div>;

  return (
    <div className="servicios-list">
      <h2>Servicios ({total})</h2>
      <table>
        <thead>
          <tr>
            <th>Nombre</th>
            <th>Descripción</th>
            <th>Precio</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          {items?.map((s) => (
            <tr key={s.id}>
              <td>{s.nombre}</td>
              <td>{s.descripcion}</td>
              <td>${s.precio}</td>
              <td>
                <button onClick={() => {/* navegar a editar */}}>Editar</button>
                <button onClick={() => { if (confirm('Eliminar servicio?')) remove(s.id); }}>Eliminar</button>
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