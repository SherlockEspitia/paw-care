import React, { useEffect } from 'react';
import useCuidadores from '@/hooks/useCuidadores';
import './CuidadoresList.css'; // crea estilos si te interesa

export default function CuidadoresList() {
  const {
    items,
    total,
    page,
    perPage,
    loading,
    error,
    setPage,
    setPerPage,
    fetchCuidadores,
    deleteCuidador
  } = useCuidadores({ initialPage: 1, initialPerPage: 10 });

  useEffect(() => {
    // fetch se llama por defecto en el hook, pero si necesitas refetch manual:
    fetchCuidadores({ page, perPage });
  }, [page, perPage, fetchCuidadores]);

  if (loading) return <div>Loading cuidadores...</div>;
  if (error) return <div>Error cargando cuidadores</div>;

  return (
    <div className="cuidadores-list">
      <h2>Cuidadores ({total})</h2>
      <table>
        <thead>
          <tr>
            <th>Nombre</th>
            <th>Telefono</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          {items?.map((c) => (
            <tr key={c.id}>
              <td>{c.nombre || `${c.first_name} ${c.last_name}`}</td>
              <td>{c.telefono}</td>
              <td>
                <button onClick={() => {/* navigate to edit */}}>Edit</button>
                <button onClick={() => deleteCuidador(c.id)}>Delete</button>
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