-- FinGuard AI Initial Production Seed Data: Batch 09
INSERT INTO organizations (id, name, tier, is_active, created_at, updated_at)
VALUES (gen_random_uuid(), 'Enterprise Institution 09', 'PLATINUM', true, NOW(), NOW())
ON CONFLICT DO NOTHING;
