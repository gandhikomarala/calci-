import React from 'react';
import { Cpu, CheckCircle2, RotateCcw } from 'lucide-react';

export default function ModelsPage() {
  return (
    <div className="space-y-6">
      <div>
        <h2 className="text-2xl font-bold text-slate-100">Model Registry & Deployments</h2>
        <p className="text-sm text-slate-400">Manage model lifecycles, promotions, and zero-downtime rollback triggers.</p>
      </div>

      <div className="rounded-xl border border-slate-800 bg-slate-900/60 overflow-hidden">
        <table className="w-full text-left text-sm text-slate-300">
          <thead className="bg-slate-800/50 text-xs font-semibold text-slate-400 uppercase">
            <tr>
              <th className="px-6 py-4">Version Tag</th>
              <th className="px-6 py-4">Algorithm</th>
              <th className="px-6 py-4">Stage</th>
              <th className="px-6 py-4">Accuracy</th>
              <th className="px-6 py-4">ROC-AUC</th>
              <th className="px-6 py-4">F1 Score</th>
              <th className="px-6 py-4 text-right">Actions</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-slate-800">
            <tr className="hover:bg-slate-800/30">
              <td className="px-6 py-4 font-mono font-bold text-brand-400">lightgbm-v1</td>
              <td className="px-6 py-4">LightGBM GBDT</td>
              <td className="px-6 py-4"><span className="px-2.5 py-1 rounded-full text-xs font-bold bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">PRODUCTION</span></td>
              <td className="px-6 py-4 font-mono">0.9142</td>
              <td className="px-6 py-4 font-mono font-bold text-emerald-400">0.9488</td>
              <td className="px-6 py-4 font-mono">0.8924</td>
              <td className="px-6 py-4 text-right">
                <button className="text-xs text-slate-400 hover:text-rose-400 inline-flex items-center gap-1">
                  <RotateCcw className="w-3.5 h-3.5" /> Rollback
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  );
}
