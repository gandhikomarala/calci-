"""ConfirmDialog: Confirmation modal for destructive actions."""

import React from 'react';

export interface ConfirmDialogProps {
  className?: string;
  children?: React.ReactNode;
  [key: string]: any;
}

export const ConfirmDialog: React.FC<ConfirmDialogProps> = ({ className = '', children, ...props }) => {
  return (
    <div className={"ui-" + "confirmdialog" + " " + className} {...props}>
      {children}
    </div>
  );
};

export default ConfirmDialog;
