"""AuthService: Authentication, token refresh, and profile endpoints."""

import { apiClient } from './apiClient';

export const authService = {
  getAll: async (params?: any) => {
    const res = await apiClient.get('/auth', { params });
    return res.data;
  },
  getById: async (id: string) => {
    const res = await apiClient.get(`/auth/${id}`);
    return res.data;
  },
  create: async (data: any) => {
    const res = await apiClient.post('/auth', data);
    return res.data;
  },
  delete: async (id: string) => {
    const res = await apiClient.delete(`/auth/${id}`);
    return res.data;
  },
};
