import logging
log = logging.getLogger(__name__)

import randomizer_options as rng_opt
import key_items_setup as key_items_s
import items_setup as item_s
import locations_setup as loc_s
import shops_setup as shop_s
import item_table as item_t



def make_difficulty_order_dict(rng_diff, item_diff):
    if item_diff == item_s.ITEM_DIF.SMALL_SOUL:
        item_diff = item_s.ITEM_DIF.EASY
    if item_diff == item_s.ITEM_DIF.KEY:
        item_diff = item_s.ITEM_DIF.HARD
    if item_diff == item_s.ITEM_DIF.BIG_SOUL:
        item_diff = item_s.ITEM_DIF.HARD
    
    MASTER_ORDER_DICT = {
        (rng_opt.RandOptDifficulty.EASY, item_s.ITEM_DIF.EASY): {0: [loc_s.LOC_DIF.EASY, loc_s.LOC_DIF.MEDIUM, loc_s.LOC_DIF.HARD]},
        (rng_opt.RandOptDifficulty.EASY, item_s.ITEM_DIF.MEDIUM): {0: [loc_s.LOC_DIF.EASY, loc_s.LOC_DIF.MEDIUM, loc_s.LOC_DIF.HARD]},
        (rng_opt.RandOptDifficulty.EASY, item_s.ITEM_DIF.HARD): {0: [loc_s.LOC_DIF.EASY, loc_s.LOC_DIF.MEDIUM, loc_s.LOC_DIF.HARD]},
        (rng_opt.RandOptDifficulty.EASY, item_s.ITEM_DIF.NPC_EASY): {0: [loc_s.LOC_DIF.NPC_EASY, loc_s.LOC_DIF.NPC_MEDIUM, loc_s.LOC_DIF.NPC_HARD]},
        (rng_opt.RandOptDifficulty.EASY, item_s.ITEM_DIF.NPC_MEDIUM): {0: [loc_s.LOC_DIF.NPC_EASY, loc_s.LOC_DIF.NPC_MEDIUM, loc_s.LOC_DIF.NPC_HARD]},
        (rng_opt.RandOptDifficulty.EASY, item_s.ITEM_DIF.NPC_HARD): {0: [loc_s.LOC_DIF.NPC_EASY, loc_s.LOC_DIF.NPC_MEDIUM, loc_s.LOC_DIF.NPC_HARD]},
        (rng_opt.RandOptDifficulty.EASY, item_s.ITEM_DIF.SALABLE_EASY): {0: [loc_s.LOC_DIF.SHOP_EASY, loc_s.LOC_DIF.SHOP_MEDIUM, loc_s.LOC_DIF.SHOP_HARD]},
        (rng_opt.RandOptDifficulty.EASY, item_s.ITEM_DIF.SALABLE_MEDIUM): {0: [loc_s.LOC_DIF.SHOP_EASY, loc_s.LOC_DIF.SHOP_MEDIUM, loc_s.LOC_DIF.SHOP_HARD]},
        (rng_opt.RandOptDifficulty.EASY, item_s.ITEM_DIF.SALABLE_HARD): {0: [loc_s.LOC_DIF.SHOP_EASY, loc_s.LOC_DIF.SHOP_MEDIUM, loc_s.LOC_DIF.SHOP_HARD]},
        (rng_opt.RandOptDifficulty.MEDIUM, item_s.ITEM_DIF.EASY): {0: [loc_s.LOC_DIF.EASY], 1: [loc_s.LOC_DIF.MEDIUM, loc_s.LOC_DIF.HARD]},
        (rng_opt.RandOptDifficulty.MEDIUM, item_s.ITEM_DIF.MEDIUM): {0: [loc_s.LOC_DIF.MEDIUM], 1: [loc_s.LOC_DIF.EASY, loc_s.LOC_DIF.HARD]},
        (rng_opt.RandOptDifficulty.MEDIUM, item_s.ITEM_DIF.HARD): {0: [loc_s.LOC_DIF.MEDIUM, loc_s.LOC_DIF.HARD], 1: [loc_s.LOC_DIF.EASY]},
        (rng_opt.RandOptDifficulty.MEDIUM, item_s.ITEM_DIF.NPC_EASY): {0: [loc_s.LOC_DIF.NPC_EASY], 1: [loc_s.LOC_DIF.NPC_MEDIUM, loc_s.LOC_DIF.NPC_HARD]},
        (rng_opt.RandOptDifficulty.MEDIUM, item_s.ITEM_DIF.NPC_MEDIUM): {0: [loc_s.LOC_DIF.NPC_MEDIUM], 1: [loc_s.LOC_DIF.NPC_EASY, loc_s.LOC_DIF.NPC_HARD]},
        (rng_opt.RandOptDifficulty.MEDIUM, item_s.ITEM_DIF.NPC_HARD): {0: [loc_s.LOC_DIF.NPC_MEDIUM, loc_s.LOC_DIF.NPC_HARD], 1: [loc_s.LOC_DIF.NPC_EASY]},
        (rng_opt.RandOptDifficulty.MEDIUM, item_s.ITEM_DIF.SALABLE_EASY): {0: [loc_s.LOC_DIF.SHOP_EASY], 1: [loc_s.LOC_DIF.SHOP_MEDIUM, loc_s.LOC_DIF.SHOP_HARD]},
        (rng_opt.RandOptDifficulty.MEDIUM, item_s.ITEM_DIF.SALABLE_MEDIUM): {0: [loc_s.LOC_DIF.SHOP_MEDIUM], 1: [loc_s.LOC_DIF.SHOP_EASY, loc_s.LOC_DIF.SHOP_HARD]},
        (rng_opt.RandOptDifficulty.MEDIUM, item_s.ITEM_DIF.SALABLE_HARD): {0: [loc_s.LOC_DIF.SHOP_MEDIUM, loc_s.LOC_DIF.SHOP_HARD], 1: [loc_s.LOC_DIF.SHOP_EASY]},
        (rng_opt.RandOptDifficulty.HARD, item_s.ITEM_DIF.EASY): {0: [loc_s.LOC_DIF.EASY], 1: [loc_s.LOC_DIF.MEDIUM], 2: [loc_s.LOC_DIF.HARD]},
        (rng_opt.RandOptDifficulty.HARD, item_s.ITEM_DIF.MEDIUM): {0: [loc_s.LOC_DIF.MEDIUM], 1: [loc_s.LOC_DIF.EASY, loc_s.LOC_DIF.HARD]},
        (rng_opt.RandOptDifficulty.HARD, item_s.ITEM_DIF.HARD): {0: [loc_s.LOC_DIF.HARD], 1: [loc_s.LOC_DIF.MEDIUM], 2: [loc_s.LOC_DIF.EASY]},
        (rng_opt.RandOptDifficulty.HARD, item_s.ITEM_DIF.NPC_EASY): {0: [loc_s.LOC_DIF.NPC_EASY], 1: [loc_s.LOC_DIF.NPC_MEDIUM], 2: [loc_s.LOC_DIF.NPC_HARD]},
        (rng_opt.RandOptDifficulty.HARD, item_s.ITEM_DIF.NPC_MEDIUM): {0: [loc_s.LOC_DIF.NPC_MEDIUM], 1: [loc_s.LOC_DIF.NPC_EASY, loc_s.LOC_DIF.NPC_HARD]},
        (rng_opt.RandOptDifficulty.HARD, item_s.ITEM_DIF.NPC_HARD): {0: [loc_s.LOC_DIF.NPC_HARD], 1: [loc_s.LOC_DIF.NPC_MEDIUM], 2: [loc_s.LOC_DIF.NPC_EASY]},
        (rng_opt.RandOptDifficulty.HARD, item_s.ITEM_DIF.SALABLE_EASY): {0: [loc_s.LOC_DIF.SHOP_EASY], 1: [loc_s.LOC_DIF.SHOP_MEDIUM], 2: [loc_s.LOC_DIF.SHOP_HARD]},
        (rng_opt.RandOptDifficulty.HARD, item_s.ITEM_DIF.SALABLE_MEDIUM): {0: [loc_s.LOC_DIF.SHOP_MEDIUM], 1: [loc_s.LOC_DIF.SHOP_EASY, loc_s.LOC_DIF.SHOP_HARD]},
        (rng_opt.RandOptDifficulty.HARD, item_s.ITEM_DIF.SALABLE_HARD): {0: [loc_s.LOC_DIF.SHOP_HARD], 1: [loc_s.LOC_DIF.SHOP_MEDIUM], 2: [loc_s.LOC_DIF.SHOP_EASY]}
    }
    
    if (rng_diff, item_diff) in MASTER_ORDER_DICT:
        return MASTER_ORDER_DICT[(rng_diff, item_diff)]
    else:
        return {}
        
        
