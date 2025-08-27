# Meraki Automation Workflows

This directory contains automation workflows for Meraki that help with Cross Network, Cross Organization or simple utility workflows.

## Directory Structure

```text
Meraki/
├── README.md  # This file
├── CheckAvailableFirmwareForNetwork__definition_workflow_02M30GYJJSYJL0wQPPnkQgIcavBkG6796mF/
│   └── definition_workflow_02M30GYJJSYJL0wQPPnkQgIcavBkG6796mF.json
├── GetOrganizationDevicesStatuses__definition_workflow_02OQTFUOR8LBS2UYcPdhVOgQwSfDAOOYyuw/
│   └── definition_workflow_02OQTFUOR8LBS2UYcPdhVOgQwSfDAOOYyuw.json
├── ScheduleFirmwareUpgradeForNetwork__definition_workflow_02M312TMR8LMG3UJlEY07a3HLYWHV8awf3M/
│   └── definition_workflow_02M312TMR8LMG3UJlEY07a3HLYWHV8awf3M.json
├── ScheduleFirmwareUpgradeForNetworksByTag__definition_workflow_02M7Z8N486Z985yvnPOvF97ovjxUaJgGjFD/
│   └── definition_workflow_02M7Z8N486Z985yvnPOvF97ovjxUaJgGjFD.json
├── SiteChecklistByTags__definition_workflow_02OKU4P173KBL1tl2NeIOmuUJV2c0FKo5ro/
│   └── definition_workflow_02OKU4P173KBL1tl2NeIOmuUJV2c0FKo5ro.json
├── SiteHandoffChecklist__definition_workflow_02OZ9J3394O0P4xLZqsxzedrUGsJ2VtgMSD/
│   └── definition_workflow_02OZ9J3394O0P4xLZqsxzedrUGsJ2VtgMSD.json
├── UnusedDeviceChecker__definition_workflow_02OZEARSNVQLF01V3BR2OFHn0tpgPFb4Uun/
    └── definition_workflow_02OZEARSNVQLF01V3BR2OFHn0tpgPFb4Uun.json
```

## Meraki Workflows Overview

This repository provides automation workflows for Cisco Meraki network management. Each workflow helps streamline common Network and Organization tasks.

### Workflow Descriptions

| Workflow Name                                      | Workflow Description                                                                                       | Workflow Type |
|----------------------------------------------------|-----------------------------------------------------------------------------------------------------------|--------------|
| Check Available Firmware for Network               | Quickly view which firmware versions are available for a selected Meraki network. Useful for planning upgrades and ensuring compatibility. | Atomic       |
| Find Tagged Networks Across Multiple Orgs          | Find all networks with specific tags across multiple organizations. Useful for cross-org asset management and reporting. |              |
| Get Organization Devices Statuses                  | Instantly fetch the operational status of all devices in your organization. Helps monitor device health and spot issues. | Atomic       |
| Schedule Firmware Upgrade for Network              | Automate scheduling of firmware upgrades for a specific network. Set the date and time to keep devices up-to-date with minimal disruption. | Atomic       |
| Schedule Firmware Upgrade for Networks by Tag      | Schedule upgrades across multiple networks by specifying tags. Ideal for batch updates in large organizations. | Atomic       |
| Site Checklist by Tags                             | Generate a customizable checklist for sites based on network tags. Ensures all required steps are completed for tagged locations. |              |
| Site Handoff Checklist                            | Provides a step-by-step checklist for handing off a site, ensuring all network setup and documentation is complete. |              |
| Unused Device Checker                             | Identify devices that haven’t been used for a specified number of days. Helps with asset management and cleanup. | Atomic       |

## Prerequisites

These workflows work with Meraki Endpoint Target.


