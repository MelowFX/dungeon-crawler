"""
This module defines the Hero class, a specialized subclass of Character, which represents the
player's hero in the game. It adds unique attributes and abilities that differentiate the hero
from other characters, including experience points, super-potions, and magical abilities.
"""

from random import randint
from character import Character
from inventory import Inventory

DEFAULT_NAME = "Hero"
DEFAULT_ICON = "🧍"
DEFAULT_HEALTH = 100
DEFAULT_DAMAGE = 20


class Hero(Character):
    """
        Subclass of Character representing the player's hero.
        Adds experience points, super-potions, and magic abilities.
    """

    def __init__(self, name: str = DEFAULT_NAME, health: int = DEFAULT_HEALTH,
                 damage: int = DEFAULT_DAMAGE,
                 icon: str = DEFAULT_ICON) -> None:
        """
        Initializes a hero with the given attributes, plus experience, super-potions, and magic.

        Args:
            name (str): The name of the hero.
            health (int): The health points of the hero.
            damage (int): The damage the hero can inflict.
            icon (str): The visual representation of the hero.
        """
        super().__init__(name=name, health=health, damage=damage, icon=icon)

        self.xp = 0
        self.dodge_chance = 50
        self.superpotion = 0
        self.fireball = False
        self.spellbook = False

        self.inventory = Inventory()

    def __str__(self) -> str:
        """
        Prints the character's current health and name.
        """
        return super().__str__() + f"\n    ✨ Experience: {self.xp}\n" + str(self.inventory)

    def pre_damage(self):
        if randint(1, 100) >= self.dodge_chance:
            print(f"💨 \033[1m{self.get_name()}\033[0m swiftly dodged the attack!")

            return True

        return False

    def set_experience(self, xp: int) -> None:
        """
        Sets the hero's experience to a specified value.

        Args:
            xp (int): The new experience value to set.
        """
        self.xp = xp

    def add_experience(self, xp: int) -> None:
        """
        Increases the hero's experience by a specified amount.

        Args:
            xp (int): The amount of experience to add.
        """
        self.xp += xp

    def get_experience(self) -> int:
        """
        Retrieves the hero's current experience points.

        Returns:
            int: The current experience points of the hero.
        """
        return self.xp
