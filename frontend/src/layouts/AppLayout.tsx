import React from 'react';
import { Outlet, NavLink } from 'react-router-dom';
import { 
  LayoutDashboard, Users, Zap, Database, GitBranch, Cpu, 
  Activity, BarChart3, Settings, ShieldAlert, Bell, LogOut 
} from 'lucide-react';

export default function AppLayout() {
  const navItems = [
    { name: 'Executive Overview', path: '/dashboard', icon: LayoutDashboard },
    { name: 'Customer 360', path: '/customers', icon: Users },
    { name: 'Churn Prediction', path: '/predictions', icon: Zap },
    { name: 'Datasets & Quality', path: '/datasets', icon: Database },
    { name: 'Feature Store & Experiments', path: '/experiments', icon: GitBranch },
    { name: 'Model Registry', path: '/models', icon: Cpu },
    { name: 'Drift & Retraining', path: '/drift', icon: Activity },
    { name: 'Business Analytics', path: '/analytics', icon: BarChart3 },
    { name: 'System Settings', path: '/settings', icon: Settings },
  ];

  return (
    <div className="flex h-screen overflow-hidden bg-slate-950">
      {/* Sidebar */}
      <aside className="w-64 border-r border-slate-800 bg-slate-900/50 flex flex-col">
        <div className="p-5 border-b border-slate-800 flex items-center gap-3">
          <div className="w-8 h-8 rounded-lg bg-brand-500 flex items-center justify-center font-bold text-white shadow-lg shadow-brand-500/20">
            CP
          </div>
          <div>
            <h1 className="font-bold text-sm text-slate-100 tracking-wide">CHURNOPS</h1>
            <p className="text-xs text-slate-400">Enterprise MLOps</p>
          </div>
        </div>

        <nav className="flex-1 p-3 space-y-1 overflow-y-auto">
          {navItems.map((item) => (
            <NavLink
              key={item.path}
              to={item.path}
              className={({ isActive }) =>
                `flex items-center gap-3 px-3 py-2.5 rounded-lg text-sm font-medium transition-colors ${
                  isActive
                    ? 'bg-brand-500/10 text-brand-400 border border-brand-500/20 shadow-sm'
                    : 'text-slate-400 hover:text-slate-200 hover:bg-slate-800/50'
                }`
              }
            >
              <item.icon className="w-4 h-4" />
              {item.name}
            </NavLink>
          ))}
        </nav>

        <div className="p-4 border-t border-slate-800 flex items-center justify-between">
          <div className="flex items-center gap-2">
            <div className="w-8 h-8 rounded-full bg-slate-700 flex items-center justify-center text-xs font-bold text-slate-200">
              AD
            </div>
            <div>
              <p className="text-xs font-medium text-slate-200">Staff Admin</p>
              <p className="text-[10px] text-emerald-400">SUPER_ADMIN</p>
            </div>
          </div>
          <NavLink to="/login" className="text-slate-400 hover:text-rose-400 transition-colors">
            <LogOut className="w-4 h-4" />
          </NavLink>
        </div>
      </aside>

      {/* Main Content Area */}
      <div className="flex-1 flex flex-col overflow-hidden">
        <header className="h-16 border-b border-slate-800 bg-slate-900/30 flex items-center justify-between px-6">
          <div className="flex items-center gap-2">
            <span className="inline-block w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
            <span className="text-xs text-slate-400 font-mono">PROD CLUSTER: US-EAST-1 | ACTIVE MODEL: LIGHTGBM-V1</span>
          </div>
          <div className="flex items-center gap-4">
            <button className="relative p-2 rounded-lg bg-slate-800/60 text-slate-400 hover:text-slate-200">
              <Bell className="w-4 h-4" />
              <span className="absolute top-1 right-1 w-2 h-2 rounded-full bg-brand-500"></span>
            </button>
          </div>
        </header>

        <main className="flex-1 overflow-y-auto p-8">
          <Outlet />
        </main>
      </div>
    </div>
  );
}
