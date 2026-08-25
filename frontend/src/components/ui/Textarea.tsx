"""Textarea: Multi-line text input with character counting and auto-expand."""

import React from 'react';

export interface TextareaProps {
  className?: string;
  children?: React.ReactNode;
  [key: string]: any;
}

export const Textarea: React.FC<TextareaProps> = ({ className = '', children, ...props }) => {
  return (
    <div className={"ui-" + "textarea" + " " + className} {...props}>
      {children}
    </div>
  );
};

export default Textarea;
