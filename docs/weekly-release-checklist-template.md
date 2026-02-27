# Weekly Release Checklist Template

Use this checklist for each weekly release. Copy it into a release-specific note and mark items as you go.

## Release Info
- Release name/version:
- Target date/time:
- Release owner:
- Scope (PRs/issues):

## 1) Pre-Release
- [ ] Confirm scope is frozen and all included PRs are identified.
- [ ] Verify all required CI checks are green on release branch.
- [ ] Review open critical/high bugs; decide go/no-go for each.
- [ ] Ensure changelog/release notes draft is prepared.
- [ ] Confirm database/config/env changes and rollback plan.
- [ ] Validate version bump and tags strategy.
- [ ] Notify stakeholders of planned release window.

## 2) Release
- [ ] Create release branch/tag from approved commit.
- [ ] Run final smoke tests on release candidate.
- [ ] Publish release artifacts/builds.
- [ ] Deploy to production (or target environment).
- [ ] Verify service health and core user journeys.
- [ ] Publish release notes/changelog.
- [ ] Announce release completion to stakeholders.

## 3) Post-Release
- [ ] Monitor errors, latency, and key metrics for 30–60 minutes.
- [ ] Confirm no new Sev1/Sev2 incidents after deployment.
- [ ] Validate tracking/analytics and scheduled jobs.
- [ ] Document issues, mitigations, and follow-up tickets.
- [ ] Confirm rollback is no longer needed.
- [ ] Close release checklist with final status (success/partial/failed).

## Sign-off
- Engineering:
- Product:
- Operations:
- Date/time:
