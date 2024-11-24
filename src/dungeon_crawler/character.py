"""
This module defines the base `Character` class, along with the `Hero` and `Enemy`
subclasses. The `Character` class handles basic attributes and actions for all characters,
while `Hero` adds specific functionality for the player character, and `Enemy` is used for
all enemy characters.
"""

from random import randint
from action import ActionResult, AttackAction, UsePotionAction, FleeAction

DEFAULT_NAME = "Unnamed"
DEFAULT_HEALTH = 100
DEFAULT_DAMAGE = 20
DEFAULT_ICON = "❌"


class Character:
    """
        Base class for all characters in the game (heroes and enemies).
        Handles basic attributes like health, damage, and actions like attack and fleeing.
    """

    def __init__(self, name: str = DEFAULT_NAME, health: int = DEFAULT_HEALTH,
                 damage: int = DEFAULT_DAMAGE,
                 icon: str = DEFAULT_ICON) -> None:
        """
        Initializes a character with the given attributes.

        Args:
            name (str): The name of the character.
            health (int): The health points of the character.
            damage (int): The damage the character can inflict.
            icon (str): The visual representation of the character.
        """

        self.name = name
        self.icon = icon

        self.stats = {
            "health": health,
            "health_max": health,
            "damage": damage,
        }

        self.inventory = None

        self.flee_chance = 25
        self.crit_chance = 50

        self.actions = {
            "attack": AttackAction(),
            "potion": UsePotionAction(),
            "flee": FleeAction(),
        }

    def __str__(self) -> str:
        """
        Prints the character's current health and name.
        """
        return (f"\033[1m{self.icon} {self.name}'s\033[0m status:\n"
                f"    ❤️ Health: {self.stats['health']} / {self.stats['health_max']}\n"
                f"    💥 Damage: {self.stats['damage']}")

    def attack(self, target: "Character") -> None:
        """
        Attacks a target, reducing their health by the character's damage.

        Args:
            target (Character): The target character being attacked.
        """
        damage = self.stats['damage']
        crit_text = ""

        if randint(1, 100) <= self.crit_chance:
            damage *= 1.5
            damage = round(damage)
            crit_text = "\033[1mCRIT!\033[0m "

        if target.pre_damage():
            return

        new_health = target.get_health() - damage
        target.set_health(new_health)

        print(f"🗡️ {crit_text}\033[1m{self.name}\033[0m attacked {target.icon} \033[1"
              f"m{target.name}\033[0m"
              f" for \033[1m{damage} damage!\033[0m")

    def perform_action(self, action_name: str, *args, **kwargs):
        """
        Executes the specified action for the character.

        This method looks up the action by its name and performs it, passing the character
        as the actor along with any additional arguments or keyword arguments.

        Args:
            action_name (str): The name of the action to perform (e.g., "attack", "flee").
            *args: Additional positional arguments to pass to the action's execute method.
            **kwargs: Additional keyword arguments to pass to the action's execute method.

        Returns: ActionResult: The result of executing the action.
        """
        action = self.actions.get(action_name)

        if action:
            return action.execute(self, *args, **kwargs)

        print("❌ Invalid action.")
        return ActionResult.NONE

    def pre_damage(self):
        """
        Checks if any special conditions or actions should occur before taking damage.

        This method can be overridden in subclasses to implement specific behavior,
        such as blocking or dodging, before damage is applied to the character.

        Returns:
            bool: Returns False by default, indicating no special pre-damage action is taken.
        """
        return False

    def alive(self) -> bool:
        """
        Checks if the character is dead (health <= 0).

        Returns:
            bool: True if the character is dead, False otherwise.
        """
        return self.stats['health'] > 0

    def get_name(self) -> str:
        """
        Retrieves the hero's name.

        Returns:
            str: The name of the hero.
        """
        return self.name

    def set_health(self, health: int) -> None:
        """
        Sets the character's health, ensuring it doesn't exceed the maximum.

        Args:
            health (int): The new health value to set.
        """
        self.stats['health'] = min(health, self.stats['health_max'])

    def get_health(self) -> int:
        """
        Returns the current health of the character.

        Returns:
            int: The character's health.
        """
        return self.stats['health']

    def get_max_health(self) -> int:
        """
        Returns the maximum health of the character.

        Returns:
            int: The character's maximum health.
        """
        return self.stats['health_max']
