"""
This module defines the base `Item` class, along with the `Potion` subclass.
The `Item` class represents an object that can be added to a character's inventory.
The `Potion` subclass represents an item that can be used to heal the character.
"""

DEFAULT_NAME = "Item"
DEFAULT_DESCRIPTION = "Description"
DEFAULT_ICON = "📦"


class Item:
    """
    Base class for items in the game.

    Represents a generic item with a name, description, and icon. Items can be
    used by a character, though the exact behavior of `use` depends on the specific item.
    """
    def __init__(self, name: str = DEFAULT_NAME, description: str = DEFAULT_DESCRIPTION,
                 icon: str = DEFAULT_ICON) -> None:
        """
        Initializes an item with the given attributes.

        Args:
            name (str): The name of the item.
            description (str): The description of the item.
            icon (str): The icon representing the item.
        """
        self.name = name
        self.description = description
        self.icon = icon

    def use(self, user):
        """
        Use the item. This method should be overridden in subclasses to define
        specific behaviors when an item is used.

        Args:
            user: The character who is using the item.

        Returns:
            bool: Whether the item was used successfully.
        """

    def __str__(self):
        """
        Returns a string representation of the item, including its icon, name, and description.

        Returns:
            str: A string describing the item.
        """
        return f"{self.icon} {self.name}: {self.description}"


class Potion(Item):
    """
    A subclass of Item representing a potion that restores health.
    """
    def use(self, user):
        """
        Uses the potion to restore the user's health to full.

        Args:
            user: The character who is using the potion.

        Returns:
            bool: Always returns True to indicate the potion was used successfully.
        """
        user.set_health(user.get_max_health())
        print("🩵 Health fully restored")
        return True
