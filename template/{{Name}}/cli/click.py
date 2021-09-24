import click


@click.command()
@click.option(
    "--example",
    prompt='Example function',
    help="Example function",
    type=click.STRING
)
def boilerplate(example: click.STRING) -> None:
    """
    Program that runs example functions.

    Args:
        example (click.STRING): example function
    """
    click.echo(f"You're example function is {example}")


if __name__ == "__main__":
    boilerplate()
