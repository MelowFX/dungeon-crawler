"""
This module defines the base `Item` class, along with the `Potion` subclass.
The `Item` class represents an object that can be added to a character's inventory.
The `Potion` subclass represents an item that can be used to heal the character.
"""

DEFAULT_NAME = "Item"
DEFAULT_DESCRIPTION = "Description"
DEFAULT_ICON = "📦"
DEFAULT_AMOUNT = 1
DEFAULT_MAX_AMOUNT = 1


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

        self._uuid = uuid
        self._name = attributes.get("name", DEFAULT_NAME)
        self._description = attributes.get("description", DEFAULT_DESCRIPTION)
        self._icon = attributes.get("icon", DEFAULT_ICON)
        self._amount = attributes.get("amount", DEFAULT_AMOUNT)
        self._max_amount = attributes.get("max_amount", DEFAULT_MAX_AMOUNT)
        self._stackable = self._max_amount > 1 and True or False

    def __str__(self):
        """
        Returns a string representation of the item, including its icon, name, and description.

        Returns:
            str: A string describing the item.
        """
        return (f"{self.icon} {self.name} \033[1m({self.amount})\033[0m: {self.description} "
                f"\033[1m[{self.uuid}]\033[0m")

    @property
    def uuid(self):
        return self._uuid

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, description: str) -> None:
        self._description = description

    @property
    def icon(self) -> str:
        return self._icon

    @icon.setter
    def icon(self, icon: str) -> None:
        self._icon = icon

    @property
    def amount(self) -> int:
        return self._amount

    @amount.setter
    def amount(self, amount: int) -> None:
        self._amount = amount

    @property
    def max_amount(self) -> int:
        return self._max_amount

    @max_amount.setter
    def max_amount(self, max_amount: int) -> None:
        self._max_amount = max_amount

    @property
    def stackable(self) -> bool:
        return self._stackable

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

        if self.amount < 1:
            return True

        return False


class NonInteractableItem(Item):
    def use(self, user):
        print(self.icon, self.description)


class PotionItem(Item):
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
        user.health = user.health_max
        print("🩵 Health fully restored")

        return super().use(user)
