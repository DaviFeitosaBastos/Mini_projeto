from rich.console import Console
from time import sleep
import os

cli = Console()


def clear() -> None:
    """Clear the terminal screen."""
    os.system("clear")


def delay(s: float) -> None:
    """Pause execution for a given number of seconds.

    Args:
        s: seconds to wait.
    """
    sleep(s)


def show_menu() -> None:
    """Display the main menu."""
    cli.print("[bold]This is a percentage calculator.")
    cli.print("[bold]What would you like to do [yellow]first[/]?")
    cli.print("[bold]-" * 30)
    cli.print("1 - Apply %    -> (100 + x%)?")
    cli.print("2 - Discount % -> (100 - x%)?")
    cli.print("3 - Discover % -> (x is what % of Z)")
    cli.print("4 - Invert %   -> (x is Y% of what)")
    cli.print("0 - Exit")
    cli.print("[bold]-" * 30)


# Color map for each header title
HEADER_COLORS = {
    "Percentage Calculator": "red",
    "Apply %":               "blue",
    "Percentage %":          "purple",
    "Discount %":            "yellow",
    "Discover %":            "pink",
    "Invert %":              "grey",
}


def header(msg: str) -> None:
    """Display a colored section header.

    Args:
        msg: the title to display. Falls back to green if not mapped.
    """
    color = HEADER_COLORS.get(msg, "green")
    width = 45 if color == "green" else 42
    cli.print(f"[bold {color}]=" * 30)
    cli.print(f"[bold {color}]{msg}[/]".center(width))
    cli.print(f"[bold {color}]=" * 30)


if __name__ == "__main__":
    ...