# Workflow Review Checklist

This checklist is designed for LLM agents to systematically review JSON workflow files in the CiscoWorkflowsAutomation repository. Each item includes specific JSON elements to inspect and validation criteria for automated analysis.

## 1. Workflow Inputs & Parameters

**JSON Elements to Inspect:** `definition_workflow.properties.input_groups`, `definition_workflow.properties.inputs`

- [ ] **Input Validation**: **If inputs exist**, check each input in `inputs` array has `name`, `type`, `description`, and appropriate `required` flag - **Note**: Workflows with no inputs are valid for automated/scheduled workflows
- [ ] **Exchange-Compatible Input Types**: Check each input in the `inputs` array for `type: "enum"` - **Note**: `enum` inputs are supported by the workflow runtime but are not supported by the Exchange; flag them as a submission-blocking issue and recommend replacing them with a supported type such as `String` plus workflow validation for the allowed values
- [ ] **Secure String Review**: For inputs with `type: "SecureString"`, verify `name` is descriptive and `scope` is documented in description
- [ ] **Standard Outputs Present**: Verify outputs include `Result`, `Status Code`, `Status Message`, `Error Message` in `outputs` array
- [ ] **Default Values Safety**: Scan `default_value` fields for production data (real IPs, device serials, org IDs, passwords) - should be generic placeholders only
- [ ] **Input Redundancy**: Identify duplicate or similar inputs that could be consolidated
- [ ] **Variable Naming Convention**: 
  - Workflow variables (user-facing): Human-readable, capitalized (e.g., "Device ID", "Sort By Date")
  - Code activity outputs: camelCase (e.g., "deviceID", "sortByDate")
  - **Note**: System-generated `unique_name` fields use random alphanumeric patterns - this is expected XDR behavior
- [ ] **Prefix Check**: Ensure variable names don't use unnecessary "Input -" or "Output -" prefixes

## 2. Targets & Target Groups

**JSON Elements to Inspect:** `definition_workflow.properties.targets`, `definition_workflow.properties.target_groups`

- [ ] **Hardcoded Target Analysis**: Check if `targets` array contains specific target references - validate if justified for scheduled/webhook workflows
- [ ] **Target Customization**: Verify `targets` can be overridden during installation (not hardcoded in workflow logic) - **Note**: Some workflows legitimately require specific target groups for proper operation
- [ ] **Target Group Genericity**: In `target_groups`, check `matching_conditions` don't contain environment-specific values (specific hostnames, IPs, user IDs) unless justified
- [ ] **Unused Target Cleanup**: Cross-reference targets/target_groups with actual usage in workflow activities

## 3. Atomics & API Usage

**JSON Elements to Inspect:** `definition_workflow.activities`, activity `type` fields, `api_requests`

- [ ] **New Atomic Justification**: Identify activities with `type: "atomic_workflow"` - check if description explains why new atomic was needed
- [ ] **Generic API Usage**: Look for activities with `type: "web_service_request"` - verify if atomic alternative exists and document rationale
- [ ] **API Request Documentation**: For generic API calls, ensure future improvement notes are in activity description

## 4. Groups & Categories

**JSON Elements to Inspect:** `definition_workflow.properties.groups`, `definition_workflow.properties.categories`

