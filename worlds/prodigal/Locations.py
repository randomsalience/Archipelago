from BaseClasses import CollectionState
from enum import IntEnum
from typing import Callable, NamedTuple

class LocationData(NamedTuple):
    region: str
    name: str
    code: int
    access_rule: Callable[[CollectionState, int], bool]

base_location_data = [
    LocationData("Vann's Point", "Warehouse Freestanding", 183,
                 lambda state, player: True),
    LocationData("Vann's Point", "Pond Freestanding", 182,
                 lambda state, player: state.prodigal_can_hit(player) or state.has("Lariat", player)),
    LocationData("Vann's Point", "Island Freestanding", 181,
                 lambda state, player: state.has("Lariat", player)),
    LocationData("Vann's Point", "Mountain Freestanding", 180,
                 lambda state, player: (state.has("Progressive Knuckle", player) and state.has("Lariat", player)) or
                 (state.has("Climbing Gear", player) and state.prodigal_can_hit(player))),
    LocationData("Vann's Point", "Pa's Desk", 227,
                 lambda state, player: True),
    LocationData("Vann's Point", "Music Box", 228,
                 lambda state, player: state.has("Harmonica", player) and state.has("Climbing Gear", player)),
    LocationData("Vann's Point", "Drowned Gift", 88,
                 lambda state, player: state.prodigal_has_enough_coins(player) and
                 (state.has("Anchor Greaves", player) or state.has("Boots of Graile", player))),
    LocationData("Vann's Point", "Near Mine Heart Ore", 146,
                 lambda state, player: state.has("Progressive Pick", player) and state.has("Progressive Knuckle", player)),
    LocationData("Vann's Point", "Near Siska Heart Ore", 147,
                 lambda state, player: state.has("Progressive Pick", player) and state.has("Lariat", player)),
    LocationData("Vann's Point", "Near Smithy Heart Ore", 148,
                 lambda state, player: state.has("Progressive Pick", player) and state.has("Lariat", player)),
    LocationData("Vann's Point", "Near Pond Heart Ore", 145,
                 lambda state, player: state.has("Progressive Pick", player)),
    LocationData("Vann's Point", "Near Magma Heart Heart Ore", 144,
                 lambda state, player: state.has("Progressive_Pick", player) and
                 (state.has("Climbing Gear", player) or (state.has("Lariat", player) and state.has("Progressive Knuckle", player)))),
    LocationData("Vann's Point", "Tara Reward", 200,
                 lambda state, player: True),
    LocationData("Vann's Point", "Tess", 201,
                 lambda state, player: True),
    LocationData("Vann's Point", "Hackett", 202,
                 lambda state, player: state.prodigal_can_hit(player)),
    LocationData("Vann's Point", "Grant Stealth Mission", 203,
                 lambda state, player: state.has("Cursed Bones", player) and state.has("Cursed Pick", player)),
    LocationData("Vann's Point", "Mariana", 204,
                 lambda state, player: state.prodigal_can_hit(player)),
    LocationData("Vann's Point", "Keaton Fishing Gift", 205,
                 lambda state, player: state.has("Lariat", player)),
    LocationData("Vann's Point", "Xavier Blessing", 208,
                 lambda state, player: state.has("Cursed Bones", player) and state.has("Cursed Pick", player)),
    LocationData("Vann's Point", "Crocodile", 209,
                 lambda state, player: True),
    LocationData("Vann's Point", "Tess Boots", 210,
                 lambda state, player: state.count("Winged Boots", player) + state.count("Anchor Greaves", player) + \
                 state.count("Cleated Boots", player) + state.count("Lucky Boots", player) + \
                 state.count("Boots of Graile", player) >= 4 and state.has("Old Hairpin", player)),
    LocationData("Vann's Point", "Lynn Gift", 211,
                 lambda state, player: (state.has("Holy Relic", player) and state.has("Wedding Ring", player) and
                 state.has("Painting", player) and state.has("Silver Mirror", player))
                 if state.multiworld.shuffle_grelin_drops[player] else state.prodigal_can_kill_grelins(player)),
    LocationData("Vann's Point", "Bolivar", 212,
                 lambda state, player: state.has("Shaedrite", player) and state.has("Drowned Ore", player) and
                 state.has("Miasmic Extract", player) and state.has("Broken Sword", player)),
    LocationData("Vann's Point", "Hooded Figure", 213,
                 lambda state, player: state.has("Progressive Hand", 2) and
                 state.has("Eerie Mask", player) and state.has("Climbing Gear", player) and
                 state.prodigal_can_hit(player)),
    LocationData("Vann's Point", "Light Spirit", 237,
                 lambda state, player: state.prodigal_time_out_2_open(player) and
                 state.has("Progressive Knuckle", player) and state.has("Lariat", player) and
                 state.prodigal_has_key("Time Out", player, 3)),
    LocationData("Vann's Point", "Hero's Rest", None,
                 lambda state, player: state.prodigal_has_enough_blessings(player) and
                 state.has("Progressive Hand", player, 2) and state.prodigal_can_hit(player)),
    
    LocationData("Colorless Void", "Colorless Void Near Portal Heart Ore", 165,
                 lambda state, player: state.has("Progressive Pick", player)),
    LocationData("Colorless Void", "Colorless Void Near Burg Heart Ore", 166,
                 lambda state, player: state.has("Progressive Pick", player)),
    LocationData("Colorless Void", "Colorless Void Near Tavern Heart Ore", 167,
                 lambda state, player: state.has("Progressive Pick", player) and state.has("Lariat", player)),
    LocationData("Colorless Void", "Colorless Void Near Waterfall Heart Ore", 168,
                 lambda state, player: state.has("Progressive Pick", player)),
    
    LocationData("Abandoned Mine", "Abandoned Mine Iron Pick Chest", 2,
                 lambda state, player: True),
    LocationData("Abandoned Mine", "Abandoned Mine Lower Chest", 44,
                 lambda state, player: state.has("Lariat", player) and state.has("Progressive Knuckle", player)),
    
    LocationData("Waterfall Cave", "Waterfall Cave Item", 135,
                 lambda state, player: state.has("Progressive Pick", player) and state.has("Lariat", player)),
    
    LocationData("Celina's Mine", "Celina's Mine Item", 179,
                 lambda state, player: state.prodigal_can_hit(player)),
    
    LocationData("Cursed Grave", "Cursed Grave Top Chest", 49,
                 lambda state, player: state.prodigal_can_hit(player)),
    LocationData("Cursed Grave", "Cursed Grave Center Chest", 48,
                 lambda state, player: state.prodigal_can_hit(player)),
    LocationData("Cursed Grave", "Cursed Grave Bottom Chest", 47,
                 lambda state, player: state.prodigal_can_hit(player)),
    LocationData("Cursed Grave", "Cursed Grave Lariat Target Chest", 46,
                 lambda state, player: state.prodigal_can_hit(player) and
                 (state.has("Lariat", player) or state.has("Progressive Knuckle", player, 2))),
    LocationData("Cursed Grave", "Cursed Grave Biggun", 45,
                 lambda state, player: state.prodigal_can_hit(player) and
                 (state.has("Lariat", player) or state.has("Progressive Knuckle", player, 2))),
    
    LocationData("Boneyard", "Boneyard Left Hidden Chest", 7,
                 lambda state, player: state.prodigal_can_hit(player)),
    LocationData("Boneyard", "Boneyard Right Hidden Chest", 8,
                 lambda state, player: state.prodigal_can_hit(player)),
    LocationData("Boneyard", "Boneyard Bottom Hidden Chest", 6,
                 lambda state, player: state.prodigal_can_hit(player)),
    LocationData("Boneyard", "Boneyard Boss Key Chest", 9,
                 lambda state, player: state.has("Progressive Hand", player) and (state.has("Progressive Pick", player) or
                 (state.has("Lariat", player) and state.has("Progressive Knuckle", player)))),
    LocationData("Boneyard", "Boneyard Lariat Target Chest", 53,
                 lambda state, player: state.has("Progressive Hand", player) and (state.has("Lariat", player) or
                 (state.has("Progressive Pick", player) and state.prodigal_can_long_jump(player)))),
    LocationData("Boneyard", "Boneyard Ball Chest", 5,
                 lambda state, player: state.has("Progressive Knuckle", player) and (state.has("Lariat", player) or
                 state.has("Progressive Knuckle", player, 2) or state.has("Progressive Hand", player, 2))),
    LocationData("Boneyard", "Boneyard Roller Chest", 4,
                 lambda state, player: state.has("Progressive Hand", player) and (state.has("Progressive Pick", player) or
                 (state.has("Lariat", player) and state.has("Progressive Knuckle", player)))),
    LocationData("Boneyard", "Boneyard Dread Hand Chest", 1,
                 lambda state, player: state.prodigal_has_key("Boneyard", player, 1) and (state.has("Progressive Pick", player) or
                 (state.has("Lariat", player) and state.has("Progressive Knuckle", player)))),
    LocationData("Boneyard", "Boneyard Bats Chest", 3,
                 lambda state, player: state.has("Progressive Pick", player)),
    LocationData("Boneyard", "Boneyard Right Side Heart Ore", 163,
                 lambda state, player: state.has("Progressive Pick", player) and state.has("Progressive Knuckle", player)),
    LocationData("Boneyard", "Boneyard Near Boss Heart Ore", 164,
                 lambda state, player: state.has("Progressive Pick", player) and state.has("Progressive Hand", player)),
    LocationData("Boneyard", "Boneyard Vulture", 142,
                 lambda state, player: state.has("Boss Key", player) and
                 state.has("Progressive Pick", player) and state.has("Progressive Hand", player)),
    
    LocationData("Tidal Mines", "Tidal Mines Rocks Chest", 13,
                 lambda state, player: (state.has("Progressive Hand", player) or state.has("Lariat", player)) and (state.has("Progressive Pick", player) or
                 state.prodigal_can_long_jump(player) or (state.has("Progressive Knuckle", player, 2) and state.has("Lariat", player)))),
    LocationData("Tidal Mines", "Tidal Mines Lariat Chest", 15,
                 lambda state, player: (state.has("Progressive Hand", player) or state.has("Lariat", player)) and (state.has("Progressive Pick", player) or
                 state.prodigal_can_long_jump(player) or (state.has("Progressive Knuckle", player, 2) and state.has("Lariat", player))) and
                 (state.has("Lariat", player) or state.prodigal_has_key("Tidal Mines", player, 4))),
    LocationData("Tidal Mines", "Tidal Mines Left Hidden Chest", 12,
                 lambda state, player: (state.has("Progressive Hand", player) or state.has("Lariat", player)) and (state.has("Progressive Pick", player) or
                 state.prodigal_can_long_jump(player) or (state.has("Progressive Knuckle", player, 2) and state.has("Lariat", player))) and
                 (state.has("Lariat", player) or state.prodigal_can_long_jump(player))),
    LocationData("Tidal Mines", "Tidal Mines Right Hidden Chest", 11,
                 lambda state, player: (state.has("Progressive Hand", player) or state.has("Lariat", player)) and (state.has("Progressive Pick", player) or
                 state.prodigal_can_long_jump(player) or (state.has("Progressive Knuckle", player, 2) and state.has("Lariat", player))) and
                 (state.has("Lariat", player) or state.prodigal_can_long_jump(player))),
    LocationData("Tidal Mines", "Tidal Mines Near Boss Chest", 16,
                 lambda state, player: state.has("Lariat", player) and
                 (state.has("Progressive Pick", player) or state.has("Progressive Knuckle", player, 2))),
    LocationData("Tidal Mines", "Tidal Mines Barrel Cage Chest", 10,
                 lambda state, player: state.has("Lariat", player) and
                 (state.has("Progressive Pick", player) or state.has("Progressive Knuckle", player, 2))),
    LocationData("Tidal Mines", "Tidal Mines Islands Chest", 14,
                 lambda state, player: state.has("Lariat", player) and state.prodigal_has_key("Tidal Mines", player, 4) and
                 (state.has("Progressive Pick", player) or state.has("Progressive Knuckle", player, 2))),
    LocationData("Tidal Mines", "Tidal Mines Tidal Frog", 170,
                 lambda state, player: state.has("Lariat", player) and state.has("Progressive Pick", player)),
    LocationData("Tidal Mines", "Deep Tidal Mines Barrel Chest", 96,
                 lambda state, player: state.has("Progressive Hand", player, 2) and
                 (state.prodigal_can_long_jump(player) or (state.has("Lariat", player) and
                 state.has("Progressive Knuckle", player)))),
    LocationData("Tidal Mines", "Deep Tidal Mines Turtles Chest", 97,
                 lambda state, player: state.has("Progressive Hand", player, 2) and
                 state.has("Lariat", player) and state.has("Progressive Pick", player) and
                 state.has("Progressive Knuckle", player, 2) and state.prodigal_has_key("Tidal Mines", player, 3)),
    LocationData("Tidal Mines", "Deep Tidal Mines Water Blessing", 230,
                 lambda state, player: state.has("Progressive Hand", player, 2) and
                 state.has("Lariat", player) and state.has("Progressive Pick", player) and
                 state.has("Progressive Knuckle", player, 2) and state.prodigal_has_key("Tidal Mines", player, 4)),
    LocationData("Tidal Mines", "Tidal Mines Barrel Puzzle Heart Ore", 151,
                 lambda state, player: state.has("Lariat", player) and state.has("Progressive Pick", player)),
    LocationData("Tidal Mines", "Tidal Mines Islands Heart Ore", 152,
                 lambda state, player: state.has("Lariat", player) and state.has("Progressive Pick", player) and
                 state.prodigal_has_key("Tidal Mines", player, 4)),
    
    LocationData("Dry Fountain", "Dry Fountain Rust Knuckle Chest", 20,
                 lambda state, player: state.prodigal_can_hit(player) and
                 (state.has("Lariat", player) or state.prodigal_can_long_jump(player))),
    LocationData("Dry Fountain", "Dry Fountain Central Room Chest", 21,
                 lambda state, player: (state.has("Lariat", player) and state.has("Progressive Knuckle", player)) or
                 state.prodigal_can_long_jump(player)),
    LocationData("Dry Fountain", "Dry Fountain Barrel Bridge Chest", 19,
                 lambda state, player: state.has("Progressive Pick", player) and state.has("Lariat", player) and
                 state.has("Progressive Knuckle", player) and state.has("Progressive Hand", player)),
    LocationData("Dry Fountain", "Dry Fountain Left Hidden Chest", 17,
                 lambda state, player: state.has("Progressive Pick", player) and state.has("Lariat", player) and state.has("Progressive Knuckle", player)),
    LocationData("Dry Fountain", "Dry Fountain Center Hidden Chest", 69,
                 lambda state, player: state.has("Progressive Pick", player) and state.has("Lariat", player) and state.has("Progressive Knuckle", player)),
    LocationData("Dry Fountain", "Dry Fountain Right Hidden Chest", 18,
                 lambda state, player: state.has("Progressive Pick", player) and state.has("Lariat", player) and state.has("Progressive Knuckle", player)),
    LocationData("Dry Fountain", "Dry Fountain Rat Potion", 63,
                 lambda state, player: state.has("Progressive Pick", player) and state.has("Lariat", player) and
                 state.has("Progressive Knuckle", player) and state.has("Progressive Hand", player)),
    LocationData("Dry Fountain", "Dry Fountain Left Side Heart Ore", 160,
                 lambda state, player: state.has("Progressive Pick", player) and state.has("Lariat", player) and
                 state.has("Progressive Knuckle", player) and state.has("Progressive Hand", player)),
    LocationData("Dry Fountain", "Dry Fountain Right Side Heart Ore", 159,
                 lambda state, player: state.has("Progressive Pick", player) and state.has("Lariat", player) and
                 state.has("Progressive Knuckle", player) and state.has("Progressive Hand", player)),
    
    LocationData("Crocasino", "Crocasino Gator Key", 232,
                 lambda state, player: state.has("Lariat", player) or state.prodigal_can_long_jump(player)),
    LocationData("Crocasino", "Crocasino Jail Chest", 50,
                 lambda state, player: state.has("Bunny Key", player) and
                 (state.has("Lariat", player) or state.has("Progressive Knuckle", player, 2)) and
                 (state.has("Gator Key", player) or (state.has("Progressive Knuckle", player) and
                 (state.has("Lariat", player) or state.prodigal_can_long_jump(player))))),
    LocationData("Crocasino", "Crocasino Hidden Chest", 68,
                 lambda state, player: (state.has("Lariat", player) or state.has("Progressive Knuckle", player, 2)) and
                 ((state.has("Gator Key", player) and state.has("Progressive Pick", player)) or (state.has("Progressive Knuckle", player) and
                 (state.has("Lariat", player) or state.prodigal_can_long_jump(player))))),
    LocationData("Crocasino", "Crocasino Turtle Chest", 22,
                 lambda state, player: state.has("Lariat", player) and state.has("Progressive Knuckle", player)),
    LocationData("Crocasino", "Crocasino Block Push Chest", 23,
                 lambda state, player: state.has("Lariat", player) and state.has("Progressive Knuckle", player) and
                 state.prodigal_has_key("Crocasino", player, 1)),
    LocationData("Crocasino", "Crocasino Wren", 62,
                 lambda state, player: state.has("Lariat", player) and state.has("Progressive Knuckle", player) and
                 state.prodigal_has_key("Crocasino", player, 2) and state.has("Bunny Key", player)),
    LocationData("Crocasino", "Crocasino Heart Ore", 161,
                 lambda state, player: state.has("Lariat", player) and state.has("Progressive Knuckle", player) and
                 state.prodigal_has_key("Crocasino", player, 2) and state.has("Progressive Pick", player)),
    
    LocationData("Howling Bjerg", "Howling Bjerg Hidden Chest", 70,
                 lambda state, player: state.has("Lariat", player) and state.has("Progressive Knuckle", player)),
    LocationData("Howling Bjerg", "Howling Bjerg Ball Chest", 24,
                 lambda state, player: state.has("Lariat", player) and state.has("Progressive Knuckle", player)),
    LocationData("Howling Bjerg", "Howling Bjerg Ice Chest", 25,
                 lambda state, player: state.has("Lariat", player) and state.has("Progressive Knuckle", player)),
    LocationData("Howling Bjerg", "Howling Bjerg Yhote", 233,
                 lambda state, player: state.has("Lariat", player) and state.has("Progressive Knuckle", player) and
                 state.prodigal_has_key("Howling Bjerg", player, 1)),
    LocationData("Howling Bjerg", "Howling Bjerg Outside Heart Ore", 157,
                 lambda state, player: state.has("Progressive Pick", player) and
                 state.has("Progressive Knuckle", player) and state.has("Lariat", player)),
    LocationData("Howling Bjerg", "Howling Bjerg Inside Heart Ore", 158,
                 lambda state, player: state.has("Progressive Pick", player) and
                 state.has("Progressive Knuckle", player) and state.has("Lariat", player)),
    
    LocationData("Castle Vann", "Castle Vann Main Room Center Chest", 52,
                 lambda state, player: True),
    LocationData("Castle Vann", "Castle Vann Main Room Upper Right Chest", 30,
                 lambda state, player: state.has("Lariat", player) and
                 state.prodigal_can_hit(player) and state.prodigal_has_key("Castle Vann", player, 4)),
    LocationData("Castle Vann", "Castle Vann Main Room Left Chest", 31,
                 lambda state, player: state.has("Lariat", player) and
                 state.prodigal_can_hit(player) and state.prodigal_has_key("Castle Vann", player, 4)),
    LocationData("Castle Vann", "Castle Vann Main Room Lower Right Chest", 32,
                 lambda state, player: state.has("Progressive Knuckle", player, 2) or state.has("Lariat", player)),
    LocationData("Castle Vann", "Castle Vann Ball Puzzle Chest", 51,
                 lambda state, player: state.has("Progressive Knuckle", player) and
                 (state.has("Lariat", player) or state.prodigal_can_long_jump(player))),
    LocationData("Castle Vann", "Castle Vann After Ball Puzzle Chest", 34,
                 lambda state, player: state.has("Progressive Knuckle", player) and
                 (state.has("Lariat", player) or state.prodigal_can_long_jump(player))),
    LocationData("Castle Vann", "Castle Vann Turtle Chest", 29,
                 lambda state, player: state.prodigal_can_long_jump(player) or
                 (state.has("Progressive Pick", player) and state.prodigal_has_key("Castle Vann", player, 4))),
    LocationData("Castle Vann", "Castle Vann Black Hole Chest", 35,
                 lambda state, player: state.prodigal_can_long_jump(player) or
                 (state.has("Progressive Knuckle", player) and state.has("Lariat", player) and
                 state.prodigal_has_key("Castle Vann", player, 4))),
    LocationData("Castle Vann", "Castle Vann Floor Switches Chest", 33,
                 lambda state, player: state.has("Lariat", player) and
                 state.prodigal_can_hit(player) and state.prodigal_has_key("Castle Vann", player, 4)),
    LocationData("Castle Vann", "Castle Vann Hidden Chest", 87,
                 lambda state, player: state.prodigal_has_crest(player) and state.prodigal_can_hit(player)),
    LocationData("Castle Vann", "Castle Vann Spirit of Vann", 234,
                 lambda state, player: state.prodigal_has_crest(player) and
                 (state.has("Lariat", player) or state.prodigal_can_long_jump(player)) and
                 state.prodigal_can_hit(player)),
    LocationData("Castle Vann", "Castle Basement Crumbling Floor Chest", 94,
                 lambda state, player: state.prodigal_has_crest(player) and state.has("Dusty Key", player) and
                 (state.has("Lariat", player) or state.has("Progressive Knuckle", player, 2))),
    LocationData("Castle Vann", "Castle Basement Puzzle Chest", 95,
                 lambda state, player: state.prodigal_has_crest(player) and state.has("Dusty Key", player) and
                 state.has("Lariat", player) and state.has("Progressive Pick", player) and
                 state.prodigal_has_key("Castle Vann", player, 3)),
    LocationData("Castle Vann", "Castle Basement Ram Wraith", 171,
                 lambda state, player: state.prodigal_has_crest(player) and state.has("Dusty Key", player) and
                 state.has("Progressive Pick", player) and state.prodigal_has_key("Castle Vann", player, 4)),
    LocationData("Castle Vann", "Castle Vann Entry Heart Ore", 154,
                 lambda state, player: state.has("Progressive Pick", player)),
    LocationData("Castle Vann", "Castle Vann Block Push Heart Ore", 153,
                 lambda state, player: state.has("Lariat", player) and
                 state.has("Progressive Pick", player) and state.prodigal_has_key("Castle Vann", player, 4)),
    
    LocationData("Magma Heart", "Magma Heart Hidden Chest", 71,
                 lambda state, player: state.prodigal_can_hit_fire(player)),
    LocationData("Magma Heart", "Magma Heart Main Room Left Chest", 27,
                 lambda state, player: state.prodigal_can_hit_fire(player) and state.has("Progressive Knuckle", player)),
    LocationData("Magma Heart", "Magma Heart Main Room Right Chest", 26,
                 lambda state, player: state.prodigal_can_hit_fire(player) and state.has("Progressive Knuckle", player)),
    LocationData("Magma Heart", "Magma Heart Near Boss Chest", 28,
                 lambda state, player: state.prodigal_can_hit_fire(player) and state.has("Progressive Knuckle", player) and
                 (state.has("Lariat", player) or state.prodigal_can_long_jump(player))),
    LocationData("Magma Heart", "Magma Heart Loomagnos", 169,
                 lambda state, player: state.prodigal_can_hit_fire(player) and state.has("Progressive Knuckle", player) and
                 (state.has("Lariat", player) or state.prodigal_can_long_jump(player))),
    LocationData("Magma Heart", "Deep Magma Heart Spike Balls Chest", 91,
                 lambda state, player: state.has("Progressive Hand", player, 2) and
                 ((state.has("Progressive Knuckle", player) and state.has("Lariat", player)) or
                 state.has("Progressive Knuckle", player, 2)) and state.prodigal_can_hit_fire(player)),
    LocationData("Magma Heart", "Deep Magma Heart Barrel Puzzle Chest", 92,
                 lambda state, player: state.has("Progressive Hand", player, 2) and
                 state.prodigal_can_hit_fire(player) and state.has("Lariat", player) and
                 state.prodigal_has_key("Magma Heart", player, 1)),
    LocationData("Magma Heart", "Deep Magma Heart Earth Blessing", 235,
                 lambda state, player: state.has("Progressive Hand", player, 2) and
                 (state.has("Lariat", player) or state.prodigal_can_long_jump(player)) and
                 state.has("Progressive Pick", player) and state.prodigal_has_key("Magma Heart", player, 2)),
    LocationData("Magma Heart", "Magma Heart Main Room Heart Ore", 155,
                 lambda state, player: state.has("Progressive Pick", player) and state.has("Progressive Knuckle", player)),
    LocationData("Magma Heart", "Magma Heart Near Boss Heart Ore", 156,
                 lambda state, player: state.has("Progressive Pick", player) and
                 state.has("Progressive Knuckle", player) and
                 (state.has("Lariat", player) or state.prodigal_can_long_jump(player))),
    
    LocationData("Time Out", "Time Out 1 First Chest", 37,
                 lambda state, player: state.prodigal_time_out_1_open(player) and
                 state.prodigal_can_hit(player)),
    LocationData("Time Out", "Time Out 1 Left Hidden Chest", 38,
                 lambda state, player: state.prodigal_time_out_1_open(player) and
                 state.has("Progressive Pick", player) and state.has("Lariat", player) and
                 state.has("Progressive Knuckle", player)),
    LocationData("Time Out", "Time Out 1 Right Hidden Chest", 39,
                 lambda state, player: state.prodigal_time_out_1_open(player) and
                 state.has("Progressive Pick", player) and state.has("Lariat", player) and
                 state.has("Progressive Knuckle", player)),
    LocationData("Time Out", "Time Out 1 Underground Chest", 36,
                 lambda state, player: state.prodigal_time_out_1_open(player) and
                 state.has("Progressive Pick", player) and state.has("Lariat", player) and
                 state.has("Progressive Knuckle", player)),
    LocationData("Time Out", "Time Out 1 Invisible Item", 123,
                 lambda state, player: state.prodigal_time_out_1_open(player) and
                 state.has("Progressive Pick", player) and state.has("Lariat", player) and
                 state.has("Progressive Knuckle", player, 2)),
    LocationData("Time Out", "Time Out 1 Near Boss Chest", 41,
                 lambda state, player: state.prodigal_time_out_1_open(player) and
                 state.has("Progressive Pick", player) and state.has("Lariat", player) and
                 state.has("Progressive Knuckle", player) and state.prodigal_has_key("Time Out", player, 3)),
    LocationData("Time Out", "Time Out 1 Pits Heart Ore", 150,
                 lambda state, player: state.prodigal_time_out_1_open(player) and
                 state.has("Progressive Pick", player) and state.has("Lariat", player) and
                 state.has("Progressive Knuckle", player)),
    LocationData("Time Out", "Time Out 1 Blocks Heart Ore", 149,
                 lambda state, player: state.prodigal_time_out_1_open(player) and
                 state.has("Progressive Pick", player) and state.has("Lariat", player) and
                 state.has("Progressive Knuckle", player)),
    LocationData("Time Out", "Time Out 2 Ball Push Chest", 40,
                 lambda state, player: state.prodigal_time_out_2_open(player) and
                 ((state.has("Lariat", player) and state.has("Progressive Knuckle", player)) or
                 state.prodigal_can_long_jump(player))),
    LocationData("Time Out", "Time Out 2 Invisible Floor Chest", 93,
                 lambda state, player: state.prodigal_time_out_2_open(player) and
                 state.has("Progressive Knuckle", player) and (state.prodigal_has_key("Time Out", player, 2) or
                 state.has("Progressive Knuckle", player, 2))),
    LocationData("Time Out", "Color Correction", 236,
                 lambda state, player: state.prodigal_time_out_1_open(player) and
                 state.has("Progressive Pick", player) and state.has("Lariat", player) and
                 state.has("Progressive Knuckle", player) and state.prodigal_has_key("Time Out", player, 3)),
    LocationData("Time Out", "Colorgrave Gift", 224,
                 lambda state, player: state.has("Shattered Soul", player) and
                 state.has("Fury Heart", player) and state.has("Frozen Heart", player) and
                 state.has("Red Crystal", player) and state.has("Sunset Painting", player)),
    
    LocationData("Crystal Caves", "Crystal Caves Three Barrels Chest", 110,
                 lambda state, player: (state.has("Progressive Knuckle", player, 2) or state.has("Lariat", player)) and
                 (state.prodigal_can_long_jump(player) or (state.has("Progressive Pick", player) and
                 (state.has("Lariat", player) or state.prodigal_has_cleats(player))))),
    LocationData("Crystal Caves", "Crystal Caves Right Side Across Ice Chest", 136,
                 lambda state, player: (state.has("Progressive Knuckle", player, 2) or state.has("Lariat", player)) and
                 (state.prodigal_can_long_jump(player) or state.has("Lariat", player) or
                 state.prodigal_has_cleats(player)) and state.has("Progressive Pick", player)),
    LocationData("Crystal Caves", "Crystal Caves Center Room Chest", 111,
                 lambda state, player: (state.has("Progressive Knuckle", player, 2) or state.has("Lariat", player)) and
                 (state.prodigal_can_long_jump(player) or (state.has("Progressive Pick", player) and
                 (state.has("Lariat", player) or state.prodigal_has_cleats(player)))) and
                 (state.prodigal_has_cleats(player) or (state.has("Progressive Pick", player) and
                 state.has("Progressive Hand", player) and state.has("Lariat", player))) and
                 state.has("Progressive Knuckle", player) and state.prodigal_has_key("Crystal Caves", player, 2)),
    LocationData("Crystal Caves", "Crystal Caves Trapped Chest", 109,
                 lambda state, player: (state.has("Progressive Knuckle", player, 2) or state.has("Lariat", player)) and
                 (state.prodigal_can_long_jump(player) or (state.has("Progressive Pick", player) and
                 (state.has("Lariat", player) or state.prodigal_has_cleats(player)))) and
                 state.has("Progressive Knuckle", player) and state.prodigal_has_key("Crystal Caves", player, 2)),
    LocationData("Crystal Caves", "Crystal Caves Yhortes Chest", 113,
                 lambda state, player: state.has("Progressive Knuckle", player, 2) and
                 (state.prodigal_can_long_jump(player) or (state.has("Progressive Pick", player) and
                 (state.has("Lariat", player) or state.prodigal_has_cleats(player)))) and
                 state.prodigal_has_key("Crystal Caves", player, 2)),
    LocationData("Crystal Caves", "Crystal Caves Rock Cross Chest", 115,
                 lambda state, player: state.has("Progressive Knuckle", player, 2) and
                 (state.prodigal_can_long_jump(player) or state.has("Progressive Pick", player)) and
                 state.has("Lariat", player) and state.prodigal_has_key("Crystal Caves", player, 2)),
    LocationData("Crystal Caves", "Crystal Caves Two Chest Room Left Chest", 112,
                 lambda state, player: state.has("Progressive Knuckle", player, 2) and
                 (state.prodigal_can_long_jump(player) or state.has("Progressive Pick", player)) and
                 (state.has("Lariat", player) or state.prodigal_has_cleats(player)) and
                 state.prodigal_has_key("Crystal Caves", player, 2)),
    LocationData("Crystal Caves", "Crystal Caves Two Chest Room Right Chest", 114,
                 lambda state, player: state.has("Progressive Knuckle", player, 2) and
                 (state.prodigal_can_long_jump(player) or (state.has("Progressive Pick", player) and
                 (state.has("Lariat", player) or state.prodigal_has_cleats(player)))) and
                 state.prodigal_has_key("Crystal Caves", player, 2)),
    LocationData("Crystal Caves", "Crystal Caves Stindle", 238,
                 lambda state, player: state.has("Progressive Knuckle", player, 2) and
                 (state.has("Lariat", player) or state.prodigal_has_cleats(player)) and
                 state.has("Progressive Pick", player) and state.prodigal_has_key("Crystal Caves", player, 3)),
    LocationData("Crystal Caves", "Crystal Caves Lariat Target Chest", 116,
                 lambda state, player: state.has("Progressive Knuckle", player, 2) and
                 state.has("Progressive Pick", player) and (state.has("Lariat", player) or
                 state.prodigal_can_long_jump(player))),
    LocationData("Crystal Caves", "Crystal Caves Barrel Bridge Chest", 118,
                 lambda state, player: state.has("Progressive Knuckle", player, 2) and
                 state.has("Progressive Pick", player) and (state.has("Lariat", player) or
                 state.prodigal_has_cleats(player))),
    LocationData("Crystal Caves", "Crystal Caves Left Side Across Ice Chest", 117,
                 lambda state, player: state.has("Progressive Knuckle", player, 2) and
                 state.has("Progressive Pick", player)),
    LocationData("Crystal Caves", "Crystal Caves Behind Rocks Chest", 120,
                 lambda state, player: state.has("Progressive Knuckle", player, 2) and
                 state.has("Progressive Pick", player)),
    LocationData("Crystal Caves", "Crystal Caves Rock Puzzle Chest", 119,
                 lambda state, player: state.has("Progressive Knuckle", player, 2) and
                 state.has("Progressive Pick", player)),
    LocationData("Crystal Caves", "Crystal Caves Frozen Heart", 177,
                 lambda state, player: state.has("Progressive Knuckle", player, 2) and
                 (state.has("Lariat", player) or state.prodigal_has_cleats(player)) and
                 state.has("Progressive Pick", player) and state.prodigal_has_key("Crystal Caves", player, 3)),

    LocationData("Haunted Hall", "Haunted Hall Right Entry Chest", 66,
                 lambda state, player: True),
    LocationData("Haunted Hall", "Haunted Hall Left Entry Chest", 65,
                 lambda state, player: state.prodigal_can_hit(player)),
    LocationData("Haunted Hall", "Haunted Hall Invisible Maze Chest", 67,
                 lambda state, player: state.prodigal_can_hit(player) and
                 state.has("Progressive Hand", player) and state.prodigal_has_key("Haunted Hall", player, 1)),
    LocationData("Haunted Hall", "Haunted Hall Crystal Chest", 72,
                 lambda state, player: state.has("Progressive Knuckle", player, 2) and
                 state.has("Progressive Hand", player) and state.prodigal_has_key("Haunted Hall", player, 2) and
                 (state.has("Lariat", player) or state.prodigal_can_long_jump(player) or state.prodigal_has_ice_key(player))),
    LocationData("Haunted Hall", "Haunted Hall Killer", 229,
                 lambda state, player: state.prodigal_can_hit(player) and
                 state.has("Progressive Hand", player) and state.prodigal_has_key("Haunted Hall", player, 2) and
                 state.has("Lariat", player)),
    
    LocationData("Siska's Workshop", "Siska's Workshop First Chest", 82,
                 lambda state, player: state.has("Lariat", player) and state.prodigal_can_hit(player)),
    LocationData("Siska's Workshop", "Siska's Workshop Energy Orb Chest", 83,
                 lambda state, player: state.has("Lariat", player) and state.prodigal_can_hit(player) and
                 state.prodigal_has_key("Siska's Workshop", player, 1)),
    LocationData("Siska's Workshop", "Siska's Workshop Cannon Chest", 84,
                 lambda state, player: state.has("Lariat", player) and state.prodigal_can_hit(player) and
                 (state.has("Progressive Hand", player) or state.has("Progressive Knuckle", player, 2)) and
                 state.prodigal_has_key("Siska's Workshop", player, 2)),
    LocationData("Siska's Workshop", "Siska's Workshop Mecha Vanns Chest", 86,
                 lambda state, player: state.has("Lariat", player) and state.prodigal_can_hit(player) and
                 (state.has("Progressive Hand", player) or state.has("Progressive Knuckle", player, 2)) and
                 state.prodigal_has_key("Siska's Workshop", player, 3)),
    LocationData("Siska's Workshop", "Siska's Workshop Crystal Chest", 85,
                 lambda state, player: state.has("Lariat", player) and state.prodigal_can_hit(player) and
                 (state.has("Progressive Hand", player) or state.has("Progressive Knuckle", player, 2)) and
                 state.prodigal_has_key("Siska's Workshop", player, 3)),
    LocationData("Siska's Workshop", "Siska's Workshop Siska", 231,
                 lambda state, player: state.has("Lariat", player) and state.prodigal_can_hit(player) and
                 (state.has("Progressive Hand", player) or state.has("Progressive Knuckle", player, 2)) and
                 state.prodigal_has_key("Siska's Workshop", player, 3)),
    
    LocationData("Backrooms", "Backrooms Entry Chest", 89,
                 lambda state, player: state.has("Progressive Knuckle", player)),
    LocationData("Backrooms", "Backrooms Left Side Chest", 172,
                 lambda state, player: state.has("Progressive Knuckle", player) and state.has("Lariat", player)),
    LocationData("Backrooms", "Backrooms Hidden Chest", 174,
                 lambda state, player: state.has("Progressive Knuckle", player) and state.has("Lariat", player)),
    LocationData("Backrooms", "Backrooms Cannon Chest", 173,
                 lambda state, player: state.has("Progressive Knuckle", player) and
                 state.prodigal_has_key("Backrooms", player, 1) and state.has("Lariat", player)),
    LocationData("Backrooms", "Backrooms Ball Chest", 178,
                 lambda state, player: state.has("Progressive Knuckle", player) and
                 state.prodigal_has_key("Backrooms", player, 1) and state.has("Lariat", player)),
    LocationData("Backrooms", "Backrooms Near Cracked Wall Chest", 76,
                 lambda state, player: state.has("Progressive Knuckle", player) and
                 state.prodigal_has_key("Backrooms", player, 1) and state.has("Lariat", player)),
    LocationData("Backrooms", "Backrooms Crystal Chest", 81,
                 lambda state, player: state.has("Progressive Knuckle", player) and
                 state.prodigal_has_key("Backrooms", player, 1) and state.has("Lariat", player) and
                 (state.prodigal_has_key("Backrooms", player, 2) or state.prodigal_has_ice_key(player))),
    LocationData("Backrooms", "Backrooms Mechanized Slot Machine", 73,
                 lambda state, player: state.has("Progressive Knuckle", player) and
                 (state.prodigal_has_key("Backrooms", player, 2) or state.prodigal_has_ice_key(player)) and
                 state.has("Progressive Pick", player) and state.has("Lariat", player)),
    
    LocationData("Pirate's Pier", "Pirate's Pier Caroline", 225,
                 lambda state, player: True),
    LocationData("Pirate's Pier", "Pirate's Pier First Chest", 134,
                 lambda state, player: True),
    LocationData("Pirate's Pier", "Pirate's Pier Lariat Target Chest", 133,
                 lambda state, player: state.has("Lariat", player)),
    LocationData("Pirate's Pier", "Pirate's Pier Locked Chest", 132,
                 lambda state, player: state.has("Lariat", player) and state.prodigal_has_key("Pirate's Pier", player, 5)),
    LocationData("Pirate's Pier", "Pirate's Pier Shelled Nipper Chest", 121,
                 lambda state, player: state.prodigal_can_hit(player)),
    LocationData("Pirate's Pier", "Pirate's Pier Block Puzzle Chest", 122,
                 lambda state, player: state.has("Progressive Knuckle", player) and
                 state.prodigal_has_key("Pirate's Pier", player, 5)),
    LocationData("Pirate's Pier", "Pirate's Pier Spikes Chest", 131,
                 lambda state, player: state.has("Progressive Knuckle", player) and
                 (state.has("Progressive Knuckle", player, 2) or state.has("Lariat", player))),
    LocationData("Pirate's Pier", "Pirate's Pier Lariat Puzzle Chest", 130,
                 lambda state, player: state.has("Progressive Knuckle", player) and state.has("Lariat", player)),
    LocationData("Pirate's Pier", "Pirate's Pier Inkwell", 239,
                 lambda state, player: state.has("Progressive Knuckle", player, 2) and
                 state.prodigal_has_key("Pirate's Pier", player, 5)),
    LocationData("Pirate's Pier", "Pirate's Pier Block Push Chest", 126,
                 lambda state, player: state.has("Progressive Pick", player) and
                 state.has("Lariat", player) and state.has("Progressive Knuckle", player, 2)),
    LocationData("Pirate's Pier", "Pirate's Pier Barrel Switches Chest", 129,
                 lambda state, player: state.has("Progressive Pick", player) and
                 state.has("Lariat", player) and state.has("Progressive Hand", player, 2) and
                 state.prodigal_has_key("Pirate's Pier", player, 5)),
    LocationData("Pirate's Pier", "Pirate's Pier Don't Drop Chest", 127,
                 lambda state, player: state.has("Progressive Pick", player) and state.has("Lariat", player)),
    LocationData("Pirate's Pier", "Pirate's Pier Drop Chest", 128,
                 lambda state, player: state.has("Progressive Pick", player) and state.has("Lariat", player)),
    LocationData("Pirate's Pier", "Pirate's Pier Kings Ring Chest", 125,
                 lambda state, player: state.has("Progressive Pick", player) and
                 state.has("Lariat", player) and state.has("Progressive Knuckle", player, 2) and
                 state.prodigal_has_key("Pirate's Pier", player, 5)),
    LocationData("Pirate's Pier", "Pirate's Pier Revulan", 226,
                 lambda state, player: state.has("Progressive Knuckle", player) and
                 state.has("Kings Ring", player) and state.prodigal_has_blessings(player, 2)),

    LocationData("Lighthouse", "Lighthouse Library Chest", 43,
                 lambda state, player: state.has("Progressive Pick", player) and
                 state.has("Progressive Knuckle", player) and state.has("Lariat", player)),
    LocationData("Lighthouse", "Lighthouse Junk Room Chest", 42,
                 lambda state, player: state.has("Progressive Pick", player) and
                 state.has("Progressive Knuckle", player) and state.has("Lariat", player)),
    LocationData("Lighthouse", "Var Defeated", None,
                 lambda state, player: state.has("Progressive Pick", player) and
                 state.has("Progressive Knuckle", player) and state.has("Lariat", player) and
                 state.has("Progressive Hand", player) and state.prodigal_has_key("Lighthouse", player, 1)),
]

