"""
Module that defines different actions that can be performed during combat.
"""

from enum import Enum, auto
from random import randint


class ActionResult(Enum):
    """Defines the possible results of an action execution."""
    NONE = auto()
    CONTINUE = auto()
    END = auto()


class Action:
    """Base class for all actions that can be performed in combat."""

    def can_perform(self):
        raise NotImplementedError()

    def perform(self, actor, *args, **kwargs) -> ActionResult:
        """Performs the action."""
        raise NotImplementedError()


class AttackAction(Action):
    """Action for attacking a target."""

    def perform(self, actor, *args, **kwargs) -> ActionResult:
        """Execute the attack action by attacking a target."""
        target = kwargs.get('target')  # Retrieve target from kwargs
        if actor and target:
            actor.attack(target)
            return ActionResult.CONTINUE

        print("❌ Attack failed: Invalid actor or target.")
        return ActionResult.NONE


class UsePotionAction(Action):
    """Action for using a potion."""

    def perform(self, actor, *args, **kwargs) -> ActionResult:
        """Execute the potion use action."""
        potion = actor.inventory.find_item("spotion")

        if potion and potion.use(actor):
            actor.inventory.remove_item(potion)
        else:
            print(f"❌ {actor.name} has no potions left!")

        return ActionResult.NONE


class FleeAction(Action):
    """Action for attempting to flee from combat."""

    def perform(self, actor, *args, **kwargs) -> ActionResult:
        """Execute the flee action, attempting to escape combat."""
        if randint(1, 100) <= actor.flee_chance:
            print(f"💨 \033[1m{actor.name}\033[0m fled the fight!")
            return ActionResult.END

        print(f"⚠️ \033[1m{actor.name}\033[0m failed to flee and must continue fighting!")
        return ActionResult.CONTINUE
