# Forward Deployed Identity Security

*Work in progress. This is my plan and where the labs will go as I build them.*

**Related certifications:** SC-300 Identity and Access Administrator, SC-100 Cybersecurity Architect, ServiceNow SecOps (CIS-DF, CIS-SIR, CIS-VR), CyberArk (planned)

A forward deployed engineer doesn't just know a tool. They deploy it in a real environment, connect it to the systems around it, and make it part of how the business runs. This track is how I'm building toward that for identity and privileged access.

It also means speaking two languages. I need to talk to a CISO about risk and accountability, then turn that into working controls and hand it off cleanly. My ISACA certs cover the first part. This track covers the second. ([How I see it](https://github.com/atoz-guy/GRC-Governance-Risk-Compliance/blob/main/Pathway.md#how-i-see-it))

There are three layers:

| Layer | Tool | What it does |
|---|---|---|
| **Protect privileged accounts** | CyberArk | Vaults admin credentials, rotates passwords, records privileged sessions |
| **Control identity** | Microsoft Entra | Who someone is, what they can sign in to, and under what conditions |
| **Run it as a process** | ServiceNow | Access requests, approvals, incidents and audit evidence |

Each one alone is useful. Connected, they answer the question every auditor asks about privileged access: **who had admin rights, who approved it, and can you prove it?**

---

## What's here

| Folder | Focus | Status |
|---|---|---|
| [CyberArk-PAM](CyberArk-PAM) | Vault administration, safes, platforms, component architecture | Starting |
| [Entra-Identity](Entra-Identity) | Conditional Access, Privileged Identity Management, access reviews | Planned |
| [Integrations](Integrations) | CyberArk + Entra + ServiceNow working together | Planned |

---

## Why this connects to GRC

Privileged access is one of the first things an audit looks at. NIST 800-53 controls like **AC-2** (account management), **AC-6** (least privilege) and **AU-2** (audit logging) all depend on it. This track is the hands-on side of those controls.

**Related:** [ServiceNow-](https://github.com/atoz-guy/ServiceNow-) (SecOps certs) · [Azure labs](../Cloud-Security-Labs/Azure) (RBAC) · [GRC-Labs](../GRC-Labs)
