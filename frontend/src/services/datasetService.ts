"""DatasetService: Dataset upload, schema profiling, and quality reports."""

import { apiClient } from './apiClient';

export const datasetService = {
  getAll: async (params?: any) => {
    const res = await apiClient.get('/dataset', { params });
    return res.data;
  },
  getById: async (id: string) => {
    const res = await apiClient.get(`/dataset/${id}`);
    return res.data;
  },
  create: async (data: any) => {
    const res = await apiClient.post('/dataset', data);
    return res.data;
  },
  delete: async (id: string) => {
    const res = await apiClient.delete(`/dataset/${id}`);
    return res.data;
  },
};
