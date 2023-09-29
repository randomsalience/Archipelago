from BaseClasses import MultiWorld, Region, Entrance

def connect(multiworld: MultiWorld, player: int, source: str, target: str, rule: callable = lambda state: True):
    source_region = multiworld.get_region(source, player)
    target_region = multiworld.get_region(target, player)
    entrance = Entrance(player, f"{source} -> {target}", source_region)
    entrance.access_rule = rule
    source_region.exits.append(entrance)
    entrance.connect(target_region)

def create_and_connect_regions(multiworld: MultiWorld, player: int):
    multiworld.regions += [Region(name, player, multiworld) for name in region_names]

    connect(multiworld, player, "Menu", "Vann's Point")
    connect(multiworld, player, "Vann's Point", "Colorless Void")
    connect(multiworld, player, "Vann's Point", "Abandoned Mine")
    connect(multiworld, player, "Vann's Point", "Waterfall Cave",
            lambda state: state.has("Climbing Gear", player))
    connect(multiworld, player, "Vann's Point", "Celina's Mine",
            lambda state: state.has("Bandana", player) and
            ((state.has("Climbing Gear", player) and state.prodigal_can_hit(player)) or
            state.has("Progressive Knuckle", player) and state.has("Lariat", player)))
    connect(multiworld, player, "Vann's Point", "Cursed Grave",
            lambda state: state.has("Cursed Bones", player))
    connect(multiworld, player, "Vann's Point", "Boneyard",
            lambda state: state.prodigal_can_hit(player))
    connect(multiworld, player, "Vann's Point", "Tidal Mines",
            lambda state: state.has("Rusty Key", player))
    connect(multiworld, player, "Vann's Point", "Dry Fountain")
    connect(multiworld, player, "Vann's Point", "Crocasino",
            lambda state: state.has("Progressive Knuckle", player))
    connect(multiworld, player, "Vann's Point", "Howling Bjerg")
    connect(multiworld, player, "Vann's Point", "Castle Vann",
            lambda state: state.has("Hallowed Key", player))
    connect(multiworld, player, "Vann's Point", "Magma Heart",
            lambda state: (state.has("Progressive Knuckle", player) and state.has("Lariat", player)) or
            state.has("Climbing Gear", player))
    connect(multiworld, player, "Colorless Void", "Time Out")
    connect(multiworld, player, "Vann's Point", "Crystal Caves",
            lambda state: state.has("Progressive Knuckle", player))
    connect(multiworld, player, "Vann's Point", "Haunted Hall",
            lambda state: state.has("Bone Key", player) and state.prodigal_can_hit(player))
    connect(multiworld, player, "Vann's Point", "Siska's Workshop",
            lambda state: state.has("Lariat", player) and
            (state.has("Progressive Pick", player) or state.has("Hallowed Key", player)))
    connect(multiworld, player, "Vann's Point", "Backrooms")
    connect(multiworld, player, "Vann's Point", "Pirate's Pier",
            lambda state: state.has("Stindle's Map", player) and state.prodigal_can_hit(player))
    connect(multiworld, player, "Vann's Point", "Lighthouse",
            lambda state: state.prodigal_has_colors(player, multiworld.colors_required[player]))
    connect(multiworld, player, "Vann's Point", "Bjerg Castle")
    connect(multiworld, player, "Vann's Point", "Daemon's Dive",
            lambda state: state.has("Progressive Hand", player, 2) and
            state.has("Hallowed Key", player) and state.has("Daemons Key", player))
    connect(multiworld, player, "Vann's Point", "Enlightenment",
            lambda state: state.prodigal_has_blessings(player, multiworld.blessings_required[player]) and
            state.has("Climbing Gear", player) and state.has("Progressive Hand", player, 2) and
            state.prodigal_has_tar(player))

region_names = [
    "Menu",
    "Vann's Point",
    "Colorless Void",
    "Abandoned Mine",
    "Waterfall Cave",
    "Celina's Mine",
    "Cursed Grave",
    "Boneyard",
    "Tidal Mines",
    "Dry Fountain",
    "Crocasino",
    "Howling Bjerg",
    "Castle Vann",
    "Magma Heart",
    "Time Out",
    "Crystal Caves",
    "Haunted Hall",
    "Siska's Workshop",
    "Backrooms",
    "Pirate's Pier",
    "Lighthouse",
    "Bjerg Castle",
    "Daemon's Dive",
    "Enlightenment",
]