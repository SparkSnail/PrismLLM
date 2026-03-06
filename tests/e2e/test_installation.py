"""E2E tests for installation"""

import subprocess


def test_pip_install():
    """Test pip installation"""
    result = subprocess.run(
        ["pip", "install", "-e", "."],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0


def test_cli_available():
    """Test CLI command is available after installation"""
    result = subprocess.run(
        ["prismllm", "--version"],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert "0.1.0" in result.stdout or "0.1.0" in result.stderr
