import React from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import AppLayout from './layouts/AppLayout';
import DashboardPage from './features/dashboard/DashboardPage';
import CustomersPage from './features/customers/CustomersPage';
import CustomerDetailPage from './features/customers/CustomerDetailPage';
import PredictionsPage from './features/predictions/PredictionsPage';
import DatasetsPage from './features/datasets/DatasetsPage';
import ModelsPage from './features/models/ModelsPage';
import ExperimentsPage from './features/experiments/ExperimentsPage';
import DriftPage from './features/drift/DriftPage';
import AnalyticsPage from './features/analytics/AnalyticsPage';
import SettingsPage from './features/settings/SettingsPage';
import LoginPage from './features/auth/LoginPage';

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<LoginPage />} />
        
        <Route path="/" element={<AppLayout />}>
          <Route index element={<Navigate to="/dashboard" replace />} />
          <Route path="dashboard" element={<DashboardPage />} />
          <Route path="customers" element={<CustomersPage />} />
          <Route path="customers/:id" element={<CustomerDetailPage />} />
          <Route path="predictions" element={<PredictionsPage />} />
          <Route path="datasets" element={<DatasetsPage />} />
          <Route path="models" element={<ModelsPage />} />
          <Route path="experiments" element={<ExperimentsPage />} />
          <Route path="drift" element={<DriftPage />} />
          <Route path="analytics" element={<AnalyticsPage />} />
          <Route path="settings" element={<SettingsPage />} />
        </Route>
        
        <Route path="*" element={<Navigate to="/dashboard" replace />} />
      </Routes>
    </BrowserRouter>
  );
}
