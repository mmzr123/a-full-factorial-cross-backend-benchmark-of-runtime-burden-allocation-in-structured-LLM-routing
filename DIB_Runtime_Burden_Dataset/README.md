# Data for a full-factorial cross-backend benchmark of runtime burden allocation in structured LLM routing

This repository-ready package accompanies a Data in Brief manuscript describing a sanitized dataset derived from a structured LLM routing benchmark. The benchmark crossed four runtime modes, three backend families, two constraint settings, and two transport settings, producing 48 deployment combinations and 15,552 routed request events at the benchmark-harness level.

## Folder layout

- `metadata/`: specifications table, metric dictionary, sanitization notes, file inventory, and checksums.
- `data/design/`: full-factorial deployment matrix and runtime-mode definitions.
- `data/processed/`: backend-mode summaries, ANOVA effect tables, targeted contrasts, workflow lower-bound completion, and failure taxonomy.
- `data/schema/`: JSON schema for sanitized request-level events.
- `code/`: lightweight scripts for integrity checks and reference local reconstruction.
- `docs/`: manuscript-facing notes used to prepare the data article.

## Quick reuse

Run the integrity check from the repository root:

```bash
python code/reproduce_summary_tables.py
```

The script verifies the 48-row factorial matrix, the 15,552 total planned request count, the 12 backend-mode summary cells, and the failure taxonomy total.

## License

Unless otherwise specified by the final repository record, the tabular dataset and metadata are intended for release under CC BY 4.0. Code snippets are intended for release under the MIT License.
