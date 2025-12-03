import { useState, useEffect, useCallback } from 'react';
import * as service from '@/services/propietariosService';

export default function usePropietarios({ initialPage = 1, initialPerPage = 10, initialSearch = '' } = {}) {
  const [items, setItems] = useState([]);
  const [total, setTotal] = useState(0);
  const [page, setPage] = useState(initialPage);
  const [perPage, setPerPage] = useState(initialPerPage);
  const [search, setSearch] = useState(initialSearch);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const parseListResponse = (data) => {
    if (!data) return { items: [], total: 0 };
    if (Array.isArray(data)) return { items: data, total: data.length };
    if (data.items && typeof data.total !== 'undefined') return { items: data.items, total: data.total };
    if (data.data && data.meta) return { items: data.data, total: data.meta.total ?? data.meta.count ?? 0 };
    if (data.data && Array.isArray(data.data)) return { items: data.data, total: data.data.length };
    return { items: data, total: Array.isArray(data) ? data.length : 1 };
  };

  const fetchPropietarios = useCallback(async (opts = {}) => {
    setLoading(true);
    setError(null);
    const params = {
      page: opts.page ?? page,
      limit: opts.perPage ?? perPage,
      search: opts.search ?? search,
      ...opts
    };
    try {
      const resp = await service.listPropietarios(params);
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
    fetchPropietarios();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  const refresh = useCallback(() => fetchPropietarios({ page, perPage, search }), [fetchPropietarios, page, perPage, search]);

  const getPropietarioById = useCallback(async (id) => {
    setLoading(true);
    try {
      const resp = await service.getPropietario(id);
      return resp;
    } catch (err) {
      setError(err);
      throw err;
    } finally {
      setLoading(false);
    }
  }, []);

  const create = useCallback(async (payload) => {
    setLoading(true);
    try {
      const created = await service.createPropietario(payload);
      await refresh();
      return created;
    } catch (err) {
      setError(err);
      throw err;
    } finally {
      setLoading(false);
    }
  }, [refresh]);

  const update = useCallback(async (id, payload) => {
    setLoading(true);
    try {
      const updated = await service.updatePropietario(id, payload);
      await refresh();
      return updated;
    } catch (err) {
      setError(err);
      throw err;
    } finally {
      setLoading(false);
    }
  }, [refresh]);

  const remove = useCallback(async (id) => {
    setLoading(true);
    try {
      const deleted = await service.deletePropietario(id);
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
    setPage,
    setPerPage,
    setSearch,
    fetchPropietarios,
    refresh,
    getPropietarioById,
    create,
    update,
    remove
  };
}