// AnalyticsPage: Operational Fraud Analytics, Amount at Risk & Prevented Loss Heatmaps

import React, { useState, useEffect } from 'react';
import { Shield, Activity, Search, Filter, RefreshCw, ArrowUpRight, CheckCircle2, AlertTriangle, XCircle } from 'lucide-react';

export default function AnalyticsPage() {
  const [loading, setLoading] = useState(false);
  const [searchQuery, setSearchQuery] = useState('');
  const [activeTab, setActiveTab] = useState('overview');

  return (
    <div className="space-y-6">
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <h2 className="text-2xl font-bold text-slate-100">Analytics</h2>
          <p className="text-sm text-slate-400">Operational Fraud Analytics, Amount at Risk & Prevented Loss Heatmaps</p>
        </div>
        <div className="flex items-center gap-3">
          <button 
            onClick={() => setLoading(true)}
            className="flex items-center gap-2 px-4 py-2 text-sm font-medium rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 transition"
          >
            <RefreshCw className={`w-4 h-4 ${loading ? 'animate-spin' : ''}`} />
            Refresh
          </button>
          <button className="flex items-center gap-2 px-4 py-2 text-sm font-medium rounded-lg bg-brand-600 hover:bg-brand-500 text-white shadow-sm transition">
            <Activity className="w-4 h-4" />
            Quick Action
          </button>
        </div>
      </div>

      <div className="p-6 rounded-xl border border-slate-800 bg-slate-900/60 shadow-sm">
        <div className="flex items-center justify-between mb-6">
          <div className="relative w-72">
            <Search className="w-4 h-4 absolute left-3 top-1/2 -translate-y-1/2 text-slate-400" />
            <input
              type="text"
              placeholder="Search records..."
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              className="w-full pl-9 pr-4 py-2 text-sm bg-slate-950 border border-slate-800 rounded-lg text-slate-100 placeholder-slate-500 focus:outline-none focus:border-brand-500"
            />
          </div>
          <div className="flex items-center gap-2">
            <button className="flex items-center gap-1.5 px-3 py-1.5 text-xs font-medium rounded-lg bg-slate-800 text-slate-300 border border-slate-700">
              <Filter className="w-3.5 h-3.5" />
              Filter
            </button>
          </div>
        </div>

        <div className="overflow-x-auto">
          <table className="w-full text-left text-sm text-slate-300">
            <thead className="bg-slate-950/80 text-xs uppercase text-slate-400 border-b border-slate-800">
              <tr>
                <th className="px-4 py-3">Identifier</th>
                <th className="px-4 py-3">Status</th>
                <th className="px-4 py-3">Risk Level</th>
                <th className="px-4 py-3">Timestamp</th>
                <th className="px-4 py-3 text-right">Actions</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-800/60">
              {[1, 2, 3, 4, 5].map((item) => (
                <tr key={item} className="hover:bg-slate-800/40 transition">
                  <td className="px-4 py-3.5 font-medium text-slate-100">REC-00{item}89</td>
                  <td className="px-4 py-3.5">
                    <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-emerald-500/10 text-emerald-400">
                      OPERATIONAL
                    </span>
                  </td>
                  <td className="px-4 py-3.5">
                    <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-rose-500/10 text-rose-400">
                      CRITICAL (88/100)
                    </span>
                  </td>
                  <td className="px-4 py-3.5 text-slate-400 text-xs">Just now</td>
                  <td className="px-4 py-3.5 text-right">
                    <button className="text-brand-400 hover:text-brand-300 text-xs font-medium inline-flex items-center gap-1">
                      Inspect <ArrowUpRight className="w-3 h-3" />
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}
