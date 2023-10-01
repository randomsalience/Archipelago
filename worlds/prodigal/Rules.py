from ..AutoWorld import LogicMixin

class ProdigalLogic(LogicMixin):
    def prodigal_can_hit(self, player):
        return self.has("Progressive Pick", player) or self.has("Progressive Knuckle", player)
    def prodigal_can_hit_fire(self, player):
        return self.has("Progressive Pick", player) or self.has("Progressive Knuckle", player, 2)
    def prodigal_can_reach_zaegul(self, player):
        return (self.has("Progressive Pick", player) or self.prodigal_can_long_jump(player) or
                ((self.has("Progressive Knuckle", player, 2) or self.prodigal_skips(player)) and self.has("Lariat", player))) and \
                self.has("Harmonica", player) and self.can_reach("Tidal Mines", "Region", player)
    def prodigal_has_key(self, region, player, count):
        return self.has(f"Key ({region})", player, count) if self.multiworld.specific_keys[player].value else \
                self.prodigal_can_reach_zaegul(player)
    def prodigal_has_ice_key(self, player):
        return self.prodigal_can_reach_zaegul(player)
    def prodigal_skips(self, player):
        return self.multiworld.skips_in_logic[player]
    def prodigal_can_long_jump(self, player):
        return self.has("Progressive Knuckle", player, 2) and self.prodigal_skips(player)
    def prodigal_can_remove_boulders(self, player):
        return self.has("Progressive Knuckle", player) or \
                (self.has("Progressive Hand", player, 2) and self.prodigal_skips(player))
    def prodigal_has_cleats(self, player):
        return self.has("Cleated Boots", player) or self.has("Boots of Graile", player)
    def prodigal_has_crest(self, player):
        return self.has("Crest Fragment", player, self.multiworld.crest_fragments_required[player])
    def prodigal_time_out_1_open(self, player):
        return self.prodigal_has_colors(player, 2)
    def prodigal_time_out_2_open(self, player):
        return self.prodigal_has_colors(player, 2)
    def prodigal_has_enough_coins(self, player):
        return self.has("Coin of Crowl", player, self.multiworld.coins_of_crowl_required[player])
    def prodigal_has_enough_blessings(self, player):
        return self.prodigal_has_blessings(player, self.multiworld.blessings_required[player])
    def prodigal_has_colors(self, player, count):
        return self.count("Shattered Soul", player) + self.count("Fury Heart", player) + \
                self.count("Frozen Heart", player) + self.count("Red Crystal", player) + \
                self.count("Sunset Painting", player) >= count
    def prodigal_has_blessings(self, player, count):
        return self.count("Life Blessing", player) + self.count("Light Blessing", player) + \
                self.count("Storm Blessing", player) + self.count("Earth Blessing", player) + \
                self.count("Water Blessing", player) >= count
    def prodigal_can_kill_grelins(self, player):
        return self.can_reach("Waterfall Cave - Item", "Location", player) or \
                self.can_reach("Magma Heart - Main Room Left Chest", "Location", player)
    def prodigal_has_tar(self, player):
        return self.can_reach("Crocasino - Hidden Chest", "Location", player)
    def prodigal_can_enter_tidal_mines(self, player):
        return self.has_any({"Progressive Hand", "Lariat"}, player) and \
                (self.has("Progressive Pick", player) or (self.has("Lariat", player) and
                (self.has("Progressive Knuckle", player, 2) or self.prodigal_skips(player))) or
                self.prodigal_can_long_jump(player))
    def prodigal_can_enter_east_crystal_caves(self, player):
        return (self.has("Progressive Knuckle", player, 2) or self.has("Lariat", player)) and \
                (self.prodigal_can_long_jump(player) or (self.has("Progressive Pick", player) and
                (self.prodigal_skips(player) or self.has("Lariat", player) or self.prodigal_has_cleats(player))))
    def prodigal_can_enter_northeast_crystal_caves(self, player):
        return self.prodigal_can_enter_east_crystal_caves(player) and self.has("Progressive Knuckle", player, 2) and \
                (self.has("Progressive Pick", player) or self.has("Lariat", player) or self.prodigal_can_long_jump(player)) and \
                self.prodigal_has_key("Crystal Caves", player, 2)