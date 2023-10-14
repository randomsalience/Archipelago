from BaseClasses import ItemClassification
from typing import Dict, List, NamedTuple

progression = ItemClassification.progression
useful = ItemClassification.useful
filler = ItemClassification.filler
trap = ItemClassification.trap

class ItemData(NamedTuple):
    code: int
    classification: ItemClassification

item_table: Dict[str, ItemData] = {
    "Gold (100)": ItemData(4, filler),
    "Lariat": ItemData(7, progression),
    "Lucky Boots": ItemData(12, progression),
    "Cleated Boots": ItemData(13, progression),
    "Anchor Greaves": ItemData(14, progression),
    "Boots of Graile": ItemData(15, progression),
    "Winged Boots": ItemData(16, progression),
    "Old Recipe": ItemData(17, filler),
    "Rare Seeds": ItemData(18, filler),
    "Herb Pouch": ItemData(19, filler),
    "Coin of Crowl": ItemData(20, progression),
    "Tidal Gem": ItemData(21, filler),
    "Lumen Beetle": ItemData(22, filler),
    "Coffee": ItemData(23, progression),
    "Tattered Cape": ItemData(24, progression),
    "Ball of Yarn": ItemData(25, progression),
    "Slime Soap": ItemData(26, progression),
    "Serpent Bracelet": ItemData(27, progression),
    "THE Carrot Cake": ItemData(28, progression),
    "Hunting Bow": ItemData(29, progression),
    "Down Pillow": ItemData(30, progression),
    "Giant's Monocle": ItemData(31, progression),
    "Forbidden Book": ItemData(32, progression),
    "Kelp Rolls": ItemData(33, progression),
    "Boss Key": ItemData(34, progression),
    "Hallowed Key": ItemData(35, progression),
    "Rusty Key": ItemData(36, progression),
    "Gator Key": ItemData(37, progression),
    "Bunny Key": ItemData(38, progression),
    "Normal Key": ItemData(39, useful),
    "Toadstool": ItemData(40, useful),
    "Frozen Thorn": ItemData(41, filler),
    "Luminous Crystal": ItemData(42, filler),
    "Fury Heart": ItemData(43, progression),
    "Shattered Soul": ItemData(44, progression),
    "Drowned Ore": ItemData(45, progression),
    "Shaedrite": ItemData(46, progression),
    "Miasmic Extract": ItemData(47, progression),
    "Lost Shipment": ItemData(48, progression),
    "Broken Sword": ItemData(49, progression),
    "Crest Fragment": ItemData(50, progression),
    "Cursed Bones": ItemData(51, progression),
    "Bone Key": ItemData(52, progression),
    "Sunset Painting": ItemData(53, progression),
    "Cursed Pick": ItemData(55, progression),
    "Daemons Key": ItemData(56, progression),
    "Divine Key": ItemData(62, progression),
    "Prison Key": ItemData(63, useful),
    "Stindles Map": ItemData(64, progression),
    "Harmonica": ItemData(65, progression),
    "Ice Key": ItemData(67, useful),
    "Silvered Scarf": ItemData(68, useful),
    "Heart Ore": ItemData(70, useful),
    "Old Hairpin": ItemData(71, progression),
    "Ora Moa": ItemData(72, filler),
    "Eerie Mask": ItemData(73, progression),
    "Frozen Heart": ItemData(74, progression),
    "Red Crystal": ItemData(75, progression),
    "Weapon Chain": ItemData(78, progression),
    "Climbing Gear": ItemData(79, progression),
    "Illusion Ring": ItemData(80, useful),
    "Golem Ring": ItemData(81, useful),
    "Magnet Ring": ItemData(82, useful),
    "Spiked Ring": ItemData(83, useful),
    "Hearth Ring": ItemData(84, useful),
    "Daemons Ring": ItemData(85, useful),
    "Kings Ring": ItemData(86, progression),
    "Dusty Key": ItemData(87, progression),
    "Life Blessing": ItemData(89, progression),
    "Light Blessing": ItemData(90, progression),
    "Storm Blessing": ItemData(91, progression),
    "Earth Blessing": ItemData(92, progression),
    "Water Blessing": ItemData(93, progression),
    "Bandana": ItemData(95, progression),
    "Holy Relic": ItemData(96, progression),
    "Wedding Ring": ItemData(97, progression),
    "Silver Mirror": ItemData(98, progression),
    "Painting": ItemData(99, progression),
    "Progressive Knuckle": ItemData(102, progression),
    "Progressive Hand": ItemData(103, progression),
    "Progressive Pick": ItemData(104, progression),
    "Key (Boneyard)": ItemData(105, progression),
    "Key (Tidal Mines)": ItemData(106, progression),
    "Key (Crocasino)": ItemData(107, progression),
    "Key (Howling Bjerg)": ItemData(108, progression),
    "Key (Castle Vann)": ItemData(109, progression),
    "Key (Magma Heart)": ItemData(110, progression),
    "Key (Time Out)": ItemData(111, progression),
    "Key (Lighthouse)": ItemData(112, progression),
    "Key (Crystal Caves)": ItemData(113, progression),
    "Key (Haunted Hall)": ItemData(114, progression),
    "Key (Siska's Workshop)": ItemData(115, progression),
    "Key (Backrooms)": ItemData(116, progression),
    "Key (Pirate's Pier)": ItemData(117, progression),
    "Key (Bjerg Castle)": ItemData(118, progression),
    "Slowness Trap": ItemData(119, trap),
    "Rust Trap": ItemData(120, trap),
    "Confusion Trap": ItemData(121, trap),
    "Disarming Trap": ItemData(122, trap),
    "Light Trap": ItemData(123, trap),
    "Glitch Trap": ItemData(124, trap),
    "Zombie Trap": ItemData(125, trap),
    "Shadow Trap": ItemData(126, trap),
    "Love Trap": ItemData(127, trap),
}

