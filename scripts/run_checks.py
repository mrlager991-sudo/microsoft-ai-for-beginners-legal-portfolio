"""One-command standard-library validation and test runner."""
from __future__ import annotations
import subprocess, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SUITES=[ROOT/"tests",*sorted((ROOT/"projects").iterdir())]

def run(command,cwd=ROOT):
    print("+"," ".join(str(x) for x in command),flush=True)
    completed=subprocess.run(command,cwd=cwd)
    if completed.returncode: raise SystemExit(completed.returncode)

if __name__=="__main__":
    run([sys.executable,str(ROOT/"scripts"/"validate_portfolio.py")])
    for suite in SUITES:
        if suite.is_dir() and list(suite.glob("test_*.py")):
            run([sys.executable,"-m","unittest","discover","-s",str(suite),"-p","test_*.py"])
    print("ALL CHECKS PASSED")
