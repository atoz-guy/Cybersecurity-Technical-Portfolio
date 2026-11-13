# Engineering: Before It Happens

*Planned. My own rules, test results and notes will go here as I complete each lab.*

This is the GRC engineering side: writing **policy as code**. Instead of a written policy that says "don't do this," the control is a rule that checks every change and blocks the bad ones automatically. It runs every time, not once a year at audit.

Labs are from [GRC Playground](https://github.com/ashpearce/GRC-Playground), a free hands-on lab series for GRC people. The lab design is theirs. The solutions and write-ups here are mine.

**Tools:** Open Policy Agent (OPA), Rego, Conftest, run from the Linux command line

---

## Planned labs

| # | Lab | Control it enforces | Status |
|---|---|---|---|
| 01 | Deny public S3 buckets | AC-3 Access Enforcement: data storage isn't open to the internet | 🔲 Planned |
| 02 | Block open security groups | SC-7 Boundary Protection: no network rules open to 0.0.0.0/0 | 🔲 Planned |
| 03 | IAM policy audits | AC-6 Least Privilege: no overly broad permissions | 🔲 Planned |

## My own rule (after the labs)

| Rule | Comes from | Control |
|---|---|---|
| Flag any account without MFA | The top finding in my [phishing investigation](../Analysis-After-It-Happens/Lab-002-Phishing-Investigation.md) | IA-2(1) Multi-Factor Authentication |

---

## What each write-up will include

- The control in plain language
- The rule I wrote
- A test that passes and a test that fails, with the output
- What this would catch in a real environment