def eval_location_for_itemlotpart(table, loc_id, itemlotpart):
    loc = table.location_dict[loc_id]
    if any(i in shop_s.DEFAULT_SHOP_DATA for i in [loc_id] + loc.linked_locations):
        # Shop locations cannot accept an item with a flag that is not shop-safe,
        #  i.e. would clobber or be clobbered by an item in 8 flag range.
        if not itemlotpart.flag_can_tolerate_shop:
            return False
        # Shop locations with flags cannot accept an item that has a non-1 count, since this
        #  ruins checks against that flag, due to quantity purchased spreading over 8 flags.
        elif loc.has_flag != -1 and itemlotpart.items[0].count != 1:
            return False
    # Do not place a None item in a location that has size not 10 (and therefore 
    #  could cause other locations to not drop, if they are actually part of the
    #  same in-game location (like an NPC drop).
    if (loc.max_size != 10 and len(itemlotpart.items) == 1 and 
     itemlotpart.items[0].item_type == item_s.ITEM_TYPE.NONE):
        return False
    return True

# difficulty_dict has orderable keys (typically integers), and sets of difficulties from LOC_DIF as values.
#  More forward-ordered keys are of higher priority, and those difficulties will
#  appear more toward the start of the list.
# Note: Creates the shuffling is prioritized based on the current size, so that 
#  empty locations have higher priority.
#  So, the ordering is, lexicographically, current_size > difficulty_dict > randomness
def create_random_placement_list(table, difficulty_dict, itemlotpart_to_place, random_source):
    log.debug("Creating random placement list.")
    return_list = []
    for diff_val in sorted(difficulty_dict.keys()):
        diff_set = difficulty_dict[diff_val]
        temp_list = [loc_id for loc_id in table.location_dict if 
         table.location_dict[loc_id].diff in diff_set and 
         table.has_room_at_location_for_itemlotpart(itemlotpart_to_place, loc_id) and
         eval_location_for_itemlotpart(table, loc_id, itemlotpart_to_place)]
        # Sort the list before shuffling, so that key ordering does not
        #  contribute to the final result.
        temp_list.sort()
        random_source.shuffle(temp_list)
        #temp_list.sort(key = lambda loc_id: len(table.get_item_at_location(loc_id)))
        return_list += temp_list
    return_list.sort(key = lambda loc_id: len(table.get_item_at_location(loc_id)))
    return return_list
    
