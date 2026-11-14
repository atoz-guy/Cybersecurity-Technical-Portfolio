"""Builds auth.log for the practice lab.

The log is made up for teaching. It uses private 10.x addresses for the
office and the documentation-only ranges (192.0.2.x, 198.51.100.x,
203.0.113.x) for the outside world, so none of it points at a real system.
"""
DAY = "2026-03-10"
events = [
    # time, source, event, user, ip, detail
    ("02:00:03", "BACKUP-01",   "Login_Success",   "svc_backup", "10.0.5.20",    "scheduled job nightly-backup"),
    ("02:00:05", "FILESRV-01",  "File_Download",   "svc_backup", "10.0.5.20",    "share=/finance (14.2 GB)"),
    ("02:41:17", "BACKUP-01",   "Logoff",          "svc_backup", "10.0.5.20",    ""),
    ("03:11:52", "VPN-GW",      "Login_Failed",    "admin",      "203.0.113.45", "bad password"),
    ("03:11:55", "VPN-GW",      "Login_Failed",    "admin",      "203.0.113.45", "bad password"),
    ("03:11:58", "VPN-GW",      "Login_Failed",    "admin",      "203.0.113.45", "bad password"),
    ("03:12:02", "VPN-GW",      "Login_Failed",    "admin",      "203.0.113.45", "bad password"),
    ("03:12:05", "VPN-GW",      "Login_Failed",    "admin",      "203.0.113.45", "bad password"),
    ("03:12:09", "VPN-GW",      "Login_Failed",    "admin",      "203.0.113.45", "bad password"),
    ("03:12:13", "VPN-GW",      "Login_Failed",    "admin",      "203.0.113.45", "bad password"),
    ("03:12:16", "VPN-GW",      "Login_Failed",    "admin",      "203.0.113.45", "bad password"),
    ("03:14:40", "VPN-GW",      "Login_Success",   "admin",      "203.0.113.45", "location=Unknown"),
    ("03:16:21", "DC-01",       "Account_Created", "admin",      "203.0.113.45", "new_user=support_tmp"),
    ("03:16:48", "DC-01",       "Group_Changed",   "admin",      "203.0.113.45", "user=support_tmp added_to=Domain Admins"),
    ("03:21:05", "FILESRV-01",  "File_Download",   "support_tmp","203.0.113.45", "file=/hr/payroll_2026.xlsx (1.8 GB)"),
    ("03:24:30", "FILESRV-01",  "Connection_Out",  "SYSTEM",     "10.0.5.30",    "dest=198.51.100.23:4444 process=C:\\Users\\Public\\Temp\\upd.exe"),
    ("03:31:12", "VPN-GW",      "Logoff",          "admin",      "203.0.113.45", ""),
    ("07:58:10", "WKS-MARIA",   "Login_Success",   "maria",      "10.0.1.21",    "location=San Diego"),
    ("08:02:44", "WKS-JLEE",    "Login_Failed",    "jlee",       "10.0.1.34",    "bad password"),
    ("08:02:59", "WKS-JLEE",    "Login_Success",   "jlee",       "10.0.1.34",    "location=San Diego"),
    ("08:15:02", "WKS-TNGUYEN", "Login_Success",   "tnguyen",    "10.0.1.40",    "location=San Diego"),
    ("09:02:11", "M365",        "Login_Success",   "jlee",       "10.0.1.34",    "location=San Diego"),
    ("09:06:37", "M365",        "Login_Success",   "jlee",       "192.0.2.80",   "location=Frankfurt, DE via=CompanyVPN-EU"),
    ("10:30:45", "FILESRV-01",  "File_Download",   "maria",      "10.0.1.21",    "file=/sales/q1_report.pdf (2.1 MB)"),
    ("12:05:19", "FILESRV-01",  "File_Download",   "tnguyen",    "10.0.1.40",    "file=/marketing/logo_pack.zip (48 MB)"),
    ("13:40:02", "WKS-MARIA",   "Login_Failed",    "maria",      "10.0.1.21",    "bad password"),
    ("13:40:20", "WKS-MARIA",   "Login_Success",   "maria",      "10.0.1.21",    "location=San Diego"),
    ("17:02:33", "WKS-JLEE",    "Logoff",          "jlee",       "10.0.1.34",    ""),
    ("17:30:50", "WKS-MARIA",   "Logoff",          "maria",      "10.0.1.21",    ""),
    ("17:45:12", "WKS-TNGUYEN", "Logoff",          "tnguyen",    "10.0.1.40",    ""),
    ("22:00:04", "DC-01",       "Login_Success",   "it_admin",   "10.0.9.5",     "location=San Diego ticket=CHG-1042"),
    ("22:07:40", "DC-01",       "Group_Changed",   "it_admin",   "10.0.9.5",     "user=tnguyen added_to=Marketing-Share ticket=CHG-1042"),
    ("22:15:09", "DC-01",       "Logoff",          "it_admin",   "10.0.9.5",     ""),
]
with open("auth.log", "w") as f:
    for t, src, ev, user, ip, detail in events:
        line = f"{DAY} {t} | {src:<11} | {ev:<15} | User: {user:<11} | IP: {ip:<13}"
        if detail:
            line += f" | {detail}"
        f.write(line.rstrip() + "\n")
print(f"wrote auth.log ({len(events)} lines)")
