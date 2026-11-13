# Manage Subscriptions and RBAC (AZ-104 Lab 02a)

## Task 1 — Implement Management Groups
I created a new management group (az104-mg1) to organize subscriptions and apply governance at scale. Management groups sit above subscriptions and allow RBAC and Azure Policy to be inherited consistently across the environment. This step establishes the foundation for directory‑wide structure and prepares the environment for more advanced access and governance configurations.
**Screenshot:**
<img width="1920" height="1128" alt="az104-lab1_task1" src="https://github.com/user-attachments/assets/43a6ce52-81b8-49d5-9046-3fcd59fecedb" />

---

## Task 3 — Create Custom RBAC Role
In this task, I created a custom RBAC role by cloning the built‑in Support Request Contributor role and removing the permission that allows registering the Microsoft Support resource provider. This demonstrates the principle of least privilege by restricting unnecessary actions while still enabling support ticket management. I then assigned the custom role at the management group scope to ensure consistent governance across all subscriptions under that hierarchy.
**Screenshot:**
<img width="1920" height="1128" alt="az104-lab2_task3_a" src="https://github.com/user-attachments/assets/c72a7658-fee6-4cc5-88ce-4793fba5ea23" />
<img width="960" height="564" alt="az104-lab2_task3_b" src="https://github.com/user-attachments/assets/f65995a8-a6ba-437e-99b4-05f9dfce5f37" />

## Summary
This lab establishes the core governance structure for Azure environments. Management groups provide scalable organization, while RBAC and custom roles enforce least privilege and secure access. These fundamentals will be used in future labs involving automation, identity governance, Defender for Cloud, and enterprise-level architecture.
