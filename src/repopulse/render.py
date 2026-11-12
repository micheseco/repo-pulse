"""Text rendering helpers."""

from __future__ import annotations

BLOCKS = " ▁▂▃▄▅▆▇█"


def sparkline(values: list[int]) -> str:
    """Map each value to a block character scaled against the series peak."""
    peak = max(values, default=0)
    if peak == 0:
        return BLOCKS[0] * len(values)
    top = len(BLOCKS) - 1
    return "".join(BLOCKS[round(v / peak * top)] for v in values)
