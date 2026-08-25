"""ExperimentService: Experiment tracking, training run comparisons."""

import { apiClient } from './apiClient';

export const experimentService = {
  getAll: async (params?: any) => {
    const res = await apiClient.get('/experiment', { params });
    return res.data;
  },
  getById: async (id: string) => {
    const res = await apiClient.get(`/experiment/${id}`);
    return res.data;
  },
  create: async (data: any) => {
    const res = await apiClient.post('/experiment', data);
    return res.data;
  },
  delete: async (id: string) => {
    const res = await apiClient.delete(`/experiment/${id}`);
    return res.data;
  },
};
