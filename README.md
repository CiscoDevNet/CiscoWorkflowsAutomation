# Cisco Workflows Automation

This repository contains automation workflows organized by target platform and functionality, plus a public toolkit for reviewing and improving workflow exports before submission.


## Repository Structure

```text
CiscoWorkflowsAutomation/
├── CODE_OF_CONDUCT.md                    # Community standards and interaction guidelines
├── CONTRIBUTING.md                       # Contribution guidelines and procedures
├── README.md                             # This file - repository overview
├── AI/                                   # AI-powered automation workflows and integrations
├── Catalyst_Center/                      # Cisco Catalyst Center automation workflows
├── Cross_Domain/                         # Multi-platform and cross-domain integration workflows
├── Learning_Series/                      # Educational workflows and training materials
├── LICENSE                               # Repository license terms
├── Meraki/                               # Cisco Meraki automation workflows and integrations
├── Restful_WebService/                   # RESTful API integration workflows and examples
├── Toolkit/                              # Public review, remediation, shared CLI, and reusable agent skills
└── SECURITY.md                           # Security policies and reporting procedures
```

## Public Toolkit

The `Toolkit/` area provides reusable helpers for the workflow review checklist in this repository. It is intended for:

- Cursor and Codex users who want reusable skills backed by a shared CLI
- solution engineers or contributors using another LLM
- external contributors who want a documented CLI and skill-based path

See `Toolkit/README.md` for the audience guide and `WorkflowReviewChecklist.md` for the canonical review contract. The recommended agent integration is the skill path in `Toolkit/skills/`, while the review and remediation guides live under `Toolkit/exchange-review/` and `Toolkit/exchange-remediation/`.

## Contributing

We welcome contributions to expand and improve the automation workflows and supporting utilities. Please review our contribution guidelines:

### How to Contribute

1. **Review Guidelines**: Read `CONTRIBUTING.md` for detailed contribution procedures
2. **Follow Standards**: Adhere to coding standards and documentation requirements
3. **Test Thoroughly**: Validate workflows in non-production environments
4. **Document Changes**: Include comprehensive documentation for new workflows
5. **Submit Pull Requests**: Follow the established review process

### Community Standards

- **Code of Conduct**: Review `CODE_OF_CONDUCT.md` for community interaction standards
- **Security**: Report security issues following procedures in `SECURITY.md`
- **Licensing**: All contributions subject to repository license terms

## Support and Resources

### Documentation

- Individual workflow documentation in respective directories
- Platform-specific guides and best practices
- API documentation and integration examples

### Community Support

- **Issues**: Report bugs and feature requests through GitHub issues
- **Discussions**: Engage with the community for questions and collaboration
- **DevNet Resources**: Access Cisco DevNet documentation and learning materials


## License

This repository is licensed under the terms specified in the `LICENSE` file. Please review the license before using or contributing to this project.

---

**Maintained by**: Cisco Workflows Automation DevNet Team
**Last Updated**: August 2025 