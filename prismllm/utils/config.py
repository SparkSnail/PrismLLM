"""Configuration management"""

from typing import Optional
from pydantic import BaseModel
import yaml


class ServeConfig(BaseModel):
    """Serve configuration"""
    backend: str = "vllm"
    model: str
    port: int = 8000
    host: str = "0.0.0.0"


class Config(BaseModel):
    """Main configuration"""
    serve: ServeConfig


def load_config(path: str) -> Config:
    """Load configuration from YAML file"""
    with open(path, "r") as f:
        data = yaml.safe_load(f)
    return Config(**data)
