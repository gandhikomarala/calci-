import React from 'react';
import { useParams, NavLink } from 'react-router-dom';
import { ArrowLeft, ShieldAlert, Zap, Clock, DollarSign } from 'lucide-react';

export default function CustomerDetailPage() {
  const { id } = useParams();

  return (
    <div className="space-y-6">
      <NavLink to="/customers" className="inline-flex items-center gap-2 text-xs font-medium text-slate-400 hover:text-slate-200">
        <ArrowLeft className="w-4 h-4" /> Back to Customer Directory
      </NavLink>

      <div className="flex justify-between items-start">
        <div>
          <h2 className="text-2xl font-bold text-slate-100">Customer 360: Eleanor Vance</h2>
          <p className="text-xs font-mono text-brand-400 mt-1">CUS-100291 | Acme Corp</p>
        </div>
        <span className="px-3 py-1.5 rounded-full text-xs font-bold bg-rose-500/10 text-rose-400 border border-rose-500/20">
          HIGH CHURN RISK (87.4%)
        </span>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="p-6 rounded-xl border border-slate-800 bg-slate-900/60 space-y-4">
          <h3 className="font-semibold text-slate-200 text-sm">Key Churn Drivers (TreeSHAP)</h3>
          <div className="space-y-2 text-xs">
            <div className="flex justify-between p-2 rounded bg-rose-500/10 border border-rose-500/20 text-rose-300 font-medium">
              <span>Contract Type (Month-to-Month)</span>
              <span>+22%</span>
            </div>
            <div className="flex justify-between p-2 rounded bg-rose-500/10 border border-rose-500/20 text-rose-300 font-medium">
              <span>Payment Failures (3 in 12m)</span>
              <span>+18%</span>
            </div>
            <div className="flex justify-between p-2 rounded bg-rose-500/10 border border-rose-500/20 text-rose-300 font-medium">
              <span>Support Complaints (2 unresolved)</span>
              <span>+14%</span>
            </div>
          </div>
        </div>

        <div className="p-6 rounded-xl border border-slate-800 bg-slate-900/60 space-y-4">
          <h3 className="font-semibold text-slate-200 text-sm">Behavioral Usage</h3>
          <div className="space-y-2 text-xs text-slate-300">
            <div className="flex justify-between py-1 border-b border-slate-800">
              <span className="text-slate-400">Monthly Usage</span>
              <span className="font-bold">420 mins (-35% trend)</span>
            </div>
            <div className="flex justify-between py-1 border-b border-slate-800">
              <span className="text-slate-400">Logins (Last 30d)</span>
              <span className="font-bold">6 logins</span>
            </div>
            <div className="flex justify-between py-1 border-b border-slate-800">
              <span className="text-slate-400">Days Since Last Active</span>
              <span className="font-bold text-rose-400">18 days</span>
            </div>
          </div>
        </div>

        <div className="p-6 rounded-xl border border-slate-800 bg-slate-900/60 space-y-4">
          <h3 className="font-semibold text-slate-200 text-sm">Financial Profile</h3>
          <div className="space-y-2 text-xs text-slate-300">
            <div className="flex justify-between py-1 border-b border-slate-800">
              <span className="text-slate-400">Monthly Plan Charge</span>
              <span className="font-bold">$79.99</span>
            </div>
            <div className="flex justify-between py-1 border-b border-slate-800">
              <span className="text-slate-400">Total Spend (LTV)</span>
              <span className="font-bold">$1,120.00</span>
            </div>
            <div className="flex justify-between py-1 border-b border-slate-800">
              <span className="text-slate-400">Payment Method</span>
              <span className="font-bold">Credit Card</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
