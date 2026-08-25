"""AuditService: Immutable audit trail event querying."""

import { apiClient } from './apiClient';

export const auditService = {
  getAll: async (params?: any) => {
    const res = await apiClient.get('/audit', { params });
    return res.data;
  },
  getById: async (id: string) => {
    const res = await apiClient.get(`/audit/${id}`);
    return res.data;
  },
  create: async (data: any) => {
    const res = await apiClient.post('/audit', data);
    return res.data;
  },
  delete: async (id: string) => {
    const res = await apiClient.delete(`/audit/${id}`);
    return res.data;
  },
};