def find_key_item_by_name(key_name):
    if key_name not in key_items_s.KEY_NAMES:
        return None
    else:
        key_item_list = [item_s.ITEMS[item_id] for item_id in item_s.ITEMS if 
         item_s.ITEMS[item_id].diff == item_s.ITEM_DIF.KEY and 
         item_s.ITEMS[item_id].key_name == key_name]
        if len(key_item_list) == 0:
            raise ValueError("Key item '" + str(key_name) + "' has no known key.")
        else:
            return key_item_list[0]
                              
def transmute_itemlotpart_to_upgrade(itemlotpart, random_source):
    (upgrade_id, upgrade_count) = random_source.choice(sorted(item_s.UPGRADES))
    itemlotpart.items = [item_s.ItemLotEntry(item_s.ITEM_TYPE.ITEM, upgrade_id, count = upgrade_count)]
    log.debug("Transmuting itemlotpart into upgrade item " + str(upgrade_id))
    return itemlotpart
    
def transmute_itemlotpart_to_rng_drop_upgrade(itemlotpart, random_source):
    (upgrade_common_id, upgrade_common_count) = random_source.choice(sorted(item_s.RANDOM_UPGRADE_COMMON))
    (upgrade_uncommon_id, upgrade_uncommon_count) = random_source.choice(sorted(item_s.RANDOM_UPGRADE_UNCOMMON))
    (upgrade_rare_id, upgrade_rare_count) = random_source.choice(sorted(item_s.RANDOM_UPGRADE_RARE))
    (upgrade_ultrarare_id, upgrade_ultrarare_count) = random_source.choice(sorted(item_s.RANDOM_UPGRADE_ULTRARARE))
    
    entry_none = item_s.ItemLotEntry(item_s.ITEM_TYPE.NONE, 0, count = 0, rate = 10)
    entry_common = item_s.ItemLotEntry(item_s.ITEM_TYPE.ITEM, upgrade_common_id, count = upgrade_common_count, rate = 30, luck = False)
    entry_uncommon = item_s.ItemLotEntry(item_s.ITEM_TYPE.ITEM, upgrade_uncommon_id, count = upgrade_uncommon_count, rate = 25, luck = False)
    entry_rare = item_s.ItemLotEntry(item_s.ITEM_TYPE.ITEM, upgrade_rare_id, count = upgrade_rare_count, rate = 20, luck = False)
    entry_ultrarare = item_s.ItemLotEntry(item_s.ITEM_TYPE.ITEM, upgrade_ultrarare_id, count = upgrade_ultrarare_count, rate = 15, luck = False)

    itemlotpart.items = [entry_none, entry_common, entry_uncommon, entry_rare, entry_ultrarare]
    log.debug("Transmuting itemlotpart into RNG drop upgrade (" + 
     str(upgrade_common_id) + " x" + str(upgrade_common_count) + ", " + 
     str(upgrade_uncommon_id) + " x" + str(upgrade_uncommon_count) +  ", " + 
     str(upgrade_rare_id) + " x" + str(upgrade_rare_count) + ", " +
     str(upgrade_ultrarare_id) + " x" + str(upgrade_ultrarare_count) + ")")
    return itemlotpart
    
