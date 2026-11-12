"""Read activity data from a git repository by invoking the git CLI."""

from __future__ import annotations

import subprocess
from collections import Counter
from datetime import date, timedelta
from pathlib import Path


class GitError(RuntimeError):
    """Raised when git is missing or the path is not a usable repository."""


def _log(repo: Path, days: int, fmt: str) -> list[str]:
    since = (date.today() - timedelta(days=days)).isoformat()
    cmd = [
        "git", "-C", str(repo), "log",
        f"--since={since}", "--date=short", f"--pretty=format:{fmt}",
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    except FileNotFoundError as exc:
        raise GitError("git executable not found on PATH") from exc
    except subprocess.CalledProcessError as exc:
        raise GitError(exc.stderr.strip() or "git log failed") from exc
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def commit_counts(repo: Path, days: int) -> Counter[date]:
    """Number of commits per calendar day within the window."""
    counts: Counter[date] = Counter()
    for line in _log(repo, days, "%ad"):
        counts[date.fromisoformat(line)] += 1
    return counts


def daily_series(counts: Counter[date], days: int, today: date | None = None) -> list[int]:
    """Daily commit counts, oldest first, ending on today."""
    today = today or date.today()
    return [counts.get(today - timedelta(days=offset), 0) for offset in range(days - 1, -1, -1)]
