# Bridge Operations Runbook

## Overview
- OpenGoat emits workflow intents and forwards them to AntFarm for execution.
- AntFarm claims steps, runs the assigned operation, and reports completion status back through the bridge.
- Operators should treat this runbook as the single source of truth for normal operations and incident response.

## Normal Flow
- Confirm the target run has a claimed step and an active worker before taking manual action.
- Observe step lifecycle transitions: queued -> claimed -> running -> completed.
- Verify completion payload includes required key/value fields so downstream workflow stages can continue.

## Failure Modes
- A worker exits before calling `step complete` or `step fail`, leaving the step stuck in running state.
- Invalid output formatting (missing required keys) causes bridge-side validation failure and blocked progression.
- Branch drift or missing files in the target repo causes tests/checks to fail before step completion.

## Manual Recovery Commands
- Inspect worker logs and rerun the failed operation in the same repository and branch context.
- Mark a failed step explicitly when recovery is not possible: `node /root/.openclaw/workspace/antfarm/dist/cli/cli.js step fail "<stepId>" "<reason>"`.
- Complete a recovered step by writing the payload to a file and piping via stdin: `cat /tmp/antfarm-step-output.txt | node /root/.openclaw/workspace/antfarm/dist/cli/cli.js step complete "<stepId>"`.

## Rollback
- Revert the story commit on the feature branch if a docs or validation change introduces regressions.
- Re-run build and tests after rollback to confirm the repository is back to a known-good state.
- Record the rollback reason in the progress log so future runs can avoid repeating the same failure mode.
