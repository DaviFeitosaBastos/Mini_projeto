from ui.diplay import cli, delay, clear
import logging

# Logging format config
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

log = logging.getLogger(__name__)


def get_int_input() -> int | None:
    """Get an integer input from the user.

    Returns:
        int: the choice if valid.
        None: if the input is not an integer.

    Raises:
        ValueError: if the value is a string.
    """
    try:
        choice = int(input("\nChoice: "))
        
        return choice
    
    except ValueError as e:
        log.error(f"ValueError:[{e}]")
        delay(0.8)
        clear()
        return None
    
def get_float_input(prompt: str) -> float | None:
    """Get a float input from the user.

    Args:
        prompt: the message shown to the user.

    Returns:
        float: the value if valid.
        None: if the input is not a number.
    """
    try:
        value = float(input(prompt))
        return value
    except ValueError as e:
        log.error(f"ValueError:[{e}]")
        delay(0.8)
        clear()
        return None

    
def option_check(user_input: int) -> int:
    """Check if the option chosen is valid.

    Args:
        user_input: the integer typed by the user.

    Returns:
        int: the same input if valid.
    """
    if not user_input in [1, 2, 3, 4, 0]:
        cli.print("[bold red]Invalid option try again")
        delay(0.8)

    return user_input

def exit_yes_or_not() -> bool:
    """Ask the user if they want to calculate again.

    Returns:
        True: if the user wants to continue.
        False: if the user wants to return to the menu.
    """
    while True:
        cli.print("[bold yellow]Again? (y/n): ")
        again = input().strip().lower()

        if again in ["y","yes"]:
            return True
        elif again in ["n","not"]:
            clear()
            cli.print('[bold] Returning...')
            delay(0.8)
            return False
        else:
            cli.print("[bold red]Invalid option[/] try[bold purple] (y/n/yes/not)!")
            delay(0.9)
            clear()
        

if __name__ == "__main__":
    ...
