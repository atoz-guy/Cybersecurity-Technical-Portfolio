# Lab 10: Read Logs Like a Detective

**By Afiz (AJ) Jiwa** · November 2026

A beginner's guide to log analysis that I wrote for customers of my store, plus a hands-on practice lab: a day of logs with a break-in hidden among normal activity and false alarms.

- **Read it on my website:** [atozcyberlabs.com/logs-guide.html](https://www.atozcyberlabs.com/logs-guide.html)
- **Try the lab:** [practice-lab](practice-lab/) (start with the log, save the answer key for last)

**Why I wrote it:** most security guides are written for people who already know security. I wanted one that a store customer could follow, and that still teaches the same habits a SOC analyst uses on the job.

**Skills shown:** log analysis, alert triage, separating real attacks from false positives, writing for a non-technical audience, Python (pattern detection)

---

## The guide

Every login, download and connection leaves a record behind. Log analysis is reading those records like a detective reads a crime scene: timestamps, IP addresses and failed passwords instead of fingerprints.

When ransomware hits at 3 AM or data quietly flows to an unknown server, the logs show how it happened and who did it. By the end of this guide you'll know what's inside a log, how to read one, and the five red flags that mean "look closer."

### What is a log?

A log is a diary that computers write about themselves, automatically, every second. Someone signs in: logged. A file is downloaded: logged. A device connects to the internet: logged.

You don't need to understand every log. Even experienced analysts don't. What matters is learning to spot patterns, the same way a detective doesn't read every page of a case file but knows which details matter.

### The 5 parts of a log

Most log lines answer the same five questions. Not every log has all five, but this is what to look for.

| Question | Part | What it tells you | Example |
| --- | --- | --- | --- |
| When? | Timestamp | When it happened. Always start here. | `2025-10-22 03:15:42` |
| Where? | Source | Which system wrote the log | `SERVER-DB01`, `firewall-prod`, `10.0.1.50` |
| What? | Event type | The action that happened | `Login_Failed`, `file_deleted` |
| Who? | User or actor | The person, account or program behind it | `admin`, a service account |
| Did it work? | Outcome | Success or failure. Failures are often the most interesting. | `Failed` |

Put together, one line looks like this:

```
2025-10-22 03:15:42 | SERVER-DB01 | Login_Failed | User: admin | Source IP: 192.168.1.100
```

**In plain English:** at 3:15 AM, someone at IP address 192.168.1.100 tried to sign in to SERVER-DB01 as "admin" and failed.

### Read a log in 4 steps

```
2025-10-22 03:14:05 | SERVER-DB01 | Login_Failed  | User: admin | Source IP: 192.168.1.100
2025-10-22 03:14:09 | SERVER-DB01 | Login_Failed  | User: admin | Source IP: 192.168.1.100
2025-10-22 03:14:12 | SERVER-DB01 | Login_Failed  | User: admin | Source IP: 192.168.1.100
2025-10-22 03:15:42 | SERVER-DB01 | Login_Success | User: admin | Source IP: 192.168.1.100
2025-10-22 03:17:10 | SERVER-DB01 | File_Download | User: admin | customer_list.csv (2.4 GB)
```

1. **Check the time.** 3:14 AM. Is anyone supposed to be working on this server in the middle of the night?
2. **Look for repetition.** Three failed logins in seven seconds from the same address. One failure is a typo. A burst like this is someone guessing.
3. **Watch for the turn.** The failures stop and a success appears. That usually means the guess worked.
4. **Follow what happens next.** Two minutes later, "admin" downloads a 2.4 GB customer file. Now you have a story: someone guessed the admin password at 3 AM and took customer data.

That last step is the one beginners skip. A single log line is a clue. The lines around it are the story.

### 5 red flags every analyst should know

None of these proves an attack on its own, so check for the innocent explanation before you sound the alarm.

| Red flag | What it looks like | Could be innocent if... |
| --- | --- | --- |
| **Failed logins, then a success** | Several failures, then a login that works | The user forgot their password and finally got it right (check the IP and time) |
| **After-hours activity** | Admin accounts active at 3 AM, big weekend file transfers, accounts created overnight | It's planned maintenance or a scheduled backup |
| **Impossible travel** | Signed in from New York at 9:00 AM, then China at 9:05 AM | A VPN, cloud proxy or phone syncing makes the location look wrong |
| **New or changed accounts** | A surprise admin account, sudden permission changes, an old account turned back on | IT made the change and has a ticket for it |
| **Unusual programs or connections** | Programs running from temp folders, servers reaching out to the internet, odd ports | New software that hasn't been documented yet |

### Detective habits

**Do:**
- **Know what normal looks like.** An admin logging in at 2 AM for planned maintenance is normal. A regular user suddenly downloading 50 GB when they usually move a few megabytes is not.
- **Start broad, then narrow.** Filter by a username, an IP address or an event type.
- **Write down your searches.** If you can't retrace your steps, no one can check your work.

**Don't:**
- **Read logs in isolation.** The lines before and after tell the story.
- **Skip the timestamps.** Time connects one event to the next.
- **Treat every alert as an emergency.** Telling routine from real keeps analysts sharp instead of burned out.

### Your investigation checklist

- [ ] What triggered the alert?
- [ ] When did it happen?
- [ ] Who was involved?
- [ ] Has this happened before?
- [ ] Does it match known bad behavior?
- [ ] Do I need to escalate it?

### Try it on your own accounts

| Account | Where to look | What it shows |
| --- | --- | --- |
| [Google](https://myaccount.google.com/security-checkup) | Security, then Security Checkup | Recent security activity from the last 28 days, plus every device signed in |
| [Microsoft](https://account.microsoft.com/) | Security, then Recent activity | Each sign-in from the past 30 days, with device and location |
| [Apple](https://account.apple.com/) | Devices (or on iPhone: Settings, then your name) | Every device currently signed in |

### Resources

- [Have I Been Pwned](https://haveibeenpwned.com/): check if your email showed up in a data breach
- [CISA Secure Our World](https://www.cisa.gov/secure-our-world): four simple steps to stay safe online
- [Google Security Checkup](https://myaccount.google.com/security-checkup): a guided review of your Google account

---

## Practice lab

The [practice-lab](practice-lab/) folder has one day of logs from a small office (33 lines). Somewhere in it is a real break-in. There are also three things that look suspicious but aren't.

**Your job:** use the 4 steps and the checklist to find the attack, write the story of what happened, and explain which flags are false alarms.

| File | What it is |
| --- | --- |
| [auth.log](practice-lab/auth.log) | The logs. Start here |
| [find_red_flags.py](practice-lab/find_red_flags.py) | A Python script that flags all 5 red flags. Run it after you've tried by hand: `python3 find_red_flags.py auth.log` |
| [ANSWER-KEY.md](practice-lab/ANSWER-KEY.md) | The full story, the false alarms, and the MITRE ATT&CK techniques |
| [make_log.py](practice-lab/make_log.py) | How the log was built |

The log is made up for teaching. Office machines use private 10.x addresses, and outside addresses use the ranges reserved for documentation (192.0.2.x, 198.51.100.x, 203.0.113.x), so nothing points at a real system.

For the real-tool version of this skill, see [Lab 05: Log analysis in Splunk](../challenge5-log-analysis).
