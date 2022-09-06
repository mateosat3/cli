import typer

app = typer.Typer()


@app.command("hello")
def hello_name(
        name: str
):
    """A simple CLI to greet someone."""
    typer.echo(f"Hello {name}")


@app.command("bye")
def bye_name(
        name: str
):
    """A simple CLI to greet someone."""
    typer.echo(f"Bye {name}")


if __name__ == "__main__":
    app()
