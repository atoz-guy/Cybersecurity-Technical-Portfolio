# SOC Defensive Labs (TCM Security PSAA)

Hands-on defensive security work from TCM Security's Practical SOC Analyst Associate (PSAA) track: network traffic analysis, endpoint triage, log analysis and threat intel.

**Related certifications:** CompTIA Security+, Google Cybersecurity, ServiceNow CIS-SIR (Security Incident Response), TCM PSAA (in progress)

*Moved here from my old TCM-Enterprise-Security-Labs repo so all my security work is in one place. The commit history came with it.*

## Tools and skills

- **Network analysis:** Wireshark, tcpdump, Snort
- **Endpoint detection:** LimaCharlie (EDR), Sysmon, Windows Event Logs
- **SIEM and logs:** Splunk (SPL), log correlation and pattern matching
- **Threat intel:** YARA rules, MITRE ATT&CK mapping, MISP, CyberChef (defanging IOCs)
- **Forensics:** FTK Imager, artifact triage

## Labs

| # | Lab | Focus |
|---|---|---|
| 01 | [Phishing email analysis](challenge1-phishing-emails) | Email triage, IoC identification |
| 02 | [tcpdump](challenge2-tcpdump) | Packet capture, traffic filtering |
| 03 | [Wireshark](challenge3-wireshark) | Protocol and traffic analysis |
| 04 | [Snort](challenge4-snort) | IDS rules and alerts |
| 05 | [Log analysis (Splunk)](challenge5-log-analysis) | SPL searches, log correlation |
| 06 | [Windows endpoint](challenge6-windows-endpoint) | EDR triage, Sysmon, event logs |
| 07 | [Linux endpoint](challenge7-linux-endpoint) | Linux logs and process triage |
| 08 | [MITRE ATT&CK](challenge8-mitre-att&ck) | Mapping activity to techniques |
| 09 | [YARA](challenge9-yara) | Writing malware signatures |

There's also a [phishing report template](phishing-template) I use for write-ups.

For the GRC side of these investigations (risk scores, NIST controls, ServiceNow tracking), see [GRC-Labs](../GRC-Labs).
