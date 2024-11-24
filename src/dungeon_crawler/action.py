"""
Module that defines different actions that can be performed during combat.
"""

from enum import Enum
from random import randint


class ActionResult(Enum):
    """Defines the possible results of an action execution."""
    NONE = 1
    CONTINUE = 2
    END = 3


class Action:
    """Base class for all actions that can be performed in combat."""

    def execute(self, actor, *args, **kwargs):
        """Executes the action."""


class AttackAction(Action):
    """Action for attacking a target."""

    def execute(self, actor, *args, **kwargs):
        """Execute the attack action by attacking a target."""
        target = kwargs.get('target')  # Retrieve target from kwargs
        if actor and target:
            actor.attack(target)
            return ActionResult.CONTINUE

        print("❌ Attack failed: Invalid actor or target.")
        return ActionResult.NONE


class UsePotionAction(Action):
    """Action for using a potion."""

    def execute(self, actor, *args, **kwargs):
        """Execute the potion use action."""
        potion = actor.inventory.find_item("spotion")

        if potion and potion.use(actor):
            actor.inventory.remove_item(potion)
        else:
            print(f"❌ {actor.get_name()} has no potions left!")

        return ActionResult.NONE


class FleeAction(Action):
    """Action for attempting to flee from combat."""

    def execute(self, actor, *args, **kwargs):
        """Execute the flee action, attempting to escape combat."""
        if randint(1, 100) <= actor.flee_chance:
            print(f"💨 \033[1m{actor.get_name()}\033[0m fled the fight!")
            return ActionResult.END

        print(f"⚠️ \033[1m{actor.get_name()}\033[0m failed to flee and must continue fighting!")
        return ActionResult.CONTINUE
