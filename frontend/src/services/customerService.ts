import { apiClient } from './apiClient';
import { Customer, Customer360 } from '../types';

export const customerService = {
  getCustomers: async (page = 1, pageSize = 20, search?: string) => {
    const params: any = { page, page_size: pageSize };
    if (search) params.search = search;
    const response = await apiClient.get<{ items: Customer[]; total: number }>('/customers', { params });
    return response.data;
  },

  getCustomer360: async (customerId: string) => {
    const response = await apiClient.get<Customer360>(`/customers/${customerId}`);
    return response.data;
  },
};
