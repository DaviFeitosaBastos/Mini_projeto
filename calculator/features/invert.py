from ui.diplay import show_menu, delay, clear, cli, header
from ui.validations import get_float_input, exit_yes_or_not


def invert_percent():
    while True:
        clear()
        header("Invert %")
        cli.print("[bold]Type the number [x]")
        number_x = get_float_input("\nNumber x: ")
        if number_x is None:
            continue

        clear()
        header("Invert %")
        cli.print("[bold]Type the known percentage [y%]")
        percentage = get_float_input("\nPercentage y%: ")
        if percentage is None:
            continue

        clear()
        result = number_x / (percentage / 100)
        header("Result")
        cli.print(f"[bold]Here is the result: {number_x:.2f} is [green]{percentage:.2f}%[/] of {result:.2f}")

        if exit_yes_or_not():
            continue
        break