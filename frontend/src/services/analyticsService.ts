"""AnalyticsService: Executive metrics, cohort analysis, and revenue-at-risk."""

import { apiClient } from './apiClient';

export const analyticsService = {
  getAll: async (params?: any) => {
    const res = await apiClient.get('/analytics', { params });
    return res.data;
  },
  getById: async (id: string) => {
    const res = await apiClient.get(`/analytics/${id}`);
    return res.data;
  },
  create: async (data: any) => {
    const res = await apiClient.post('/analytics', data);
    return res.data;
  },
  delete: async (id: string) => {
    const res = await apiClient.delete(`/analytics/${id}`);
    return res.data;
  },
};
