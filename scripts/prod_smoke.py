from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PY = ROOT / ".venv" / "bin" / "python"


def run(cmd: list[str]) -> dict:
    proc = subprocess.run(cmd, capture_output=True, text=True)
    return {
        "cmd": cmd,
        "ok": proc.returncode == 0,
        "code": proc.returncode,
        "stdout": (proc.stdout or "")[:1200],
        "stderr": (proc.stderr or "")[:1200],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="生产向 smoke test")
    parser.add_argument("--keyword", default="露营")
    parser.add_argument("--include-login", action="store_true")
    args = parser.parse_args()

    runner = str(PY if PY.exists() else sys.executable)
    checks = [
        run([runner, str(ROOT / "scripts" / "doctor.py")]),
        run([runner, str(ROOT / "scripts" / "cli.py"), "list-accounts"]),
        run([runner, str(ROOT / "scripts" / "cli.py"), "search-feeds", "--keyword", args.keyword]),
    ]
    if args.include_login:
        checks.insert(2, run([runner, str(ROOT / "scripts" / "cli.py"), "check-login"]))

    print(json.dumps({
        "success": all(c["ok"] for c in checks),
        "checks": checks,
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
