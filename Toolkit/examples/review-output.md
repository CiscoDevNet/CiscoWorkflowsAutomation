# Sample Review Output

```markdown
## Exchange Review Results

### Enumeration
- Workflow 1: Parent Workflow
- Workflow 2: Embedded Workflow

### Critical issues
- None.

### High priority issues
- Activity "Submit API Request" does not surface failure details in the workflow outputs.

### Medium priority issues
- None.

### Low priority issues
- The main workflow description is too thin for Exchange reviewers.

### Workflow-by-workflow notes
#### Parent Workflow
- Logic & Flow: Add explicit success and failure output updates.

#### Embedded Workflow
- Essential Hygiene & Security: Replace a real org ID default with a placeholder.

### Overall assessment
- Score: 7/10
- Approval readiness: approve with suggestions

### Remediation suggestions
- Improve output handling.
- Remove production-like defaults.
- Strengthen reviewer-facing descriptions.
```
