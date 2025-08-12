# Scripts Directory

This directory contains Python utility scripts that can be embedded in automation workflows in the `../workflows/` directory. These scripts are essential functions for data processing, API interactions, and workflow orchestration across various Cisco platforms and Domain Controllers.

## Purpose

The scripts directory serves as a centralized repository for reusable utility functions that can be:

- **Called from within workflows** to perform specific data processing tasks
- **Executed independently** as standalone utilities for automation support
- **Integrated into larger automation pipelines** for complex workflow orchestration
- **Used for API preparation** including data formatting and encoding

## Current Scripts

### URL Encoding Utilities

#### `url_encode_string.py`

**Purpose**: Encodes strings for safe use in URLs and API calls, ensuring proper formatting for REST API interactions.

**Functionality**:

- Takes a string input as a command-line argument
- Applies URL encoding using Python's `urllib.parse.quote()` function
- Returns the encoded string suitable for use in API URLs

**Usage**:

```bash
python url_encode_string.py "string to encode"
```

