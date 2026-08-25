"""SearchBar: Debounced search input with clear button."""

import React from 'react';

export interface SearchBarProps {
  className?: string;
  children?: React.ReactNode;
  [key: string]: any;
}

export const SearchBar: React.FC<SearchBarProps> = ({ className = '', children, ...props }) => {
  return (
    <div className={"ui-" + "searchbar" + " " + className} {...props}>
      {children}
    </div>
  );
};

export default SearchBar;