def transmute_itemlotpart_to_consumable(itemlotpart, random_source):
    (cons_type, cons_id, cons_count_min, cons_count_max) = random_source.choice(sorted(item_s.RANDOM_CONSUMABLES))
    cons_count = random_source.randrange(cons_count_min, cons_count_max + 1)
    itemlotpart.items = [item_s.ItemLotEntry(cons_type, cons_id, count = cons_count)]
    log.debug("Transmuting itemlotpart into consumable (" + str(cons_type) + ", " +
     str(cons_id) + ", " + str(cons_count) + ")")
    return itemlotpart
    

def place_ignored_items(table):
    log.info("Placing ignored items.")
    for loc_id in table.location_dict:
        loc = table.location_dict[loc_id]
        if loc.diff in [loc_s.LOC_DIF.IGNORE, loc_s.LOC_DIF.EMPTY, loc_s.LOC_DIF.LEAVE_ALONE]:
            log.debug("Placing ignored item ID# " + str(loc_id) + " at location ID# " + str(loc_id))
            table.place_itemlotpart_at_location(item_s.ITEMS[loc_id], loc_id)

def place_upgrade_items(table, random_source):
    log.info("Placing upgrade items.")
    for loc_id in table.location_dict:
        loc = table.location_dict[loc_id]
        if loc.diff in [loc_s.LOC_DIF.UPGRADE, loc_s.LOC_DIF.RANDOM_UPGRADE]:
            log.debug("Placing upgrade item at location ID# " + str(loc_id))
            itemlotpart = item_s.ITEMS[loc_id]
            if loc.diff == loc_s.LOC_DIF.UPGRADE:
                itemlotpart = transmute_itemlotpart_to_upgrade(itemlotpart, random_source)
            if loc.diff == loc_s.LOC_DIF.RANDOM_UPGRADE:
                itemlotpart = transmute_itemlotpart_to_rng_drop_upgrade(itemlotpart, random_source)
            table.place_itemlotpart_at_location(itemlotpart, loc_id)
            
