import React from 'react';
import { Activity, CheckCircle2 } from 'lucide-react';

export default function DriftPage() {
  return (
    <div className="space-y-6">
      <div>
        <h2 className="text-2xl font-bold text-slate-100">Data Drift & Retraining Monitor</h2>
        <p className="text-sm text-slate-400">Population Stability Index (PSI) and two-sample Kolmogorov-Smirnov distribution checks.</p>
      </div>

      <div className="p-6 rounded-xl border border-slate-800 bg-slate-900/60 flex items-center justify-between">
        <div>
          <h3 className="font-bold text-slate-100 text-base">Overall Drift Status: NORMAL</h3>
          <p className="text-xs text-slate-400 mt-1">Average Feature PSI: 0.029 | 0 Features with Critical Drift</p>
        </div>
        <span className="p-3 rounded-full bg-emerald-500/10 text-emerald-400">
          <CheckCircle2 className="w-6 h-6" />
        </span>
      </div>
    </div>
  );
}
