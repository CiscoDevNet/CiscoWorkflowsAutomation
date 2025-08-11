# Cisco Catalyst Center Automation Workflows

This directory contains automation workflows for Cisco Catalyst Center (formerly DNA Center) that help with operations of **Campus networks** and **Software Defined Access Fabrics (SD-Access)**. The workflows are organized in directories by network operation type to provide targeted automation for specific network management functions.

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
├── README.md                    # This file - Catalyst Center workflow overview
├── Network Hierarchy/           # Site, building, and area management workflows
├── Tasks/                      # General task automation and utility workflows
├── Campus Networks/            # Traditional campus network operation workflows
├── SD-Access/                  # Software Defined Access fabric workflows
├── Device Management/          # Device provisioning and lifecycle workflows
├── Policy Management/          # Network policy and compliance workflows
└── Monitoring/                 # Network monitoring and reporting workflows
```

## Current Workflows

### Tasks Directory

Contains utility workflows for common Catalyst Center operations:

- **Get Execution ID.json** - Retrieve execution identifiers for workflow tracking
- **Get Task ID.json** - Obtain task identifiers for operation monitoring
- **Wait For Catalyst Center Execution.json** - Wait for execution completion
- **Wait For Catalyst Center Task.json** - Wait for task completion

## Workflow Categories

### Network Operations

- **Site Management**: Creation, modification, and deletion of network sites
- **Device Lifecycle**: Device discovery, provisioning, and decommissioning
- **Configuration Management**: Template deployment and configuration compliance
- **Policy Enforcement**: Security and QoS policy application

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

### Authentication

- Username/password or certificate-based authentication
- Role-based access control (RBAC) permissions
- API rate limiting considerations

## Usage Guidelines

1. **Network Assessment**: Evaluate current network state before automation
2. **Workflow Selection**: Choose workflows appropriate for your network type
3. **Parameter Configuration**: Configure workflow parameters for your environment
4. **Testing**: Test workflows in non-production environment first
5. **Monitoring**: Use task and execution tracking workflows for operation visibility

## Best Practices

### Campus Network Best Practices

- Start with site hierarchy establishment
- Use configuration templates for consistency
- Implement gradual rollout strategies
- Monitor compliance and policy adherence

### SD-Access Fabric Best Practices

- Ensure ISE integration is established
- Plan IP address space and VLAN allocation
- Validate underlay connectivity before overlay deployment
- Test segmentation policies thoroughly

## Integration Points

- **Identity Services Engine (ISE)**: For authentication and authorization
- **Cisco DNA Spaces**: For location analytics and insights
- **Cisco SD-WAN**: For branch connectivity integration
- **Third-party ITSM**: For workflow orchestration and ticketing

## Resources

- [Cisco DNA Center Platform API Documentation](https://developer.cisco.com/docs/dna-center/)
- [SD-Access Design Guide](https://www.cisco.com/c/en/us/solutions/enterprise-networks/software-defined-access/design-guide.html)
- [Catalyst Center User Guide](https://www.cisco.com/c/en/us/support/cloud-systems-management/dna-center/products-user-guide-list.html)
- [DevNet Learning Labs](https://developer.cisco.com/learning/labs/)

---

Last updated: August 2025