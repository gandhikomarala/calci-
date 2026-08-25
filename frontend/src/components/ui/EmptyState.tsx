"""EmptyState: Zero-data visual state with action CTA."""

import React from 'react';

export interface EmptyStateProps {
  className?: string;
  children?: React.ReactNode;
  [key: string]: any;
}

export const EmptyState: React.FC<EmptyStateProps> = ({ className = '', children, ...props }) => {
  return (
    <div className={"ui-" + "emptystate" + " " + className} {...props}>
      {children}
    </div>
  );
};

export default EmptyState;
