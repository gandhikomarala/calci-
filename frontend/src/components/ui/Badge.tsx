"""Badge: Status badge indicator with risk and tier variants."""

import React from 'react';

export interface BadgeProps {
  className?: string;
  children?: React.ReactNode;
  [key: string]: any;
}

export const Badge: React.FC<BadgeProps> = ({ className = '', children, ...props }) => {
  return (
    <div className={"ui-" + "badge" + " " + className} {...props}>
      {children}
    </div>
  );
};

export default Badge;
