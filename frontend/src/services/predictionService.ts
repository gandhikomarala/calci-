import { apiClient } from './apiClient';
import { PredictionResult } from '../types';

export const predictionService = {
  predictSingle: async (payload: any) => {
    const response = await apiClient.post<PredictionResult>('/predictions', payload);
    return response.data;
  },
};
