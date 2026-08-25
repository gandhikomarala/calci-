"""Customer Profile Update, Linked Device Addition and Risk Flag Schemas."""

import { z } from 'zod';

export const CustomerSchemasBase = z.object({
  id: z.string().uuid().optional(),
  name: z.string().min(2, 'Name must contain at least 2 characters').max(255),
  code: z.string().min(2, 'Code must contain at least 2 characters').max(100).optional(),
  description: z.string().max(1000).optional(),
  isActive: z.boolean().default(true),
  metadata: z.record(z.any()).optional(),
});

export type CustomerSchemasFormValues = z.infer<typeof CustomerSchemasBase>;
