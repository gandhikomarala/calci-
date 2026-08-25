"""RadioGroup: Radio button group for single option selection."""

import React from 'react';

export interface RadioGroupProps {
  className?: string;
  children?: React.ReactNode;
  [key: string]: any;
}

export const RadioGroup: React.FC<RadioGroupProps> = ({ className = '', children, ...props }) => {
  return (
    <div className={"ui-" + "radiogroup" + " " + className} {...props}>
      {children}
    </div>
  );
};

export default RadioGroup;
