import apiClient from './apiClient';

const BASE_PATH = '/agenda';

export const listAgenda = async (params = {}) => {
  const res = await apiClient.get(BASE_PATH, { params });
  return res.data;
};

export const getAgenda = async (id) => {
  const res = await apiClient.get(`${BASE_PATH}/${id}`);
  return res.data;
};

export const createAgenda = async (payload) => {
  const res = await apiClient.post(BASE_PATH, payload);
  return res.data;
};

export const updateAgenda = async (id, payload) => {
  const res = await apiClient.put(`${BASE_PATH}/${id}`, payload);
  return res.data;
};

export const deleteAgenda = async (id) => {
  const res = await apiClient.delete(`${BASE_PATH}/${id}`);
  return res.data;
};

export default {
  listAgenda,
  getAgenda,
  createAgenda,
  updateAgenda,
  deleteAgenda
};