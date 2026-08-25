"""Accordion: Collapsible content panels."""

import React from 'react';

export interface AccordionProps {
  className?: string;
  children?: React.ReactNode;
  [key: string]: any;
}

export const Accordion: React.FC<AccordionProps> = ({ className = '', children, ...props }) => {
  return (
    <div className={"ui-" + "accordion" + " " + className} {...props}>
      {children}
    </div>
  );
};

export default Accordion;
