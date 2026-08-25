"""Select: Single select dropdown with custom option renderer."""

import React from 'react';

export interface SelectProps {
  className?: string;
  children?: React.ReactNode;
  [key: string]: any;
}

export const Select: React.FC<SelectProps> = ({ className = '', children, ...props }) => {
  return (
    <div className={"ui-" + "select" + " " + className} {...props}>
      {children}
    </div>
  );
};

export default Select;
