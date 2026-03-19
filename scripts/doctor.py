from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VENV_BIN = ROOT / ".venv" / "bin"


def check_cmd(name: str) -> dict:
    preferred = VENV_BIN / name
    if preferred.exists():
        return {"name": name, "found": True, "path": str(preferred), "source": ".venv"}
    path = shutil.which(name)
    return {"name": name, "found": bool(path), "path": path, "source": "system" if path else None}


def run(cmd: list[str]) -> tuple[bool, str]:
    try:
        out = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
        text = (out.stdout or out.stderr).strip()
        return out.returncode == 0, text
    except Exception as e:
        return False, str(e)


def main() -> None:
    py_ok = sys.version_info >= (3, 11)
    chrome = (
        shutil.which("google-chrome")
        or shutil.which("chrome")
        or shutil.which("chromium")
        or shutil.which("chromium-browser")
    )
    uv = check_cmd("uv")
    runner = str(VENV_BIN / "python") if (VENV_BIN / "python").exists() else sys.executable
    python = {
        "name": "python3",
        "found": True,
        "path": runner,
        "version": sys.version.split()[0],
    }

    cli_ok, cli_help = run([runner, str(ROOT / "scripts" / "cli.py"), "--help"])
    launcher_ok, launcher_help = run([runner, str(ROOT / "scripts" / "chrome_launcher.py"), "--help"])
    pyproject_exists = (ROOT / "pyproject.toml").exists()
    skill_exists = (ROOT / "SKILL.md").exists()
    refs_dir = ROOT / "references"

    result = {
        "success": py_ok and uv["found"] and bool(chrome) and cli_ok and launcher_ok and pyproject_exists and skill_exists,
        "python": python,
        "python_requires": ">=3.11",
        "python_ok": py_ok,
        "uv": uv,
        "chrome": {"found": bool(chrome), "path": chrome},
        "project": {
            "root": str(ROOT),
            "venv_exists": (ROOT / ".venv").exists(),
            "pyproject_exists": pyproject_exists,
            "skill_exists": skill_exists,
            "references_exists": refs_dir.exists(),
        },
        "smoke_tests": {
            "cli_help": {"ok": cli_ok, "snippet": cli_help[:400]},
            "chrome_launcher_help": {"ok": launcher_ok, "snippet": launcher_help[:400]},
        },
        "next_steps": [],
    }

    if not py_ok:
        result["next_steps"].append("升级 Python 到 3.11 或更高版本")
    if not uv["found"]:
        result["next_steps"].append("在项目虚拟环境或系统环境安装 uv")
    if not chrome:
        result["next_steps"].append("安装 Google Chrome 或 Chromium")
    if not cli_ok:
        result["next_steps"].append("检查 scripts/cli.py 是否可运行")
    if not launcher_ok:
        result["next_steps"].append("检查 scripts/chrome_launcher.py 是否可运行")
    if result["success"]:
        result["next_steps"].append("运行 python scripts/chrome_launcher.py 启动浏览器")
        result["next_steps"].append("运行 python scripts/cli.py check-login 检查登录状态")

    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
