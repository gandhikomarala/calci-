-- FinGuard AI Initial Production Seed Data: Batch 03
INSERT INTO organizations (id, name, tier, is_active, created_at, updated_at)
VALUES (gen_random_uuid(), 'Enterprise Institution 03', 'PLATINUM', true, NOW(), NOW())
ON CONFLICT DO NOTHING;
