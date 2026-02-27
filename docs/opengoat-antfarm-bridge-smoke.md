# OpenGoat-to-Antfarm Dispatch Bridge Smoke Test

OpenGoatTask: `task-bridge-smoke-opengoat-to-antfarm-dispatch-f31a05a2`

## Overview
The OpenGoat-to-Antfarm dispatch bridge forwards a task trigger from OpenGoat into an Antfarm workflow run. This smoke test verifies the end-to-end integration at a high level so the team can quickly confirm that dispatch, execution handoff, and completion signaling still work after changes.

## Bridge Smoke Test Description
1. Trigger the bridge smoke test task from OpenGoat.
2. Confirm Antfarm creates a run from the dispatched task.
3. Confirm an agent claims the step and receives the expected input.
4. Confirm the step result is reported with the required `KEY: value` output format and `STATUS: done`.
5. Confirm the run advances to completion without manual intervention.

## Acceptance Checklist
- [ ] Dispatch trigger from OpenGoat initiates the workflow run correctly.
- [ ] Dispatched task payload is well-formed (required fields, IDs, and input content are present).
- [ ] Antfarm receives the task and acknowledges it by creating/claiming the expected step.
- [ ] Error handling is verified when Antfarm is unreachable (failure is surfaced clearly and does not hang silently).
- [ ] Dispatch is idempotent for repeated trigger attempts (no duplicate or inconsistent runs beyond expected behavior).
- [ ] Logging and observability are sufficient to trace dispatch, claim, execution, and completion events.

## Notes
- This is a smoke test, not an exhaustive integration test.
- Use this checklist for quick validation during bridge changes, release readiness, or incident triage.
