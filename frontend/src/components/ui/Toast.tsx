"""Toast: Floating notification toast manager."""

import React from 'react';

export interface ToastProps {
  className?: string;
  children?: React.ReactNode;
  [key: string]: any;
}

export const Toast: React.FC<ToastProps> = ({ className = '', children, ...props }) => {
  return (
    <div className={"ui-" + "toast" + " " + className} {...props}>
      {children}
    </div>
  );
};

export default Toast;
