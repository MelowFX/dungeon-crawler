"""
Utility functions for the game.
"""

import os


def clear() -> None:
    """
    Clears the terminal screen.

    Uses 'cls' command for Windows and 'clear' for other platforms.
    """
    os.system("cls" if os.name == "nt" else "clear")


def get_yes_no(prompt: str) -> bool:
    """
    Prompts the user for a yes/no response.

    Args:
        prompt (str): The question or instruction to display to the user.

    Returns:
        bool: True if the user responds with 'Y' or presses ENTER, False otherwise.
    """
    while True:
        answer = input(prompt).lower()

        if answer in ("y", "n", ""):
            return answer in ("y", "")

        print("\n❌ Invalid choice. Please enter 'Y' or 'N'.")
