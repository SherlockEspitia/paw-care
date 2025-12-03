import { useEffect } from 'react';
import useAgenda from '@/hooks/useAgenda';
import './AgendaList.css';

export default function AgendaList() {
  const {
    items,
    total,
    page,
    perPage,
    loading,
    error,
    setPage,
    setPerPage,
    fetchAgenda,
    remove
  } = useAgenda({ initialPage: 1, initialPerPage: 10 });

  useEffect(() => {
    fetchAgenda({ page, perPage });
  }, [page, perPage, fetchAgenda]);

  if (loading) return <div>Cargando agenda...</div>;
  if (error) return <div>Error cargando agenda</div>;

  return (
    <div className="agenda-list">
      <h2>Agenda ({total})</h2>
      <table>
        <thead>
          <tr>
            <th>Cuidador</th>
            <th>Mascota</th>
            <th>Fecha</th>
            <th>Hora</th>
            <th>Estado</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          {items?.map((a) => (
            <tr key={a.id}>
              <td>{a.cuidador?.nombre || a.cuidador_id}</td>
              <td>{a.mascota?.nombre || a.mascota_id}</td>
              <td>{new Date(a.fecha).toLocaleDateString()}</td>
              <td>{a.hora}</td>
              <td>{a.estado || 'Pendiente'}</td>
              <td>
                <button onClick={() => {/* navegar a editar */}}>Editar</button>
                <button onClick={() => { if (confirm('Eliminar cita?')) remove(a.id); }}>Eliminar</button>
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