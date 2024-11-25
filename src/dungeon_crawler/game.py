"""
This module handles the game flow, including the hero's progression through the dungeon,
combat mechanics with enemies, and the various in-game events like using potions, battling
enemies, and handling the days of survival. The game is turn-based, and the hero must survive
while making strategic decisions each day.
"""

import sys
from random import choice, randint
from time import sleep
from util import clear, get_yes_no

import config
from enemy import Goblin
from player import Player
from item import Item, Potion
from combat import Combat


def get_start_message(hero: Player) -> str:
    """
    Gets a random start message for the hero.

    Args:
        hero (Player): The hero object.

    Returns:
        str: A randomly generated start message string.
    """
    message = choice(config.TEMPLATE_START)
    return message.format(name=hero.name)


class Game:
    """
    Main game class that handles the flow of the game, including starting the game,
    handling hero actions, and processing encounters.
    """

    def __init__(self) -> None:
        self.hero = Player()
        self.day = config.GAME_STARTING_DAY

    def reset(self) -> None:
        """
        Resets the game state for a new playthrough.
        """
        self.hero = Player()
        self.day = config.GAME_STARTING_DAY

    def pre_start_game(self) -> None:
        """
        Initializes the game by setting up the hero and displaying a start message.
        """
        print(config.GAME_NAME)

        self.hero = Player()
        self.hero.prompt_name()
        sleep(1 * config.GAME_SPEED)

        # Generate and display a random start message
        print(f"\n{get_start_message(self.hero)}")
        sleep(1 * config.GAME_SPEED)

        input("\n> [press \033[1mENTER\033[0m to start]")

    def start_game(self) -> None:
        """
        Runs the main game loop, handling daily events and progression.
        """
        clear()
        self.reset()
        self.pre_start_game()
        clear()

        # Game loop for each day
        while self.day < config.GAME_MAX_DAYS:
            self.day += 1

            sleep(0.5 * config.GAME_SPEED)
            print("============================")
            print(f"     ☀️ Day {self.day} begins...")
            print("============================")
            print(self.hero)

            self.prompt_potion()

            sleep(1.5 * config.GAME_SPEED)
            move_text = choice(config.TEMPLATE_MOVE)
            print("\n" + move_text)
            sleep(1.5 * config.GAME_SPEED)

            self.goblin_encounter()
            self.find_spellbook()
            self.learn_fireball()

            sleep(1 * config.GAME_SPEED)
            print("============================")
            print(f"      🌑 Day {self.day} ends...")
            print("============================")

            input("\n> [press \033[1mENTER\033[0m to continue...]")
            clear()

        # Game ends when terminal day is reached
        self.end_game()

    def prompt_potion(self):
        """
        Prompts the hero to use a SUPER-POTION to restore full health if available.

        Checks if the hero has a super-potion in their inventory and asks the user
        if they want to use it. If the user agrees, the potion is used to restore
        the hero's health.
        """
        if (self.hero.inventory.find_item("spotion") and
                get_yes_no("\n> ⚗️ Use a SUPER-POTION to restore full health? [Y/n] ")):
            item_spotion = self.hero.inventory.find_item("spotion")
            if item_spotion:
                self.hero.inventory.use_item(item_spotion, self.hero)

    def learn_fireball(self):
        """
        Allows the hero to learn the Fireball spell if they have a spellbook and enough experience.

        Checks if the hero has the spellbook and whether they have gained enough experience
        to learn the Fireball spell. If so, the Fireball spell is added to their inventory.
        """
        if (self.hero.inventory.find_item("spellbook")
                and not self.hero.inventory.find_item("fireball")
                and self.hero.experience >= config.FIREBALL_XP):
            item_fireball = Item(
                "fireball",
                {
                    "name": "Fireball",
                    "description": "A devastating burst of fiery magic",
                    "icon": "🔥"
                }
            )
            self.hero.inventory.add_item(item_fireball)

            print(f"🔥 \033[1m{self.hero.name}\033[0m learned the Fireball spell!")

    def find_spellbook(self):
        """
        Handles the event where the hero acquires a spellbook on a specific day.

        Checks if the current day matches the day when the spellbook should be found.
        If so, the spellbook is added to the hero's inventory.
        """
        if self.day == config.GAME_SPELLBOOK_DAY:
            item_spellbook = Item(
                "spellbook",
                {
                    "name": "Spellbook",
                    "description": "An ancient tome imbued with magical knowledge.",
                    "icon": "📔"
                }
            )
            self.hero.inventory.add_item(item_spellbook)

            print(f"📔 \033[1m{self.hero.name}\033[0m found a spellbook!")

    def show_end_screen(self, message: str) -> None:
        """
        Displays the end screen with a message and prompts the player to replay or quit.

        Args:
            message (str): The message to display on the end screen.
        """
        print(message)

        # Prompt to play again or quit
        play_again = input(
            "> [press \033[1mENTER\033[0m to play again, or type 'q' to quit]: "
        ).lower()

        if play_again == "q":
            print("Thanks for playing! Exiting...")
            sys.exit()
        else:
            self.start_game()

    def game_over(self) -> None:
        """
        Displays the game-over screen when the hero loses.
        """
        clear()

        message = f"💀 \033[1m{self.hero.name}\033[0m has died...\n"

        if self.day >= config.GAME_MAX_DAYS and self.hero.experience <= 0:
            message += f"\n...because they reached day {config.GAME_MAX_DAYS} with no experience.\n"

        self.show_end_screen(message)

    def end_game(self) -> None:
        """
        Displays the victory screen if the hero survives until the final day.
        """
        if self.hero.experience <= 0:
            self.game_over()
            return

        self.show_end_screen(f"🥳 \033[1m{self.hero.name}\033[0m survived!"
                             f"\nWith ✨ \033[1m{self.hero.experience} experience\033[0m\n")

    def goblin_encounter(self) -> None:
        """
        Handles a goblin encounter.

        Prompts the user to either fight a goblin or avoid the encounter.
        If the user chooses to fight, initiates a combat sequence.
        """
        enemy = Goblin()

        combat = Combat(self, self.hero, enemy)
        combat.prompt()

    def find_superpotion(self) -> None:
        """
        Handles the logic for finding a super-potion after battle.

        A super-potion is found based on a random chance. If found,
        it increases the hero's super-potion count and displays the result.
        This feature is only available if the hero has a spellbook.
        """
        if (self.hero.inventory.find_item("spellbook") and randint(1, 100) <=
                config.POTION_SUPER_FIND_CHANCE):
            # old_spotion = self.hero.superpotion

            item_spotion = Potion(
                "spotion",
                {
                    "name": "Super-potion",
                    "description": "Restores the hero's health completely when used.",
                    "icon": "⚗️"
                }
            )

            self.hero.inventory.add_item(item_spotion)
            # print(f"    ⚗️ \033[1m{self.hero.name}\033[0m found a SUPER-POTION! |",
            #       old_spotion, f"-> {self.hero.superpotion}")

    def find_potion(self) -> None:
        """
        Handles the logic for finding and optionally consuming a potion.

        A potion is found based on a random chance. The player is prompted to decide whether to
        consume the potion. The potion may have a positive or negative effect on the hero's
        health. If the hero possesses a spellbook, the potion effect is always positive.
        """
        if randint(1, 100) <= config.POTION_FIND_CHANCE:
            print(f"🧪 \033[1m{self.hero.name}\033[0m found a potion!")

            # Prompt to consume the potion
            if get_yes_no("    > Potion may be poisonous or healing. Consume it? [Y/n] "):
                potion_effect = randint(*config.POTION_EFFECT_RANGE)

                if self.hero.inventory.find_item("spellbook"):
                    potion_effect = abs(potion_effect)

                self.hero.health = self.hero.health + potion_effect

                print(f"\n{'😇' if potion_effect > 0 else '🤮'} {potion_effect:+} health")

                # If health is 0 or less - game over
                if not self.hero.alive():
                    self.game_over()
            else:
                print(f"\n\033[1m{self.hero.name}\033[0m decided not to drink the potion...")
