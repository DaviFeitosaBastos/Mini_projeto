from ui.diplay import show_menu, delay, clear, cli, header
from ui.validations import get_float_input, exit_yes_or_not


def discount_percent():
    while True:
        clear()
        header("Discount %")
        cli.print("[bold]Type the number you want to discount from: ")
        number_x = get_float_input("\nNumber x: ")
        if number_x is None:
            continue

        clear()
        header("Discount %")
        cli.print("[bold]Type the percentage to discount")
        percentage = get_float_input("\nPercentage x%: ")  
        if percentage is None:
            continue 

        clear()
        result = number_x * (1 - percentage / 100)
        header("Result")
        cli.print(f"[bold]Here is the result of {number_x:.2f} - {percentage:.2f}% = [green][{result:.2f}]")

        if exit_yes_or_not() != False:
            continue
        break