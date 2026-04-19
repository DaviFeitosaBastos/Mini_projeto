from ui.diplay import show_menu, delay, clear, cli, header
from ui.validations import get_float_input, exit_yes_or_not


def discover_percent():
    """Calculate what percentage x is of z."""
    while True:
        # First input: the base number
        clear()
        header("Discover %")
        cli.print("[bold]Type the base number")
        number_x = get_float_input("\nNumber x: ")
        if number_x is None:
            continue

        # Second input: the total number
        clear()
        header("Discover %")
        cli.print("[bold]Type the total number")
        number_z = get_float_input("\nNumber z: ")
        if number_z is None:
            continue

        # Calculate: x is what % of z?
        result = (number_x / number_z) * 100

        clear()
        header("Result")
        cli.print(f"[bold]Here is the result: {number_x:.2f} is [green][{result:.2f}%][/] of {number_z:.2f}")

        if exit_yes_or_not():
            continue
        break