"""Spinner: Loading spinner for asynchronous operations."""

import React from 'react';

export interface SpinnerProps {
  className?: string;
  children?: React.ReactNode;
  [key: string]: any;
}

export const Spinner: React.FC<SpinnerProps> = ({ className = '', children, ...props }) => {
  return (
    <div className={"ui-" + "spinner" + " " + className} {...props}>
      {children}
    </div>
  );
};

export default Spinner;