def place_key_items(table, rand_options, random_source):
    log.info("Placing key items.")
    current_key_locations = {}
    if rand_options.key_placement == rng_opt.RandOptKeyDifficulty.LEAVE_ALONE:
        log.info("Placing key items in vanilla locations.")
        # Find the original locations of all the keys, and place them there.
        for key_name in key_items_s.KEY_NAMES:
            key_itemlotpart = find_key_item_by_name(key_name)
            for loc_id in table.location_dict:
                loc = table.location_dict[loc_id]
                if loc.default_key == key_name:
                    table.place_itemlotpart_at_location(key_itemlotpart, loc_id)
                    current_key_locations[key_name] = loc
    else:
        log.info("Placing key items in random locations.")
        for key in key_items_s.KEY_NAMES:
            current_key_locations[key] = "cannot_place"       
        current_areas = set(["starting"])
        
        if not rand_options.use_lordvessel:
            log.info("Placing Lordvessel in vanilla location.")
            lv_loc_ids = [loc_id for loc_id in table.location_dict
             if table.location_dict[loc_id].default_key == "lordvessel"]
            first_lv_loc_id = lv_loc_ids[0]
            current_key_locations["lordvessel"] = table.location_dict[first_lv_loc_id]
            lv_item = find_key_item_by_name("lordvessel")
            table.place_itemlotpart_at_location(lv_item, first_lv_loc_id)
            
        key_items_s.update_locations_and_keys(current_key_locations, current_areas)
    
        while(len([key for key in current_key_locations if not key_items_s.key_placed(key, current_key_locations)]) > 0):
            keys_to_place = sorted([key for key in current_key_locations if current_key_locations[key] == "to_place"])         
            random_source.shuffle(keys_to_place)
            for key_name in keys_to_place:
                log.info("Attempting to place key '" + key_name + "'.")
                key = find_key_item_by_name(key_name)               
                plausible_loc_ids = create_random_placement_list(table, 
                 make_difficulty_order_dict(rand_options.difficulty, key.diff), key, random_source)
                pre_possible_locations = [table.location_dict[loc_id] for loc_id in plausible_loc_ids if 
                 key_items_s.is_location_okay_for_key(key_name, table.location_dict[loc_id], 
                 current_key_locations, current_areas)]
                
                if rand_options.key_placement == rng_opt.RandOptKeyDifficulty.RACE_MODE:
                    possible_locations = [loc for loc in pre_possible_locations if loc.is_race_key_loc]
                else:
                    possible_locations = pre_possible_locations
                
                if len(possible_locations) > 0:
                    loc = possible_locations[0]
                    table.place_itemlotpart_at_location(key, loc.location_id)
                    current_key_locations[key_name] = loc
                    break
            key_items_s.update_locations_and_keys(current_key_locations, current_areas)
            log.debug("current_key_locations: " + str(current_key_locations))
            log.debug("current_areas: " + str(current_areas))
    table.key_locs = current_key_locations
            
def get_price_for_difficulty(diff, itemlotpart, random_source):
    if diff not in shop_s.PRICE_DISTIBUTION:
        return None
    else:
        possible_prices = shop_s.PRICE_DISTIBUTION[diff]
        if itemlotpart.diff in [item_s.ITEM_DIF.SALABLE_EASY, 
         item_s.ITEM_DIF.SALABLE_MEDIUM, item_s.ITEM_DIF.SALABLE_HARD]:
             min_price = shop_s.SALABLE_MIN_SELL_PRICE[(itemlotpart.items[0].item_type, itemlotpart.items[0].item_id)]
             possible_prices = [x for x in possible_prices if x >= min_price]
        return random_source.choice(possible_prices)

            
