"""DriftService: Data drift reports, PSI metrics, and retraining alerts."""

import { apiClient } from './apiClient';

export const driftService = {
  getAll: async (params?: any) => {
    const res = await apiClient.get('/drift', { params });
    return res.data;
  },
  getById: async (id: string) => {
    const res = await apiClient.get(`/drift/${id}`);
    return res.data;
  },
  create: async (data: any) => {
    const res = await apiClient.post('/drift', data);
    return res.data;
  },
  delete: async (id: string) => {
    const res = await apiClient.delete(`/drift/${id}`);
    return res.data;
  },
};
