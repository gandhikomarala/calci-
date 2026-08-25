// CustomerProfileDrawer: View customer 360 profile, linked bank accounts and device history

import React from 'react';
import { X } from 'lucide-react';

export interface CustomerProfileDrawerProps {
  isOpen: boolean;
  onClose: () => void;
  item?: any;
}

export const CustomerProfileDrawer: React.FC<CustomerProfileDrawerProps> = ({ isOpen, onClose, item }) => {
  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-50 overflow-hidden bg-slate-950/70 backdrop-blur-xs">
      <div className="absolute inset-y-0 right-0 flex max-w-full pl-10">
        <div className="w-screen max-w-md bg-slate-900 border-l border-slate-800 p-6 shadow-2xl flex flex-col justify-between">
          <div>
            <div className="flex items-center justify-between border-b border-slate-800 pb-4">
              <h3 className="text-lg font-bold text-slate-100">CustomerProfile</h3>
              <button onClick={onClose} className="rounded-lg p-1 text-slate-400 hover:bg-slate-800 hover:text-slate-200">
                <X className="h-5 w-5" />
              </button>
            </div>
            <div className="mt-6 space-y-4">
              <p className="text-xs text-slate-400 uppercase font-semibold">Overview</p>
              <p className="text-xs text-slate-300">View customer 360 profile, linked bank accounts and device history</p>
              <div className="p-4 rounded-lg bg-slate-950 border border-slate-800">
                <pre className="text-xs text-slate-400 overflow-x-auto">
                  {JSON.stringify(item || { status: 'OPERATIONAL', tier: 'ENTERPRISE' }, null, 2)}
                </pre>
              </div>
            </div>
          </div>
          <div className="border-t border-slate-800 pt-4 flex justify-end">
            <button
              onClick={onClose}
              className="px-4 py-2 text-sm font-medium rounded-lg bg-slate-800 text-slate-200 hover:bg-slate-700"
            >
              Close Drawer
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default CustomerProfileDrawer;
