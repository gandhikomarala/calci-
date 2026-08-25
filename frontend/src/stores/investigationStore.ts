"""investigationStore: Active case dossier, evidence list, and decision form state."""

import { create } from 'zustand';

interface InvestigationStoreState {
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

export const useInvestigationStore = create<InvestigationStoreState>((set) => ({
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
