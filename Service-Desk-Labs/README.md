# Service Desk Labs

How I handle IT support tickets from start to finish: triage, troubleshooting, resolution and documentation. Built during TCM Security's Practical Help Desk Associate (PHDA) training using Spiceworks Cloud Help Desk.

**Related certifications:** TCM PHDA, ServiceNow CSA (Certified System Administrator)

This is the ITSM foundation under my ServiceNow work. Ticket lifecycle, priorities and SLAs are the same ideas ServiceNow is built on.

*Moved here from my old Cloud-IT-Service-Management-Workflow repo. The commit history came with it.*

---

## How I work a ticket

1. **Acknowledge:** confirm I got it and set expectations with the user
2. **Triage:** set the priority and category
3. **Diagnose:** isolate the fault (logs, permissions, connectivity)
4. **Resolve or escalate:** fix it, or hand it to Tier 2/3 with full notes
5. **Document:** write down the fix so the next person doesn't start from zero

---

## Case studies

| # | Case | Category |
|---|---|---|
| 1 | [Spiceworks Cloud Help Desk Setup](Case-01-Help-Desk-Setup.md) | Ticketing platform |
| 2 | [Cloud Account Lockout](Case-02-Account-Lockout.md) | Identity and access |
| 3 | [Network Connectivity](Case-03-Network-Connectivity.md) | Networking |
| 4 | [User Permissions and Access](Case-04-User-Permissions.md) | Active Directory |
| 5 | [Printer Spooler](Case-05-Printer-Spooler.md) | Operating system |

---

## Tools I use

- [Ticket Template](Ticket-Template.md): the structure every case follows
- [Troubleshooting Script](Troubleshooting-Script.md): the questions I ask to get the facts fast
- [PHDA Roadmap](PHDA-Roadmap.md): what the certification covers
- [PHDA Certificate](TCM-PHDA-Certificate.pdf)

---

## The GRC angle

Cases 2 and 4 are access control problems: lockouts and permissions. In NIST 800-53 those fall under **AC-2** (account management) and **AC-7** (failed logon attempts), the same controls that show up in my [GRC-Labs](../GRC-Labs).