grelin_location_data = [
    LocationData("Vann's Point", "Grelin Drop 1", 240,
                 lambda state, player: state.prodigal_can_kill_grelins(player)),
    LocationData("Vann's Point", "Grelin Drop 2", 241,
                 lambda state, player: state.prodigal_can_kill_grelins(player)),
    LocationData("Vann's Point", "Grelin Drop 3", 242,
                 lambda state, player: state.prodigal_can_kill_grelins(player)),
    LocationData("Vann's Point", "Grelin Drop 4", 243,
                 lambda state, player: state.prodigal_can_kill_grelins(player)),
]

trade_location_data = [
    LocationData("Vann's Point", "Tess Trade", 206,
                 lambda state, player: state.has("Lost Shipment", player)),
    LocationData("Vann's Point", "Quinlan Trade", 207,
                 lambda state, player: state.has("THE Carrot Cake", player)),
    LocationData("Colorless Void", "Vulhara Trade", 214,
                 lambda state, player: state.has("Coffee", player) and state.has("Lariat", player)),
    LocationData("Colorless Void", "Reskel Trade", 215,
                 lambda state, player: state.has("Tattered Cape", player) and state.has("Lariat", player)),
    LocationData("Colorless Void", "Mynir Trade", 216,
                 lambda state, player: state.has("Ball of Yarn", player) and state.has("Lariat", player)),
    LocationData("Colorless Void", "Orima Trade", 217,
                 lambda state, player: state.has("Slime Soap", player)),
    LocationData("Colorless Void", "Wren Trade", 218,
                 lambda state, player: state.has("Serpent Bracelet", player)),
    LocationData("Colorless Void", "Leer Trade", 219,
                 lambda state, player: state.has("Hunting Bow", player)),
    LocationData("Colorless Void", "Burg Trade", 220,
                 lambda state, player: state.has("Down Pillow", player)),
    LocationData("Colorless Void", "Crelon Trade", 221,
                 lambda state, player: state.has("Giant's Monocle", player) and state.has("Lariat", player)),
    LocationData("Colorless Void", "Tedra Trade", 222,
                 lambda state, player: state.has("Forbidden Cookbook", player)),
    LocationData("Colorless Void", "Ulni Trade", 223,
                 lambda state, player: state.has("Kelp Rolls", player)),
]

