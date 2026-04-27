<!-- AUTO-GENERATED — do not edit manually. Edit blueprints/blueprints.yaml instead. -->

# OPI Blueprint Dashboard

> Last updated: 2026-04-27

## Summary

| Metric | Value |
|--------|-------|
| Total blueprints | 5 |
| Published | 1 |
| In progress | 3 |
| Partners involved | 8 |

---

## Pipeline

### 📋 Proposed (1)

| ID | Title | Category | Partners | Progress | Updated |
|----|-------|----------|----------|----------|---------|
| [BP-005](https://github.com/opiproject/opi/issues/5) | IPSec / MACsec Line-Rate Encryption Offload for East-West Traffic | security | Marvell, F5 | `░░░░░░░░░░ 0/5` | 2025-04-01 |

### 🔍 TSC Review (1)

| ID | Title | Category | Partners | Progress | Updated |
|----|-------|----------|----------|----------|---------|
| [BP-004](https://github.com/opiproject/opi/issues/4) | NVMe-oF Storage Offload with SPDK on Intel IPU E2100 | storage | Intel, Dell Technologies | `██░░░░░░░░ 1/5` | 2025-03-28 |

### 🔨 Build & Document (1)

| ID | Title | Category | Partners | Progress | Updated |
|----|-------|----------|----------|----------|---------|
| [BP-003](https://github.com/opiproject/opi/issues/3) | Multi-Tenant Network Isolation with OVS Offload on NVIDIA BlueField-3 | networking | NVIDIA, Red Hat | `████░░░░░░ 2/5` | 2025-04-05 |

### 🧪 Validate (1)

| ID | Title | Category | Partners | Progress | Updated |
|----|-------|----------|----------|----------|---------|
| [BP-002](https://github.com/opiproject/opi/issues/2) | Zero-Touch Provisioning with sZTP on Marvell OCTEON DPU | provisioning | Marvell, Keysight Technologies | `████████░░ 4/5` | 2025-04-10 |

### ✅ Published (1)

| ID | Title | Category | Partners | Progress | Updated |
|----|-------|----------|----------|----------|---------|
| [BP-001](https://github.com/opiproject/opi/issues/1) | F5 BIG-IP Next + Intel IPU E2100 on Red Hat OpenShift | networking | WorldTech IT, Dell Technologies, Intel, F5, Red Hat | `██████████ 5/5` | 2025-03-10 |

---

## Blueprint Details

### BP-001 — F5 BIG-IP Next + Intel IPU E2100 on Red Hat OpenShift

**Stage:** ✅ Published  
**Category:** networking  
**Submitted:** 2024-09-15  
**Updated:** 2025-03-10  

**Use case:** Kubernetes-native L4–L7 load balancing offloaded to Intel IPU E2100, freeing host CPU cores for application workloads in a multi-tenant OpenShift cluster.

**Target persona:** Network architect, platform engineer

**Partners:**

- WorldTech IT — Lead integrator
- Dell Technologies — Hardware
- Intel — IPU hardware
- F5 — BIG-IP Next software
- Red Hat — OpenShift platform

**Hardware:** Dell PowerEdge R760, Intel IPU E2100

**OPI components:** opi-api (networking), DPU Operator

**Deliverables:**

- ✅ Reference Architecture
- ✅ Bill Of Materials
- ✅ Deployment Guide
- ✅ Use Case Narrative
- ✅ Validation Results

**Notes:** Showcased at OCP Global Summit 2024.

**Links:** [GitHub Issue](https://github.com/opiproject/opi/issues/1)

---

### BP-002 — Zero-Touch Provisioning with sZTP on Marvell OCTEON DPU

**Stage:** 🧪 Validate  
**Category:** provisioning  
**Submitted:** 2024-11-01  
**Updated:** 2025-04-10  

**Use case:** Automated, cryptographically-secure initial provisioning of a DPU/IPU fleet using OPI's sZTP implementation — no manual intervention required from factory floor to production rack.

**Target persona:** Infrastructure engineer, NetOps team

**Partners:**

- Marvell — DPU hardware + sZTP implementation
- Keysight Technologies — Test & validation

**Hardware:** Marvell OCTEON CN10K DPU

**OPI components:** sztp, opi-prov-life

**Deliverables:**

- ✅ Reference Architecture
- ✅ Bill Of Materials
- ✅ Deployment Guide
- ✅ Use Case Narrative
- ⬜ Validation Results

**Notes:** Validation testing underway in OPI Lab. Expected completion Q2 2025.

**Links:** [GitHub Issue](https://github.com/opiproject/opi/issues/2)

---

### BP-003 — Multi-Tenant Network Isolation with OVS Offload on NVIDIA BlueField-3

**Stage:** 🔨 Build & Document  
**Category:** networking  
**Submitted:** 2025-01-20  
**Updated:** 2025-04-05  

**Use case:** Hardware-enforced tenant isolation for cloud-native workloads; OVS dataplane offloaded to BlueField-3 DPU, enabling strict separation between provider infrastructure and tenant applications.

**Target persona:** Cloud operator, SecOps engineer

**Partners:**

- NVIDIA — DPU hardware + DOCA SDK
- Red Hat — OpenShift platform

**Hardware:** NVIDIA BlueField-3 DPU

**OPI components:** opi-api (networking)

**Deliverables:**

- ✅ Reference Architecture
- ⬜ Bill Of Materials
- ⬜ Deployment Guide
- ✅ Use Case Narrative
- ⬜ Validation Results

**Notes:** IaC artifacts (Helm charts, Ansible playbooks) in progress.

**Links:** [GitHub Issue](https://github.com/opiproject/opi/issues/3)

---

### BP-004 — NVMe-oF Storage Offload with SPDK on Intel IPU E2100

**Stage:** 🔍 TSC Review  
**Category:** storage  
**Submitted:** 2025-02-14  
**Updated:** 2025-03-28  

**Use case:** Disaggregated storage fabric using NVMe over Fabrics (NVMe-oF), with the compute plane offloaded to the Intel IPU E2100 via OPI's SPDK bridge — reducing host CPU overhead for storage I/O to near zero.

**Target persona:** Storage architect, platform engineer

**Partners:**

- Intel — IPU hardware + SPDK
- Dell Technologies — Server platform

**Hardware:** Intel IPU E2100, Dell PowerEdge R760

**OPI components:** opi-spdk-bridge, opi-api (storage)

**Deliverables:**

- ⬜ Reference Architecture
- ⬜ Bill Of Materials
- ⬜ Deployment Guide
- ✅ Use Case Narrative
- ⬜ Validation Results

**Notes:** TSC presentation scheduled for next meeting. Lab hardware availability TBD.

**Links:** [GitHub Issue](https://github.com/opiproject/opi/issues/4)

---

### BP-005 — IPSec / MACsec Line-Rate Encryption Offload for East-West Traffic

**Stage:** 📋 Proposed  
**Category:** security  
**Submitted:** 2025-04-01  
**Updated:** 2025-04-01  

**Use case:** Line-rate encryption of data-center east-west traffic (IPSec and MACsec) offloaded to Marvell OCTEON DPU — eliminating host CPU encryption overhead while meeting compliance requirements for data-in-transit.

**Target persona:** CISO, SecOps engineer

**Partners:**

- Marvell — DPU hardware + crypto offload
- F5 — Policy & orchestration

**Hardware:** Marvell OCTEON CN10K DPU

**OPI components:** opi-api (security)

**Deliverables:**

- ⬜ Reference Architecture
- ⬜ Bill Of Materials
- ⬜ Deployment Guide
- ⬜ Use Case Narrative
- ⬜ Validation Results

**Notes:** One-pager submitted. Awaiting TSC scheduling.

**Links:** [GitHub Issue](https://github.com/opiproject/opi/issues/5)

---
