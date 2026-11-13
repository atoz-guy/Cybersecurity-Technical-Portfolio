# Lab 05: Log Analysis & Splunk Investigation

## Objective
Analyze structured and unstructured logs to detect malicious activity, correlate events, and generate actionable intelligence using Splunk.

## Methodology
- Ingest raw log data into Splunk.
- Utilize Search Processing Language (SPL) to filter, transform, and visualize event data.
- Perform behavioral analysis to identify anomalies (e.g., failed logins, command injection, path traversal).

## Tools Used
- Splunk Enterprise
- CLI Log Analysis (e.g., `grep`, `awk`, `sed`)

## Analysis & Findings
- **Log Source Analysis:** (What data was ingested? e.g., web server logs, auth logs)
- **Key SPL Queries:** - (Example: `index=main | stats count by src_ip | sort - count`)
- **Malicious Patterns Detected:** (Summary of findings, e.g., brute force attempts, unauthorized directory access)

## Lessons Learned
- (How did Splunk’s correlation features change your detection capability vs. manual grep-ing?)
