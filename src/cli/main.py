import typer

app = typer.Typer()


@app.command("hello")
def hello_name(
        name: str = typer.Option('Jasper', '-n', help="The name to greet.", show_default=True),
):
    """A simple CLI to greet someone."""
    typer.echo(f"Hello {name}")


@app.command("bye")
def bye_name(
        name: str = typer.Option('Jasper', '-n', help="The name to say goodbye", show_default=True),
):
    """A simple CLI to greet someone."""
    typer.echo(f"Bye {name}")


def main():
    app()
