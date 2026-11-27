"""Shared test setup.

Phase folders start with a number (e.g. 02-kuhn-cfr), so they can't be
imported as packages. We add them to the import path instead.

Any test that hits a NotImplementedError is skipped rather than failed,
so the test suite doubles as a progress tracker.
"""

import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
for phase_dir in sorted(ROOT.glob("0*-*")):
    sys.path.insert(0, str(phase_dir))


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_call(item):
    outcome = yield
    if outcome.excinfo is not None and issubclass(outcome.excinfo[0], NotImplementedError):
        outcome.force_exception(pytest.skip.Exception("not implemented yet"))
