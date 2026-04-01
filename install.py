#!/usr/bin/env python3
"""
Create a virtual environment for the current repository and install
dependencies from common requirement files.

Usage:
    python setup_venv.py

Optional:
    python setup_venv.py .venv
"""

from __future__ import annotations

import os
import platform
import shutil
import subprocess
import sys
from pathlib import Path


def run_command(cmd: list[str], cwd: Path | None = None) -> None:
    """Run a command and raise a clear error if it fails."""
    print(f"\n[RUN] {' '.join(cmd)}")
    try:
        subprocess.run(cmd, cwd=cwd, check=True)
    except subprocess.CalledProcessError as exc:
        raise RuntimeError(
            f"Command failed with exit code {exc.returncode}: {' '.join(cmd)}"
        ) from exc


def find_dependency_file(repo_path: Path) -> tuple[str, Path] | None:
    """
    Find the first supported dependency file in the repository.

    Priority:
    1. requirements.txt
    2. requirements-dev.txt
    3. pyproject.toml
    """
    candidates = [
        ("requirements", repo_path / "requirements.txt"),
        ("requirements-dev", repo_path / "requirements-dev.txt"),
        ("pyproject", repo_path / "pyproject.toml"),
    ]

    for dep_type, dep_path in candidates:
        if dep_path.exists():
            return dep_type, dep_path

    return None


def get_venv_python(venv_path: Path) -> Path:
    """Return the Python executable path inside the virtual environment."""
    if platform.system().lower() == "windows":
        return venv_path / "Scripts" / "python.exe"
    return venv_path / "bin" / "python"


def get_activation_command(venv_path: Path) -> str:
    """Return a shell-specific activation command."""
    if platform.system().lower() == "windows":
        return str(venv_path / "Scripts" / "activate")
    return f"source {venv_path / 'bin' / 'activate'}"


def main() -> None:
    repo_path = Path.cwd()
    venv_name = sys.argv[1] if len(sys.argv) > 1 else ".venv"
    venv_path = repo_path / venv_name

    print(f"[INFO] Repository path: {repo_path}")
    print(f"[INFO] Virtual environment path: {venv_path}")

    if shutil.which(sys.executable) is None:
        raise RuntimeError("Python executable not found.")

    if not venv_path.exists():
        print("[INFO] Creating virtual environment...")
        run_command([sys.executable, "-m", "venv", str(venv_path)])
    else:
        print("[INFO] Virtual environment already exists. Reusing it.")

    venv_python = get_venv_python(venv_path)

    if not venv_python.exists():
        raise RuntimeError(
            f"Virtual environment Python not found at: {venv_python}"
        )

    print("[INFO] Upgrading pip, setuptools, and wheel...")
    run_command(
        [
            str(venv_python),
            "-m",
            "pip",
            "install",
            "--upgrade",
            "pip",
            "setuptools",
            "wheel",
        ]
    )

    dep_info = find_dependency_file(repo_path)
    if dep_info is None:
        print(
            "[WARN] No supported dependency file found. "
            "Checked: requirements.txt, requirements-dev.txt, pyproject.toml"
        )
    else:
        dep_type, dep_path = dep_info
        print(f"[INFO] Found dependency file: {dep_path.name}")

        if dep_type in {"requirements", "requirements-dev"}:
            run_command(
                [str(venv_python), "-m", "pip", "install", "-r", str(dep_path)]
            )
        elif dep_type == "pyproject":
            run_command([str(venv_python), "-m", "pip", "install", "-e", "."])

    print("\n[SUCCESS] Environment is ready.")
    print(f"[INFO] Activate it with:\n{get_activation_command(venv_path)}")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"\n[ERROR] {exc}", file=sys.stderr)
        sys.exit(1)