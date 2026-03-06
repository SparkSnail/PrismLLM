"""Unit tests for CLI module"""

from click.testing import CliRunner
from prismllm.cli import main


def test_cli_version():
    """Test CLI version command"""
    runner = CliRunner()
    result = runner.invoke(main, ["--version"])
    assert result.exit_code == 0
    assert "0.1.0" in result.output


def test_cli_help():
    """Test CLI help command"""
    runner = CliRunner()
    result = runner.invoke(main, ["--help"])
    assert result.exit_code == 0
    assert "PrismLLM" in result.output


def test_serve_command_help():
    """Test serve command help"""
    runner = CliRunner()
    result = runner.invoke(main, ["serve", "--help"])
    assert result.exit_code == 0
    assert "Start inference server" in result.output


def test_serve_command_with_model():
    """Test serve command with model parameter"""
    runner = CliRunner()
    result = runner.invoke(main, ["serve", "--model", "test-model"])
    assert result.exit_code == 0
    assert "test-model" in result.output
