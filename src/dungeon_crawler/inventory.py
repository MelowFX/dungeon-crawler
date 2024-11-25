"""
This module defines the `Inventory` class, which manages a collection of items that a character
can carry. The class allows adding, removing, checking for, and using items, as well as displaying
the inventory contents.
"""

from character import Character
from item import Item


class Inventory:
    """
    Represents an inventory containing a list of items.

    This class provides methods to add, remove, and use items, as well as to check if an item
    exists in the inventory and display the current contents of the inventory.
    """

    def __init__(self):
        """
        Initializes an empty inventory.

        This method creates an empty list to store the items in the inventory.
        """
        self.items = []

    def __str__(self):
        """
        Returns a string representation of the inventory, listing all items.

        If the inventory is empty, it returns a message stating that the inventory is empty.

        Returns:
            str: The inventory's contents as a string.
        """
        return "\n🎒 Inventory:\n" + ("\n".join(
            f"    {str(item)}" for item in self.items) if self.items else "    Inventory is empty.")

    def add_item(self, item: Item):
        """
        Adds an item to the inventory.

        Args:
            item: The item to be added to the inventory.
        """
        self.items.append(item)

    def remove_item(self, item: Item):
        """
        Removes an item from the inventory.

        Args:
            item: The item to be removed from the inventory.
        """
        item.on_remove()
        self.items.remove(item)

    def find_item(self, uuid: str):
        """
        Finds a specific item in the inventory.

        Args:
            uuid: The item UUID to search for in the inventory.

        Returns:
            Item or None: The item if found, or None if not found.
        """
        for item in self.items:
            if item.uuid == uuid:
                return item

        return None

    def use_item(self, item: Item, user: Character):
        """
        Uses an item from the inventory and removes it after use.

        Args:
            item: The item to be used.
            user: The character using the item.
        """
        if item.use(user):
            self.remove_item(item)
