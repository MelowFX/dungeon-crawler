"""
This module defines the Enemy class, a subclass of Character, representing adversaries
encountered by the hero during the game.
"""

from character import Character


class Enemy(Character):
    """
    Subclass of Character representing an enemy in the game.
    This class can be extended to add specific enemy behaviors.
    """

    def __init__(self, name: str, health: int, damage: int, icon: str) -> None:
        super().__init__(name=name, health=health, damage=damage, icon=icon)

        self.dodge_chance = 0


class Goblin(Enemy):
    """
    Subclass of Enemy representing a Goblin character in the game.
    """
    def __init__(self, name: str, health: int, damage: int, icon: str) -> None:
        super().__init__(name=name, health=health, damage=damage, icon=icon)
