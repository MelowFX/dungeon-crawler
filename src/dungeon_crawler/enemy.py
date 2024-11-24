"""
This module defines the Enemy class, a subclass of Character, representing adversaries
encountered by the hero during the game.
"""

from random import choice

import config
from action import AttackAction
from character import Character


def generate_goblin_name() -> str:
    """
    Generates a random goblin name.

    Returns:
        str: A randomly selected goblin name from the predefined list.
    """
    return choice(config.GOBLIN_NAMES)


class Enemy(Character):
    """
    Subclass of Character representing an enemy in the game.
    This class can be extended to add specific enemy behaviors.
    """

    def __init__(self, name: str, health: int, damage: int, icon: str) -> None:
        super().__init__(name=name, health=health, damage=damage, icon=icon)

        self.dodge_chance = 0
        self.actions = {
            "attack": AttackAction(),
        }


class Goblin(Enemy):
    """
    Subclass of Enemy representing a Goblin character in the game.
    """
    def __init__(self, name: str = generate_goblin_name(), health: int = config.GOBLIN_HEALTH,
                 damage: int = config.GOBLIN_DAMAGE, icon: str = config.GOBLIN_ICON) -> None:
        super().__init__(name=name, health=health, damage=damage, icon=icon)
