from typer.testing import CliRunner

from src.cli.main import app

runner = CliRunner()


def test_hello_name():
    result = runner.invoke(app, ['hello', "-n", "Jasper"])
    assert result.exit_code == 0
    assert "Hello Jasper" in result.stdout


def test_bye_name():
    result = runner.invoke(app, ['bye', "-n", "Jasper"])
    assert result.exit_code == 0
    assert "Bye Jasper" in result.stdout
