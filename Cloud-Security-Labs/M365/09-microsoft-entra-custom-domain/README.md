# Lab 9: Adding and Verifying a Custom Domain in Microsoft Entra ID

**Skill area:** Identity administration, DNS, domain verification  
**Related exam:** SC-300, AZ-104  
**Status:** ✅ Complete  
**Date completed:** 2026-11-13

---

## Objective

Move my tenant off the default `.onmicrosoft.com` address and onto my own business domain, `atozcyberlabs.com`. That meant proving to Microsoft that I own the domain, then changing the admin account's display name and sign-in name to match the business.

This was done in my real tenant for my business, ATOZ Cyber Labs, not a throwaway lab.

---

## Environment / Setup

| Piece | Where it lives |
|---|---|
| Identity | Microsoft Entra ID tenant (AtoZ CyberLabs) |
| Domain registrar | Porkbun (where I bought the domain) |
| DNS host | Wix (where the domain's records are managed) |
| Email | Forwarded through Porkbun's mail forwarding |

---

## Steps

1. **Added the domain in Entra.** Entra admin center → Custom domain names → Add custom domain → `atozcyberlabs.com`. Microsoft gave me a TXT record to prove ownership: host `@`, value `MS=ms########`, TTL 3600.
2. **Found out who actually runs the DNS.** I bought the domain at Porkbun, so I checked there first. Porkbun said the domain wasn't using its nameservers. The nameservers were `ns8.wixdns.net` and `ns9.wixdns.net`, so **Wix** manages the records. Porkbun offered to "update my domain" to its own nameservers. I didn't, because that would have taken my website offline.
3. **Added the TXT record in Wix.** Wix → Domains → Manage DNS Records → TXT → Add Record. Host left blank (root domain), value `MS=ms########`, TTL 1 hour. I left every other record alone: the website's A and CNAME records, the email MX records, and the existing SPF record.
4. **Verified in Entra.** Waited a few minutes for the record to spread, then clicked Verify. It passed on the first try.
5. **Updated the admin account.** Changed the display name from "AtoZ Wireless" (my old business name) to "AtoZ CyberLabs", and changed the sign-in name's domain from `.onmicrosoft.com` to `atozcyberlabs.com`.

---

## Results

| Test | Expected | Actual | Pass/Fail |
|---|---|---|---|
| Domain added to the tenant | Shows in Custom domain names | Shows, waiting for verification | ✅ Pass |
| TXT record added without breaking anything | Website, email and SPF unchanged | Only the new TXT line added | ✅ Pass |
| Domain verification | Microsoft finds the record | Verified | ✅ Pass |
| Display name updated | "AtoZ CyberLabs" | Updated, initials changed AW → AC | ✅ Pass |
| Sign-in name updated | Ends in `@atozcyberlabs.com` | Updated | ✅ Pass |

---

## What I learned

**The registrar and the DNS host aren't always the same.** Where you bought a domain and where its records live can be two different companies. When you connect a domain to a website builder like Wix, it often takes over the DNS. Checking the nameservers first tells you where changes actually need to go.

**Know what each DNS record does before touching anything.** A records point to the website, CNAME handles `www`, MX routes email, TXT holds proof-of-ownership notes like SPF and Microsoft's code, and NS says who's in charge. Adding one TXT record was safe because I knew what everything else was doing.

**The `.onmicrosoft.com` name is permanent.** Microsoft doesn't let you rename or delete the tenant's original domain. You add your own domain next to it instead.

**Changing a sign-in name changes how you log in.** The old `.onmicrosoft.com` sign-in stops working, so you need to know the new one before signing out.

---

## What I'd do in production

- **Keep a break-glass admin.** Have a second emergency admin account that stays on the `.onmicrosoft.com` domain. If the custom domain ever has a DNS problem, you can still get in.
- **Don't use "admin" as the username.** It's the first name attackers guess. Use something less predictable.
- **Don't do daily work as Global Administrator.** Use a regular account day to day and a separate admin account only when needed.
- **Set the custom domain as primary** so new users get the business domain by default.
- **Document the change.** Record what changed, when and why, so there's an audit trail.

---

## The GRC angle

| Control (NIST 800-53) | How this lab supports it |
|---|---|
| **IA-4** Identifier Management | Admin identity now uses the organization's own domain and name |
| **AC-2** Account Management | Account details kept accurate and current (old business name removed) |
| **CM-3** Configuration Change Control | Change made carefully, with no impact on other services, and documented here |

---

## Resources / References

- [Microsoft Learn: Add your custom domain name to Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/fundamentals/add-custom-domain)
