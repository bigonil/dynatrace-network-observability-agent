# Dynatrace Network Observability Agent

Enterprise-grade network monitoring agent for Windows 11,
installed as a Windows Service and distributed via signed MSI.

## Architecture
Windows 11 → Agent Service → Dynatrace Extension v2 → ActiveGate → Dynatrace SaaS → Davis AI

## Metrics
- custom.network.icmp.latency
- custom.network.tcp.connect_time
- custom.network.jitter
- custom.network.packet_loss

## Installation (Silent)
msiexec /i NetworkAgent.msi /qn

## Service
Service Name: NetworkObservabilityAgent  
Startup: Automatic

## Governance
- NetOps: thresholds
- SecOps: signing certificate
- IT Ops: Intune rollout