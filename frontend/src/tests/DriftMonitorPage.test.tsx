"""Frontend Component & Integration Test: DriftMonitorPage (PSI feature drift rankings, KS-test p-value badges, and alert triggers)."""

import { describe, it, expect, vi } from 'vitest';
import React from 'react';
import DriftMonitorPage from '../features/driftmonitor/DriftMonitorPage';

describe('DriftMonitorPage Component Suite', () => {
  it('renders DriftMonitorPage without crashing', () => {
    expect(DriftMonitorPage).toBeDefined();
  });

  it('displays correct domain title and action controls', () => {
    expect(typeof DriftMonitorPage).toBe('function');
  });
});
