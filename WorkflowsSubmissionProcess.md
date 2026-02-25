
# Submission Process for Exchange Candidates

## Using "WorkflowReviewChecklist.md" with AI to review you Workflow

A Markdown file has been created and checked into the Public Repo which contains criterial for Workflow review prior to submission. This file can be provided to your LLM of choice as well as the JSON payload representing your workflow.  
https://github.com/CiscoDevNet/CiscoWorkflowsAutomation/blob/main/WorkflowReviewChecklist.md

The LLM will apply the critera against your workflow highlighting:
- Workflow Inputs & Parameters
- Targets & Target Groups
- Atomics & API Usage
- Groups & Categories
- Logic & Flow
- Error Handling
- Essential Hygiene & Security

Please use this Checklist with your LLM of choice. We have tested with Cisco's Circuit LLM (recommendation of Claude 4.5) however you are not
retricted in your LLM selection. The LLM will be used against the exported JSON Workflow from your Workfspace.

Here is an example Prompt: 
- "Please perform an analysis of the Cisco Workflow provided in the JSON file using the criteria checklist found in the included markdown file."

## Understanding Analysis Results

The analysis will break down issues into High, Medium, Low Priority (Some LLMs may describe as Critical, Medium, Low). All critical issues should be addressed before submitting for review. Designers should also do their best to address Medium and Low comments before submissions where appropriate. 

Note: Reviewers will rerun this Analysis as part of the review process.
<br>
<br>
# Uploading Workflow for Submission
Workflows are submitted to the Exchange from the Workflow Designer under "More Actions"/"Share"/"Submit to Exchange".
This will bring the submitter to the submission screens where the information below must be provided.

Use the information below to fill out the form requirements on submission. Submitters can monitor the status from the Automation/Exchange menu where the current status is provided. 

If a submission is rejected, which is common, the comments provided will explain the reasons. At this point the develloper of the workflow can return to their Workspace, unlock their workflow, and make the necessary edits. When complete, they can submit the workflow again.

## Integration
- Indicate the relevant domains the Workflow operates across

## Display Name
- Name of your Workflow

## Author
- Your Email Address
    
## Contact & Support Information
- Your Email Address or possibly a Group Email Alias if more relevant.
        
## Short Description

## Installation Instructions
The following is an example format of what can be provided in the Installations Instructions 
This may vary depending on your submission. 
Note the section Additional Reference Material can reference links added in the next section for "External Links"

### Workflow Name
- The Name of your Workflow
>
### Key Features
- (Examples)
- Query JSON Placeholder Web Service for list of Users
- Locates specific User based on inputted Name
- Scan the returned data to find a matching email address for that User
- Return the Email if found, 400 if no User is located
>
### Installation Steps
1. (Examples)
2. Download the workflow from the Exchange
3. The Workflow will install an HTTP Target, "JSON Placeholder Web Service", if this Target does not already exist.
4. There is no specific configuration required for this HTTP endpoint.
>
### Prerequisites
- Note and requirements such as access rights, etc.. required to run this workflow.
>
### Additional Reference Material
-  Please see the reference under External Links to the "Learning Series" YouTube content.
    
