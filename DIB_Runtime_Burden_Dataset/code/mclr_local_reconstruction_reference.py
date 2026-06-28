"""Reference implementation sketch for compact-code local reconstruction.

This file documents the deterministic structure-realization step used by a compact
routing package. It intentionally excludes provider credentials and endpoint code.
"""

ROUTE_MAP = {
    "C": "chat",
    "T": "task",
    "D": "dev",
    "O": "doc",
}


def reconstruct_control_record(route_code, confidence=None, memory_flag=False, tool_flag=False, reason=""):
    """Convert a compact route code into the downstream JSON-style control record.

    Parameters
    ----------
    route_code : str
        Compact symbolic route code emitted by the model.
    confidence : float or None
        Optional model confidence. If absent, the field is set to None.
    memory_flag : bool
        Whether the downstream memory layer should be queried.
    tool_flag : bool
        Whether the downstream tool layer should be activated.
    reason : str
        Sanitized short rationale string.
    """
    code = str(route_code).strip().upper()
    if code not in ROUTE_MAP:
        raise ValueError(f"Unknown route code: {route_code!r}")
    return {
        "route": ROUTE_MAP[code],
        "confidence": confidence,
        "use_memory": bool(memory_flag),
        "use_tool": bool(tool_flag),
        "reason": str(reason).strip(),
    }
