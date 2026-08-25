"""Checkbox: Accessible custom styled checkbox."""

import React from 'react';

export interface CheckboxProps {
  className?: string;
  children?: React.ReactNode;
  [key: string]: any;
}

export const Checkbox: React.FC<CheckboxProps> = ({ className = '', children, ...props }) => {
  return (
    <div className={"ui-" + "checkbox" + " " + className} {...props}>
      {children}
    </div>
  );
};

export default Checkbox;
