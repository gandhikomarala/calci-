"""ProgressBar: Linear progress indicator for batch jobs and training steps."""

import React from 'react';

export interface ProgressBarProps {
  className?: string;
  children?: React.ReactNode;
  [key: string]: any;
}

export const ProgressBar: React.FC<ProgressBarProps> = ({ className = '', children, ...props }) => {
  return (
    <div className={"ui-" + "progressbar" + " " + className} {...props}>
      {children}
    </div>
  );
};

export default ProgressBar;
