"""ModelService: Model registry, deployment stages, and rollback."""

import { apiClient } from './apiClient';

export const modelService = {
  getAll: async (params?: any) => {
    const res = await apiClient.get('/model', { params });
    return res.data;
  },
  getById: async (id: string) => {
    const res = await apiClient.get(`/model/${id}`);
    return res.data;
  },
  create: async (data: any) => {
    const res = await apiClient.post('/model', data);
    return res.data;
  },
  delete: async (id: string) => {
    const res = await apiClient.delete(`/model/${id}`);
    return res.data;
  },
};
