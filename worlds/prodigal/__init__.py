from typing import Optional
from BaseClasses import Item, ItemClassification, Location, Tutorial
from Options import StartInventoryPool
from ..AutoWorld import World, WebWorld
from worlds.generic.Rules import set_rule
from .Items import *
from .Locations import *
from .Regions import create_and_connect_regions
from .Options import prodigal_options, Goal, TradingQuest
from .Rules import ProdigalLogic

prodigal_base_id = 77634425000

class ProdigalItem(Item):
    game: str = "Prodigal"

class ProdigalLocation(Location):
    game: str = "Prodigal"

class ProdigalWebWorld(WebWorld):
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Prodigal for Archipelago.",
        "English",
        "setup_en.md",
        "setup/en",
        ["randomsalience"]
    )]

class ProdigalWorld(World):
    '''Grab your pick and strike out into a vibrant world of monsters, puzzling dungeons and curious townsfolk!
    Can you unravel the mysteries of this old town and keep its people safe? It's time to return home,
    Vann's Point needs you.''' # from Steam description
    game: str = "Prodigal"
    option_definitions = prodigal_options
    topology_present = False
    required_client_version = (0, 4, 2)
    data_version = 2
    web = ProdigalWebWorld()

    item_name_to_id = {name: prodigal_base_id + data.code for name, data in item_table.items()}
    location_name_to_id = {data.name: prodigal_base_id + data.code if data.code != None else None for data in all_location_data}
    item_name_groups = item_name_groups

    def create_item(self, name: str):
        return ProdigalItem(name, item_table[name].classification, prodigal_base_id + item_table[name].code, self.player)

    def enabled_traps(self):
        all_traps = [f"{trap} Trap" for trap in trap_items]
        if self.multiworld.enable_all_traps[self.player]:
            return all_traps
        enabled_traps = [f"{trap} Trap" for trap in trap_items if getattr(self.multiworld, f"{trap.lower()}_traps")[self.player]]
        if len(enabled_traps) > 0 or not self.multiworld.curse_of_horns[self.player]:
            return enabled_traps
        return all_traps

    def get_trap_name(self):
        if self.random.randrange(1000) == 0:
            return "Love Trap"
        return self.random.choice(self.enabled_traps())

    def get_filler_item_name(self):
        enabled_traps = self.enabled_traps()
        if self.multiworld.curse_of_horns[self.player] or (len(enabled_traps) > 0 and self.random.randrange(100) < self.multiworld.trap_chance[self.player]):
            return self.get_trap_name()
        return self.random.choice(filler_items)

    def create_item_or_trap(self, name: str):
        if self.multiworld.curse_of_horns[self.player] and name in filler_items:
            return self.create_item(self.get_trap_name())
        return self.create_item(name)

    def generate_early(self):
        start_inventory_from_pool = self.multiworld.start_inventory_from_pool.setdefault(self.player, StartInventoryPool({})).value
        for item_name, count in self.multiworld.start_inventory[self.player].value.items():
            start_inventory_from_pool.setdefault(item_name, 0)
            start_inventory_from_pool[item_name] += count
        self.multiworld.start_inventory[self.player].value = {}
        if self.multiworld.start_with_winged_boots[self.player]:
            start_inventory_from_pool.setdefault("Winged Boots", 1)

    def create_regions(self):
        create_and_connect_regions(self.multiworld, self.player)
        
        location_data = base_location_data[:]
        if self.multiworld.trading_quest[self.player] == TradingQuest.option_shuffle:
            location_data += trade_location_data
        elif self.multiworld.trading_quest[self.player] == TradingQuest.option_vanilla:
            location_data += vanilla_trade_location_data
        if self.multiworld.shuffle_grelin_drops[self.player]:
            location_data += grelin_location_data
        if self.multiworld.shuffle_hidden_items[self.player]:
            location_data += hidden_location_data
        if self.multiworld.shuffle_bjerg_castle[self.player]:
            location_data += bjerg_castle_location_data
        if self.multiworld.shuffle_daemons_dive[self.player]:
            location_data += daemons_dive_location_data
        else:
            location_data += daemons_dive_vanilla_location_data
        if self.multiworld.shuffle_enlightenment[self.player]:
            location_data += enlightenment_location_data
        else:
            location_data += enlightenment_location_data[-1:]
        if self.multiworld.shuffle_secret_shop[self.player]:
            location_data += secret_shop_location_data

        for data in location_data:
            region = self.multiworld.get_region(data.region, self.player)
            location = ProdigalLocation(self.player, data.name, prodigal_base_id + data.code if data.code != None else None, region)
            region.locations.append(location)
            set_rule(location, lambda state, data=data, player=self.player: data.access_rule(state, player))
    
    def create_items(self):
        item_pools = [base_item_pool]
        if self.multiworld.trading_quest[self.player] == TradingQuest.option_shuffle:
            item_pools.append(trade_item_pool)
        elif self.multiworld.trading_quest[self.player] == TradingQuest.option_vanilla:
            item_pools.append({"Lost Shipment": 1})
        if self.multiworld.shuffle_grelin_drops[self.player]:
            item_pools.append(grelin_item_pool)
        if self.multiworld.shuffle_hidden_items[self.player]:
            item_pools.append(hidden_item_pool)
        if self.multiworld.specific_keys[self.player]:
            item_pools.append(specific_key_item_pool)
            if self.multiworld.shuffle_bjerg_castle[self.player]:
                item_pools.append(bjerg_castle_specific_item_pool)
        else:
            item_pools.append(universal_key_item_pool)
            if self.multiworld.shuffle_bjerg_castle[self.player]:
                item_pools.append(bjerg_castle_universal_item_pool)
        if self.multiworld.shuffle_daemons_dive[self.player]:
            item_pools.append(daemons_dive_item_pool)
        if self.multiworld.shuffle_enlightenment[self.player]:
            item_pools.append(enlightenment_item_pool)
        
        num_items = 0
        for item_pool in item_pools:
            for item, count in item_pool.items():
                num_items += count
                for _ in range(count):
                    self.multiworld.itempool.append(self.create_item_or_trap(item))
        
        num_locations = len([location for location in self.multiworld.get_locations(self.player) if location.address != None])
        
        for _ in range(num_locations - num_items):
            self.multiworld.itempool.append(self.create_filler())
    
    def generate_basic(self):
        if self.multiworld.goal[self.player] == Goal.option_var or self.multiworld.goal[self.player] == Goal.option_any:
            self.multiworld.get_location("Var Defeated", self.player).place_locked_item(Item("Victory", ItemClassification.progression, None, self.player))
        else:
            self.multiworld.get_location("Var Defeated", self.player).place_locked_item(Item("Nothing", ItemClassification.filler, None, self.player))
        if self.multiworld.goal[self.player] == Goal.option_rest or self.multiworld.goal[self.player] == Goal.option_any:
            self.multiworld.get_location("Hero's Rest", self.player).place_locked_item(Item("Victory", ItemClassification.progression, None, self.player))
        else:
            self.multiworld.get_location("Hero's Rest", self.player).place_locked_item(Item("Nothing", ItemClassification.filler, None, self.player))
        if self.multiworld.goal[self.player] == Goal.option_shadow or self.multiworld.goal[self.player] == Goal.option_any:
            self.multiworld.get_location("Shadow Oran Defeated", self.player).place_locked_item(Item("Victory", ItemClassification.progression, None, self.player))
        else:
            self.multiworld.get_location("Shadow Oran Defeated", self.player).place_locked_item(Item("Nothing", ItemClassification.filler, None, self.player))
        if self.multiworld.goal[self.player] == Goal.option_torran or self.multiworld.goal[self.player] == Goal.option_any:
            self.multiworld.get_location("Torran Defeated", self.player).place_locked_item(Item("Victory", ItemClassification.progression, None, self.player))
        else:
            self.multiworld.get_location("Torran Defeated", self.player).place_locked_item(Item("Nothing", ItemClassification.filler, None, self.player))
        self.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player)
    
    def fill_slot_data(self):
        slot_data = {}
        for option_name in prodigal_options:
            option = getattr(self.multiworld, option_name)[self.player]
            slot_data[option_name] = option.value
        slot_data["seed"] = self.random.randrange(1, 2**31)
        pick_location = self.find_earliest("Progressive Pick")
        if pick_location:
            slot_data["pick_hint_player"] = self.multiworld.player_name[pick_location.player]
            slot_data["pick_hint_location"] = pick_location.name
        return slot_data

    def find_earliest(self, item_name: str) -> Optional[Location]:
        for sphere in self.multiworld.get_spheres():
            for location in sphere:
                if location.item.player == self.player and location.item.name == item_name:
                    return location
        return None