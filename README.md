<<<<<<< HEAD
## Description

This repository contains a training-focused UI automation project built with **Python**, **Playwright**, and **pytest**, targeting the OrangeHRM demo application.
It is intended for learning and experimentation with browser automation, test structuring, and maintainable Page Object Model design.

Dependencies and virtual environments are managed using **uv**, providing fast and reproducible installs via `pyproject.toml` and lockfile resolution.


## UV Installation
The uv tool is a high-speed package and project manager for Python

Install uv with our standalone installers:

```bash
# On macOS and Linux.
curl -LsSf https://astral.sh/uv/install.sh | sh
```

```bash
# On Windows.
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Or, from [PyPI](https://pypi.org/project/uv/):

```bash
# With pip.
pip install uv
```

### Setup

Install dependencies:

```bash
uv sync
```

Install Playwright browsers:

```bash
uv run playwright install
```

Run tests:

```bash
uv run pytest
```
=======
# orange-hrm-playwright-aya
Playwright automation project for Orange HRM with CI/CD pipeline
>>>>>>> aec60d024f5caa7c912be3e333b84736575f4a44
