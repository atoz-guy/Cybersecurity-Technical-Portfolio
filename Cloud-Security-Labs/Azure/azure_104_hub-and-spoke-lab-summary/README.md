# AZ-104: Hub-and-Spoke Virtual Network Lab

## Overview
This lab implements a hub-and-spoke network topology in Microsoft Azure as part of the AZ-104 Administrator learning path. The goal is to create two virtual networks, configure required subnets, and establish virtual network peering so the VNets behave as a single routed network.

This pattern is foundational for:
- Centralized firewalls
- Shared services
- Landing zones
- Enterprise network segmentation

---

## Architecture Summary

### Hub Virtual Network
- **Name:** hub-vnet  
- **Address space:** 10.0.0.0/16  
- **Purpose:** Centralized network for shared services (e.g., Azure Firewall)

#### Subnets
| Subnet Name            | Address Range      | Notes |
|------------------------|--------------------|-------|
| AzureFirewallSubnet    | 10.0.0.0/26        | Required minimum size for Azure Firewall |

---

### Spoke Virtual Network
- **Name:** app-vnet  
- **Address space:** 10.1.0.0/16  
- **Purpose:** Application workloads, isolated from hub

#### Subnets
| Subnet Name | Address Range      | Notes |
|-------------|--------------------|-------|
| app-subnet  | 10.1.0.0/24        | General application subnet |

---

## Virtual Network Peering

Peering allows VNets to communicate privately using Azure’s backbone network. Peering is **bidirectional**, and Azure automatically creates both directions.

### Peering Configuration
| Direction | Peering Name         | From → To      |
|----------|------------------------|----------------|
| Outbound | app-vnet-to-hub        | app-vnet → hub-vnet |
| Inbound  | hub-to-app-vnet        | hub-vnet → app-vnet |

### Status
- **Connected**

This confirms both VNets can route traffic to each other.

---

## Notes & Lessons Learned

- Azure Firewall requires a **/26** subnet minimum.
- Default subnets (10.0.0.0/24) may cause **overlap conflicts** and must be removed before creating the firewall subnet.
- VNet address spaces **must not overlap** for peering to work.
- Peering is **automatically bidirectional** — you only configure it once.
- Hub-and-spoke is the basis for:
  - Private endpoints  
  - Bastion  
  - VPN/ExpressRoute gateways  
  - Centralized security inspection  

---

## Lab Completion
This lab successfully demonstrates:
- VNet creation  
- Subnet planning  
- Firewall subnet requirements  
- VNet peering  
- Hub-and-spoke architecture fundamentals  

<img width="1920" height="1128" alt="AZ-104 Hub-and-Spoke Lab Summary" src="https://github.com/user-attachments/assets/7a5bdbd9-a4e6-47d8-8a99-86e39449aa05" />
