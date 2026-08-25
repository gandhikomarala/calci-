"""alertStore: Real-time incoming fraud alerts, active filters, and triage queue."""

import { create } from 'zustand';

interface AlertStoreState {
  data: any[];
  selectedItem: any | null;
  isLoading: boolean;
  error: string | null;
  setData: (data: any[]) => void;
  setSelectedItem: (item: any) => void;
  setLoading: (loading: boolean) => void;
  setError: (err: string | null) => void;
  reset: () => void;
}

export const useAlertStore = create<AlertStoreState>((set) => ({
  data: [],
  selectedItem: null,
  isLoading: false,
  error: null,
  setData: (data) => set({ data }),
  setSelectedItem: (selectedItem) => set({ selectedItem }),
  setLoading: (isLoading) => set({ isLoading }),
  setError: (error) => set({ error }),
  reset: () => set({ data: [], selectedItem: null, isLoading: false, error: null }),
}));
