from __future__ import annotations

import argparse
from pathlib import Path

from . import __version__
from .git_stats import commit_counts, daily_series
from .render import sparkline


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="repopulse",
        description="Summarize git repository activity from the terminal.",
    )
    parser.add_argument(
        "path", nargs="?", default=".", type=Path,
        help="repository path (default: current directory)",
    )
    parser.add_argument("-d", "--days", type=int, default=30, help="window in days (default: 30)")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    args = parser.parse_args(argv)

    repo = args.path.resolve()
    series = daily_series(commit_counts(repo, args.days), args.days)
    print(f"{repo.name}: last {args.days} days")
    print(f"  {sparkline(series)}")
    return 0
