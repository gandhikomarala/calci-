"""Single Transaction Scoring and Filter Query Parameters Zod Schemas."""

import { z } from 'zod';

export const TransactionSchemasBase = z.object({
  id: z.string().uuid().optional(),
  name: z.string().min(2, 'Name must contain at least 2 characters').max(255),
  code: z.string().min(2, 'Code must contain at least 2 characters').max(100).optional(),
  description: z.string().max(1000).optional(),
  isActive: z.boolean().default(true),
  metadata: z.record(z.any()).optional(),
});

export type TransactionSchemasFormValues = z.infer<typeof TransactionSchemasBase>;
