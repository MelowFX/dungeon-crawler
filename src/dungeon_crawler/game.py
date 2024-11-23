"""
This module handles the game flow, including the hero's progression through the dungeon,
combat mechanics with enemies, and the various in-game events like using potions, battling
enemies, and handling the days of survival. The game is turn-based, and the hero must survive
while making strategic decisions each day.
"""

import os
import sys
from random import choice, randint
from time import sleep

import config
from enemy import Enemy
from player import Hero
from item import Item, Potion


def clear() -> None:
    """
    Clears the terminal screen.

    Uses 'cls' command for Windows and 'clear' for other platforms.
    """
    os.system("cls" if os.name == "nt" else "clear")


def get_hero_name() -> str:
    """
    Prompts the user for a valid hero name.

    Returns:
        str: The hero's name entered by the user.
    """
    while True:
        hero_name = input("> Hero name: ")

        if not hero_name:
            print("\n❌ Please enter a valid hero name. The name cannot be empty.\n")
        else:
            return hero_name


def generate_goblin_name() -> str:
    """
    Generates a random goblin name.

    Returns:
        str: A randomly selected goblin name from the predefined list.
    """
    return choice(config.GOBLIN_NAMES)


def get_start_message(hero: Hero) -> str:
    """
    Gets a random start message for the hero.

    Args:
        hero (Hero): The hero object.

    Returns:
        str: A randomly generated start message string.
    """
    message = choice(config.TEMPLATE_START)
    return message.format(name=hero.name)


def get_yes_no(prompt: str) -> bool:
    """
    Prompts the user for a yes/no response.

    Args:
        prompt (str): The question or instruction to display to the user.

    Returns:
        bool: True if the user responds with 'Y' or presses ENTER, False otherwise.
    """
    while True:
        answer = input(prompt).lower()

        if answer in ("y", "n", ""):
            return answer in ("y", "")

        print("\n❌ Invalid choice. Please enter 'Y' or 'N'.")


def show_actions() -> None:
    """
       Displays the available actions to the player during combat.
    """
    print("🎭 \033[1mActions:\033[0m")
    print("    [1] Attack")
    print("    [2] Drink Super-Potion (restore full health)")
    print("    [3] Flee")


