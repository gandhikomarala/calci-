"""ErrorState: API failure display with retry trigger."""

import React from 'react';

export interface ErrorStateProps {
  className?: string;
  children?: React.ReactNode;
  [key: string]: any;
}

export const ErrorState: React.FC<ErrorStateProps> = ({ className = '', children, ...props }) => {
  return (
    <div className={"ui-" + "errorstate" + " " + className} {...props}>
      {children}
    </div>
  );
};

export default ErrorState;
