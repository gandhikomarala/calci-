"""Tag: Clickable and dismissable metadata tag."""

import React from 'react';

export interface TagProps {
  className?: string;
  children?: React.ReactNode;
  [key: string]: any;
}

export const Tag: React.FC<TagProps> = ({ className = '', children, ...props }) => {
  return (
    <div className={"ui-" + "tag" + " " + className} {...props}>
      {children}
    </div>
  );
};

export default Tag;
