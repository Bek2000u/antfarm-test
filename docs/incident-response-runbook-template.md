# Incident Response Runbook Template

Use this template to guide incident handling from detection through closure.

## Incident Metadata
- Incident ID:
- Severity (Sev1/Sev2/Sev3):
- Status (Investigating/Identified/Mitigating/Resolved):
- Start time:
- Incident commander:
- Communications lead:
- Impacted systems/services:

## 1) Detection & Triage
- [ ] Confirm incident signal (alerts, reports, logs).
- [ ] Assess blast radius and customer impact.
- [ ] Assign severity level and incident commander.
- [ ] Open incident channel/bridge and start timeline log.
- [ ] Declare incident publicly/internal based on severity.

## 2) Containment & Mitigation
- [ ] Identify immediate mitigation options.
- [ ] Apply safe guardrails (feature flag off, traffic shift, rate limit).
- [ ] If needed, execute rollback to last known good state.
- [ ] Record every action with timestamp and owner.
- [ ] Post status updates at regular cadence (e.g., every 15 min for Sev1).

## 3) Diagnosis & Resolution
- [ ] Confirm root-cause hypothesis with evidence.
- [ ] Implement and validate fix in controlled environment.
- [ ] Deploy fix and verify service recovery.
- [ ] Validate core user journeys and error budgets.
- [ ] Mark incident as resolved when stability criteria are met.

## 4) Communication
- [ ] Internal update template used (what happened, impact, ETA).
- [ ] External/customer update sent when required.
- [ ] Final resolution summary distributed.

## 5) Post-Incident
- [ ] Complete postmortem within agreed SLA.
- [ ] Document timeline, root cause, contributing factors.
- [ ] Create follow-up actions with owners/dates.
- [ ] Track remediation and prevention tasks to closure.

## Timeline Log (append entries)
- `HH:MM` — action/observation — owner

## Exit Criteria
- [ ] Service stable for agreed monitoring window.
- [ ] No ongoing customer impact.
- [ ] Stakeholders informed of closure.
