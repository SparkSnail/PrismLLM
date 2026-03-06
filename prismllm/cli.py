"""CLI entry point for PrismLLM"""

import click


@click.group()
@click.version_option(version="0.1.0")
def main():
    """PrismLLM - Progressive LLM Data Platform"""
    pass


@main.command()
@click.option("--model", required=True, help="Model name or path")
@click.option("--host", default="0.0.0.0", help="Host to bind")
@click.option("--port", default=8000, help="Port to bind")
def serve(model: str, host: str, port: int):
    """Start inference server"""
    click.echo(f"Starting PrismLLM server...")
    click.echo(f"Model: {model}")
    click.echo(f"Server: http://{host}:{port}")


if __name__ == "__main__":
    main()
