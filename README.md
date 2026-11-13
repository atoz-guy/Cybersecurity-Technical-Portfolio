# Cybersecurity Technical Portfolio

**Afiz (AJ) Jiwa** | GRC | ServiceNow SecOps & IRM

This is where my hands-on security work lives. Labs show I can do the technical analysis. The GRC investigations show what happens next: scoring the risk, finding which controls failed, and tracking the fix to closure.

For my GRC focus and roadmap, see [GRC-Governance-Risk-Compliance](https://github.com/atoz-guy/GRC-Governance-Risk-Compliance).

---

## What's here

| Folder | What's in it |
|---|---|
| [SOC-Defensive-Labs](SOC-Defensive-Labs) | TCM Security PSAA labs: Wireshark, tcpdump, Snort, Splunk, endpoint triage, MITRE ATT&CK, YARA |
| [GRC-Investigations](GRC-Investigations) | TCM Security PSAA cases taken further: a phishing and BEC investigation with risk scores, NIST 800-53 control gaps and remediation |
| [Forward-Deployed-Identity-Security](Forward-Deployed-Identity-Security) | Work in progress: CyberArk PAM, Microsoft Entra, and connecting both to ServiceNow |
| [Service-Desk-Labs](Service-Desk-Labs) | Access control and service desk work |
| [tools/simulations](tools/simulations) | Simulation projects |

---

## How the pieces connect

1. **Detect:** a SOC lab finds something (a phishing email, a strange login, bad traffic)
2. **Score:** rate it with Likelihood x Impact using my [risk matrix](GRC-Investigations/risk-matrix.md)
3. **Map:** find the NIST 800-53 controls that should have stopped it
4. **Track:** open it in ServiceNow and follow it to closure

---

## Related repos

- [Python-Automation-Lab](https://github.com/atoz-guy/Python-Automation-Lab): the GRC audit logger and risk scoring scripts used in these investigations
- [ServiceNow-](https://github.com/atoz-guy/ServiceNow-): ServiceNow certs and builds
- [azure-labs](https://github.com/atoz-guy/azure-labs): AZ-104 labs
- [ms365-compliance-governance-security-labs](https://github.com/atoz-guy/ms365-compliance-governance-security-labs): Microsoft 365 compliance labs
