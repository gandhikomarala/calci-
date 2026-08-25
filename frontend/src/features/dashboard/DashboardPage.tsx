import React from 'react';
import { ShieldAlert, Activity, DollarSign, AlertTriangle, TrendingUp, CheckCircle2 } from 'lucide-react';

export default function DashboardPage() {
  return (
    <div className="space-y-6">
      <div>
        <h2 className="text-2xl font-bold text-slate-100">FinGuard AI — Fraud Intelligence Command Center</h2>
        <p className="text-sm text-slate-400">Real-time financial transaction scoring, risk decision engine, and MLOps telemetry.</p>
      </div>

      {/* KPI Cards */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-5">
        <div className="p-5 rounded-xl border border-slate-800 bg-slate-900/60">
          <div className="flex justify-between items-start">
            <div>
              <p className="text-xs font-medium text-slate-400 uppercase">24h Ingested Volume</p>
              <h3 className="text-2xl font-bold text-slate-100 mt-1">$42,850,200</h3>
            </div>
            <div className="p-2.5 rounded-lg bg-brand-500/10 text-brand-400">
              <DollarSign className="w-5 h-5" />
            </div>
          </div>
          <p className="text-xs text-emerald-400 mt-3">+8.4% volume growth</p>
        </div>

        <div className="p-5 rounded-xl border border-slate-800 bg-slate-900/60">
          <div className="flex justify-between items-start">
            <div>
              <p className="text-xs font-medium text-slate-400 uppercase">Fraud Detection Rate</p>
              <h3 className="text-2xl font-bold text-rose-400 mt-1">1.48%</h3>
            </div>
            <div className="p-2.5 rounded-lg bg-rose-500/10 text-rose-400">
              <ShieldAlert className="w-5 h-5" />
            </div>
          </div>
          <p className="text-xs text-slate-400 mt-3">Precision: 94.2% | Recall: 91.8%</p>
        </div>

        <div className="p-5 rounded-xl border border-slate-800 bg-slate-900/60">
          <div className="flex justify-between items-start">
            <div>
              <p className="text-xs font-medium text-slate-400 uppercase">Critical Fraud Alerts</p>
              <h3 className="text-2xl font-bold text-amber-400 mt-1">42 Open</h3>
            </div>
            <div className="p-2.5 rounded-lg bg-amber-500/10 text-amber-400">
              <AlertTriangle className="w-5 h-5" />
            </div>
          </div>
          <p className="text-xs text-amber-400 mt-3">Score &gt; 80 (Avg SLA: 4.2m)</p>
        </div>

        <div className="p-5 rounded-xl border border-slate-800 bg-slate-900/60">
          <div className="flex justify-between items-start">
            <div>
              <p className="text-xs font-medium text-slate-400 uppercase">Prevented Loss</p>
              <h3 className="text-2xl font-bold text-emerald-400 mt-1">$634,180</h3>
            </div>
            <div className="p-2.5 rounded-lg bg-emerald-500/10 text-emerald-400">
              <CheckCircle2 className="w-5 h-5" />
            </div>
          </div>
          <p className="text-xs text-slate-400 mt-3">Automated blocks & challenges</p>
        </div>
      </div>
    </div>
  );
}