base_item_pool: Dict[str, int] = {
    "Gold (100)": 20,
    "Lariat": 1,
    "Lucky Boots": 1,
    "Cleated Boots": 1,
    "Anchor Greaves": 1,
    "Boots of Graile": 1,
    "Winged Boots": 1,
    "Old Recipe": 3,
    "Rare Seeds": 4,
    "Herb Pouch": 5,
    "Coin of Crowl": 13,
    "Lumen Beetle": 4,
    "Boss Key": 1,
    "Hallowed Key": 1,
    "Rusty Key": 1,
    "Gator Key": 1,
    "Bunny Key": 1,
    "Toadstool": 1,
    "Frozen Thorn": 1,
    "Luminous Crystal": 1,
    "Fury Heart": 1,
    "Shattered Soul": 1,
    "Drowned Ore": 1,
    "Shaedrite": 1,
    "Miasmic Extract": 1,
    "Broken Sword": 1,
    "Crest Fragment": 5,
    "Cursed Bones": 1,
    "Bone Key": 1,
    "Sunset Painting": 1,
    "Cursed Pick": 1,
    "Daemons Key": 1,
    "Prison Key": 1,
    "Stindles Map": 1,
    "Harmonica": 1,
    "Ice Key": 1,
    "Silvered Scarf": 1,
    "Heart Ore": 24,
    "Old Hairpin": 1,
    "Ora Moa": 1,
    "Eerie Mask": 1,
    "Frozen Heart": 1,
    "Red Crystal": 1,
    "Weapon Chain": 1,
    "Climbing Gear": 1,
    "Illusion Ring": 1,
    "Golem Ring": 1,
    "Magnet Ring": 1,
    "Spiked Ring": 1,
    "Hearth Ring": 1,
    "Daemons Ring": 1,
    "Kings Ring": 1,
    "Dusty Key": 1,
    "Life Blessing": 1,
    "Light Blessing": 1,
    "Storm Blessing": 1,
    "Earth Blessing": 1,
    "Water Blessing": 1,
    "Bandana": 1,
    "Progressive Knuckle": 2,
    "Progressive Hand": 2,
    "Progressive Pick": 3,
}

trade_item_pool: Dict[str, int] = {
    "Lost Shipment": 1,
    "Coffee": 1,
    "Tattered Cape": 1,
    "Ball of Yarn": 1,
    "Slime Soap": 1,
    "Serpent Bracelet": 1,
    "THE Carrot Cake": 1,
    "Hunting Bow": 1,
    "Down Pillow": 1,
    "Giant's Monocle": 1,
    "Forbidden Book": 1,
    "Kelp Rolls": 1,
}

grelin_item_pool: Dict[str, int] = {
    "Holy Relic": 1,
    "Wedding Ring": 1,
    "Silver Mirror": 1,
    "Painting": 1,
}

hidden_item_pool: Dict[str, int] = {
    "Gold (100)": 1,
    "Old Recipe": 2,
    "Rare Seeds": 2,
    "Herb Pouch": 1,
    "Tidal Gem": 2,
    "Lumen Beetle": 2,
}

universal_key_item_pool: Dict[str, int] = {
    "Normal Key": 33,
}

specific_key_item_pool: Dict[str, int] = {
    "Key (Boneyard)": 1,
    "Key (Tidal Mines)": 4,
    "Key (Crocasino)": 2,
    "Key (Howling Bjerg)": 1,
    "Key (Castle Vann)": 4,
    "Key (Magma Heart)": 2,
    "Key (Time Out)": 3,
    "Key (Lighthouse)": 1,
    "Key (Crystal Caves)": 3,
    "Key (Haunted Hall)": 2,
    "Key (Siska's Workshop)": 3,
    "Key (Backrooms)": 2,
    "Key (Pirate's Pier)": 5,
}

bjerg_castle_universal_item_pool: Dict[str, int] = {
    "Gold (100)": 4,
    "Tidal Gem": 2,
    "Normal Key": 1,
}

bjerg_castle_specific_item_pool: Dict[str, int] = {
    "Gold (100)": 4,
    "Tidal Gem": 2,
    "Key (Bjerg Castle)": 1,
}

daemons_dive_item_pool: Dict[str, int] = {
    "Divine Key": 12,
}

enlightenment_item_pool: Dict[str, int] = {
    "Old Recipe": 2,
    "Rare Seeds": 3,
    "Herb Pouch": 1,
    "Ice Key": 2,
}

filler_items: List[str] = [
    "Gold (100)",
    "Old Recipe",
    "Rare Seeds",
    "Herb Pouch",
    "Tidal Gem",
    "Lumen Beetle",
]

trap_items: List[str] = [
    "Slowness",
    "Rust",
    "Confusion",
    "Disarming",
    "Light",
    "Glitch",
    "Zombie",
    "Shadow",
]