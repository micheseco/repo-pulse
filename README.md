# repo-pulse

Summarize git repository activity from the terminal: a daily commit sparkline
built from git log. No runtime dependencies beyond Python and git.

## Installation

```bash
git clone https://github.com/micheseco/repo-pulse.git
cd repo-pulse
pip install -e .
```

## Usage

```bash
repopulse                       # current repository, last 30 days
repopulse ~/projects/api -d 90  # another repository, last 90 days
repopulse --version
```

## Development

```bash
pip install -e ".[dev]"
pytest
```

## License

MIT, see [LICENSE](LICENSE).
