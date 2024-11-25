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

        self._name = name
        self._icon = icon

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

        new_health = target.health - damage
        target.health = new_health

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
            *args: Additional positional arguments to pass to the action's perform method.
            **kwargs: Additional keyword arguments to pass to the action's perform method.

        Returns: ActionResult: The result of executing the action.
        """
        action = self.actions.get(action_name)

        if action:
            return action.perform(self, *args, **kwargs)

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

    @property
    def name(self) -> str:
        """
        Gets the character's name.

        Returns:
            str: The name of the character.
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the character's name.

        Args:
            name (str): The name to assign to the character.
        """
        self._name = name

    @property
    def icon(self) -> str:
        """
        Gets the character's icon.

        Returns:
            str: The icon representing the character.
        """
        return self._icon

    @icon.setter
    def icon(self, icon: str) -> None:
        """
        Sets the character's icon.

        Args:
            icon (str): The icon to represent the character.
        """
        self._icon = icon

    @property
    def health(self) -> int:
        """
        Gets the character's current health.

        Returns:
            int: The current health of the character.
        """
        return self.stats['health']

    @health.setter
    def health(self, health: int) -> None:
        """
        Sets the character's current health.

        Ensures the health does not exceed the maximum health value.

        Args:
            health (int): The new health value.
        """
        self.stats['health'] = min(health, self.max_health)

    @property
    def max_health(self) -> int:
        """
        Gets the character's maximum health.

        Returns:
            int: The maximum health value.
        """
        return self.stats['health_max']

    @max_health.setter
    def max_health(self, max_health: int) -> None:
        """
        Sets the character's maximum health.

        Args:
            max_health (int): The new maximum health value.
        """
        self.stats['health_max'] = max_health
