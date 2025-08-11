# Cisco Automation Workflows

This directory contains Cisco automation workflows organized by product and functionality. Each workflow is designed to automate common tasks and operations across various Cisco platforms.

## Directory Structure

```text
workflows/
├── README.md                 # This file - overview and documentation
└── CatalystCenter/          # Cisco Catalyst Center automation workflows
    ├── NetworkHierarchy/    # Network hierarchy management workflows
    └── Tasks/              # General task automation workflows
```

## Organization Principles

### By Product/Platform

Workflows are organized into directories based on the target Cisco product or platform:

- **CatalystCenter**: Workflows for Cisco Catalyst Center (DNA Center) automation

### By Functionality

Within each product directory, workflows are further categorized by their primary function:

- **NetworkHierarchy**: Workflows related to network topology, site management, and hierarchical organization
- **Tasks**: General automation tasks, maintenance operations, and utility workflows

## Workflow Naming Convention

Workflows should follow a consistent naming pattern:

- Use descriptive names that clearly indicate the workflow's purpose
- Include the target platform when not obvious from the directory structure
- Use camelCase or snake_case consistently
- Example: `createSiteHierarchy`, `device_inventory_sync`

## Workflow Standards

### JSON Workflow Definitions

- Each workflow should include a complete JSON definition file
- Follow Cisco workflow automation standards and best practices
- Include proper error handling and logging
- Document input parameters and expected outputs

### Documentation Requirements

Each workflow directory should contain:

1. **Workflow definition file** (JSON format)
2. **README.md** with workflow description, prerequisites, and usage instructions
3. **Examples** showing typical use cases and parameter values

## Getting Started

### Prerequisites

- Access to target Cisco platforms (Catalyst Center, etc.)
- Appropriate API credentials and permissions
- Workflow automation platform (SecureX Orchestrator, etc.)

### Usage

1. Navigate to the appropriate product directory
2. Select the workflow category that matches your use case
3. Review the workflow documentation and prerequisites
4. Import the workflow definition into your automation platform
5. Configure required parameters and credentials
6. Test the workflow in a non-production environment

## Contributing

When adding new workflows:

1. Place them in the appropriate product/functionality directory
2. Follow the established naming conventions
3. Include comprehensive documentation
4. Test thoroughly before committing
5. Update this README if adding new categories or products

## Support

For questions or issues with these workflows:

- Check the individual workflow documentation
- Review Cisco DevNet resources and documentation
- Open an issue in this repository for workflow-specific problems

