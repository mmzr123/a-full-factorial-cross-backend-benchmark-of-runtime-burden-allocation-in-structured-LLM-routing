# Data acquisition protocol summary

The data were acquired with a deterministic structured-routing benchmark harness. The harness applied a full-factorial design with the factors `mode`, `backend`, `constraint_setting`, and `transport_setting`. Each of the 48 combinations was evaluated against 324 routing requests. The emitted routing control record was checked for format compliance, routing correctness, state retention where applicable, full-response latency, and token consumption.

The distributed CSV files contain the design matrix and sanitized aggregate layers used for descriptive and inferential reuse. The request-level event schema is provided so that future users can map fully sanitized event records into the same structure.
