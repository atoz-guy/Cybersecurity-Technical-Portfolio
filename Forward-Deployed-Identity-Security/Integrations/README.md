# Integrations: CyberArk + Entra + ServiceNow

*Planned. This is the goal the rest of the track builds toward.*

This is where the forward deployed part comes in: making the three tools work as one process instead of three separate ones.

## The flow I want to build

```
1. Request      An admin asks for privileged access in ServiceNow
2. Approve      Their manager approves the ticket
3. Verify       Entra confirms who they are (MFA, Conditional Access)
4. Grant        CyberArk checks the approved ticket and releases the credential
5. Record       The session is recorded in CyberArk
6. Evidence     Ticket, approval and session log are tied together for audit
```

## Why it matters

In most companies these are three separate tools run by three separate teams. When an auditor asks "who used this admin account last month and why?", someone has to dig through all three. Connected, the answer is one ticket with the approval, the identity check and the session recording attached.

## Planned labs

- [ ] Entra as the sign-in provider for CyberArk
- [ ] CyberArk checking for an approved ServiceNow ticket before releasing a credential
- [ ] Privileged session events flowing into ServiceNow SecOps as evidence
