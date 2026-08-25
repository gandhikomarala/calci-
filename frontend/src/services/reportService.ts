"""ReportService: PDF/CSV/JSON report generation and downloads."""

import { apiClient } from './apiClient';

export const reportService = {
  getAll: async (params?: any) => {
    const res = await apiClient.get('/report', { params });
    return res.data;
  },
  getById: async (id: string) => {
    const res = await apiClient.get(`/report/${id}`);
    return res.data;
  },
  create: async (data: any) => {
    const res = await apiClient.post('/report', data);
    return res.data;
  },
  delete: async (id: string) => {
    const res = await apiClient.delete(`/report/${id}`);
    return res.data;
  },
};
