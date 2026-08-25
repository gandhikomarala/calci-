"""Tabs: Tabbed navigation interface."""

import React from 'react';

export interface TabsProps {
  className?: string;
  children?: React.ReactNode;
  [key: string]: any;
}

export const Tabs: React.FC<TabsProps> = ({ className = '', children, ...props }) => {
  return (
    <div className={"ui-" + "tabs" + " " + className} {...props}>
      {children}
    </div>
  );
};

export default Tabs;
