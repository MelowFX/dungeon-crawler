"""
This module contains all configuration constants and templates that drive the core mechanics,
visual design, and narrative elements of the dungeon crawler game.
"""

GAME_NAME = r"""
______                                      _____                    _
|  _  \                                    /  __ \                  | |
| | | |_   _ _ __   __ _  ___  ___  _ __   | /  \/_ __ __ ___      _| | ___ _ __
| | | | | | | '_ \ / _` |/ _ \/ _ \| '_ \  | |   | '__/ _` \ \ /\ / / |/ _ \ '__|
| |/ /| |_| | | | | (_| |  __/ (_) | | | | | \__/\ | | (_| |\ V  V /| |  __/ |
|___/  \__,_|_| |_|\__, |\___|\___/|_| |_|  \____/_|  \__,_| \_/\_/ |_|\___|_|
                    __/ |
                   |___/
"""

# Hero
HERO_XP_GAIN_RANGE = (15, 30)

# Game
GAME_SPEED = 0.5
GAME_MAX_DAYS = 10
GAME_STARTING_DAY = 0
GAME_SPELLBOOK_DAY = 2

# Potions
POTION_EFFECT_RANGE = (-20, 20)
POTION_FIND_CHANCE = 50
POTION_SUPER_FIND_CHANCE = 100

# Magic
FIREBALL_XP = 0

# Goblin
GOBLIN_NAMES = [
    "Grukk", "Zorg", "Ragdug", "Thrak", "Vog", "Krog", "Dorg",
    "Zarnok", "Brog", "Narg", "Wog", "Kruuk", "Grog", "Skrag",
    "Ruk", "Vrak", "Korr", "Lurt", "Snagg", "Gulth"
]
GOBLIN_ICON = "👺"
GOBLIN_HEALTH = 100
GOBLIN_DAMAGE = 15

# Story
TEMPLATE_START = [
    "🏰 \033[1m{name}\033[0m wakes up in the dark dungeon. The stench of goblins fills theair.",
    "🌑 \033[1m{name}\033[0m stretches their weary limbs, the dim light barely illuminating the "
    "cold stone walls.",
    "👂 \033[1m{name}\033[0m hears faint growls echoing in the distance. Another day of survival "
    "begins.",
    "💧 A drop of water echoes in the stillness as \033[1m{name}\033[0m rises to face the unknown.",
    "⚠️ The dungeon feels more oppressive today, and \033[1m{name}\033[0m can sense danger "
    "lurking nearby."
]

TEMPLATE_MOVE = [
    "🕯️ The dungeon is quiet, and your footsteps echo against the cold stone walls. You feel "
    "uneasy, but nothing stirs... yet.",
    "👣 Your footsteps grow louder in the silence. Shadows flicker along the walls as you move "
    "deeper into the dungeon.",
    "🕸️ A web of spider silk covers the path ahead. You push through, careful not to disturb "
    "anything...",
    "️🔈 The distant sound of claws scraping against stone sends a shiver down your spine... "
    "Someone or something is near.",
    "👻 A cold breeze sweeps through the corridor, carrying with it a faint, eerie whisper... You "
    "feel watched.",
    "⚔️ As you turn a corner, a pair of glowing eyes meet yours in the darkness. A figure steps "
    "forward — an enemy approaches!",
    "💀 The dungeon’s air grows heavier with each step. Suddenly, a guttural growl breaks the "
    "silence. A goblin leaps from the shadows!",
    "🦇 The sound of flapping wings fills the air. A swarm of bats flies overhead, but something "
    "more sinister lurks in the shadows."
]
