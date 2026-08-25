"""FileUploadZone: Drag-and-drop file upload zone for datasets and batch CSVs."""

import React from 'react';

export interface FileUploadZoneProps {
  className?: string;
  children?: React.ReactNode;
  [key: string]: any;
}

export const FileUploadZone: React.FC<FileUploadZoneProps> = ({ className = '', children, ...props }) => {
  return (
    <div className={"ui-" + "fileuploadzone" + " " + className} {...props}>
      {children}
    </div>
  );
};

export default FileUploadZone;
