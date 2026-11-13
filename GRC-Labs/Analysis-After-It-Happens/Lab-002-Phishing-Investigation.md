# Lab 002: Credential Phishing Investigation (Microsoft Impersonation)

**Source:** TCM Security PSAA, Phishing Analysis Challenge 1. The technical analysis is in my [SOC lab write-up](../../SOC-Defensive-Labs/challenge1-phishing-emails). This page takes it into GRC.  
**Investigator:** [@atoz-guy](https://github.com/atoz-guy)  
**Tools:** email header analysis, URL reputation scan, sandbox, [custom Python risk scoring](https://github.com/atoz-guy/Python-Automation-Lab/blob/main/grc_audit_logger_w-risk-scoring.py)  

## 1. What came in

| Field | Value |
|---|---|
| **Subject** | Your account has been flagged for unusual activity |
| **Display name** | Outlook Support Team |
| **Actual sender** | `social201511138@social.helwan.edu.eg` |
| **Reply-To / Return-Path** | Same university address |
| **Sending server** | 40.107.22.60 (`outbound.protection.outlook.com`) |

Classic credential phishing. A scary account warning, a trusted brand, and a push to log in right away.

## 2. Email header evidence

| Check | Result | What it means |
|---|---|---|
| **Display name vs sender** | Mismatch | Says "Outlook Support," but the domain belongs to a university. Brand impersonation. |
| **SPF** | Pass | The sending server is allowed to send for `social.helwan.edu.eg`. It says nothing about whether the sender is really Microsoft. |
| **DKIM** | Pass | Signed by `socialhelwanedu.onmicrosoft.com`, a Microsoft 365 tenant. Microsoft *infrastructure* is not Microsoft the *company*. |
| **DMARC** | bestguesspass | Weak alignment. Strict domain enforcement wasn't satisfied. |

**The key point:** this email **passed authentication** and was still phishing. SPF and DKIM prove *which domain* sent it, not *who it claims to be*. Any filter that trusts a passing result would have let this straight through.

## 3. Payload

**Links** (defanged):
- `hxxps[://]raw[.]githubusercontent[.]com/.../microsoft[.]jpg`: a Microsoft logo pulled in to make the email look real
- `hxxps[://]0[.]232[.]205[.]92[.]host[.]secureserver[.]net/lclbluewin08812/`: the credential harvesting page

**Reputation:** 6 of 91 vendors flagged the link, with verdicts of phishing and malicious. That low a detection rate means most security tools would have missed it.

**Sandbox:** opening the email made `OUTLOOK.EXE` reach out to `raw.githubusercontent.com` and download the logo image. That's the logo-spoofing step.

**File hash (SHA256):** `91fc4aa2257b9c69684ac2bbc220ed7556c3db68cf725812ce365ef3febc8604`

## 4. Risk scoring

Scored with my risk scoring script (Risk = Likelihood x Impact), using my [risk matrix](risk-matrix.md):

- **Likelihood: 4** (Likely). It passed authentication and only 6 of 91 vendors caught the link.
- **Impact: 4** (Major). Stolen Microsoft 365 credentials mean access to email, files and anything else that account can reach.
- **Risk Score: 16 (HIGH)**

## 5. Control gaps (NIST 800-53)

| Control | Gap |
|---|---|
| **SI-8** Spam Protection | The email was delivered because it passed authentication. Nothing checked for a brand name in the display name coming from an unrelated external domain. |
| **IA-2(1)** Multi-Factor Authentication | If the user enters their password on the fake page, a password alone shouldn't be enough to get in. MFA stops a stolen password from becoming a stolen account. |
| **AT-2** Security Awareness Training | The user is the last line of defense. "Outlook Support" from a `.edu.eg` address should be an instant red flag. |
| **SC-7** Boundary Protection | The phishing host was reachable. Known-bad domains should be blocked at the web proxy. |

## 6. Remediation

**Immediate**
- Isolated the affected endpoint to prevent lateral movement
- Blocked the phishing host and the exact image URL at the firewall and web proxy. I blocked the specific path, not all of `raw.githubusercontent.com`, since developers rely on it.
- Added the file hash to the EDR blocklist
- If anyone entered their password: reset it and review recent sign-ins

**Follow-up**
- Require MFA for all users, starting with admins and privileged accounts
- Add an impersonation rule: flag external email whose display name uses "Microsoft," "Outlook" or "Support"
- Tag external email with an [EXTERNAL] banner
- Run a phishing simulation within 30 days using a brand impersonation template

## 7. What I took away

Passing SPF and DKIM made this email look trustworthy to a machine. That's exactly why it's dangerous. Authentication tells you which domain sent a message, not whether it's honest. The real fix is layered: MFA covers the stolen password, the impersonation rule covers the email, and training covers the person. No one layer would have been enough.

## 8. Next: close the gap with code

The top finding here, MFA, is the subject of **Lab 04: MFA for Privileged Accounts** on the engineering side. See [Engineering-Before-It-Happens](../Engineering-Before-It-Happens).
