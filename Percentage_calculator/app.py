from ui.diplay import show_menu, delay, clear, cli, header
from ui.validations import get_int_input, option_check
from features.apply import apply_percent
from features.discount import discount_percent
from features.discover import discover_percent
from features.invert import invert_percent

# Maps each menu option to its corresponding function
router = {
    1: apply_percent,
    2: discount_percent,
    3: discover_percent,
    4: invert_percent,
}


def main():
    """Main loop — shows the menu and routes to the chosen feature."""
    while True:
        clear()
        header("Percentage Calculator")
        show_menu()

        input_validate = get_int_input()
        if input_validate is None:
            continue

        # Validate if the option exists
        choice = option_check(input_validate)

        # Exit the program
        if input_validate == 0:
            clear()
            cli.print("[bold yellow]Exiting...")
            delay(0.8)
            clear()
            exit()

        # Route to the chosen feature
        action = router.get(choice)
        if action:
            action()


if __name__ == "__main__":
    main()