"""Drawer: Slide-over right drawer for filters and detail views."""

import React from 'react';

export interface DrawerProps {
  className?: string;
  children?: React.ReactNode;
  [key: string]: any;
}

export const Drawer: React.FC<DrawerProps> = ({ className = '', children, ...props }) => {
  return (
    <div className={"ui-" + "drawer" + " " + className} {...props}>
      {children}
    </div>
  );
};

export default Drawer;
