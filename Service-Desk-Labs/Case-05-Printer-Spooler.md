# Case Study #5: Printer Spooler Troubleshooting

## Incident Details
* **Category:** Peripherals and Workstation
* **Priority:** Medium
* **Status:** Has been Resolved

## Issue
User reported that they could not print. Received error: "Spooler Subsystem App has stopped."

## Diagnostic Steps
1. **Verification:** Verified printer does turn on and connected to the network.
2. **Investigation:** Confirmed "Print Spooler" service status in `services.msc.
3. **Finding:** Service was stopped and crashed. Attempting to start it resulted in an error.
4. **Resolution:** Cleared corrupted print jobs in `C:\Windows\System32\spool\PRINTERS` and restarted the Print Spooler service.

## Lessons Learned
* **Service Management:** Familiarity with `services.msc` is essential for resolving background process failures.
* **Corrupt Spool Files:** Print jobs stuck in the queue can often corrupt the spooler service itself.
