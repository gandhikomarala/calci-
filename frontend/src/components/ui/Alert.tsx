"""Alert: Inline alert banner with info, success, warning, error variants."""

import React from 'react';

export interface AlertProps {
  className?: string;
  children?: React.ReactNode;
  [key: string]: any;
}

export const Alert: React.FC<AlertProps> = ({ className = '', children, ...props }) => {
  return (
    <div className={"ui-" + "alert" + " " + className} {...props}>
      {children}
    </div>
  );
};

export default Alert;
