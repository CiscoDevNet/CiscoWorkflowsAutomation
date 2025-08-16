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
├── ComposeSiteHierachyName__definition_workflow_02NG8EASZBL4E3bes3yy0amgTb0RQCG1v2n/
├── CreateTemplate__definition_workflow_02OEWDBJ0W6V02w8ZPbJkgtBALD7nFIwmMg/
├── DeployNetworkSettingsandCredentials__definition_workflow_02NG1H6MKH0GJ4g9gEeP0STvn5AwirGGF1F/
├── DeployTemplatetoMultipleCatalystCenters__definition_workflow_02OHG69IQ4LYA3ueBbULOgjS8UGLDHocEdV/
├── GetExecutionID__definition_workflow_02NIIS1MJRLC03UGv6ranhuvuNIv5RDKFyx/
├── GetFabricDeviceAttributes__definition_workflow_02P6BJYYJ2QJ11dbaqjqZ2NfEaBbbz0xDna/
├── GetTaskID__definition_workflow_01MXNG0KEEZFY4tZ9xFzej731gBSpkNrzwO/
├── GetTemplates__definition_workflow_02OF18QTTJWI76Q81OfAI7wjq6ppQ0S6u6b/
├── RetrieveCatalystCenterInventory__definition_workflow_02LUCD8E5P4ZU17bpnk6E5qWw11nrOeyEig/
├── WaitForCatalystCenterExecution__definition_workflow_02NHXIR9YQLLH4km689n0NCuWFwW5MuL4BD/
└── WaitForCatalystCenterTask__definition_workflow_02MYO8WQRTQ0L0yqAI6aoCSoM5AD9vA6vBQ/
```

## Current Workflows

The following workflows are currently available in this repository:

### Task Management and Utility Workflows

| Workflow Name | Description | Type |
|---------------|-------------|------|
| Get Execution ID | Parses Intent API response and retrieves Catalyst Center Service Job Execution Id | Atomic |
| Get Task ID | Parses Intent API response and retrieves Catalyst Center Service Task Id | Atomic |
| Wait For Catalyst Center Execution | Waits for a Catalyst Center Job execution and monitors until it completes or fails | Atomic |
| Wait For Catalyst Center Task | Waits for a Catalyst Center task to complete or fail | Atomic |

### Configuration Template Management

| Workflow Name | Description | Type |
|---------------|-------------|------|
| Create Template | Creates Template in a Project at Template Hub | |
| Get Templates | Retrieves Templates from a Project at Template Hub | |
| Deploy Template to Multiple Catalyst Centers | Deploys a Configuration Template to Multiple Catalyst Centers | |

### Network Settings and Credentials

| Workflow Name | Description | Type |
|---------------|-------------|------|
| Assign Network Settings | Assign Network and AAA Settings to Site In Network Hierarchy | |
| Assign Network Credentials | Assign Network Credentials to Site Hierarchy | |
| Deploy Network Settings and Credentials | Sets Settings and Credentials to Network Site Hierarchy | |

### Site and Hierarchy Management

| Workflow Name | Description | Type |
|---------------|-------------|------|
| Compose Site Hierachy Name | Returns the Site Hierarchy name by concatenating the Parent, Area, Building & Floor elements | |

### Device and Inventory Management

| Workflow Name | Description | Type |
|---------------|-------------|------|
| Retrieve Catalyst Center Inventory | Retrieves Catalyst Center Inventory, automates retrieving inventory of devices under management | |
| Get Fabric Device Attributes | Returns a summary of all attributes of a fabric device | |


## Prerequisites

### Catalyst Center Access

- Catalyst Center platform with appropriate licensing
- API credentials with sufficient privileges for intended operations
- Network connectivity to Catalyst Center instance

### SD-Access Requirements

- SD-Access licensing and entitlements
- Identity Services Engine (ISE) integration
- Compatible network hardware (Catalyst switches, Wireless controllers)
