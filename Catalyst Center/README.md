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
└── README.md /  # This file - Catalyst Center workflow overview
```

## Current Workflows

The following workflows are currently available in this repository:

### Task Management and Utility Workflows

- **Get Execution ID** - Retrieve execution identifiers for workflow tracking and monitoring
- **Get Task ID** - Obtain task identifiers for operation monitoring and status checking
- **Wait For Catalyst Center Execution** - Wait for execution completion with timeout handling
- **Wait For Catalyst Center Task** - Wait for task completion with proper status validation

### Configuration Template Management

- **Create Template** - Create configuration templates for device provisioning and standardization
- **Get Templates** - Retrieve existing configuration templates from Catalyst Center
- **Deploy Template to Multiple Catalyst Centers** - Deploy templates across multiple Catalyst Center instances

### Network Settings and Credentials

- **Assign Network Settings** - Configure network settings including AAA servers, DHCP, and DNS
- **Assign Network Credentials** - Assign authentication credentials for device management
- **Deploy Network Settings and Credentials** - Combined deployment of network settings and credentials to sites

## Prerequisites

### Catalyst Center Access

- Catalyst Center platform with appropriate licensing
- API credentials with sufficient privileges for intended operations
- Network connectivity to Catalyst Center instance

### SD-Access Requirements

- SD-Access licensing and entitlements
- Identity Services Engine (ISE) integration
- Compatible network hardware (Catalyst switches, Wireless controllers)