vanilla_trade_location_data = [
    LocationData("Colorless Void", "Trading Quest", 223,
                 lambda state, player: state.has("Lost Shipment", player) and state.has("Lariat", player)),
]

hidden_location_data = [
    LocationData("Vann's Point", "Hidden Item Bush On Farm", 141,
                 lambda state, player: True),
    LocationData("Vann's Point", "Hidden Item Bush Near Bridge", 137,
                 lambda state, player: True),
    LocationData("Vann's Point", "Hidden Item Bush Near Bench", 139,
                 lambda state, player: True),
    LocationData("Vann's Point", "Hidden Item Bush Near River's House", 162,
                 lambda state, player: state.has("Progressive Pick", player) or
                 state.has("Progressive Knuckle", player) or state.has("Lariat", player)),
    LocationData("Vann's Point", "Hidden Item Bush Near Old House", 0,
                 lambda state, player: state.has("Climbing Gear", player)),
    LocationData("Vann's Point", "Hidden Item Crate Near Boot Shop", 140,
                 lambda state, player: True),
    LocationData("Vann's Point", "Hidden Item Crate Near Tidal Mines", 138,
                 lambda state, player: state.prodigal_can_hit(player)),
    LocationData("Vann's Point", "Hidden Item Dock Chest", 176,
                 lambda state, player: state.prodigal_can_hit(player)),
    LocationData("Vann's Point", "Hidden Item Ashwood Plant", 184,
                 lambda state, player: True),
    LocationData("Vann's Point", "Hidden Item Crocasino Cactus", 175,
                 lambda state, player: True),
]

