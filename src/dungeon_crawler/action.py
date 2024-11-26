"""
Module that defines different actions that can be performed during combat.
"""

from enum import Enum, auto
from random import randint
from player import PlayerState


class ActionResult(Enum):
    """Defines the possible results of an action execution."""
    NONE = auto()
    CONTINUE = auto()
    END = auto()


class Action:
    """Base class for all actions that can be performed in combat."""

    def can_perform(self, actor):
        raise NotImplementedError()

    def perform(self, actor, *args, **kwargs) -> ActionResult:
        """Performs the action."""
        raise NotImplementedError()


class AttackAction(Action):
    """Action for attacking a target."""

    def can_perform(self, actor):
        return actor.state == PlayerState.IN_COMBAT

    def perform(self, actor, *args, **kwargs) -> ActionResult:
        """Execute the attack action by attacking a target."""
        target = kwargs.get('target')  # Retrieve target from kwargs
        if actor and target:
            actor.attack(target)
            return ActionResult.CONTINUE

        print("❌ Attack failed: Invalid actor or target.")
        return ActionResult.NONE


class FleeAction(Action):
    """Action for attempting to flee from combat."""

    def can_perform(self, actor):
        return actor.state == PlayerState.IN_COMBAT

    def perform(self, actor, *args, **kwargs) -> ActionResult:
        """Execute the flee action, attempting to escape combat."""
        if randint(1, 100) <= actor.flee_chance:
            print(f"💨 \033[1m{actor.name}\033[0m fled the fight!")
            return ActionResult.END

        print(f"⚠️ \033[1m{actor.name}\033[0m failed to flee and must continue fighting!")
        return ActionResult.CONTINUE


class UseItemAction(Action):
    """Action for using item."""

    def can_perform(self, actor):
        return True

    def perform(self, actor, *args, **kwargs) -> ActionResult:
        while True:
            print(actor.inventory)

            item_uuid = input("\n❔ Which item do you want to use? \033[1m('c' or 'continue' to "
                              "continue)\033[0m: ")
            if item_uuid.lower() in ("c", "continue"):
                break

            item = actor.inventory.find_item(item_uuid)
            if item:
                actor.inventory.use_item(item, actor)
                print()
                continue

            print(f"\n❌ \033[1m{actor.name}\033[0m doesnt have \033[1m{item_uuid}\033[0m!\n")

        return ActionResult.NONE


class ContinueAction(Action):
    """Action for skipping."""

    def can_perform(self, actor):
        return actor.state == PlayerState.IDLE

    def perform(self, actor, *args, **kwargs) -> ActionResult:
        print(f"👟 \033[1m{actor.name}\033[0m continues his adventure.")

        return ActionResult.END
