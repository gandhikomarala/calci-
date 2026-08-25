"""driftStore: Active drift metrics, PSI feature rankings, and alert thresholds."""

import { create } from 'zustand';

interface DriftStoreState {
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

export const useDriftStore = create<DriftStoreState>((set) => ({
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
