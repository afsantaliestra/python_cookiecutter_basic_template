"""Cli."""

import typer

from src import hello_world

typer_app = typer.Typer(rich_markup_mode=True)


@typer_app.command()
def hello_world_command():
    """Hello world."""
    hello_world()


if __name__ == "__main__":
    typer_app()
