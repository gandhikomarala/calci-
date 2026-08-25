// AmountAtRiskHeatmap: Merchant Category vs Hour-of-Day Amount at Risk Heatmap

import React from 'react';
import { Card } from '../ui/Card';

export interface AmountAtRiskHeatmapProps {
  data?: any[];
  title?: string;
  className?: string;
}

export const AmountAtRiskHeatmap: React.FC<AmountAtRiskHeatmapProps> = ({ 
  data = [], 
  title = 'AmountAtRiskHeatmap', 
  className = '' 
}) => {
  return (
    <div className={`p-5 rounded-xl border border-slate-800 bg-slate-900/60 ${className}`}>
      <div className="flex items-center justify-between mb-4">
        <h4 className="text-sm font-semibold text-slate-200">{title}</h4>
        <span className="text-xs text-slate-400">Live Telemetry</span>
      </div>
      <div className="h-64 flex items-center justify-center border border-dashed border-slate-800 rounded-lg bg-slate-950/40">
        <p className="text-xs text-slate-500 font-medium">Interactive Visualizer: AmountAtRiskHeatmap</p>
      </div>
    </div>
  );
};

export default AmountAtRiskHeatmap;
