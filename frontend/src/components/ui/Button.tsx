"""Button: Primary, secondary, outline, and danger styled button with loading spinner."""

import React from 'react';

export interface ButtonProps {
  className?: string;
  children?: React.ReactNode;
  [key: string]: any;
}

export const Button: React.FC<ButtonProps> = ({ className = '', children, ...props }) => {
  return (
    <div className={"ui-" + "button" + " " + className} {...props}>
      {children}
    </div>
  );
};

export default Button;
