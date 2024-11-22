"""
This module defines the `Inventory` class, which manages a collection of items that a character
can carry. The class allows adding, removing, checking for, and using items, as well as displaying
the inventory contents.
"""


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

    def add_item(self, item):
        """
        Adds an item to the inventory.

        Args:
            item: The item to be added to the inventory.
        """
        self.items.append(item)

    def remove_item(self, item):
        """
        Removes an item from the inventory.

        Args:
            item: The item to be removed from the inventory.
        """
        self.items.remove(item)

    def has_item(self, item) -> bool:
        """
        Checks if the inventory contains a specific item.

        Args:
            item: The item to check for in the inventory.

        Returns:
            bool: True if the item is in the inventory, False otherwise.
        """
        return item in self.items

    def find_item(self, target_item):
        """
        Finds a specific item in the inventory.

        Args:
            target_item: The item to search for in the inventory.

        Returns:
            Item or None: The item if found, or None if not found.
        """
        for item in self.items:
            if item == target_item:
                return item

        return None

    def use_item(self, item, user):
        """
        Uses an item from the inventory and removes it after use.

        Args:
            item: The item to be used.
            user: The character using the item.
        """
        if item.use(user):
            self.remove_item(item)

    def __str__(self):
        """
        Returns a string representation of the inventory, listing all items.

        If the inventory is empty, it returns a message stating that the inventory is empty.

        Returns:
            str: The inventory's contents as a string.
        """
        return "\n🎒 Inventory:\n" + ("\n".join(
            f"    {str(item)}" for item in self.items) if self.items else "    Inventory is empty.")
