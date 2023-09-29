from Options import Toggle, Range, Choice, AssembleOptions
from typing import Dict

class SpecificKeys(Toggle):
    """Normal keys are specific to a dungeon. The key count for each dungeon may be found in extra pages in the pause menu. Turn off to make normal keys act like in vanilla. If off, you may need to buy keys from Zaegul."""
    display_name = "Specific Keys"

class ColorsRequired(Range):
    """Number of colors out of 5 needed to enter the Lighthouse."""
    display_name = "Colors Required"
    range_start = 0
    range_end = 5
    default = 5

class BlessingsRequired(Range):
    """Number of blessings out of 5 needed to access Enlightenment or to get the Hero's Rest ending."""
    display_name = "Blessings Required"
    range_start = 0
    range_end = 5
    default = 5

class CrestFragmentsRequired(Range):
    """Number of crest fragments out of 5 needed to get past the door in Castle Vann."""
    display_name = "Crest Fragments Required"
    range_start = 0
    range_end = 5
    default = 5

class CoinsOfCrowlRequired(Range):
    """Number of Coins of Crowl out of 13 needed to get past the underwater door."""
    display_name = "Coins of Crowl Required"
    range_start = 0
    range_end = 13
    default = 13

class Goal(Choice):
    """The goal of the game.
        var: Defeat Var.
        rest: Revive Torran.
        shadow: Defeat Shadow Oran.
        torran: Defeat Torran.
        any: Defeat any of the three."""
    display_name = "Goal"
    option_var = 0
    option_rest = 1
    option_shadow = 2
    option_torran = 3
    option_any = 4
    default = 0

class TradingQuest(Choice):
    """How to handle the trading quest.
        vanilla: The Lost Shipment and Ulni checks are randomized. The entire trading quest must be completed as in vanilla to get Ulni's check.
        skip: The Lost Shipment location and Anchor Greaves are randomized. The Lost Shipment itself is not randomized, and Ulni is not a check.
        shuffle: All items in the trading quest are randomized, and each of the corresponding NPCs is a check."""
    display_name = "Trading Quest"
    option_vanilla = 0
    option_skip = 1
    option_shuffle = 2
    default = 0

class ShuffleGrelinDrops(Toggle):
    """Grelin randomly drop four Archipelago items, and the Holy Relic, Wedding Ring, Silver Mirror, and Painting are added to the pool."""
    display_name = "Shuffle Grelin Drops"

class ShuffleHiddenItems(Toggle):
    """Include hidden overworld items in the pool."""
    display_name = "Shuffle Hidden Items"

class ShuffleBjergCastle(Toggle):
    """Include Bjerg Castle (Mariana's marriage dungeon) in the pool. A sailor near the arena will take you there."""
    display_name = "Shuffle Bjerg Castle"

class ShuffleDaemonsDive(Toggle):
    """Include Daemon's Dive in the pool."""
    display_name = "Shuffle Daemon's Dive"

class ShuffleEnlightenment(Toggle):
    """Include Enlightenment in the pool."""
    display_name = "Shuffle Enlightenment"

class ShuffleSecretShop(Toggle):
    """Include Zaegul's Secret Shop in the pool."""
    display_name = "Shuffle Secret Shop"

class LongJumpsInLogic(Toggle):
    """The seed may require two-tile jumps with the flare knuckle. (This setting does not affect Enlightenment which necessarily requires such jumps.)"""
    display_name = "Long Jumps In Logic"

class StartWithSpicedHam(Toggle):
    """Start with a buff that lets you run."""
    display_name = "Start With Spiced Ham"

class SkipOneSmallFavor(Toggle):
    """Tara gives you an item directly instead of requiring you to go on a fetch quest."""
    display_name = "Skip One Small Favor"

class FakeDreadHand(Toggle):
    """Allow using teleport statues without having the dread hand."""
    display_name = "Fake Dread Hand"

class FastFishing(Toggle):
    """Only 100 points are required in the fishing minigame to get the item from Keaton and to get free fish."""
    display_name = "Fast Fishing"

prodigal_options: Dict[str, AssembleOptions] = {
    "specific_keys": SpecificKeys,
    "colors_required": ColorsRequired,
    "blessings_required": BlessingsRequired,
    "crest_fragments_required": CrestFragmentsRequired,
    "coins_of_crowl_required": CoinsOfCrowlRequired,
    "goal": Goal,
    "trading_quest": TradingQuest,
    "shuffle_grelin_drops": ShuffleGrelinDrops,
    "shuffle_hidden_items": ShuffleHiddenItems,
    "shuffle_bjerg_castle": ShuffleBjergCastle,
    "shuffle_daemons_dive": ShuffleDaemonsDive,
    "shuffle_enlightenment": ShuffleEnlightenment,
    "shuffle_secret_shop": ShuffleSecretShop,
    "long_jumps_in_logic": LongJumpsInLogic,
    "start_with_spiced_ham": StartWithSpicedHam,
    "skip_one_small_favor": SkipOneSmallFavor,
    "fake_dread_hand": FakeDreadHand,
    "fast_fishing": FastFishing,
}