"""BatchService: Asynchronous batch inference job management."""

import { apiClient } from './apiClient';

export const batchService = {
  getAll: async (params?: any) => {
    const res = await apiClient.get('/batch', { params });
    return res.data;
  },
  getById: async (id: string) => {
    const res = await apiClient.get(`/batch/${id}`);
    return res.data;
  },
  create: async (data: any) => {
    const res = await apiClient.post('/batch', data);
    return res.data;
  },
  delete: async (id: string) => {
    const res = await apiClient.delete(`/batch/${id}`);
    return res.data;
  },
};
