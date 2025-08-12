# Cisco Catalyst Center Automation Workflows

This directory contains automation workflows for Cisco Catalyst Center that help with operations of **Campus networks** and **Software Defined Access Fabrics (SD-Access)**. The workflows provide targeted automation for specific network management functions.

## Network Operation Types

### Campus Network Operations

Workflows designed for traditional campus network deployments including:

- Network device management and provisioning
- Site and building hierarchy configuration
- Policy enforcement and compliance
- Network monitoring and health checks
- Configuration templates and standards

### Software Defined Access (SD-Access) Operations

Workflows specifically designed for SD-Access fabric operations including:

- Fabric site configuration and management
- Identity Services Engine (ISE) integration
- Segmentation and policy enforcement
- Edge node and border node management
- Fabric underlay and overlay provisioning

## Directory Structure

```text
Catalyst Center/
├── README.md                   # This file - Catalyst Center workflow overview

```

## Current Workflows

### Tasks & Execution Operations

- **Get Execution ID** - Retrieve execution identifiers for workflow tracking
- **Get Task ID** - Obtain task identifiers for operation monitoring
- **Wait For Catalyst Center Execution** - Wait for execution completion
- **Wait For Catalyst Center Task** - Wait for task completion

### SD-Access Operations

- **Fabric Management**: Fabric creation, expansion, and maintenance
- **Segmentation**: Virtual network (VN) and scalable group tag (SGT) management
- **Authentication**: Identity and access control integration
- **Analytics**: Fabric health monitoring and troubleshooting

## Prerequisites

### Catalyst Center Access

- Catalyst Center platform with appropriate licensing
- API credentials with sufficient privileges for intended operations
- Network connectivity to Catalyst Center instance

### SD-Access Requirements

- SD-Access licensing and entitlements
- Identity Services Engine (ISE) integration
- Compatible network hardware (Catalyst switches, Wireless controllers)
