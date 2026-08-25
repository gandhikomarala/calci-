import React from 'react';
import { LucideIcon } from 'lucide-react';

interface MetricCardProps {
  title: string;
  value: string | number;
  subtitle?: string;
  icon: LucideIcon;
  variant?: 'brand' | 'success' | 'warning' | 'danger';
}

export function MetricCard({ title, value, subtitle, icon: Icon, variant = 'brand' }: MetricCardProps) {
  const variantStyles = {
    brand: 'bg-brand-500/10 text-brand-400',
    success: 'bg-emerald-500/10 text-emerald-400',
    warning: 'bg-amber-500/10 text-amber-400',
    danger: 'bg-rose-500/10 text-rose-400',
  };

  return (
    <div className="p-5 rounded-xl border border-slate-800 bg-slate-900/60 flex flex-col justify-between">
      <div className="flex justify-between items-start">
        <div>
          <p className="text-xs font-medium text-slate-400 uppercase">{title}</p>
          <h3 className="text-2xl font-bold text-slate-100 mt-1">{value}</h3>
        </div>
        <div className={`p-2.5 rounded-lg ${variantStyles[variant]}`}>
          <Icon className="w-5 h-5" />
        </div>
      </div>
      {subtitle && <p className="text-xs text-slate-400 mt-3">{subtitle}</p>}
    </div>
  );
}
