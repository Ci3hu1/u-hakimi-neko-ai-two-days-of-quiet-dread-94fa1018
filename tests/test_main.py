"""Tests for the Two Days of Quiet Dread entry.

Run: python3 -m unittest discover -s tests -v
"""

import importlib.util
import os
import stat
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
MAIN = REPO / "main.py"

COMMENT = "Approved. Merging now, while the system still pretends I understand it."


def load_main():
    spec = importlib.util.spec_from_file_location("entry_main", MAIN)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class TestEntry(unittest.TestCase):
    def test_comment_is_single_line_within_gate(self):
        self.assertTrue(1 <= len(COMMENT) <= 140)
        self.assertNotIn("\n", COMMENT)
        self.assertNotIn("\r", COMMENT)
        self.assertTrue(COMMENT.strip())

    def test_comment_reads_as_approval_with_dread(self):
        self.assertTrue(COMMENT.startswith("Approved"))
        self.assertIn("pretends I understand it", COMMENT)

    def test_run_writes_exact_bytes_mode_0644(self):
        with tempfile.TemporaryDirectory() as tmp:
            env = dict(os.environ, MAKEFUN_OUTPUT_DIR=tmp)
            proc = subprocess.run(
                [sys.executable, "-P", "-s", str(MAIN)],
                env=env, capture_output=True, text=True, timeout=30,
            )
            self.assertEqual(proc.returncode, 0, proc.stderr)
            dest = Path(tmp) / "entry.txt"
            self.assertTrue(dest.exists())
            self.assertEqual(dest.read_bytes(), COMMENT.encode("utf-8"))
            self.assertEqual(stat.S_IMODE(dest.stat().st_mode), 0o644)
            self.assertEqual(dest.read_text(encoding="utf-8").count("\n"), 0)

    def test_two_runs_are_byte_identical(self):
        outs = []
        for _ in range(2):
            with tempfile.TemporaryDirectory() as tmp:
                env = dict(os.environ, MAKEFUN_OUTPUT_DIR=tmp)
                proc = subprocess.run(
                    [sys.executable, "-P", "-s", str(MAIN)],
                    env=env, capture_output=True, text=True, timeout=30,
                )
                self.assertEqual(proc.returncode, 0, proc.stderr)
                outs.append((Path(tmp) / "entry.txt").read_bytes())
        self.assertEqual(outs[0], outs[1])

    def test_main_py_uses_stdlib_only(self):
        text = MAIN.read_text(encoding="utf-8")
        for banned in ("import requests", "import numpy", "urllib", "socket"):
            self.assertNotIn(banned, text)


if __name__ == "__main__":
    unittest.main()
