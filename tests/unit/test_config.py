"""Unit tests for configuration module"""

import pytest
from pathlib import Path
from prismllm.utils.config import Config, ServeConfig, load_config


def test_config_defaults():
    """Test default configuration values"""
    config = Config(serve=ServeConfig(model="Qwen2-7B"))
    assert config.serve.backend == "vllm"
    assert config.serve.port == 8000
    assert config.serve.host == "0.0.0.0"


def test_config_custom_values():
    """Test custom configuration values"""
    config = Config(
        serve=ServeConfig(
            model="Qwen2-7B",
            backend="ollama",
            port=9000,
            host="127.0.0.1"
        )
    )
    assert config.serve.backend == "ollama"
    assert config.serve.port == 9000
    assert config.serve.host == "127.0.0.1"


def test_load_config(tmp_path):
    """Test loading configuration from YAML file"""
    config_file = tmp_path / "config.yaml"
    config_file.write_text("""
serve:
  model: Qwen2-7B
  backend: vllm
  port: 8000
""")

    config = load_config(str(config_file))
    assert config.serve.model == "Qwen2-7B"
    assert config.serve.backend == "vllm"
    assert config.serve.port == 8000
