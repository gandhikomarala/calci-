"""FilterDrawer: Faceted filter drawer with multi-criteria filters."""

import React from 'react';

export interface FilterDrawerProps {
  className?: string;
  children?: React.ReactNode;
  [key: string]: any;
}

export const FilterDrawer: React.FC<FilterDrawerProps> = ({ className = '', children, ...props }) => {
  return (
    <div className={"ui-" + "filterdrawer" + " " + className} {...props}>
      {children}
    </div>
  );
};

export default FilterDrawer;
