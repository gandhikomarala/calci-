// ResolveAlertModal: Mark fraud alert as resolved or false positive with decision rationale

import React, { useState } from 'react';
import { X, Check, AlertCircle } from 'lucide-react';

export interface ResolveAlertModalProps {
  isOpen: boolean;
  onClose: () => void;
  onConfirm?: (data: any) => void;
}

export const ResolveAlertModal: React.FC<ResolveAlertModalProps> = ({ isOpen, onClose, onConfirm }) => {
  const [formData, setFormData] = useState<any>({});
  const [loading, setLoading] = useState(false);

  if (!isOpen) return null;

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    if (onConfirm) onConfirm(formData);
    setLoading(false);
    onClose();
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-slate-950/80 backdrop-blur-sm p-4">
      <div className="w-full max-w-lg rounded-xl border border-slate-800 bg-slate-900 p-6 shadow-2xl">
        <div className="flex items-center justify-between border-b border-slate-800 pb-4">
          <h3 className="text-lg font-bold text-slate-100">ResolveAlert</h3>
          <button onClick={onClose} className="rounded-lg p-1 text-slate-400 hover:bg-slate-800 hover:text-slate-200">
            <X className="h-5 w-5" />
          </button>
        </div>
        <form onSubmit={handleSubmit} className="mt-4 space-y-4">
          <div>
            <label className="block text-xs font-medium uppercase text-slate-400">Description</label>
            <p className="mt-1 text-xs text-slate-300">Mark fraud alert as resolved or false positive with decision rationale</p>
          </div>
          <div className="flex items-center justify-end gap-3 pt-4 border-t border-slate-800">
            <button
              type="button"
              onClick={onClose}
              className="rounded-lg border border-slate-700 bg-slate-800 px-4 py-2 text-sm font-medium text-slate-300 hover:bg-slate-700"
            >
              Cancel
            </button>
            <button
              type="submit"
              disabled={loading}
              className="rounded-lg bg-brand-600 px-4 py-2 text-sm font-medium text-white hover:bg-brand-500 shadow-sm"
            >
              Confirm Action
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default ResolveAlertModal;
