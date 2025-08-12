# Workflows Automation

This directory contains automation workflows organized by functionality. Each workflow is designed to automate common tasks and operations across various Domain Controllers or platforms.

## Directory Structure

```text
workflows/
├── README.md                # This file - overview and documentation
├── Catalyst Center/         # Cisco Catalyst Center automation workflows
│   ├── Network Hierarchy/   # Network hierarchy management workflows
│   └── Tasks/               # Catalyst Center task & Execution automation
│
scripts/                     # Python scripts and utilities supporting workflows
    └── url_encode_string.py # URL encoding utility script
```

## Organization

### Workflows

The workflows directory follows a structured approach to organize automation content:

### By Domain Controller/Platform

Within the workflows directory, automation content is organized into subdirectories based on the target Domain Controller or platform:

- **Catalyst Center**: Workflows specifically designed for Cisco Catalyst Center automation and management

### By Functionality

Within each platform directory, workflows are further categorized by their primary operational function:

- **Network Hierarchy**: Workflows related to network topology, site management, and hierarchical organization
- **Tasks**: General automation workflows for processing tasks and executions

### Scripts

The companion scripts' directory (located at the repository root level) contains Python utility scripts that support and enhance the workflow automation:

These scripts can be embedded within workflows or used independently to support automation tasks across different platforms.

## Support

For questions or issues with these workflows:

- Check the individual workflow documentation
- Review Cisco DevNet resources and documentation