def place_non_key_fixed_items(table, rand_options, random_source):
    log.info("Placing non-key fixed items.")
    item_ids_to_place = [item_id for item_id in item_s.ITEMS if 
     item_s.ITEMS[item_id].diff in [item_s.ITEM_DIF.EASY, item_s.ITEM_DIF.MEDIUM, 
     item_s.ITEM_DIF.HARD, item_s.ITEM_DIF.SMALL_SOUL, item_s.ITEM_DIF.BIG_SOUL, 
     item_s.ITEM_DIF.NPC_EASY, item_s.ITEM_DIF.NPC_MEDIUM, item_s.ITEM_DIF.NPC_HARD,
     item_s.ITEM_DIF.SALABLE_EASY, item_s.ITEM_DIF.SALABLE_MEDIUM, item_s.ITEM_DIF.SALABLE_HARD]]
     
    if rand_options.fashion_souls:
        # If Fashion Souls is on, stop EASY, MEDIUM, HARD, SMALL_SOUL, BIG_SOUL 
        #  items from following other items.
        for item_id in item_ids_to_place:
            if item_s.ITEMS[item_id].diff in [item_s.ITEM_DIF.EASY, 
             item_s.ITEM_DIF.MEDIUM, item_s.ITEM_DIF.HARD, 
             item_s.ITEM_DIF.SMALL_SOUL, item_s.ITEM_DIF.BIG_SOUL]:
                item_s.ITEMS[item_id].follow_items = []
    # Remove following items from items_to_place.
    following_items = set(f_item_id for item_id in item_ids_to_place for 
     f_item_id in item_s.ITEMS[item_id].follow_items)
    item_ids_to_place = [item_id for item_id in item_ids_to_place if 
     item_id not in following_items]
    item_ids_to_place.sort(key = lambda item_id: item_s.ITEMS[item_id].get_max_effective_size(), reverse = True)
    
    for item_id in item_ids_to_place:
        item = item_s.ITEMS[item_id]
        
        # Deal with soul consumables, if needed.
        if item.diff in [item_s.ITEM_DIF.SMALL_SOUL, item_s.ITEM_DIF.BIG_SOUL]:
            if rand_options.soul_items_diff == rng_opt.RandOptSoulItemsDifficulty.CONSUMABLE:
                item = transmute_itemlotpart_to_consumable(item, random_source)
                
        # Fix count on infinitely-sold items.
        if item.diff in [item_s.ITEM_DIF.SALABLE_EASY, item_s.ITEM_DIF.SALABLE_MEDIUM, 
         item_s.ITEM_DIF.SALABLE_HARD]:
             item.items[0].count = -1
        
        # Place item.
        possible_loc_ids = create_random_placement_list(table, 
         make_difficulty_order_dict(rand_options.difficulty, item.diff), item, random_source)
        if len(possible_loc_ids) > 0:
            loc_id = possible_loc_ids[0]
            price_overwrite = get_price_for_difficulty(table.location_dict[loc_id].diff, item, random_source)
            if price_overwrite != None:
                log.info("Placing ItemLotPart ID# " + str(item_id) + " at location ID# " + str(loc_id) + " with price " + str(price_overwrite))
            else:
                log.info("Placing ItemLotPart ID# " + str(item_id) + " at location ID# " + str(loc_id))
            table.place_itemlotpart_at_location(item, loc_id, price = price_overwrite)
        else:
            log.warn("Warning: Could not place ItemLotPart ID# " + str(item_id) + " during non-key fixed item placement.")

