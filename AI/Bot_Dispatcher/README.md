# Bot Dispatcher

This directory contains Cisco Workflows assets for a Webex-driven workflow dispatcher. The dispatcher receives messages from a Webex bot webhook, validates the sender, interprets the request, and either returns help content, searches for workflows, or launches a downstream workflow.

## Contents

- `Webinar_Workflow_Dispatcher_Actual.json`: Main dispatcher workflow. This workflow processes inbound Webex webhook payloads, retrieves the original message from Webex, performs basic authorization checks, uses an LLM to interpret the request, and sends responses back into the originating Webex room or thread.
- `Create_Workflow_Variable_Structure_for_Dispatcher.json`: Helper workflow that looks up another Cisco Workflow by name, retrieves its start configuration, and reduces the input variable schema into a compact JSON structure that can be reused by the dispatcher.
- `Bot_Association_Curl_Commmands`: Example `curl` commands for associating a Webex bot webhook with a Cisco Workflows webhook endpoint, listing existing webhook associations, and deleting associations.

## How It Works

The dispatcher workflow is designed around a Webex bot integration pattern:

1. A Webex webhook posts a notification into Cisco Workflows when the bot is mentioned.
2. The dispatcher retrieves the actual message body and room metadata from Webex.
3. The workflow validates whether the sender is allowed to use the bot.
4. An LLM classifies the request into a dispatcher action such as help, execute, or workflow search.
5. The dispatcher either responds directly in Webex or launches a downstream workflow with the required inputs.

The helper workflow supports this model by converting workflow start configuration data into a simpler structure that is easier to include in dispatcher prompt content or workflow metadata.

## Configuration Notes

These assets are examples and should be reviewed before use in another environment.

- Update runtime targets, runtime users, organization IDs, webhook IDs, and bearer tokens to match your own environment.
- Review the `RBAC Allowed List` local variable in the dispatcher workflow and replace it with your own allowed users or a stronger authorization source.
- Review any embedded workflow IDs and variable IDs in the dispatcher definitions before promoting changes between tenants or organizations.
- Treat Webex bot access tokens, workflow bearer credentials, and API keys as secrets. Do not commit real values into version control.

## Import and Usage

- Import the JSON workflow definitions into Cisco Workflows.
- Configure the referenced targets and runtime users.
- Create a Cisco Workflows webhook that invokes the dispatcher workflow.
- Use the examples in `Bot_Association_Curl_Commmands` to bind a Webex bot webhook to that Cisco Workflows webhook URL.
- Test in a non-production Webex space before broader rollout.

## Operational Notes

- The dispatcher includes logic for sending either plain text or Markdown responses back to Webex.
- The helper workflow currently produces a reduced `Variable Structure` output suitable for downstream prompt or execution preparation.
- Because these workflows rely on multiple external services, validation should include Webex webhook delivery, Cisco Workflows API access, and any configured LLM provider credentials.
