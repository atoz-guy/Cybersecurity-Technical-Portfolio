**# Case Study #2 : Cloud Account Lockout Resolution**

# Cloud Account Lockout Resolution
**Ticket ID:** #1043
**Category:** Identity & Access Management (IAM)
**Priority:** High

### 1. Initial Assessment
* **User Report:** User reported an "Account Locked" error while attempting to sign into the corporate cloud-based portal.
* **Impact:** User unable to access mission-critical applications, causing a direct work stoppage.

### 2. Troubleshooting Steps
* **Step 1:** Verified user identity against the company directory.
* **Step 2:** Accessed the Cloud Identity Provider (IDP) console.
* **Step 3:** Confirmed account status was set to "Locked" due to multiple failed login attempts.

### 3. Resolution
* Reset the user's password via the IDP console.
* Unlocked the account and provided the user with temporary credentials.
* Instructed the user to update their password immediately upon successful login.

### 4. Verification
* Confirmed with the user that portal access was restored and they could successfully log in with their new credentials.

### 5. Root Cause
* Account lockout triggered by excessive failed authentication attempts; common in environments where password policies are strictly enforced or sync errors occur between local and cloud environments.