def place_starting_equipment(table, rand_options, random_source):
    log.info("Placing starting equipment.")
    for start_class in loc_s.STARTING_ITEM_TABLE:
        class_gear = item_s.CLASS_STARTING_GEAR[start_class]
        
        # Deal with the left- and right-hand items first.
        lh_location_id = loc_s.STARTING_ITEM_TABLE[start_class]["left_hand"]
        rh_location_id = loc_s.STARTING_ITEM_TABLE[start_class]["right_hand"]
        if rand_options.start_items_diff == rng_opt.RandOptStartItemsDifficulty.SHIELD_AND_1H:
            lh_pool = class_gear["shields"]
            rh_pool = class_gear["weapons_1h"]
        elif rand_options.start_items_diff == rng_opt.RandOptStartItemsDifficulty.SHIELD_AND_2H:
            lh_pool = class_gear["shields"]
            rh_pool = class_gear["weapons_2h"]
        elif rand_options.start_items_diff == rng_opt.RandOptStartItemsDifficulty.COMBINED_POOL_AND_2H:
            lh_pool = class_gear["shields"] + class_gear["weapons_2h"]
            rh_pool = class_gear["weapons_2h"]
        else:
            raise ValueError("Bad starting item difficulty. Received: " + str(rand_options.start_items_diff))
            
        lh_item_id = random_source.choice(sorted(lh_pool))
        rh_item_id = random_source.choice(sorted(rh_pool))
        lh_item = item_s.ItemLotPart(item_s.ITEM_DIF.EASY, 4, [item_s.ItemLotEntry(item_s.ITEM_TYPE.WEAPON, lh_item_id)])
        rh_item = item_s.ItemLotPart(item_s.ITEM_DIF.EASY, 4, [item_s.ItemLotEntry(item_s.ITEM_TYPE.WEAPON, rh_item_id)])
        
        table.place_itemlotpart_at_location(lh_item, lh_location_id)
        table.place_itemlotpart_at_location(rh_item, rh_location_id)
            
        # Deal with extra items, if needed.
        if "extra" in loc_s.STARTING_ITEM_TABLE[start_class]:
            extra_location_id = loc_s.STARTING_ITEM_TABLE[start_class]["extra"]
            
            pool_groups = class_gear["extra"]
            pools = random_source.choice(pool_groups)
            for (pool, count) in pools:
                extra_item_id = random_source.choice(sorted(pool))
                extra_item = item_s.ItemLotPart(item_s.ITEM_DIF.EASY, 4, [item_s.ItemLotEntry(item_s.ITEM_TYPE.WEAPON, extra_item_id, count = count)])
                table.place_itemlotpart_at_location(extra_item, extra_location_id)
                
def build_table(rand_options, random_source):
    table = item_t.ItemTable(loc_s.LOCATIONS)
    place_ignored_items(table)
    place_upgrade_items(table, random_source)
    place_key_items(table, rand_options, random_source)
    place_starting_equipment(table, rand_options, random_source)
    place_non_key_fixed_items(table, rand_options, random_source)
    table.fix_pickup_flags()
    return table
                
if __name__ == "__main__":
    import random 
    import sys
    
    if len(sys.argv) < 2:
        print "Usage: " + str(sys.argv[0]) + " <seed>"
        sys.exit(1)
    
    seed = sys.argv[1]
    
    #logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    logging.basicConfig(stream=sys.stdout, level=logging.WARN)
    options = rng_opt.RandomizerOptions(
      rng_opt.RandOptDifficulty.EASY, 
      True, 
      rng_opt.RandOptKeyDifficulty.RACE_MODE, 
      True, 
      rng_opt.RandOptSoulItemsDifficulty.SHUFFLE,
      rng_opt.RandOptStartItemsDifficulty.COMBINED_POOL_AND_2H)
    
    rng = random.Random()
    rng.seed(seed)
    table = build_table(options, rng)
    result_ilp = table.build_itemlotparam()
    result_slp = table.build_shoplineup()
    cheat_string = table.build_cheatsheet(show_event_flags = True)
    hint_string = table.build_hintsheet()
    ilp_binary_export = result_ilp.export_as_binary()
    slp_binary_export = result_slp.export_as_binary()
    
    #with open("ItemLotParam.param", 'wb') as f:
    #    f.write(ilp_binary_export)
    #    f.close()
    
    #with open("ShopLineupParam.param", 'wb') as f:
    #    f.write(slp_binary_export)
    #    f.close()
        
    with open("cheatsheet.txt", "w") as f:
        f.write("Seed: " + str(seed) + "\n\n")
        f.write(cheat_string)
        f.close()
        
    with open("hintsheet.txt", "w") as f:
        f.write(hint_string)
        f.close()
    
    #sys.stdout.write("Seed: " + str(seed) + "\n\n")
    #sys.stdout.write(options.as_string())
    #sys.stdout.flush()
    
    #sys.stdout.write(cheat_string)
    #sys.stdout.write(ilp_binary_export)
    #sys.stdout.write(slp_binary_export)
    #sys.stdout.flush()

