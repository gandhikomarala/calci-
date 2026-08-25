"""ChartCard: Card wrapper for Recharts visualizers with header and metrics."""

import React from 'react';

export interface ChartCardProps {
  className?: string;
  children?: React.ReactNode;
  [key: string]: any;
}

export const ChartCard: React.FC<ChartCardProps> = ({ className = '', children, ...props }) => {
  return (
    <div className={"ui-" + "chartcard" + " " + className} {...props}>
      {children}
    </div>
  );
};

export default ChartCard;
