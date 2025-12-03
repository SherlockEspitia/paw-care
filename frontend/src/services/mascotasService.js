import apiClient from './apiClient';

const BASE_PATH = '/mascotas';

export const listMascotas = async (params = {}) => {
  const res = await apiClient.get(BASE_PATH, { params });
  return res.data;
};

export const getMascota = async (id) => {
  const res = await apiClient.get(`${BASE_PATH}/${id}`);
  return res.data;
};

export const createMascota = async (payload) => {
  const res = await apiClient.post(BASE_PATH, payload);
  return res.data;
};

export const updateMascota = async (id, payload) => {
  const res = await apiClient.put(`${BASE_PATH}/${id}`, payload);
  return res.data;
};

export const deleteMascota = async (id) => {
  const res = await apiClient.delete(`${BASE_PATH}/${id}`);
  return res.data;
};

export default {
  listMascotas,
  getMascota,
  createMascota,
  updateMascota,
  deleteMascota
};