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
├── README.md                                                                           # This file - Catalyst Center workflow overview
├── AssignNetworkCredentials__definition_workflow_02NGXCSAT5Q6T33Z4pykwejT9wziPP6KTwe/
├── AssignNetworkSettings__definition_workflow_02NG39Z6F63K749IbHoph8nGVpEhHaIUHt6/
├── CreateTemplate__definition_workflow_02OEWDBJ0W6V02w8ZPbJkgtBALD7nFIwmMg/
├── DeployNetworkSettingsandCredentials__definition_workflow_02NG1H6MKH0GJ4g9gEeP0STvn5AwirGGF1F/
├── DeployTemplatetoMultipleCatalystCenters__definition_workflow_02OHG69IQ4LYA3ueBbULOgjS8UGLDHocEdV/
├── GetExecutionID__definition_workflow_02NIIS1MJRLC03UGv6ranhuvuNIv5RDKFyx/
├── GetTaskID__definition_workflow_01MXNG0KEEZFY4tZ9xFzej731gBSpkNrzwO/
├── GetTemplates__definition_workflow_02OF18QTTJWI76Q81OfAI7wjq6ppQ0S6u6b/
├── WaitForCatalystCenterExecution__definition_workflow_02NHXIR9YQLLH4km689n0NCuWFwW5MuL4BD/
└── WaitForCatalystCenterTask__definition_workflow_02MYO8WQRTQ0L0yqAI6aoCSoM5AD9vA6vBQ/
```

## Current Workflows

The following workflows are currently available in this repository:

### Task Management and Utility Workflows

- **Get Execution ID** - Parses Intent API response and retrieves Catalyst Center Service Job Execution Id
- **Get Task ID** - Parses JSON objects to extract task identifiers from Catalyst Center API responses
- **Wait For Catalyst Center Execution** - Waits for execution completion with configurable timeout and retry logic
- **Wait For Catalyst Center Task** - Waits for task completion with customizable wait time between polling attempts

### Configuration Template Management

- **Create Template** - Creates configuration templates with specified content and parameters for device provisioning
- **Get Templates** - Retrieves templates from a Project at Template Hub by searching for specific template names
- **Deploy Template to Multiple Catalyst Centers** - Deploys configuration templates across multiple Catalyst Center instances

### Network Settings and Credentials

- **Assign Network Settings** - Configures comprehensive network settings including AAA servers, DHCP, DNS, and other network parameters
- **Assign Network Credentials** - Assigns and manages authentication credentials including SNMP, CLI, and other device access credentials
- **Deploy Network Settings and Credentials** - Combined workflow that deploys both network settings and credentials to specified sites

## Prerequisites

### Catalyst Center Access

- Catalyst Center platform with appropriate licensing
- API credentials with sufficient privileges for intended operations
- Network connectivity to Catalyst Center instance

### SD-Access Requirements

- SD-Access licensing and entitlements
- Identity Services Engine (ISE) integration
- Compatible network hardware (Catalyst switches, Wireless controllers)
