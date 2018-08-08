import logging
log = logging.getLogger(__name__)

import items_setup as item_s
import locations_setup as loc_s
import item_lot_formatter

import item_lot_param as ilp
import shop_lineup_param as slp

import itertools

class ItemTable:
    def __init__(self, location_dict = None, shop_dict = None):
        if location_dict == None:
            location_dict = {}
        if shop_dict == None:
            shop_dict = {}
        self.table = {}
        self.location_dict = location_dict
        self.shop_dict = shop_dict
        self.key_locs = {}
        
        for loc_id in location_dict:
            if location_dict[loc_id].location_id != loc_id:
                raise ValueError("Location at index " + str(loc_id) + 
                 " does not have matching location_id.")
            self.table[loc_id] = []
    
    def get_item_at_location(self, loc_id):
        return self.table[loc_id]
            
    def place_itemlotpart_at_location(self, itemlotpart, loc_id, item_list, price = None):
        log.info("Placing itemlotpart with first component (" + 
         str(itemlotpart.items[0].item_type) + ", " + 
         str(itemlotpart.items[0].item_id) + ", " +
         str(itemlotpart.items[0].count) + ") at location ID# " + str(loc_id))
        if not self.has_room_at_location_for_itemlotpart(itemlotpart, loc_id, item_list):
            raise ValueError("Location at index " + str(loc_id) + 
             " cannot accept proposed itemlotpart due to size.")
        else:
            self.table[loc_id] += [itemlotpart] + [item_list[i] for i in itemlotpart.follow_items]
        if price != None:
            for linkloc_id in [loc_id] + self.location_dict[loc_id].linked_locations:
                if linkloc_id in self.shop_dict:
                    log.info("Setting price of location ID# " + str(linkloc_id) + " to " + str(price))
                    self.shop_dict[linkloc_id].cost = price
                    
    def has_room_at_location_for_itemlotpart(self, itemlotpart, loc_id, item_list):
        if loc_id not in self.table:
            raise KeyError("ItemTable does not have location with ID " + str(loc_id))
        
        max_size = self.location_dict[loc_id].max_size
        current_size = len(self.table[loc_id])
        item_size = 1 + len(itemlotpart.follow_items)
        
        #log.debug("Max Size: " + str(max_size) + ", Current Size: " + 
        # str(current_size) + ", Item Size: " + str(item_size))
        
        location = self.location_dict[loc_id]
        
        proposed_new_itemlot = self.table[loc_id] + [itemlotpart] + [item_list[i] for i in itemlotpart.follow_items]
        proposed_flags = [i.flag for i in proposed_new_itemlot]
        has_replaceable_flag = (len([i.flag for i in proposed_new_itemlot if not i.needs_flag]) > 0)
        
        if (location.has_flag != -1 and location.has_flag not in proposed_flags and not has_replaceable_flag):
             # This location needs a flag, and none of the proposed items can 
             #  accept a flag modification, so a dummy item will need to be
             #  used.
            return current_size + item_size + 1 <= max_size
        else:
            return current_size + item_size <= max_size
            
    def build_flag_usage_dict(self, loc_id):
        return_dict = {}
        loc = self.location_dict[loc_id]
        for itemlotpart in self.table[loc_id]:
            if itemlotpart.flag not in return_dict:
                return_dict[itemlotpart.flag] = {"length": 0, "req": False, "at_start": False}
            return_dict[itemlotpart.flag]["length"] += 1
            if itemlotpart.needs_flag:
                return_dict[itemlotpart.flag]["req"] = True
        if loc.has_flag != -1:
            if loc.has_flag not in return_dict:
                return_dict[loc.has_flag] = {"length": 0, "req": True, "at_start": True}
            else:
                return_dict[loc.has_flag]["req"] = True
                return_dict[loc.has_flag]["at_start"] = True
        return return_dict
        
    def reduce_flag_usage(self, loc_id):
        MAX_FLAG_GROUP_LEN = 5
        
        change_made = False
        flag_usage_dict = self.build_flag_usage_dict(loc_id)
        log.debug("flag_usage_dict: " + str(flag_usage_dict))
        sorted_flags = sorted(list(flag_usage_dict.keys()), key = lambda flag: flag_usage_dict[flag]["length"], reverse = True)
        for (flag1, flag2) in itertools.product(sorted_flags, repeat = 2):
            if (flag1 < flag2 and not (flag_usage_dict[flag1]["req"] and flag_usage_dict[flag2]["req"]) and
             flag_usage_dict[flag1]["length"] + flag_usage_dict[flag2]["length"] <= MAX_FLAG_GROUP_LEN):
                dominant_flag = flag1
                recessive_flag = flag2
                if flag_usage_dict[flag2]["req"]:
                    dominant_flag = flag2
                    recessive_flag = flag1
                log.debug("Replacing flag " + str(recessive_flag) +
                 " with flag " + str(dominant_flag) + " at location ID# " +
                 str(loc_id))
                for itemlotpart in self.table[loc_id]:
                    if itemlotpart.flag == recessive_flag:
                        itemlotpart.flag = dominant_flag
                change_made = True
                break
        return change_made
            
    def merge_flags(self, loc_id):
        change_made = True
        while change_made:
            change_made = self.reduce_flag_usage(loc_id)
        
        # Check for required flags that have no itemlotpart.
        #  A dummy item is needed to carry the flag in this case.
        flag_usage_dict = self.build_flag_usage_dict(loc_id)
        for flag in flag_usage_dict:
            if flag_usage_dict[flag]["length"] == 0:
                log.info("Adding dummy item at location ID# " + str(loc_id) + 
                 " to represent flag " + str(flag))
                dummy = item_s.ItemLotPart(item_s.ITEM_DIF.EASY, 2, 
                 [item_s.ItemLotEntry(item_s.ITEM_TYPE.ITEM, 330)], flag = flag, needs_flag = True)
                old_item_list = self.table[loc_id]
                self.table[loc_id] = [dummy] + old_item_list
        
        # Sort item list to collect items with the same flag together.
        self.table[loc_id].sort(key = lambda item: item.flag)
        
        # Sort item list to bring flags that must be at the start to the start.
        # Note that this preserves the collections above, but moves 0+ of these
        #  collections to the start of the item list.
        # * Since False < True, this sort will work.
        self.table[loc_id].sort(key = lambda item: (not flag_usage_dict[item.flag]["at_start"]))

    # Should only be called after the entire table is constructed.
    def fix_pickup_flags(self):
        log.info("Fixing pickup flags.")
        BASE_NEWLY_CREATED_FLAG = 51812000
        
        # Add flags used by unshuffled locations to the conflict list.
        used_flags = set([])
        free_flags = set([])
        for loc_id in sorted(self.location_dict):
            loc = self.location_dict[loc_id]
            if loc.diff in [loc_s.LOC_DIF.IGNORE, 
             loc_s.LOC_DIF.EMPTY, 
             loc_s.LOC_DIF.LEAVE_ALONE] and loc.has_flag != -1:
                self.merge_flags(loc_id)
                flags_after_merge = self.build_flag_usage_dict(loc_id)
                for flag in flags_after_merge:
                    log.debug("Adding flag " + str(flag) + " to used_flags.")
                    used_flags.add(flag)
        
        current_newly_created_flag = BASE_NEWLY_CREATED_FLAG
        
        # Deal with 100% fixed item drops.
        log.info("Fixing 100% fixed item drop pickup flags.")
        for loc_id in sorted(self.location_dict):
            loc = self.location_dict[loc_id]
            if loc.diff in [loc_s.LOC_DIF.EASY, loc_s.LOC_DIF.MEDIUM, 
             loc_s.LOC_DIF.HARD, loc_s.LOC_DIF.STARTING_ITEM]:
                 
                log.info("Fixing flags at location ID# " + str(loc_id))
                # Remove any flags that are in used_flags or currently in use in this
                #  item lot from free_flags, since they should not be considered freed.
                for item in self.table[loc_id]:
                    if item.flag in free_flags:
                        log.debug("Discarding flag " + str(item.flag) + 
                            " from free_flags, since it is in use at location ID# " + str(loc_id))
                        free_flags.discard(item.flag)
                for flag in used_flags:
                    if flag in free_flags:
                        log.debug("Discarding flag " + str(flag) + 
                            " from free_flags, since it is in used_flags")
                        free_flags.discard(flag)
                
                # Deal with items that have a previously used flag, or have no flag.
                for item in self.table[loc_id]:
                    if item.flag in used_flags or item.flag == -1:
                        log.debug("Replacing already used flag " + str(item.flag) + ".")
                        flag_to_replace = item.flag
                        # Get a new flag to replace this one.
                        if free_flags:
                            new_flag = free_flags.pop()
                            log.debug("Popping flag " + str(new_flag) + " from free_flags.")
                        else:
                            new_flag = current_newly_created_flag
                            log.debug("Creating new flag " + str(new_flag) + " since free_flags is empty.")
                            current_newly_created_flag = current_newly_created_flag + 10
                        
                        # Replace the offending flag with the new one.
                        #  Items that are missing a flag get a unique flag,
                        #  rather than the same new flag for every such item.
                        if item.flag == -1:
                            item.flag = new_flag
                        else:
                            for item_2 in self.table[loc_id]:
                                if item_2.flag == flag_to_replace:
                                    item_2.flag = new_flag
                
                log.info("Merging flags in location ID# " + str(loc_id))
                # Merge flags to (roughly) minimize the number of item groups.
                flags_before_merge = self.build_flag_usage_dict(loc_id)
                self.merge_flags(loc_id)
                flags_after_merge = self.build_flag_usage_dict(loc_id)
                
                # Sort flags, either freeing them for later use, or marking them as used.
                for flag in flags_before_merge:
                    if flag in flags_after_merge:
                        log.debug("Adding flag " + str(flag) + " to used_flags.")
                        used_flags.add(flag)
                    else:
                        log.debug("Pushing flag " + str(flag) + " back onto free_flags.")
                        free_flags.add(flag)
                        
        # Deal with non-100% item drops. (Usually NPC drop tables.)
        log.info("Fixing non-100% item drop pickup flags.")
        for loc_id in sorted(self.location_dict):
            loc = self.location_dict[loc_id]
            if loc.diff in [loc_s.LOC_DIF.NPC_EASY, loc_s.LOC_DIF.NPC_MEDIUM, 
             loc_s.LOC_DIF.NPC_HARD, loc_s.LOC_DIF.UPGRADE, 
             loc_s.LOC_DIF.RANDOM_UPGRADE]: 
                 for item in self.table[loc_id][1:]:
                     item.flag = -2

    def build_itemlotparam(self):
        CATEGORY_TRANSLATION = {
         item_s.ITEM_TYPE.WEAPON: ilp.ItemLotItemType.WEAPON,
         item_s.ITEM_TYPE.ARMOR: ilp.ItemLotItemType.ARMOR,
         item_s.ITEM_TYPE.RING: ilp.ItemLotItemType.RING,
         item_s.ITEM_TYPE.ITEM: ilp.ItemLotItemType.ITEM,
         item_s.ITEM_TYPE.NONE: ilp.ItemLotItemType.NONE,
         item_s.ITEM_TYPE.SHOP_SPELL: ilp.ItemLotItemType.ITEM
        } 
        
        log.info("Building ItemLotParam from ItemTable.")
        
        result = ilp.ItemLotParam()
        
        for loc_id in self.location_dict:
            loc = self.location_dict[loc_id]
            itemlotparts = self.table[loc_id]
            log.info("Processing location ID# " + str(loc_id) + " holding " + 
             str(len(itemlotparts)) + " itemlotparts.")
            for itemlotpart in itemlotparts:
                # Build item list for this itemlotpart.
                items = []
                for entry in itemlotpart.items:
                    item = ilp.ItemLotItem(CATEGORY_TRANSLATION[entry.item_type],
                     entry.item_id, entry.count, entry.rate, 0, 0, entry.luck, False)
                    items.append(item)
                # Deal with locations that have cumulative items.
                if loc.has_cumul_flag and len(items) > 0:
                    items[0].item_weight = loc.has_cumul_flag.chance_numer
                    items[0].item_cumul = loc.has_cumul_flag.cumulative_point
                    items[0].item_cumul_reset = True
                    empty = ilp.ItemLotItem(ilp.ItemLotItemType.NONE, 0, 0, 
                     loc.has_cumul_flag.chance_denom - loc.has_cumul_flag.chance_numer,
                     0, 0, True, False)
                    items = [empty, items[0]]
                    
                cumul_flag = -1
                cumul_count = 0
                if loc.has_cumul_flag and len(items) > 0:
                    cumul_flag = loc.has_cumul_flag.flag
                    cumul_count = loc.has_cumul_flag.count
                
                # Add the Itemlot to the ItemLotParam at each of the 
                #  linked locations as well as the given location.
                #  * Using a dummy '.' as the description, to save space.
                for link_loc_id in [loc_id] + loc.linked_locations:
                    if link_loc_id not in self.shop_dict:
                        for i in range(link_loc_id, link_loc_id + loc.max_size):
                            if not result.has_used_lot_id(i):
                                log.debug("Placing ItemLot at index " + str(i) + " for location # " + str(link_loc_id))
                                itemlot = ilp.ItemLot(i, itemlotpart.flag, cumul_flag, 
                                 cumul_count, itemlotpart.rarity, items, ".")
                                result.item_lots.append(itemlot)
                                break
                log.debug("ItemLotParam now has " + str(len(result.item_lots)) + " item lots.")
        return result

    def build_shoplineup(self):
        CATEGORY_TRANSLATION = {
         item_s.ITEM_TYPE.WEAPON: slp.ShopLineItemType.WEAPON,
         item_s.ITEM_TYPE.ARMOR: slp.ShopLineItemType.ARMOR,
         item_s.ITEM_TYPE.RING: slp.ShopLineItemType.RING,
         item_s.ITEM_TYPE.ITEM: slp.ShopLineItemType.ITEM,
         item_s.ITEM_TYPE.NONE: slp.ShopLineItemType.NONE,
         item_s.ITEM_TYPE.SHOP_SPELL: slp.ShopLineItemType.SHOP_SPELL
        } 
        
        log.info("Building ShopLineupParam from ItemTable.")
        
        result = slp.ShopLineupParam()
    
        for loc_id in self.location_dict:
            loc = self.location_dict[loc_id]
            if len(self.table[loc_id]) > 0 and len(self.table[loc_id][0].items) > 0:
                itemlotpart = self.table[loc_id][0]
                item = itemlotpart.items[0]
                for link_loc_id in [loc_id] + loc.linked_locations:
                    if link_loc_id in self.shop_dict:
                        shop_data = self.shop_dict[link_loc_id]
                        lineup = slp.ShopLineup(shop_data.shop_id, 
                         CATEGORY_TRANSLATION[item.item_type], item.item_id, 
                         shop_data.cost, item.count, itemlotpart.flag,
                         shop_data.mtrl_id, item.count, shop_data.shop_type, ".")
                        log.debug("Placing ShopLineup at index " + str(shop_data.shop_id) + " for location # " + str(link_loc_id))
                        result.shop_lineups.append(lineup)       
        return result

    def build_cheatsheet(self, show_event_flags = False):
        fixed_item_string_list = []
        rng_item_string_list = []
        
        for loc_id in sorted(list(self.location_dict.keys())):
            loc = self.location_dict[loc_id]
            if loc.diff in [loc_s.LOC_DIF.EASY, loc_s.LOC_DIF.MEDIUM, 
             loc_s.LOC_DIF.HARD, loc_s.LOC_DIF.UPGRADE, 
             loc_s.LOC_DIF.STARTING_ITEM, loc_s.LOC_DIF.SHOP_EASY, 
             loc_s.LOC_DIF.SHOP_MEDIUM, loc_s.LOC_DIF.SHOP_HARD]:
                 cost = None
                 if loc_id in self.shop_dict:
                     cost = self.shop_dict[loc_id].cost
                 location_string = item_lot_formatter.format_item_table_entry_as_human_readable(loc, self.table[loc_id], cost = cost, show_event_flags = show_event_flags)
                 fixed_item_string_list.append(location_string)
            elif loc.diff in [loc_s.LOC_DIF.NPC_EASY, loc_s.LOC_DIF.NPC_MEDIUM, 
             loc_s.LOC_DIF.NPC_HARD, loc_s.LOC_DIF.RANDOM_UPGRADE]:
                 location_string = item_lot_formatter.format_item_table_entry_as_human_readable(loc, self.table[loc_id], cost = False, show_event_flags = show_event_flags)
                 rng_item_string_list.append(location_string)
        
        return "\n".join(fixed_item_string_list) + "\n\n" + "\n".join(rng_item_string_list)
        
    def build_hintsheet(self):
        AREA_HINT_NAMES = {
            loc_s.AREA.NONE: "None",
            loc_s.AREA.MOVING_NPC: "Gift/Drop/Shop from an NPC that moves around",
            loc_s.AREA.DEPTHS: "Depths",
            loc_s.AREA.LOWER_UNDEAD_BURG: "Lower Undead Burg",
            loc_s.AREA.LOWER_UNDEAD_BURG_RESIDENCE: "Lower Undead Burg",
            loc_s.AREA.UNDEAD_BURG: "Undead Burg",
            loc_s.AREA.UNDEAD_BURG_RESIDENCE: "Undead Burg",
            loc_s.AREA.WATCHTOWER_BASEMENT: "Watchtower Basement",
            loc_s.AREA.UNDEAD_PARISH: "Undead Parish",
            loc_s.AREA.FIRELINK: "Firelink Shrine",
            loc_s.AREA.PAINTED_WORLD: "Painted World of Ariamis",
            loc_s.AREA.PAINTED_WORLD_ANNEX: "Painted World of Ariamis",
            loc_s.AREA.DARKROOT_GARDEN: "Darkroot Garden",
            loc_s.AREA.DARKROOT_FOREST: "Darkroot Garden",
            loc_s.AREA.DARKROOT_BASIN: "Darkroot Basin",
            loc_s.AREA.OOLACILE_SANCTUARY: "Oolacile Sanctuary",
            loc_s.AREA.ROYAL_WOOD: "Royal Wood",
            loc_s.AREA.OOLACILE_TOWNSHIP: "Oolacile Township",
            loc_s.AREA.OOLACILE_HIDDEN: "Oolacile Township",
            loc_s.AREA.KALAMEET_FIGHT: "Royal Wood",
            loc_s.AREA.CHASM_OF_THE_ABYSS: "Chasm of the Abyss",
            loc_s.AREA.CATACOMBS: "Catacombs",
            loc_s.AREA.TOMB_OF_THE_GIANTS_PRE_LV: "Tomb of the Giants",
            loc_s.AREA.TOMB_OF_THE_GIANTS_POST_LV: "Tomb of the Giants",
            loc_s.AREA.GREAT_HOLLOW: "Great Hollow",
            loc_s.AREA.ASH_LAKE: "Ash Lake",
            loc_s.AREA.BLIGHTTOWN: "Blighttown",
            loc_s.AREA.QUELAAGS_DOMAIN: "Quelaag's Domain",
            loc_s.AREA.DEMON_RUINS_NO_LAVA_PRE_LV: "Demon Ruins",
            loc_s.AREA.DEMON_RUINS_NO_LAVA_POST_LV: "Demon Ruins",
            loc_s.AREA.DEMON_RUINS_LAVA: "Demon Ruins",
            loc_s.AREA.LOST_IZALITH: "Lost Izalith",
            loc_s.AREA.SENS_FORTRESS: "Sen's Fortress",
            loc_s.AREA.SENS_CAGE: "Sen's Fortress",
            loc_s.AREA.ANOR_LONDO: "Anor Londo",
            loc_s.AREA.DARKMOON_TOMB: "Anor Londo",
            loc_s.AREA.NEW_LONDO_PRE_SEAL: "New Londo Ruins",
            loc_s.AREA.NEW_LONDO_POST_LV: "New Londo Ruins",
            loc_s.AREA.NEW_LONDO_POST_SEAL: "New Londo Ruins",
            loc_s.AREA.NEW_LONDO_POST_SEAL_SKIP: "New Londo Ruins",
            loc_s.AREA.VALLEY_OF_DRAKES: "Valley of Drakes",
            loc_s.AREA.POST_4K: "After defeating the Four Kings",
            loc_s.AREA.DUKES_PRISON: "The Duke's Archives",
            loc_s.AREA.DUKES_PRISON_EXTRA: "The Duke's Archives",
            loc_s.AREA.DUKES_PRISON_GIANT_CELL: "The Duke's Archives",
            loc_s.AREA.DUKES_ARCHIVES: "The Duke's Archives",
            loc_s.AREA.CRYSTAL_CAVE: "Crystal Cave",
            loc_s.AREA.KILN: "Kiln of the First Flame",
            loc_s.AREA.UNDEAD_ASYLUM: "Undead Asylum",
            loc_s.AREA.UNDEAD_ASYLUM_F2_WEST: "Undead Asylum",
            loc_s.AREA.NPC_RNG_DROP: "Random Enemy Drop"
        }
        
        KEY_HINT_NAMES = {
            "lordvessel": "Lordvessel", 
            "key_to_the_seal": "Key to the Seal", 
            "blighttown_key": "Blighttown Key",
            "key_to_depths": "Key to Depths", 
            "covenant_of_artorias": "Covenant of Artorias",
            "rite_of_kindling": "Rite of Kindling",
            "orange_charred_ring": "Orange Charred Ring", 
            "sewer_chamber_key": "Sewer Chamber Key", 
            "large_ember": "Large Ember", 
            "mystery_key": "Mystery Key", 
            "basement_key": "Basement Key", 
            "undead_asylum_f2_west_key": "Undead Asylum F2 West Key",
            "annex_key": "Annex Key", 
            "watchtower_basement_key": "Watchtower Basement Key", 
            "darkmoon_seance_ring": "Darkmoon Seance Ring",
            "key_to_new_londo_ruins": "Key to New Londo Ruins", 
            "cage_key": "Cage Key", 
            "archive_prison_extra_key": "Archive Prison Extra Key",
            "archive_tower_giant_cell_key": "Archive Tower Giant Cell Key", 
            "archive_tower_giant_door_key": "Archive Tower Giant Door Key",
            "peculiar_doll": "Peculiar Doll", 
            "broken_pendant": "Broken Pendant", 
            "crest_key": "Crest Key", 
            "crest_of_artorias": "Crest of Artorias",
            "residence_key": "Residence Key", 
            "dark_ember": "Dark Ember", 
            "divine_ember": "Divine Ember", 
            "enchanted_ember": "Enchanted Ember",
            "large_divine_ember": "Large Divine Ember", 
            "large_flame_ember": "Large Flame Ember", 
            "chaos_flame_ember": "Chaos Flame Ember", 
            "very_large_ember": "Very Large Ember", 
            "large_magic_ember": "Large Magic Ember", 
            "crystal_ember": "Crystal Ember",
            "cast_light": "Cast Light",
            "lord_soul_shard_seath": "Bequeathed Lord Soul Shard (Seath)", 
            "lord_soul_shard_four_kings": "Bequeathed Lord Soul Shard (Four Kings)", 
            "lord_soul_bed_of_chaos": "Lord Soul (Bed of Chaos)", 
            "lord_soul_nito": "Lord Soul (Gravelord Nito)",
            "purple_cowards_crystal": "Purple Coward's Crystal"
        }
        
        hintarray = []
        for key_name in self.key_locs:
            key_hint_name = KEY_HINT_NAMES[key_name]
            area_hint_name = AREA_HINT_NAMES[self.key_locs[key_name].area]
            hintarray.append(key_hint_name + ": " + area_hint_name)
        
        return "Hint Locations for Keys:\n\n" + '\n'.join(sorted(hintarray))
            
            
                 
            
                
