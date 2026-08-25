"""FeatureService: Feature catalog and feature engineering pipeline triggers."""

import { apiClient } from './apiClient';

export const featureService = {
  getAll: async (params?: any) => {
    const res = await apiClient.get('/feature', { params });
    return res.data;
  },
  getById: async (id: string) => {
    const res = await apiClient.get(`/feature/${id}`);
    return res.data;
  },
  create: async (data: any) => {
    const res = await apiClient.post('/feature', data);
    return res.data;
  },
  delete: async (id: string) => {
    const res = await apiClient.delete(`/feature/${id}`);
    return res.data;
  },
};
