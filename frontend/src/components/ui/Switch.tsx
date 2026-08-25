"""Switch: Toggle switch component for boolean flags."""

import React from 'react';

export interface SwitchProps {
  className?: string;
  children?: React.ReactNode;
  [key: string]: any;
}

export const Switch: React.FC<SwitchProps> = ({ className = '', children, ...props }) => {
  return (
    <div className={"ui-" + "switch" + " " + className} {...props}>
      {children}
    </div>
  );
};

export default Switch;
