# Lab 001: Privileged Access Review

**Date:** 2026-05-11
**Reviewer:** [@atoz-guy](https://github.com/atoz-guy)
**Framework:** NIST 800-53 (Access Control, Personnel Security)

## 1. Executive Summary

I reviewed admin access in the internal ticketing system to check whether least privilege was actually being followed. Short answer: not fully. 3 of the 50 admin accounts I reviewed (6%) belonged to people who no longer work here, and the Service Desk portal wasn't locking out brute-force attempts.

Both issues are fixable fast, but the first one is the kind of thing that ends up in a breach report.

## 2. Methodology

- **Tool:** [grc_audit_logger.py](https://github.com/atoz-guy/Python-Automation-Lab/blob/main/grc_audit_logger.py)
- **Platform:** ServiceNow and a local Active Directory lab
- **Scope:** 50 accounts with admin rights
- **How:**
  1. Exported admin accounts from AD and the ServiceNow user table
  2. Pulled the HR termination list for the last ____ months
  3. Cross-referenced the two to find accounts still active after termination
  4. Reviewed portal login logs for repeated failures from the same source

## 3. Findings

| ID | Control | Risk (L x I) | Finding | Owner | Due |
|---|---|---|---|---|---|
| AUDIT-001 | PS-4, AC-2, AC-6 | 4 x 5 = 20 (CRITICAL) | 3 terminated employees still had active admin credentials. Longest gap after termination: ____ days. | IT / IAM | 24 hrs |
| AUDIT-002 | AC-7 | 3 x 4 = 12 (MEDIUM) | ____ failed login attempts from ____ source(s) on the Service Desk portal. Lockout policy never fired. | Service Desk | 7 days |

## 4. Evidence

- AUDIT-001: ____ (screenshot or redacted export showing account status vs termination date)
- AUDIT-002: ____ (log excerpt showing repeated failures with no lockout)

## 5. Remediation

**Immediate**
- Disable the 3 flagged accounts in AD and revoke their ServiceNow roles
- Check those accounts' recent activity to make sure nobody used them after termination

**Short term**
- Fix the lockout policy (5 failed attempts, 15 minute lockout) and confirm it triggers
- Alert the SOC on repeated portal login failures

**Long term**
- Automate offboarding in ServiceNow so an HR termination record disables access the same day
- Quarterly admin access reviews with manager sign-off

## 6. Status

| ID | Status |
|---|---|
| AUDIT-001 | ____ |
| AUDIT-002 | ____ |
