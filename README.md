# `dungeon_crawler`
Python project for codesters.club

**Dungeon Crawler** is a text-based role-playing game (RPG) where players control a hero navigating a dungeon, battling enemies, collecting items, and leveling up with experience points. The game features turn-based combat and dynamic action sequences.

## Objective 🎯

The goal of the game is to defeat enemies, progress through dungeon levels, and grow your hero's power through experience points, magical items, and combat abilities. The hero can use items like potions to heal or acquire powerful magic such as the Fireball spell.

## Features ✨

1. **Turn-Based Combat** ⚔️: The player and enemy take turns to perform actions (e.g., attacking, using potions).
2. **Inventory System** 🎒: The player can collect and use items (potions, spellbooks) that provide various effects.
3. **Experience and Leveling** 📈: The player gains experience points (XP) from defeating enemies and can unlock new abilities.
4. **Random Events** 🎲: Random events like finding new items (spellbooks, super-potions) or encountering enemies.

## Installation ⚙️

To run **Dungeon Crawler** on your local machine, follow these steps:

### 1. Clone the repository:

```bash
git clone https://github.com/MelowFX/dungeon_crawler.git
```

### 2. Navigate to the project directory:

```bash
cd dungeon_crawler
```

### 3. Install dependencies:

Make sure you have Python 3.x installed. You can use a virtual environment or install dependencies globally.

```bash
pip install -r requirements.txt
```

### 4. Run the game:

```bash
python main.py
```

## Classes and Their Relationships 📚

### 1. **Character (Base Class)** 👤

- **Purpose**: Represents any character in the game (either a hero or an enemy).
- **Attributes**: 
    - `name`: Character’s name.
    - `health`, `health_max`: Health points and maximum health.
    - `damage`: Damage the character can deal.
    - `icon`: Visual representation of the character.
    - `flee_chance`, `crit_chance`: Chance of fleeing or landing critical hits.
    - `inventory`: An instance of the `Inventory` class to manage items.
    - `actions`: A dictionary of available actions for the character (e.g., attack, flee).
- **Methods**: 
    - `attack()`: Performs an attack on another character.
    - `perform_action()`: Executes a specific action from the `actions` dictionary.
    - `pre_damage()`: Checks any special behavior (e.g., dodging) before taking damage.
    - `alive()`: Checks if the character is still alive (health > 0).

The `Character` class serves as the base for both the `Hero` and `Enemy` classes.

---

### 2. **Hero (Subclass of Character)** 🦸‍♂️

- **Purpose**: Represents the player's character in the game.
- **Attributes**:
    - `xp`: Experience points earned by the hero.
    - `dodge_chance`: Chance of dodging attacks.
    - `actions`: A dictionary of actions (specific to the hero), such as attacking, using potions, and fleeing.
- **Methods**: 
    - `prompt_name()`: Prompts the user for a hero name.
    - `show_actions()`: Displays the available actions for the player to choose during combat.

The `Hero` class extends the `Character` class and adds unique attributes and abilities that make the hero distinct from enemies, such as the ability to gain experience and use magical abilities.

---

### 3. **Enemy (Subclass of Character)** 👹

- **Purpose**: Represents an enemy character in the dungeon.
- **Attributes**: Similar to the `Hero` class but without the experience, magic, or potion features.
- **Methods**: 
    - `perform_action()`: Executes an action for the enemy, such as attacking or fleeing.
    - `pre_damage()`: Checks if the enemy dodges or avoids taking damage.

The `Enemy` class is another subclass of `Character`, but it has fewer features than the `Hero` class. This makes sense as enemies typically do not use items or gain experience.

---

### 4. **Item** 📦

- **Purpose**: Represents an item in the game (could be potions, spellbooks, etc.).
- **Attributes**:
    - `uuid`: Unique identifier for the item.
    - `name`, `description`, `icon`: Basic properties describing the item.
    - `amount`: Number of times the item can be used.
- **Methods**: 
    - `use()`: Method to define what happens when the item is used (overridden by subclasses).
    - `on_remove()`: Placeholder method for when an item is removed from the inventory.
    - `__str__()`: Returns a string representation of the item.

Items can be added to the hero’s inventory and used during the game. Subclasses of `Item` (e.g., `Potion`) define the specific effects of the items.

---

### 5. **Potion (Subclass of Item)** ⚗️

- **Purpose**: A subclass of `Item` specifically for potions.
- **Methods**: 
    - `use()`: Restores the hero's health to full when used.

The `Potion` class extends the `Item` class and defines specific behavior for healing items.

---

### 6. **Inventory** 🎒

- **Purpose**: Manages a collection of items that a character (typically the hero) owns.
- **Methods**: 
    - `add_item()`: Adds an item to the inventory.
    - `find_item()`: Searches for a specific item by its UUID or name.
    - `use_item()`: Uses an item from the inventory.

The `Inventory` class helps manage the player's collection of items, providing the ability to add, find, and use items like potions or spellbooks.

---

### 7. **Actions (Attack, UsePotion, Flee)** 🏃‍♂️⚔️💉

- **Purpose**: Defines actions the characters can take during the game (attacks, using potions, and fleeing).
- **Attributes**: Each action class (e.g., `AttackAction`, `UsePotionAction`, `FleeAction`) defines the execution logic for its corresponding action.
- **Methods**: 
    - `perform()`: Defines how the action is executed (e.g., performing an attack, using a potion).

Actions are mapped in the `actions` attribute of both `Hero` and `Enemy` classes, allowing for easy execution of actions during combat.

---

## How These Classes Connect 🔗

- **`Character`**: The base class for all characters. Both the `Hero` and `Enemy` classes inherit from `Character`.
- **`Hero` and `Enemy`**: Specific types of characters, with the `Hero` class having more attributes like XP, magical abilities, and inventory management.
- **`Inventory`**: Managed by both `Hero` and `Enemy` to store items like potions or spellbooks.
- **`Item` and `Potion`**: Represent items that characters can use. Potions restore health, while other items may provide different effects.
- **`Action`**: Defines actions that characters can take during combat. These actions are stored in the `actions` attribute of both the `Hero` and `Enemy`.

---

## Contributing 🤝

If you'd like to contribute to **Dungeon Crawler**, feel free to fork the repository and submit a pull request with your improvements or bug fixes.

Please ensure that your contributions adhere to the project's coding standards and include adequate test coverage.

---

## License 📜
This project is licensed under the MIT License - see the LICENSE file for details.