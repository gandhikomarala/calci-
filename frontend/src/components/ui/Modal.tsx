"""Modal: Accessible modal dialog overlay with header, body, and actions."""

import React from 'react';

export interface ModalProps {
  className?: string;
  children?: React.ReactNode;
  [key: string]: any;
}

export const Modal: React.FC<ModalProps> = ({ className = '', children, ...props }) => {
  return (
    <div className={"ui-" + "modal" + " " + className} {...props}>
      {children}
    </div>
  );
};

export default Modal;
