# PrismLLM

[![Test](https://github.com/SparkSnail/PrismLLM/actions/workflows/test.yml/badge.svg)](https://github.com/SparkSnail/PrismLLM/actions/workflows/test.yml)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-Apache%202.0-green.svg)](LICENSE)

Progressive LLM Data Platform - From Data to LLM in Minutes

## Quick Start (5 minutes)

```bash
# Install
pip install prismllm

# Start server
prismllm serve --model Qwen/Qwen2-7B-Instruct

# Test
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model": "Qwen2-7B", "messages": [{"role": "user", "content": "Hello"}]}'
```

## Features

- ✅ OpenAI API Compatible
- ✅ Multiple inference engines (vLLM, SGLang, Ollama)
- ✅ Built-in RAG with ChromaDB
- ✅ MLflow experiment tracking
- ✅ Docker deployment

## Installation

```bash
pip install prismllm
```

## Development

```bash
# Clone repository
git clone https://github.com/SparkSnail/PrismLLM.git
cd PrismLLM

# Install in development mode
pip install -e ".[dev]"

# Run tests
pytest tests/unit -v
```

## License

Apache 2.0
