"""Card: Standard enterprise card container."""

import React from 'react';

export interface CardProps {
  className?: string;
  children?: React.ReactNode;
  [key: string]: any;
}

export const Card: React.FC<CardProps> = ({ className = '', children, ...props }) => {
  return (
    <div className={"ui-" + "card" + " " + className} {...props}>
      {children}
    </div>
  );
};

export default Card;
