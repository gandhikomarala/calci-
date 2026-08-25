"""UserService: User accounts, role assignment, and permissions."""

import { apiClient } from './apiClient';

export const userService = {
  getAll: async (params?: any) => {
    const res = await apiClient.get('/user', { params });
    return res.data;
  },
  getById: async (id: string) => {
    const res = await apiClient.get(`/user/${id}`);
    return res.data;
  },
  create: async (data: any) => {
    const res = await apiClient.post('/user', data);
    return res.data;
  },
  delete: async (id: string) => {
    const res = await apiClient.delete(`/user/${id}`);
    return res.data;
  },
};
