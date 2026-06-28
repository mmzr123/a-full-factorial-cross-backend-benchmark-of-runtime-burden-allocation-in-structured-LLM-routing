# Sanitization notes

This repository-ready package removes provider credentials, endpoint identifiers, account-level metadata, and environment-specific secrets. The distributed tables are aggregate or design-level CSV files derived from the benchmark matrix and reported summary layers. The JSON schema in `data/schema/request_level_event_schema.json` documents the request-level event structure for future reuse when fully sanitized event logs are available.

No personally identifiable human-subject data are included. Prompt templates are described at the routing-category level rather than as private user conversations.