class Game:
    """
        Main game class that handles the flow of the game, including starting the game,
        handling hero actions, and processing encounters.
    """

    def __init__(self) -> None:
        self.hero = Hero()
        self.day = config.GAME_STARTING_DAY

    def reset(self) -> None:
        """
        Resets the game state for a new playthrough.
        """
        self.hero = Hero()
        self.day = config.GAME_STARTING_DAY

    def pre_start_game(self) -> None:
        """
        Initializes the game by setting up the hero and displaying a start message.
        """
        print(config.GAME_NAME)

        name = get_hero_name()
        self.hero = Hero(name=name)

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

            # If the hero has a super-potion, ask if they want to use it
            if (self.hero.inventory.find_item("spotion") and
                    get_yes_no("\n> ⚗️ Use a SUPER-POTION to restore full health? [Y/n] ")):
                item_spotion = self.hero.inventory.find_item("spotion")
                if item_spotion:
                    self.hero.inventory.use_item(item_spotion, self.hero)

            sleep(1.5 * config.GAME_SPEED)

            filler = choice(config.TEMPLATE_MOVE)
            print("\n" + filler)
            sleep(1.5 * config.GAME_SPEED)

            self.goblin_encounter()

            # Day X event: hero acquires a spellbook
            if self.day == config.GAME_SPELLBOOK_DAY:
                item_spellbook = Item("spellbook", "Spellbook", "An ancient tome imbued with "
                                                                "magical knowledge.", "📔")
                self.hero.inventory.add_item(item_spellbook)

                print(f"📔 \033[1m{self.hero.get_name()}\033[0m found a spellbook!")

            # If the hero has the spellbook and enough experience, they learn the Fireball spell
            if (self.hero.inventory.find_item("spellbook")
                    and not self.hero.inventory.find_item("fireball")
                    and self.hero.get_experience() >= config.FIREBALL_XP):
                item_fireball = Item("fireball", "Fireball", "A devastating burst of fiery magic.",
                                     "🔥")
                self.hero.inventory.add_item(item_fireball)

                print(f"🔥 \033[1m{self.hero.get_name()}\033[0m learned the Fireball spell!")

            sleep(1 * config.GAME_SPEED)
            print("============================")
            print(f"      🌑 Day {self.day} ends...")
            print("============================")

            input("\n> [press \033[1mENTER\033[0m to continue...]")
            clear()

        # Game ends when terminal day is reached
        self.end_game()

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

        message = f"💀 \033[1m{self.hero.get_name()}\033[0m has died...\n"

        if self.day >= config.GAME_MAX_DAYS and self.hero.get_experience() <= 0:
            message += f"\n...because they reached day {config.GAME_MAX_DAYS} with no experience.\n"

        self.show_end_screen(message)

    def end_game(self) -> None:
        """
        Displays the victory screen if the hero survives until the final day.
        """
        if self.hero.get_experience() <= 0:
            self.game_over()
            return

        self.show_end_screen(f"🥳 \033[1m{self.hero.get_name()}\033[0m survived!"
                             f"\nWith ✨ \033[1m{self.hero.get_experience()} experience\033[0m\n")

    def goblin_encounter(self) -> None:
        """
        Handles a goblin encounter.

        Prompts the user to either fight a goblin or avoid the encounter.
        If the user chooses to fight, initiates a combat sequence.
        """
        enemy_name = generate_goblin_name()
        enemy = Enemy(name=enemy_name, health=config.GOBLIN_HEALTH, damage=config.GOBLIN_DAMAGE,
                      icon=config.GOBLIN_ICON)

        print("\n============================")
        print("      ⚠️ ENEMY ALERT")
        print("============================")
        print(f"⚔️ \033[1m{self.hero.get_name()}\033[0m encounters:")
        print(enemy)

        # Prompt for a fight with a goblin
        if get_yes_no("\n> 🤺 Fight? [Y/n] "):
            self.fight(enemy)
        else:
            self.dont_fight()

    def dont_fight(self) -> None:
        """
        Handles the scenario where the hero avoids fighting an enemy.
        """
        print(f"\n💨 \033[1m{self.hero.get_name()}\033[0m decided to avoid this fight...")

        # Random chance to find a potion
        self.find_potion()

    def fight(self, enemy: Enemy) -> None:
        """
        Simulates a turn-based combat sequence between the hero and the enemy.

        Args:
            enemy (Enemy): The enemy character the hero is fighting.
        """
        clear()

        old_health = self.hero.get_health()
        turn = 1

        while enemy.alive() and self.hero.alive():
            sleep(1 * config.GAME_SPEED)

            # Player's turn
            print(f"        🕰️ TURN: {turn}    ")
            print("============================")

            # Display current stats
            print(self.hero)
            print()
            print(enemy)
            print()

            # If hero flees, break the cycle
            if self.hero_turn(enemy):
                return

            sleep(1.5 * config.GAME_SPEED)
            self.enemy_turn(enemy)

            sleep(0.5 * config.GAME_SPEED)
            if not enemy.alive():
                input("\n> [press \033[1mENTER\033[0m to finish the fight]")
            else:
                input("\n> [press \033[1mENTER\033[0m to continue your next turn...]")

            turn += 1
            clear()

        damage = old_health - self.hero.get_health()

        # Random experience gained from defeating enemy
        xp = randint(*config.HERO_XP_GAIN_RANGE)
        self.hero.add_experience(xp)

        print("\n============================")
        print("        🎉 VICTORY!         ")
        print("============================")
        print(f"⚔️ {enemy.get_name()} defeated!")
        print(f"    🩸 Damage taken: {damage}")
        print(f"    ✨ Experience gained: {xp}")

        # Random chance to find a super-potion after battle
        self.find_superpotion()

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

            item_spotion = Potion("spotion", "Super-potion", "Restores the hero's health "
                                                             "completely when used.","⚗️")

            self.hero.inventory.add_item(item_spotion)
            # print(f"    ⚗️ \033[1m{self.hero.get_name()}\033[0m found a SUPER-POTION! |",
            #       old_spotion, f"-> {self.hero.superpotion}")

    def find_potion(self) -> None:
        """
        Handles the logic for finding and optionally consuming a potion.

        A potion is found based on a random chance. The player is prompted to decide whether to
        consume the potion. The potion may have a positive or negative effect on the hero's
        health. If the hero possesses a spellbook, the potion effect is always positive.
        """
        if randint(1, 100) <= config.POTION_FIND_CHANCE:
            print(f"🧪 \033[1m{self.hero.get_name()}\033[0m found a potion!")

            # Prompt to consume the potion
            if get_yes_no("    > Potion may be poisonous or healing. Consume it? [Y/n] "):
                potion_effect = randint(*config.POTION_EFFECT_RANGE)

                if self.hero.inventory.find_item("spellbook"):
                    potion_effect = abs(potion_effect)

                self.hero.set_health(self.hero.get_health() + potion_effect)

                print(f"\n{'😇' if potion_effect > 0 else '🤮'} {potion_effect:+} health")

                # If health is 0 or less - game over
                if not self.hero.alive():
                    self.game_over()
            else:
                print(f"\n\033[1m{self.hero.get_name()}\033[0m decided not to drink the potion...")

    def hero_turn(self, enemy: Enemy) -> int:
        """
        Handles the hero's turn in combat by prompting the player to choose an action.

        Args:
            enemy (Enemy): The enemy the hero is currently facing.

        Returns:
            int: An integer indicating the next action:
                - 0: The hero attacks or fails to flee.
                - 1: The hero uses a super-potion or selects an invalid action.
                - 2: The hero successfully flees, ending the fight.
        """
        print("============================")
        print("      ⚔️ HERO'S TURN        ")
        print("============================")
        show_actions()

        while True:
            action = input("\n> Choose an action (1 / 2 / 3): ").strip()
            print()
            sleep(1 * config.GAME_SPEED)

            if action == "1":  # Attack
                self.hero.attack(enemy)

                return False

            if action == "2":  # Use super-potion
                item = self.hero.inventory.find_item("spotion")
                if item:
                    self.hero.inventory.use_item(item, self.hero)
                else:
                    print("❌ You have no Super-potions left!")
                print()

                continue

            if action == "3":  # Try to flee
                return self.hero.try_flee()

            print("❌ Invalid action. Please choose 1, 2, or 3.")

    def enemy_turn(self, enemy) -> None:
        """
            Handles the enemy's turn during combat, where the enemy attempts to attack the hero.

            Args:
                enemy (Enemy): The enemy character attacking the hero.
        """
        if enemy.alive():
            print("\n============================")
            print("      👺 ENEMY'S TURN       ")
            print("============================")

            enemy.attack(self.hero)

            if not self.hero.alive():
                self.game_over()
