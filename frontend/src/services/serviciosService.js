import apiClient from './apiClient';

const BASE_PATH = '/servicios';

export const listServicios = async (params = {}) => {
  const res = await apiClient.get(BASE_PATH, { params });
  return res.data;
};

export const getServicio = async (id) => {
  const res = await apiClient.get(`${BASE_PATH}/${id}`);
  return res.data;
};

export const createServicio = async (payload) => {
  const res = await apiClient.post(BASE_PATH, payload);
  return res.data;
};

export const updateServicio = async (id, payload) => {
  const res = await apiClient.put(`${BASE_PATH}/${id}`, payload);
  return res.data;
};

export const deleteServicio = async (id) => {
  const res = await apiClient.delete(`${BASE_PATH}/${id}`);
  return res.data;
};

export default {
  listServicios,
  getServicio,
  createServicio,
  updateServicio,
  deleteServicio
};