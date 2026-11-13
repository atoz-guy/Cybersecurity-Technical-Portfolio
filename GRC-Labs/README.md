# GRC Labs

GRC work happens on both sides of an incident.

| Folder | When | What it does |
|---|---|---|
| [Analysis-After-It-Happens](Analysis-After-It-Happens) | **After something happens** | Investigate it, score the risk, find which controls failed, and write up the fix |
| [Engineering-Before-It-Happens](Engineering-Before-It-Happens) | **Before anything happens** | Turn controls into code that blocks a bad change automatically, so the gap can't open in the first place |

---

## How they connect

Analysis finds the gap. Engineering closes it for good.

For example, my phishing investigation found that MFA was the missing control. On the engineering side, [Lab 04](Engineering-Before-It-Happens/04-MFA-for-Privileged-Accounts) turns that into a rule that enforces MFA automatically, so nobody has to remember to check.

```
Something happens  →  Analysis: score it, map the failed control, recommend a fix
                                              ↓
                      Engineering: write the fix as a rule that runs automatically
                                              ↓
                      Next time, it gets blocked before it happens
```

Risk scores use my [risk matrix](Analysis-After-It-Happens/risk-matrix.md) and the [risk scoring script](https://github.com/atoz-guy/Python-Automation-Lab) I wrote in Python.
