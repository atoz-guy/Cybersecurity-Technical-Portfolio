# Lab 8: Baseline Identity Hardening with Microsoft Entra Security Defaults

**Skill area:** Identity Security, Zero Trust, MFA
**Related exam:** SC-300
**Status:** ✅ Complete

## Objective
Implement baseline Zero Trust security policies on a Microsoft Entra ID free tenant to enforce mandatory Multi-Factor Authentication (MFA) and block legacy authentication protocols.

## Why Security Defaults
On a free Microsoft Entra ID tenant, advanced identity tools like Privileged Identity Management (PIM) and custom Conditional Access Policies aren't available. They require an Entra ID P1/P2 or Entra Suite license. Security Defaults was the right architectural call within that constraint:

- **Zero cost, zero setup friction**: works instantly on free developer/test tenants, no sandbox workarounds needed
- **Core protection baseline**: enforces MFA via Microsoft Authenticator for every account, standard users and admins alike
- **Protocol hardening**: automatically blocks legacy sign-in methods (POP3, IMAP, SMTP basic auth) that attackers routinely target for credential harvesting
- **Pragmatic engineering**: shows the ability to lock down an environment with built-in controls when enterprise-tier tools aren't on the table

## Execution
1. Navigated to Microsoft Entra ID → Properties in the Azure portal
2. Located Security Defaults and enabled the tenant-wide protection baseline
3. Confirmed global enforcement: every account in the directory, standard and admin, now required to register for and use MFA at sign-in

## Validation
- ✅ Tenant properties dashboard confirms the organization is protected by Security Defaults
- ✅ Legacy authentication protocols fully blocked across the directory

## Evidence
*Email and tenant identifiers blurred for privacy.*

![Entra Security Defaults enabled: organization protected by security defaults](lab8-security-defaults-evidence.png)

