"""
This module defines the `Inventory` class, which manages a collection of items that a character
can carry. The class allows adding, removing, checking for, and using items, as well as displaying
the inventory contents.
"""

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
        self._items = []
        self.capacity = 5

    def __str__(self):
        """
        Returns a string representation of the inventory, listing all items.

        If the inventory is empty, it returns a message stating that the inventory is empty.

        Returns:
            str: The inventory's contents as a string.
        """
        return "🎒 Inventory:\n" + ("\n".join(
            f"    {str(item)}" for item in self._items) if self._items else "    Inventory is empty.")

    def add_item(self, item: Item):
        """
        Adds an item to the inventory.
        """
        if item.stackable:
            existing_item = self.find_item(item.uuid)
            if existing_item:
                existing_item.amount += item.amount
                return True

        if len(self._items) < self.capacity:
            self._items.append(item)
            return True

        return False

    def remove_item(self, item_uuid: str, amount: int = 1):
        """
        Removes an item from the inventory.
        """
        for item in self._items:
            if item.uuid == item_uuid:
                if item.stackable:
                    if item.amount <= amount:
                        item.on_remove()
                        self._items.remove(item)
                        return item

                    item.amount -= amount
                    return None
                else:
                    item.on_remove()
                    self._items.remove(item)
                    return item

        return None

    def find_item(self, item_uuid: str):
        """
        Finds a specific item in the inventory.

        Args:
            item_uuid: The item UUID to search for in the inventory.

        Returns:
            Item or None: The item if found, or None if not found.
        """
        for item in self._items:
            if item.uuid == item_uuid:
                return item

        return None

    def use_item(self, item: Item, user):
        """
        Uses an item from the inventory and removes it after use.

        Args:
            item: The item to be used.
            user: The character using the item.
        """
        if item.use(user):
            self._items.remove(item)
