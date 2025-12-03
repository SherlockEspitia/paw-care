import apiClient from './apiClient';

const BASE_PATH = '/calificacion-cuidador';

export const listCalificaciones = async (params = {}) => {
  const res = await apiClient.get(BASE_PATH, { params });
  return res.data;
};

export const getCalificacion = async (id) => {
  const res = await apiClient.get(`${BASE_PATH}/${id}`);
  return res.data;
};

export const createCalificacion = async (payload) => {
  const res = await apiClient.post(BASE_PATH, payload);
  return res.data;
};

export const updateCalificacion = async (id, payload) => {
  const res = await apiClient.put(`${BASE_PATH}/${id}`, payload);
  return res.data;
};

export const deleteCalificacion = async (id) => {
  const res = await apiClient.delete(`${BASE_PATH}/${id}`);
  return res.data;
};

export default {
  listCalificaciones,
  getCalificacion,
  createCalificacion,
  updateCalificacion,
  deleteCalificacion
};