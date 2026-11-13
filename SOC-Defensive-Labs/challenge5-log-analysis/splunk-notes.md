# Technical Log: Log Analysis & Splunk Investigation

## Date: 2026-05-26

### Tools Used
- Splunk Enterprise
- CLI (grep, awk, sed)

### Quick Reference: SPL Cheat Sheet
- **Filter by index:** `index=main`
- **Search for specific IP:** `index=main src_ip=192.168.1.5`
- **Count events by user:** `index=main | stats count by user`
- **Filter by status code:** `index=main status=404`

### Analysis Log
* **Task 1:** (Describe the search goal)
  - **Query Used:** - **Result:** (Did you find the anomaly?)
* **Task 2:** (Describe the next stage of the investigation)
  - **Query Used:** - **Result:** ### Issues & Troubleshooting
- (Note any syntax errors in your SPL or issues with data ingestion)

### Key Findings
- (Summarize the "malicious" activity discovered in the logs)
