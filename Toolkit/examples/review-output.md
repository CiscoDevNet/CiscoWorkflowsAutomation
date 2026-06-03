# Sample Review Output

```markdown
## Workflow Review Results

### Enumeration
- Workflow 1: Parent Workflow
- Workflow 2: Embedded Workflow

### High Priority Issues
- Activity "Submit API Request" does not surface failure details in the workflow outputs.

### Low Priority Issues
- The main workflow description is too thin for Exchange reviewers.

### Workflow-by-Workflow Notes
#### Parent Workflow
- Error Handling: Add explicit success and failure output updates.

#### Embedded Workflow
- Essential Hygiene & Security: Replace a real org ID default with a placeholder.

### Overall Assessment
- Score: 7/10
- Approval readiness: approve with suggestions
- Top improvements:
  - improve output handling
  - remove production-like defaults
  - strengthen reviewer-facing descriptions
```
