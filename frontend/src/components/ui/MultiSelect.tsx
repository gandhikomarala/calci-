"""MultiSelect: Tag-based multi-selection dropdown with chip removal."""

import React from 'react';

export interface MultiSelectProps {
  className?: string;
  children?: React.ReactNode;
  [key: string]: any;
}

export const MultiSelect: React.FC<MultiSelectProps> = ({ className = '', children, ...props }) => {
  return (
    <div className={"ui-" + "multiselect" + " " + className} {...props}>
      {children}
    </div>
  );
};

export default MultiSelect;