daemons_dive_location_data = [   
    LocationData("Daemon's Dive", "Daemon's Dive 1 Barrel Puzzle Chest", 98,
                 lambda state, player: (state.has("Lariat", player) or state.prodigal_can_long_jump(player)) and
                 state.prodigal_can_hit(player)),
    LocationData("Daemon's Dive", "Daemon's Dive 1 Lariat Puzzle Chest", 108,
                 lambda state, player: state.has("Divine Key", player, 1) and
                 state.has("Progressive Hand", player, 2) and state.has("Lariat", player)),
    LocationData("Daemon's Dive", "Daemon's Dive 2 Skull Chest", 99,
                 lambda state, player: state.has("Divine Key", player, 2) and
                 (state.prodigal_has_ice_key(player) or state.has("Progressive Hand", player, 2)) and
                 state.has("Progressive Knuckle", player, 2) and state.has("Progressive Hand", player) and
                 state.has("Lariat", player)),
    LocationData("Daemon's Dive", "Daemon's Dive 2 Near Boss Chest", 100,
                 lambda state, player: state.has("Divine Key", player, 2) and
                 (state.prodigal_has_ice_key(player) or state.has("Progressive Hand", player, 2)) and
                 state.has("Progressive Knuckle", player, 2) and state.has("Progressive Hand", player) and
                 state.has("Lariat", player)),
    LocationData("Daemon's Dive", "Daemon's Dive 3 Cannon Chest", 101,
                 lambda state, player: state.has("Divine Key", player, 2) and
                 (state.prodigal_has_ice_key(player) or (state.has("Progressive Hand", player, 2) and
                 state.has("Divine Key", player, 4))) and state.has("Progressive Knuckle", player, 2) and
                 state.has("Progressive Hand", player) and state.has("Lariat", player) and
                 state.has("Progressive Pick", player)),
    LocationData("Daemon's Dive", "Daemon's Dive 3 Turtles Chest", 102,
                 lambda state, player: state.has("Divine Key", player, 5) and
                 (state.prodigal_has_ice_key(player) or state.has("Progressive Hand", player, 2)) and
                 state.has("Progressive Knuckle", player, 2) and state.has("Progressive Hand", player) and
                 state.has("Lariat", player) and state.has("Progressive Pick", player)),
    LocationData("Daemon's Dive", "Daemon's Dive 4 Turtles Chest", 103,
                 lambda state, player: state.has("Divine Key", player, 6) and
                 (state.prodigal_has_ice_key(player) or state.has("Progressive Hand", player, 2)) and
                 state.has("Progressive Knuckle", player, 2) and state.has("Progressive Hand", player) and
                 state.has("Lariat", player) and state.has("Progressive Pick", player)),
    LocationData("Daemon's Dive", "Daemon's Dive 5 Many Switches Chest", 104,
                 lambda state, player: state.has("Divine Key", player, 7) and
                 (state.prodigal_has_ice_key(player) or state.has("Progressive Hand", player, 2)) and
                 state.has("Progressive Knuckle", player, 2) and state.has("Progressive Hand", player) and
                 state.has("Lariat", player) and state.has("Progressive Pick", player)),
    LocationData("Daemon's Dive", "Daemon's Dive 5 Junk Pile Chest", 105,
                 lambda state, player: state.has("Divine Key", player, 7) and
                 (state.prodigal_has_ice_key(player) or state.has("Progressive Hand", player, 2)) and
                 state.has("Progressive Knuckle", player, 2) and state.has("Progressive Hand", player) and
                 state.has("Lariat", player) and state.has("Progressive Pick", player)),
    LocationData("Daemon's Dive", "Daemon's Dive 6 Main Room Chest", 106,
                 lambda state, player: state.has("Divine Key", player, 7) and
                 (state.prodigal_has_ice_key(player) or
                 (state.has("Divine Key", 9) and state.has("Progressive Hand", player, 2))) and
                 state.has("Progressive Knuckle", player, 2) and state.has("Progressive Hand", player) and
                 state.has("Lariat", player) and state.has("Progressive Pick", player)),
    LocationData("Daemon's Dive", "Daemon's Dive 7 Crystal Key Chest", 124,
                 lambda state, player: state.has("Divine Key", player, 10) and
                 state.has("Progressive Hand", player, 2) and state.has("Progressive Knuckle", player, 2) and
                 state.has("Lariat", player) and state.has("Progressive Pick", player)),
    LocationData("Daemon's Dive", "Daemon's Dive 7 Turtles Chest", 107,
                 lambda state, player: state.has("Divine Key", player, 11) and
                 (state.prodigal_has_ice_key(player) or state.has("Progressive Hand", player, 2)) and
                 state.has("Progressive Knuckle", player, 2) and state.has("Progressive Hand", player) and
                 state.has("Lariat", player) and state.has("Progressive Pick", player)),
    LocationData("Daemon's Dive", "Daemon's Dive Shadow Oran", 244,
                 lambda state, player: state.has("Divine Key", player, 12) and
                 (state.prodigal_has_ice_key(player) or state.has("Progressive Hand", player, 2)) and
                 state.has("Progressive Knuckle", player, 2) and state.has("Progressive Hand", player) and
                 state.has("Lariat", player) and state.has("Progressive Pick", player)),
    LocationData("Daemon's Dive", "Shadow Oran Defeated", None,
                 lambda state, player: state.has("Divine Key", player, 12) and
                 (state.prodigal_has_ice_key(player) or state.has("Progressive Hand", player, 2)) and
                 state.has("Progressive Knuckle", player, 2) and state.has("Progressive Hand", player) and
                 state.has("Lariat", player) and state.has("Progressive Pick", player)),
]

