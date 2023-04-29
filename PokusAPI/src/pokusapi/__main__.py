"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """pokusapi."""
    excellentApi = "Pokus"
    print(f"What's the best API ? {excellentApi}, period.")


if __name__ == "__main__":
    main(prog_name="pokusapi")  # pragma: no cover
