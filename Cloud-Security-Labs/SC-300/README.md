# SC-300: Microsoft Identity and Access Administrator

My course log for the Microsoft Certified: Identity and Access Administrator Associate. Every lab is done in **my real Microsoft Entra tenant**, the one I run for my two stores (AtoZ CyberLabs and Touchtel Wireless), not a throwaway sandbox.

For each module I show what I set up, why it matters, and which NIST SP 800-53 control it supports.

**Status:** ✅ SC-300 certified. In November 2026 I went back through the full learning path as a refresher and redid the labs in my real tenant, documented here.

**Exam domains:** manage user identities · authentication and access management · workload identities · identity governance

---

## How I explain every security decisio n

Every choice in these labs is written the same way:

**Business need → Security risk → Control implemented → Expected outcome**

Example from module 01:

> **Business need:** we need external contractors to collaborate with our organization.
> **Security risk:** unrestricted guest invitations increase the risk of unauthorized access.
> **Control implemented:** I restricted guest invitations to designated administrators and limited guest directory visibility.
> **Expected outcome:** less unnecessary exposure of tenant data, and every outside account is approved by an admin.

---

## Course log

| # | Module | What I did in my tenant | NIST | Status |
|---|---|---|---|---|
| 01 | [Explore identity in Microsoft Entra ID](01-explore-identity) | Created a user, assigned least-privilege roles, made atozcyberlabs.com the primary domain, reviewed tenant properties, added a privacy contact, locked down guest access and invites | AC-2, AC-3, AC-6, IA-4, CM-3, PM-19, PT-5 | 🟡 AJ's notes to add |

---

## Privacy

Before any screenshot goes up, I blur tenant IDs, object IDs, staff email addresses, IP addresses, and anything about the break-glass account.
