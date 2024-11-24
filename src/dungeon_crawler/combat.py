from enemy import Enemy
import config

from random import randint
from time import sleep
from action import ActionResult
from util import clear, get_yes_no
from player import Hero


class Combat:
    def __init__(self, game, hero: Hero, enemy: Enemy):
        self.game = game
        self.turn = 1
        self.hero = hero
        self.enemy = enemy

        print("\n============================")
        print("      ⚠️ ENEMY ALERT")
        print("============================")
        print(f"⚔️ \033[1m{hero.get_name()}\033[0m encounters:")
        print(enemy)

        if get_yes_no("\n> 🤺 Fight? [Y/n] "):
            self.fight()
        else:
            self.dont_fight()

    def fight(self) -> None:
        """
        Simulates a turn-based combat sequence between the hero and the enemy.
        """
        clear()

        old_health = self.hero.get_health()
        self.turn = 1

        while self.enemy.alive() and self.hero.alive():
            sleep(1 * config.GAME_SPEED)

            print(f"        🕰️ TURN: {self.turn}    ")
            print("============================")

            # Display current stats
            print(self.hero)
            print()
            print(self.enemy)
            print()

            # If hero flees, break the cycle
            if self.hero_turn() == ActionResult.END:
                return

            sleep(1.5 * config.GAME_SPEED)
            self.enemy_turn()

            sleep(0.5 * config.GAME_SPEED)
            if not self.enemy.alive():
                input("\n> [press \033[1mENTER\033[0m to finish the fight]")
            else:
                input("\n> [press \033[1mENTER\033[0m to continue your next turn...]")

            self.turn += 1
            clear()

        damage = old_health - self.hero.get_health()

        # Random experience gained from defeating enemy
        xp = randint(*config.HERO_XP_GAIN_RANGE)
        self.hero.add_experience(xp)

        print("\n============================")
        print("        🎉 VICTORY!         ")
        print("============================")
        print(f"⚔️ {self.enemy.get_name()} defeated!")
        print(f"    🩸 Damage taken: {damage}")
        print(f"    ✨ Experience gained: {xp}")

        # Random chance to find a super-potion after battle
        self.game.find_superpotion()

    def dont_fight(self) -> None:
        """
        Handles the scenario where the hero avoids fighting an enemy.
        """
        print(f"\n💨 \033[1m{self.hero.get_name()}\033[0m decided to avoid this fight...")

        # Random chance to find a potion
        self.game.find_potion()

    def hero_turn(self):
        """
        Handles the hero's turn in combat by prompting the player to choose an action.
        """
        print("============================")
        print("      ⚔️ HERO'S TURN        ")
        print("============================")
        self.hero.show_actions()

        while True:
            action = input("\n> Choose an action: ").strip()
            print()
            sleep(1 * config.GAME_SPEED)

            result = self.hero.perform_action(action, target=self.enemy)

            if result == ActionResult.NONE:
                continue

            return result

    def enemy_turn(self) -> None:
        """
        Handles the enemy's turn during combat, where the enemy attempts to attack the hero.
        """
        if self.enemy.alive():
            print("\n============================")
            print("      👺 ENEMY'S TURN       ")
            print("============================")

            self.enemy.perform_action("attack", target=self.hero)

            if not self.hero.alive():
                self.game.game_over()
