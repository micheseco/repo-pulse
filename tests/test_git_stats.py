import shutil
import subprocess
from collections import Counter
from datetime import date

import pytest

from repopulse.git_stats import GitError, commit_counts, daily_series

needs_git = pytest.mark.skipif(shutil.which("git") is None, reason="git not installed")


def test_daily_series_ends_today_and_has_requested_length():
    today = date(2026, 10, 26)
    counts = Counter({date(2026, 10, 26): 3, date(2026, 10, 24): 1})
    assert daily_series(counts, 3, today=today) == [1, 0, 3]


@needs_git
def test_git_error_outside_a_repository(tmp_path):
    with pytest.raises(GitError):
        commit_counts(tmp_path, 7)


@needs_git
def test_counts_commits_in_a_real_repository(tmp_path):
    subprocess.run(["git", "init", "-q", str(tmp_path)], check=True)
    for message in ("first", "second"):
        subprocess.run(
            ["git", "-C", str(tmp_path),
             "-c", "user.name=Tester", "-c", "user.email=t@example.com",
             "commit", "-q", "--allow-empty", "-m", message],
            check=True,
        )
    assert sum(commit_counts(tmp_path, 7).values()) == 2
