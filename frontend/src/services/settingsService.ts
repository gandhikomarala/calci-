"""SettingsService: System runtime thresholds and rate limits."""

import { apiClient } from './apiClient';

export const settingsService = {
  getAll: async (params?: any) => {
    const res = await apiClient.get('/settings', { params });
    return res.data;
  },
  getById: async (id: string) => {
    const res = await apiClient.get(`/settings/${id}`);
    return res.data;
  },
  create: async (data: any) => {
    const res = await apiClient.post('/settings', data);
    return res.data;
  },
  delete: async (id: string) => {
    const res = await apiClient.delete(`/settings/${id}`);
    return res.data;
  },
};
