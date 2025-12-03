import { useState, useEffect, useCallback } from 'react';
import * as service from '@/services/cuidadoresService';

export default function useCuidadores({ initialPage = 1, initialPerPage = 10, initialSearch = '' } = {}) {
  const [items, setItems] = useState([]);
  const [total, setTotal] = useState(0);
  const [page, setPage] = useState(initialPage);
  const [perPage, setPerPage] = useState(initialPerPage);
  const [search, setSearch] = useState(initialSearch);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const parseListResponse = (data) => {
    // Adaptador: soporta varias formas de respuesta del backend
    if (!data) return { items: [], total: 0 };
    // Si el wrapper es {items, total}
    if (Array.isArray(data)) return { items: data, total: data.length };
    if (data.items && typeof data.total !== 'undefined') return { items: data.items, total: data.total };
    if (data.data && data.meta) return { items: data.data, total: data.meta.total ?? data.meta.totalItems ?? data.meta.count };
    if (data.data && Array.isArray(data.data)) return { items: data.data, total: data.data.length };
    // fallback
    return { items: data, total: Array.isArray(data) ? data.length : 1 };
  };

  const fetchCuidadores = useCallback(async (opts = {}) => {
    setLoading(true);
    setError(null);

    const params = {
      page: opts.page ?? page,
      limit: opts.perPage ?? perPage,
      search: opts.search ?? search,
      ...opts
    };
    try {
      const resp = await service.listCuidadores(params);
      const { items: parsedItems, total: parsedTotal } = parseListResponse(resp);
      setItems(parsedItems);
      setTotal(parsedTotal ?? parsedItems.length);
      setPage(params.page);
      setPerPage(params.limit);
    } catch (err) {
      setError(err);
    } finally {
      setLoading(false);
    }
  }, [page, perPage, search]);

  useEffect(() => {
    // Carga inicial
    fetchCuidadores();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  const refresh = useCallback(() => fetchCuidadores({ page, perPage, search }), [fetchCuidadores, page, perPage, search]);

  const getCuidadorById = useCallback(async (id) => {
    setLoading(true);
    try {
      const resp = await service.getCuidador(id);
      return resp;
    } catch (err) {
      setError(err);
      throw err;
    } finally {
      setLoading(false);
    }
  }, []);

  const createCuidador = useCallback(async (payload) => {
    setLoading(true);
    try {
      const created = await service.createCuidador(payload);
      // Refresh list (puedes hacer un push local si prefieres optimista)
      await refresh();
      return created;
    } catch (err) {
      setError(err);
      throw err;
    } finally {
      setLoading(false);
    }
  }, [refresh]);

  const updateCuidador = useCallback(async (id, payload) => {
    setLoading(true);
    try {
      const updated = await service.updateCuidador(id, payload);
      await refresh();
      return updated;
    } catch (err) {
      setError(err);
      throw err;
    } finally {
      setLoading(false);
    }
  }, [refresh]);

  const deleteCuidador = useCallback(async (id) => {
    setLoading(true);
    try {
      const deleted = await service.deleteCuidador(id);
      await refresh();
      return deleted;
    } catch (err) {
      setError(err);
      throw err;
    } finally {
      setLoading(false);
    }
  }, [refresh]);

  return {
    items,
    total,
    page,
    perPage,
    search,
    loading,
    error,
    // setters para controles de UI:
    setPage,
    setPerPage,
    setSearch,
    // acciones CRUD:
    fetchCuidadores,
    refresh,
    getCuidadorById,
    createCuidador,
    updateCuidador,
    deleteCuidador
  };
}