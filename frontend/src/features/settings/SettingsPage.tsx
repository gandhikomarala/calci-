import React from 'react';
import { Settings } from 'lucide-react';

export default function SettingsPage() {
  return (
    <div className="space-y-6">
      <div>
        <h2 className="text-2xl font-bold text-slate-100">System Settings & Threshold Configuration</h2>
        <p className="text-sm text-slate-400">Configure global churn probability thresholds, drift limits, and API rate quotas.</p>
      </div>

      <div className="p-6 rounded-xl border border-slate-800 bg-slate-900/60 space-y-4 max-w-xl">
        <div>
          <label className="block text-xs font-medium text-slate-400 mb-1">Low Risk Threshold (p &lt; X)</label>
          <input type="number" defaultValue={0.30} step={0.05} className="w-full px-3 py-2 rounded bg-slate-800 border border-slate-700 text-sm text-slate-200" />
        </div>
        <div>
          <label className="block text-xs font-medium text-slate-400 mb-1">High Risk Threshold (p &gt; X)</label>
          <input type="number" defaultValue={0.70} step={0.05} className="w-full px-3 py-2 rounded bg-slate-800 border border-slate-700 text-sm text-slate-200" />
        </div>
      </div>
    </div>
  );
}
