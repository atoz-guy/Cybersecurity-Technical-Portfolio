Technical Log: Snort Analysis
Date: 2026-05-26
Raw Commands
snort -A console -q -c /etc/snort/snort.conf -i eth0

Rule Development
Attempt 1: (Failed: syntax error on port)

Attempt 2: (Successful: alert tcp any any -> any 80 ...)

Troubleshooting
Encountered permission issues with the configuration file. Resolved by running as sudo.

False positive rate was high; tuned the rule to look at specific headers rather than all traffic.
