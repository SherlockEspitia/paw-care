import apiClient from './apiClient';

const BASE_PATH = '/propietarios';

export const listPropietarios = async (params = {}) => {
  const res = await apiClient.get(BASE_PATH, { params });
  return res.data;
};

export const getPropietario = async (id) => {
  const res = await apiClient.get(`${BASE_PATH}/${id}`);
  return res.data;
};

export const createPropietario = async (payload) => {
  const res = await apiClient.post(BASE_PATH, payload);
  return res.data;
};

export const updatePropietario = async (id, payload) => {
  const res = await apiClient.put(`${BASE_PATH}/${id}`, payload);
  return res.data;
};

export const deletePropietario = async (id) => {
  const res = await apiClient.delete(`${BASE_PATH}/${id}`);
  return res.data;
};

export default {
  listPropietarios,
  getPropietario,
  createPropietario,
  updatePropietario,
  deletePropietario
};