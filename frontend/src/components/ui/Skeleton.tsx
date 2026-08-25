"""Skeleton: Placeholder skeleton loading block for cards and tables."""

import React from 'react';

export interface SkeletonProps {
  className?: string;
  children?: React.ReactNode;
  [key: string]: any;
}

export const Skeleton: React.FC<SkeletonProps> = ({ className = '', children, ...props }) => {
  return (
    <div className={"ui-" + "skeleton" + " " + className} {...props}>
      {children}
    </div>
  );
};

export default Skeleton;
