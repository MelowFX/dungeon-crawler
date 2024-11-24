"""
This module defines the base `Item` class, along with the `Potion` subclass.
The `Item` class represents an object that can be added to a character's inventory.
The `Potion` subclass represents an item that can be used to heal the character.
"""

DEFAULT_NAME = "Item"
DEFAULT_DESCRIPTION = "Description"
DEFAULT_ICON = "📦"
DEFAULT_AMOUNT = 1


class Item:
    """
    Base class for items in the game.

    Represents a generic item with a name, description, and icon. Items can be
    used by a character, though the exact behavior of `use` depends on the specific item.
    """

    def __init__(self, uuid: str, attributes: dict = None) -> None:
        """
        Initializes an item with the given attributes.

        Args: uuid (str): Unique identifier for the item. attributes (dict): A dictionary
        containing item attributes like name, description, icon, and amount.
        """
        if attributes is None:
            attributes = {}

        self.uuid = uuid
        self.name = attributes.get("name", DEFAULT_NAME)
        self.description = attributes.get("description", DEFAULT_DESCRIPTION)
        self.icon = attributes.get("icon", DEFAULT_ICON)
        self.amount = attributes.get("amount", DEFAULT_AMOUNT)

    def get_name(self):
        """Returns the name of the item."""
        return self.name

    def get_description(self):
        """Returns the description of the item."""
        return self.description

    def get_icon(self):
        """Returns the icon representing the item."""
        return self.icon

    def get_amount(self):
        """Returns the current amount of the item."""
        return self.amount

    def on_remove(self):
        """Handles any behavior when the item is removed from the inventory."""

    def use(self, user):
        """
        Use the item. This method should be overridden in subclasses to define
        specific behaviors when an item is used.

        Args:
            user: The character who is using the item.

        Returns:
            bool: Whether the item was used successfully.
        """
        self.amount -= 1

    def __str__(self):
        """
        Returns a string representation of the item, including its icon, name, and description.

        Returns:
            str: A string describing the item.
        """
        return f"{self.icon} {self.name} ({self.amount}): {self.description}"


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
        super().use(user)

        user.set_health(user.get_max_health())
        print("🩵 Health fully restored")

        return True
