**# Case Study #3 : Network-Connectivity Troubleshooting**

# Network Connectivity Issue
**Ticket ID:** #1042
**Category:** Networking Basics
**Priority:** High

### 1. Initial Assessment
* **User Report:** User reported an inability to access the internal "Finance" file server. Internet connectivity is confirmed active, suggesting a localized network issue.
* **Impact:** User unable to access critical financial documents.

### 2. Troubleshooting Steps
* **Step 1:** Verified user has active internet access.
* **Step 2:** Attempted to ping the file server IP address from the user's machine.
* **Step 3:** Ran `tracert` to the server IP to identify where the connection was dropping.
* **Step 4:** Observed a timeout occurring at the local switch gateway.

### 3. Resolution
* Physically inspected the workstation area and identified a faulty network patch cable at the wall jack.
* Replaced the damaged Cat6 patch cable with a new, tested cable.

### 4. Verification
* Performed a ping test to the file server IP; received successful replies.
* Confirmed with the user that the "Finance" folder share is now accessible.

### 5. Root Cause
* Physical layer failure (damaged network patch cable) preventing local network communication.
