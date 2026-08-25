"""DateRangePicker: Custom date interval selector for analytics filters."""

import React from 'react';

export interface DateRangePickerProps {
  className?: string;
  children?: React.ReactNode;
  [key: string]: any;
}

export const DateRangePicker: React.FC<DateRangePickerProps> = ({ className = '', children, ...props }) => {
  return (
    <div className={"ui-" + "daterangepicker" + " " + className} {...props}>
      {children}
    </div>
  );
};

export default DateRangePicker;
