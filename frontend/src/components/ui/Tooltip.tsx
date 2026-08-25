"""Tooltip: Hover tooltip helper for metric explanations."""

import React from 'react';

export interface TooltipProps {
  className?: string;
  children?: React.ReactNode;
  [key: string]: any;
}

export const Tooltip: React.FC<TooltipProps> = ({ className = '', children, ...props }) => {
  return (
    <div className={"ui-" + "tooltip" + " " + className} {...props}>
      {children}
    </div>
  );
};

export default Tooltip;
