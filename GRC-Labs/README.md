# GRC Labs

GRC work happens on both sides of an incident.

**Related certifications:** ISACA CRISC (exam passed), ServiceNow CIS-RC (Risk and Compliance), ISACA CISM and CISA (booking next)

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

## Policy as code works with any GRC platform

The engineering side isn't tied to one product. The rules I write check settings and produce a pass or fail. A GRC platform like ServiceNow or Archer then uses that result as evidence.

```
Policy as code (GRC Playground)
   → checks the setting automatically: "Is MFA on? Is this bucket public?"
   → produces a pass or fail result
            ↓
GRC platform (ServiceNow or Archer)
   → records the result as evidence for the control
   → flags failures as issues, assigns owners, tracks the fix
```

**The rule does the checking. The platform does the tracking and proving.** The platforms don't run the rules themselves. They receive the results through integrations and use them for automated control testing, so evidence is collected all the time instead of by hand once a year.

That's why I learn policy as code first: it plugs into whichever platform a company uses.

---

Risk scores use my [risk matrix](Analysis-After-It-Happens/risk-matrix.md) and the [risk scoring script](https://github.com/atoz-guy/Python-Automation-Lab) I wrote in Python.
