"""Flag the 5 red flags from "Read Logs Like a Detective" in a log file.

Usage:  python3 find_red_flags.py auth.log

It only points at lines worth a closer look. Every flag still needs a
human to check for the innocent explanation (a ticket, a VPN, a backup job).
"""
import re
import sys
from collections import defaultdict
from datetime import datetime, timedelta

BUSINESS_HOURS = (7, 20)          # 7 AM to 8 PM counts as normal
BRUTE_FORCE_FAILS = 3             # this many failures before a success
BRUTE_FORCE_WINDOW = timedelta(minutes=10)
TRAVEL_WINDOW = timedelta(hours=1)
NORMAL_PORTS = {"80", "443", "53", "22", "25", "587", "993"}


def parse(path):
    events = []
    for n, raw in enumerate(open(path, encoding="utf-8"), 1):
        parts = [p.strip() for p in raw.rstrip("\n").split("|")]
        if len(parts) < 5:
            continue
        when = datetime.strptime(parts[0], "%Y-%m-%d %H:%M:%S")
        events.append({
            "line": n,
            "time": when,
            "source": parts[1],
            "event": parts[2],
            "user": parts[3].replace("User:", "").strip(),
            "ip": parts[4].replace("IP:", "").strip(),
            "detail": parts[5] if len(parts) > 5 else "",
        })
    return events


def location(e):
    m = re.search(r"location=([^|]+?)(?: via=| ticket=|$)", e["detail"])
    return m.group(1).strip() if m else None


def main(path):
    events = parse(path)
    flags = []

    # 1. Failed logins, then a success
    fails = defaultdict(list)
    for e in events:
        key = (e["user"], e["ip"])
        if e["event"] == "Login_Failed":
            fails[key].append(e["time"])
        elif e["event"] == "Login_Success":
            recent = [t for t in fails[key] if e["time"] - t <= BRUTE_FORCE_WINDOW]
            if len(recent) >= BRUTE_FORCE_FAILS:
                flags.append((e, "Failed logins, then a success",
                              f"{len(recent)} failures from {e['ip']} before this login"))
            fails[key] = []

    # 2. After-hours activity (sign-ins and changes, not logoffs)
    for e in events:
        if e["event"] in ("Login_Success", "Account_Created", "Group_Changed", "File_Download"):
            if not BUSINESS_HOURS[0] <= e["time"].hour < BUSINESS_HOURS[1]:
                flags.append((e, "After-hours activity", f"{e['event']} at {e['time']:%H:%M}"))

    # 3. Impossible travel
    last_seen = {}
    for e in events:
        loc = location(e)
        if e["event"] != "Login_Success" or not loc:
            continue
        prev = last_seen.get(e["user"])
        if prev and prev[1] != loc and e["time"] - prev[0] <= TRAVEL_WINDOW:
            mins = int((e["time"] - prev[0]).total_seconds() // 60)
            flags.append((e, "Impossible travel", f"{prev[1]} to {loc} in {mins} min"))
        last_seen[e["user"]] = (e["time"], loc)

    # 4. New or changed accounts
    for e in events:
        if e["event"] in ("Account_Created", "Group_Changed"):
            flags.append((e, "New or changed account", e["detail"]))

    # 5. Unusual programs or connections
    for e in events:
        if e["event"] == "Connection_Out":
            port = re.search(r"dest=[\d.]+:(\d+)", e["detail"])
            odd_port = port and port.group(1) not in NORMAL_PORTS
            temp_exe = re.search(r"\\Temp\\|/tmp/", e["detail"], re.I)
            if odd_port or temp_exe:
                why = []
                if odd_port:
                    why.append(f"unusual port {port.group(1)}")
                if temp_exe:
                    why.append("program running from a temp folder")
                flags.append((e, "Unusual program or connection", ", ".join(why)))

    flags.sort(key=lambda f: (f[0]["time"], f[0]["line"]))
    print(f"{len(flags)} flags in {path} ({len(events)} lines)\n")
    for e, kind, why in flags:
        print(f"line {e['line']:>3}  {e['time']:%H:%M:%S}  {kind:<30} user={e['user']:<11} {why}")
    print("\nNext step: check each flag for an innocent explanation (ticket, VPN, scheduled job).")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "auth.log")
