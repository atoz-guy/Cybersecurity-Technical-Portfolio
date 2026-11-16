# 01: Explore identity in Microsoft Entra ID

**Module:** [Explore identity in Microsoft Entra ID](https://learn.microsoft.com/en-us/training/modules/explore-identity-azure-active-directory/)
**Done in:** my real tenant for AtoZ CyberLabs and Touchtel Wireless

## What this module covers

<!-- AJ: 2 to 3 sentences in your own words. What is identity, and what does Entra ID do? -->

## What I did

### 1. Created and managed Microsoft Entra users
![Users list with the new test user Akonman](screenshots/01-add-user.png)

Created a test user account named **Akonman** in the AtoZ CyberLabs Microsoft Entra tenant, alongside the existing staff accounts. This exercise showed user provisioning and centralized identity management, supporting NIST AC-2 (Account Management). Real names are blurred.

<!-- AJ: why did you mark test users with a * in front of the name? -->

### 2. Configured Microsoft Entra roles and least privilege
![Akonman's assigned roles: Authentication Administrator and License Administrator](screenshots/02-assign-roles.png)

Assigned Akonman the **Authentication Administrator** and **License Administrator** roles instead of Global Administrator. That's enough to handle a lockout or a new hire's license without handing over the whole tenant. It's role-based access control (RBAC) and least privilege in practice, supporting NIST AC-6 (Least Privilege).

### 3. Changed the primary domain to the business domain
![atozcyberlabs.com verified and set as the primary domain](screenshots/03-primary-domain.png)

Changed the primary domain from the default onmicrosoft.com address to **atozcyberlabs.com**, so new accounts get the business domain. Every account now carries the same organizational identity, supporting NIST IA-4 (Identifier Management). Verifying the domain was an earlier lab: [M365 Lab 09: Entra custom domain](../../M365/09-microsoft-entra-custom-domain).

### 4. Reviewed tenant-wide properties (and chose not to change them)
![Tenant properties: name, region, data location and contacts](screenshots/04-tenant-properties.png)

The lab asks you to change the tenant display name. This is my live business tenant, and that name shows on my staff's sign-in pages and emails, so I reviewed the settings and **left them as they are**. Knowing when not to click Save on a production system is part of the job (NIST CM-3, Configuration Change Control).

What the review confirmed:
- **Name:** AtoZ CyberLabs, matching the new brand
- **Data location:** United States datacenters
- **Technical and privacy contacts:** set (blurred here)
- **Gap found:** the **privacy statement URL is empty**. My website doesn't have a privacy page yet. Adding one, then linking it here, is on my to-do list (NIST PT-5, Privacy Notice).

## NIST SP 800-53 mapping

| Control | Name | How this lab supports it |
|---|---|---|
| AC-2 | Account Management | New accounts are created in one place, with a type and a clear owner |
| AC-6 | Least Privilege | The user got two narrow roles instead of Global Administrator |
| IA-4 | Identifier Management | One naming scheme and one business domain for every account |
| CM-3 | Configuration Change Control | Reviewed tenant settings in production without making an unplanned change |
| PT-5 | Privacy Notice | Found the missing privacy statement URL and logged it as a follow-up |

## Privacy

Real people's names and photos, the admin account name, the signed-in admin in the top corner, the tenant ID and contact emails are blurred.

## What I learned

<!-- AJ: 1 or 2 things that clicked for you in this module -->
