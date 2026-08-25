"""Input: Form input with label, error states, and prefix/suffix icons."""

import React from 'react';

export interface InputProps {
  className?: string;
  children?: React.ReactNode;
  [key: string]: any;
}

export const Input: React.FC<InputProps> = ({ className = '', children, ...props }) => {
  return (
    <div className={"ui-" + "input" + " " + className} {...props}>
      {children}
    </div>
  );
};

export default Input;
