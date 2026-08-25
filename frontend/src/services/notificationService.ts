"""NotificationService: User alerts and webhook channel configurations."""

import { apiClient } from './apiClient';

export const notificationService = {
  getAll: async (params?: any) => {
    const res = await apiClient.get('/notification', { params });
    return res.data;
  },
  getById: async (id: string) => {
    const res = await apiClient.get(`/notification/${id}`);
    return res.data;
  },
  create: async (data: any) => {
    const res = await apiClient.post('/notification', data);
    return res.data;
  },
  delete: async (id: string) => {
    const res = await apiClient.delete(`/notification/${id}`);
    return res.data;
  },
};
