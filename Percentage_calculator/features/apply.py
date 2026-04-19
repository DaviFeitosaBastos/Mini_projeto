from ui.diplay import show_menu, delay, clear, cli, header
from ui.validations import get_float_input, exit_yes_or_not


def apply_percent():
    """Apply a percentage increase to a number."""
    while True:
        # First input: the percentage to apply
        clear()
        header("Apply %")
        cli.print("[bold]Type the (x%) that will be applied to the number")
        percentage = get_float_input("\nPercentage x%: ")
        if percentage is None:
            continue

        # Second input: the base number
        clear()
        header("Apply %")
        cli.print("[bold]Type the (x) that will receive the percentage")
        number_x = get_float_input("\nNumber x: ")
        if number_x is None:
            continue

        # Calculate: number + percentage
        result = number_x * (1 + percentage / 100)

        clear()
        header("Result")
        cli.print(f"[bold]Here is {number_x:.2f} with {percentage:.2f}% = [green][{result:.2f}][/]")

        if exit_yes_or_not():
            continue
        break