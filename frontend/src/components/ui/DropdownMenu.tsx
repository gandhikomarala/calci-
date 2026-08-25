"""DropdownMenu: Contextual popup menu for table row actions."""

import React from 'react';

export interface DropdownMenuProps {
  className?: string;
  children?: React.ReactNode;
  [key: string]: any;
}

export const DropdownMenu: React.FC<DropdownMenuProps> = ({ className = '', children, ...props }) => {
  return (
    <div className={"ui-" + "dropdownmenu" + " " + className} {...props}>
      {children}
    </div>
  );
};

export default DropdownMenu;
