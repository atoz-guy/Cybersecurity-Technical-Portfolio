# Answer key

Try the lab by hand first. This page gives everything away.

## The story

Someone outside the company guessed the `admin` password on the VPN at 3 AM, made themselves a hidden admin account, took the payroll file, and left a program on the file server that calls home.

| Time | Line | What happened | Red flag |
| --- | --- | --- | --- |
| 03:11:52 to 03:12:16 | 4 to 11 | 8 failed VPN logins as `admin` from 203.0.113.45 in 24 seconds | Repetition, after hours |
| 03:14:40 | 12 | The guess works. `admin` is in, from an unknown location | Failed logins, then a success |
| 03:16:21 | 13 | `admin` creates a new account, `support_tmp` | New account |
| 03:16:48 | 14 | `support_tmp` is added to Domain Admins. Now the attacker has a second way in, even if `admin`'s password is changed | Changed account |
| 03:21:05 | 15 | `support_tmp` downloads `/hr/payroll_2026.xlsx` (1.8 GB) | After hours, large file |
| 03:24:30 | 16 | The file server opens a connection to 198.51.100.23 on port 4444, from `upd.exe` in a Temp folder | Unusual program and connection |
| 03:31:12 | 17 | `admin` logs off the VPN | |

**Escalate:** yes. Disable `admin` and `support_tmp`, reset the `admin` password, isolate FILESRV-01, block 203.0.113.45 and 198.51.100.23, and treat the payroll file as leaked (that's employee personal data, so HR and possibly legal need to know).

## The false alarms

The script flags these too. Each one has an innocent explanation in the log itself.

| Line | Flag | Why it's fine |
| --- | --- | --- |
| 1 to 2 | After hours: `svc_backup` downloads 14.2 GB at 2 AM | It's a service account running `scheduled job nightly-backup` from the backup server, inside the office (10.0.5.20). Same thing every night |
| 23 | Impossible travel: `jlee` in San Diego, then Frankfurt 4 minutes later | The Frankfurt login came `via=CompanyVPN-EU`, the company's own VPN. Her laptop routed through the EU gateway |
| 31 to 32 | After hours and changed account: `it_admin` at 10 PM adds `tnguyen` to a group | It has a change ticket (`CHG-1042`), comes from the IT subnet (10.0.9.5), and only gives access to a marketing share |

**Not flagged, and shouldn't be:** `jlee` at 8:02 AM and `maria` at 1:40 PM each fail once, then succeed seconds later from their own desks. One typo is just a typo.

## MITRE ATT&CK mapping

| Step | Technique |
| --- | --- |
| Guessing the VPN password | [T1110.001 Brute Force: Password Guessing](https://attack.mitre.org/techniques/T1110/001/) |
| Getting in through the VPN | [T1133 External Remote Services](https://attack.mitre.org/techniques/T1133/) |
| Logging in as a real account | [T1078 Valid Accounts](https://attack.mitre.org/techniques/T1078/) |
| Creating `support_tmp` | [T1136.002 Create Account: Domain Account](https://attack.mitre.org/techniques/T1136/002/) |
| Adding it to Domain Admins | [T1098 Account Manipulation](https://attack.mitre.org/techniques/T1098/) |
| Taking the payroll file from the share | [T1039 Data from Network Shared Drive](https://attack.mitre.org/techniques/T1039/) |
| Calling home on port 4444 | [T1571 Non-Standard Port](https://attack.mitre.org/techniques/T1571/) |

## What would have stopped it

- **MFA on the VPN.** The guessed password alone wouldn't have been enough.
- **Account lockout** after a few failed logins.
- **No shared account named `admin`.** Admins should sign in with their own named accounts, so every action traces to a person.
- **An alert** on new members of Domain Admins.