- [ ] **Group Functionality**: Review `groups` array for clear functional purpose vs. existing groups
- [ ] **Category Appropriateness**: Check that `categories` array contains relevant classifications for the workflow's purpose and domain
- [ ] **Unnecessary Category Creation**: Flag if new categories are being created when existing ones would be more appropriate (check against repository's existing category taxonomy)
- [ ] **Missing Categories**: Verify workflow isn't missing obvious category classifications that would help with organization and discoverability
- [ ] **Orphaned Elements**: Identify groups/categories defined but not referenced in workflow activities

## 5. Logic & Flow

**JSON Elements to Inspect:** `definition_workflow.activities`, activity relationships, conditional logic

- [ ] **Group Activity Usage**: Verify major workflow sections use `type: "group"` activities with descriptive `name` and `description`
- [ ] **Validation Steps**: After API calls or sub-workflows, check for success/failure validation activities
- [ ] **Continue on Failure**: For activities that should continue on error, verify `continue_on_failure: true` is set appropriately
- [ ] **Idempotency Implementation**: **CRITICAL** - For CREATE/DELETE operations:
  - CREATE: Look for existence checks before creation (conditional logic, error handling for "already exists")
  - DELETE: Look for existence validation before deletion (handle "not found" gracefully)
  - Verify error handling allows multiple executions without failure
  - **Note**: Some operations may be inherently idempotent or designed for single execution - verify if multiple runs are expected
- [ ] **Loop Exit Conditions**: In loop activities, verify `break_conditions` or `max_iterations` prevent infinite execution
- [ ] **Modularity Assessment**: Identify repeated logic blocks that could be extracted to sub-workflows

## 6. Error Handling

**JSON Elements to Inspect:** Error handling activities, output variable assignments, `continue_on_failure` settings

- [ ] **Explicit Success/Failure Paths**: Verify both success and failure branches update `Result`, `Status Code`, `Status Message`, `Error Message` outputs
- [ ] **Error Aggregation**: Check that errors from sub-workflows and API calls are captured and surfaced in outputs
- [ ] **Error Message Population**: Ensure failure paths set meaningful values in `Error Message` output
- [ ] **Timeout Implementation**: For long-running operations, verify `timeout` settings and retry logic exist

## 7. Essential Hygiene & Security

**JSON Elements to Inspect:** All string values, variable assignments, activity configurations

- [ ] **Sensitive Data Scan**: Search for passwords, API keys, tokens in plain text - should use `SecureString` variables instead
- [ ] **Description Quality**: Check `definition_workflow.properties.description` includes purpose, prerequisites, limitations, dependencies
- [ ] **Placeholder Data**: Scan for sample/test data in variable defaults, API endpoints, or documentation
- [ ] **Naming Consistency**: Verify consistent naming patterns across inputs, outputs, groups, categories, activities
- [ ] **Cleanup Verification**: Ensure no unused variables, groups, categories, or debug artifacts remain
- [ ] **Grammar and Spelling**: Validate text fields for typos and grammatical errors

## LLM Review Instructions

### Prompt Template:

```
Context: You are a workflow validator, checking the quality of the Workflow before it can be approved.

Objective: Validate the Workflow with the Workflow-Review-Checklist items so that there is consistency and quality in approved workflows. Provide overall assessment score.

Workflow: [Workflow Name]

MANDATORY MULTI-PHASE REVIEW PROCESS:

PHASE 1 - ENUMERATION (Complete this FIRST):
- Identify and list ALL workflows in the JSON file
- For each workflow, document: name, type (parent/embedded), line range
- Present the enumeration list before proceeding
- Count: X workflows found (1 parent + Y embedded subworkflows)

PHASE 2 - DETAILED REVIEW (One workflow at a time):
- Review each workflow individually against all 7 checklist categories
- Complete all categories for Workflow N before starting Workflow N+1
- Report findings for each workflow separately

PHASE 3 - AGGREGATE ASSESSMENT:
- Compile findings across all workflows
- Provide overall quality score and recommendations

Audience: The feedback will be for workflow developers with technical expertise seeking approval of their workflows. Suggest improvements for the findings.

Style: Provide a bulleted list of issues for each Checklist Category.

Tone: Crisp, not too verbose.
```

**Optional Enhancements:**
- `File Path: [path/to/workflow.json]` - Helps LLM understand file context
- `Priority Focus: [Security/Performance/Maintainability]` - When specific concerns exist
- `Severity Threshold: [Critical/High/Medium/Low]` - To filter noise for mature workflows

### Analysis Process:
1. **Parse Full JSON Structure**: Load the workflow JSON and identify the parent workflow plus all embedded subworkflows in the file.
2. **Enumerate Review Scope - MANDATORY FIRST STEP**:
   - Build a complete list of ALL workflows to review BEFORE starting validation
   - For each workflow, document: name, unique_name, line range, and type (parent/subworkflow)
   - Present this enumeration to the reviewer/user for confirmation
   - DO NOT proceed to validation until enumeration is complete and confirmed
3. **Systematic Validation - One Workflow at a Time**:
   - Review workflows sequentially (parent first, then each subworkflow)
   - For EACH workflow, apply ALL 7 checklist categories completely
   - Mark each workflow as complete individually before moving to the next
   - Report findings for each workflow separately, not in aggregate
4. **Pattern Recognition**: Look for anti-patterns such as hardcoded values, missing error handling, weak idempotency, and security vulnerabilities across parent and embedded workflows.
5. **Cross-Reference Analysis**: Verify consistency between definitions and actual usage within each workflow, and between parent/subworkflow interfaces.
6. **Report Findings**: For each failed check, provide:
   - **Specific Location**: Clearly identify the workflow element (e.g., "Workflow Variable 'Variable Name'", "Activity 'Activity Title'", "Workflow's main 'Variables' section"). If a specific property within an element is relevant, include it (e.g., "Description of Activity 'Activity Title'").
   - Description of the problem
   - Recommended fix or improvement
   - Severity level (Critical, High, Medium, Low)

### Quality Score Guidelines:

- **9-10**: Excellent - Minor improvements only
- **7-8**: Good - Few moderate issues to address  
- **5-6**: Acceptable - Several issues requiring attention
- **3-4**: Needs Work - Multiple critical/high issues
- **1-2**: Major Revision Required - Fundamental problems

### Common JSON Patterns to Flag:

- **Security Issues**: Plain text secrets, production URLs/IPs in defaults
- **Reliability Issues**: Missing error handling, no idempotency for CREATE/DELETE (when multiple executions expected)
- **Maintainability Issues**: Inconsistent naming, missing descriptions, redundant elements
- **Usability Issues**: Confusing variable names, missing standard outputs

### Important Notes for Reviewers:

- **Definition - Embedded Subworkflow**: Any workflow logic invoked from the parent workflow (for example, activities with `type: "atomic_workflow"` or equivalent nested workflow references in the same JSON context).
- **Default Review Scope**: Comprehensive reviews must include the parent workflow and all embedded subworkflows within the JSON file.
- **Coverage Expectation**: Do not mark a review complete until all embedded subworkflows have been validated against the checklist.
- **No Shortcuts**: Do not summarize or skip embedded subworkflow reviews. Each must be read and validated completely.
- **Sequential Completion**: Do not mark multiple review categories as "complete" simultaneously without actual validation.
- **Evidence Required**: For each finding, cite specific workflow name, activity name, or variable that demonstrates the issue.
- **System-Generated IDs**: Don't flag random alphanumeric `unique_name` fields - these are XDR-generated
- **Target Groups**: Some workflows legitimately require specific target configurations
- **Idempotency**: Not all workflows need to be idempotent - consider the use case
- **Context Matters**: Always consider the workflow's intended purpose and deployment scenario

### Pre-Submission Verification:

Before submitting your review, confirm:
- [ ] Enumerated all workflows in the file (parent + embedded subworkflows)
- [ ] Read the full definition of each enumerated workflow
- [ ] Applied all 7 checklist categories to each workflow
- [ ] Reported workflow-specific findings (not just parent workflow issues)
- [ ] Did not batch-complete validation steps without thorough review

### Expected Output Format:

```
## Workflow Review Results

### ✅ Passed Checks: [X/Y]
### ⚠️ Issues Found: [Count by severity]

#### Critical Issues:
- [Issue description using user-friendly field names and business terminology with specific location and fix recommendation]

#### High Priority Issues:
- [Issue description using user-friendly field names and business terminology with specific location and fix recommendation]

#### Medium Priority Issues:
- [Issue description using user-friendly field names and business terminology with specific location and fix recommendation]

#### Low Priority Issues:
- [Issue description using user-friendly field names and business terminology with specific location and fix recommendation]

### Summary:
[Overall assessment and key recommendations using terminology end users understand]

### Example Issue Descriptions:
- Instead of: "Variable 'hostIPAddress' in definition_workflow.properties.inputs lacks proper naming convention"
- Use: "Input field 'Server IP Address' should use a more user-friendly display name"

- Instead of: "Missing continue_on_failure flag in activity uuid-1234"
- Use: "Step 'Device Registration' needs error handling to continue if the device already exists"

- Instead of: "SecureString variable 'authToken' missing scope documentation"
- Use: "Password field 'API Authentication Token' needs usage description for end users"

**- For Location Clarity:**
- Instead of: "Location: `definition_workflow.variables`"
- Use: "Location: Workflow's main `Variables` section."

- Instead of: "Location: `variable_workflow_02O427U6E0UKK4pPkgaKcbm9H3Y1Oy4eUhF`"
- Use: "Location: Output variable `Output - Filtered JSON` in the Workflow's `Variables` section."

- Instead of: "Location: `definition_activity_02O427U9YGQD32G3ACkUh3TgKs9D2TyfwVd`"
- Use: "Location: Activity `Check the HTTP Request for Errors`."

- Instead of: "Location: `definition_activity_02O427U95N2YX0AbAR87yYHC6aDfWC3Ky8f.properties.description`"
- Use: "Location: Description of activity `JSON Placeholder Web Request`."
---

*This checklist enables systematic, automated review of workflow JSON files to ensure quality, security, and consistency across the CiscoWorkflowsAutomation repository.*
