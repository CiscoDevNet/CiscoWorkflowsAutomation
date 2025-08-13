# Meraki Automation Workflows

This directory contains automation workflows for Meraki that help with Cross Network, Cross Organization or simple utility workflows.

## Directory Structure

```text
Meraki/
├── README.md                   # This file - Catalyst Center workflow overview

```
## Current Atomics

GetOrganizationDevicesStatues - This API is currently deprecated in Meraki and hence not available as a system atomic. Please use this sparingly knowing this will be removed any time. 

## Current Workflows

UnusedDevicesChecker - This workflow helps to check if the devices in the Organization are used in the last N days. This check is based on the last reported date in GetOrganizationDevicesStatues atomic.


## Prerequisites

These workflows work with Meraki Endpoint Target.