daemons_dive_vanilla_location_data = [
    LocationData("Daemon's Dive", "Shadow Oran Defeated", None,
                 lambda state, player: state.has("Progressive Hand", player, 2) and
                 state.has("Progressive Knuckle", player, 2) and state.has("Lariat", player) and
                 state.has("Progressive Pick", player)),
]

enlightenment_location_data = [
    LocationData("Enlightenment", "Enlightenment 1 Right Side Chest", 64,
                 lambda state, player: state.has("Progressive Knuckle", player, 2) and
                 state.has("Lariat", player) and state.has("Progressive Pick", player)),
    LocationData("Enlightenment", "Enlightenment 1 Left Side Chest", 77,
                 lambda state, player: state.has("Progressive Knuckle", player, 2) and
                 state.has("Lariat", player) and state.has("Progressive Pick", player) and
                 state.has("Progressive Hand", player, 2)),
    LocationData("Enlightenment", "Enlightenment 1 Center Room Chest", 80,
                 lambda state, player: state.has("Progressive Knuckle", player, 2) and
                 state.has("Lariat", player) and state.has("Progressive Pick", player) and
                 state.has("Progressive Hand", player, 2)),
    LocationData("Enlightenment", "Enlightenment 2 Crystal Key Chest", 74,
                 lambda state, player: state.has("Progressive Knuckle", player, 2) and
                 state.has("Lariat", player) and state.has("Progressive Pick", player) and
                 state.has("Progressive Hand", player, 2)),
    LocationData("Enlightenment", "Enlightenment 3 Perilous Platforms Chest", 78,
                 lambda state, player: state.has("Progressive Knuckle", player, 2) and
                 state.has("Lariat", player) and state.has("Progressive Pick", player) and
                 state.has("Progressive Hand", player, 2)),
    LocationData("Enlightenment", "Enlightenment 4 Roller Chest", 90,
                 lambda state, player: state.has("Progressive Knuckle", player, 2) and
                 state.has("Lariat", player) and state.has("Progressive Pick", player) and
                 state.has("Progressive Hand", player, 2)),
    LocationData("Enlightenment", "Enlightenment 4 Spike Floor Chest", 75,
                 lambda state, player: state.has("Progressive Knuckle", player, 2) and
                 state.has("Lariat", player) and state.has("Progressive Pick", player) and
                 state.has("Progressive Hand", player, 2)),
    LocationData("Enlightenment", "Enlightenment 5 Falling Floor Chest", 79,
                 lambda state, player: state.has("Progressive Knuckle", player, 2) and
                 state.has("Lariat", player) and state.has("Progressive Pick", player) and
                 state.has("Progressive Hand", player, 2)),
    LocationData("Enlightenment", "Torran Defeated", None,
                 lambda state, player: state.has("Progressive Knuckle", player, 2) and
                 state.has("Lariat", player) and state.has("Progressive Pick", player) and
                 state.has("Progressive Hand", player, 2)),
]

secret_shop_location_data = [
    LocationData("Tidal Mines", "Secret Shop Item 1", 245,
                 lambda state, player: state.prodigal_can_reach_zaegul(player)),
    LocationData("Tidal Mines", "Secret Shop Item 2", 246,
                 lambda state, player: state.prodigal_can_reach_zaegul(player)),
    LocationData("Tidal Mines", "Secret Shop Item 3", 247,
                 lambda state, player: state.prodigal_can_reach_zaegul(player)),
]

all_location_data = base_location_data + grelin_location_data + trade_location_data + hidden_location_data + daemons_dive_location_data + enlightenment_location_data + secret_shop_location_data