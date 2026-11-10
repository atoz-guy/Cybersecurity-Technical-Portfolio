# Lab 002: Phishing & Business Email Compromise (BEC) Investigation

**Date:** 2026-05-11
**Investigator:** [@atoz-guy](https://github.com/atoz-guy)
**Tools:** custom Python risk scoring, MXToolbox, PhishTank

## 1. What came in

- **Subject:** Urgent Invoice - Action Required
- **Sender:** `ceo.office@company-urgent-updates.com` (look-alike domain posing as the CEO)
- **Payload:** Malicious URL dressed up as a PDF invoice link

Classic BEC setup. Urgency, an authority figure, and money on the line.

## 2. Email header evidence

I pulled the headers and ran them through MXToolbox:

| Check | Result | What it means |
|---|---|---|
| SPF | ____ | |
| DKIM | ____ | |
| DMARC | ____ | |
| Domain age | ____ | |
| Reply-To | ____ | |

The URL was checked against PhishTank: ____

## 3. Risk scoring

Scored with my [grc_audit_logger_w-risk-scoring.py](https://github.com/atoz-guy/Python-Automation-Lab/blob/main/grc_audit_logger_w-risk-scoring.py) (Risk = Likelihood x Impact):

- **Likelihood: 4** (Likely. Targeted BEC keeps going up.)
- **Impact: 5** (Critical. This could end in a fraudulent wire transfer.)
- **Risk Score: 20 (CRITICAL)**

## 4. Control gaps (NIST 800-53)

| Control | Gap |
|---|---|
| **IA-2(1)** Multi-Factor Authentication | The attacker tried logging in with harvested credentials. MFA would have stopped that cold even with the right password. |
| **AC-7** Unsuccessful Logon Attempts | Failed logins from the attacker weren't locked out or alerted on fast enough. |
| **SI-8** Spam Protection | The email gateway didn't flag the look-alike domain. |
| **AT-2** Security Awareness Training | At least one user clicked, so phishing training needs a refresh. |

## 5. Remediation

**Immediate**
- Blocked the URL at the firewall
- ServiceNow **INC-10928** opened to reset passwords for affected users

**Follow-up**
- Turn on MFA for all users, starting with finance and execs
- Add a look-alike domain rule to the email gateway
- Tag external emails with an [EXTERNAL] banner
- Run a phishing simulation within 30 days

## 6. What I took away

The tech failed in one spot (the gateway), but the real fix is layered. MFA covers stolen passwords, the gateway covers the email, and training covers the person. Any one of those alone wouldn't have been enough.
