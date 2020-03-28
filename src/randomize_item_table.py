import logging
log = logging.getLogger(__name__)

import randomizer_options as rng_opt
import key_items_setup as key_items_s
import items_setup as item_s
import locations_setup as loc_s
import shops_setup as shop_s
import item_table as item_t
import chr_setup as chr_s
import chr_init_param as cip

import copy


def make_difficulty_order_dict(rng_diff, item_diff):
    if item_diff == item_s.ITEM_DIF.SMALL_SOUL:
        item_diff = item_s.ITEM_DIF.EASY
    if item_diff == item_s.ITEM_DIF.KEY:
        item_diff = item_s.ITEM_DIF.HARD
    if item_diff == item_s.ITEM_DIF.BIG_SOUL:
        item_diff = item_s.ITEM_DIF.HARD
    if item_diff == item_s.ITEM_DIF.BOSS_SOUL:
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
    # Do not place a None item in a location that has size not 9 (and therefore 
    #  could cause other locations to not drop, if they are actually part of the
    #  same in-game location (like an NPC drop).
    if (loc.max_size != 9 and len(itemlotpart.items) == 1 and 
     itemlotpart.items[0].item_type == item_s.ITEM_TYPE.NONE):
        return False
    return True

# difficulty_dict has orderable keys (typically integers), and sets of difficulties from LOC_DIF as values.
#  More forward-ordered keys are of higher priority, and those difficulties will
#  appear more toward the start of the list.
# Note: Creates the shuffling is prioritized based on the current size, so that 
#  empty locations have higher priority.
#  So, the ordering is, lexicographically, current_size > difficulty_dict > randomness
def create_random_placement_list(table, difficulty_dict, itemlotpart_to_place, random_source, item_list):
    log.debug("Creating random placement list.")
    return_list = []
    for diff_val in sorted(list(difficulty_dict.keys())):
        diff_set = difficulty_dict[diff_val]
        temp_list = [loc_id for loc_id in table.location_dict if 
         table.location_dict[loc_id].diff in diff_set and 
         table.has_room_at_location_for_itemlotpart(itemlotpart_to_place, loc_id, item_list) and
         eval_location_for_itemlotpart(table, loc_id, itemlotpart_to_place)]
        # Sort the list before shuffling, so that key ordering does not
        #  contribute to the final result.
        temp_list.sort()
        random_source.shuffle(temp_list)
        #temp_list.sort(key = lambda loc_id: len(table.get_item_at_location(loc_id)))
        return_list += temp_list
    return_list.sort(key = lambda loc_id: len(table.get_item_at_location(loc_id)))
    return return_list
    
def find_key_item_by_name(key_name, item_list):
    if key_name not in (key_items_s.KEY_NAMES + key_items_s.ADDITIONAL_SPEEDRUN_KEYS):
        return None
    else:
        key_item_list = [item_list[item_id] for item_id in item_list if 
         item_list[item_id].diff == item_s.ITEM_DIF.KEY and 
         item_list[item_id].key_name == key_name]
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
   
def transmute_itemlotpart_to_boss_item(itemlotpart, random_source):
    if itemlotpart.items:
        for itemlotentry in itemlotpart.items:
            if (itemlotentry.item_type == item_s.ITEM_TYPE.ITEM and 
             itemlotentry.item_id in item_s.BOSS_SOUL_ITEMS):
                if random_source.random() < 0.75:
                    boss_item_list_to_use = random_source.choice(item_s.BOSS_SOUL_ITEMS[itemlotentry.item_id])
                    (boss_item_type, boss_item_id) = random_source.choice(sorted(boss_item_list_to_use))
                    itemlotentry.item_type = boss_item_type
                    itemlotentry.item_id = boss_item_id
                    log.debug("Transmuting itemlotpart into boss item (" + str(boss_item_type) + ", " +
                     str(boss_item_id) + ")")
    return itemlotpart
    
def place_ignored_items(table, item_list):
    log.info("Placing ignored items.")
    for loc_id in table.location_dict:
        loc = table.location_dict[loc_id]
        if loc.diff in [loc_s.LOC_DIF.IGNORE, loc_s.LOC_DIF.EMPTY, loc_s.LOC_DIF.LEAVE_ALONE]:
            log.debug("Placing ignored item ID# " + str(loc_id) + " at location ID# " + str(loc_id))
            table.place_itemlotpart_at_location(item_list[loc_id], loc_id, item_list)

def place_upgrade_items(table, random_source, item_list):
    log.info("Placing upgrade items.")
    for loc_id in table.location_dict:
        loc = table.location_dict[loc_id]
        if loc.diff in [loc_s.LOC_DIF.UPGRADE, loc_s.LOC_DIF.RANDOM_UPGRADE]:
            log.debug("Placing upgrade item at location ID# " + str(loc_id))
            itemlotpart = item_list[loc_id]
            if loc.diff == loc_s.LOC_DIF.UPGRADE:
                itemlotpart = transmute_itemlotpart_to_upgrade(itemlotpart, random_source)
            if loc.diff == loc_s.LOC_DIF.RANDOM_UPGRADE:
                itemlotpart = transmute_itemlotpart_to_rng_drop_upgrade(itemlotpart, random_source)
            table.place_itemlotpart_at_location(itemlotpart, loc_id, item_list)
            
def place_key_item_in_vanilla_location(table, key_name, current_key_locations, item_list):
    key_loc_ids = [loc_id for loc_id in table.location_dict
     if table.location_dict[loc_id].default_key == key_name]
    first_key_loc_id = key_loc_ids[0]
    current_key_locations[key_name] = table.location_dict[first_key_loc_id]
    key_item = find_key_item_by_name(key_name, item_list)
    table.place_itemlotpart_at_location(key_item, first_key_loc_id, item_list)
            
def place_key_items(table, rand_options, random_source, item_list):
    log.info("Placing key items.")
    current_key_locations = {}
    if rand_options.key_placement == rng_opt.RandOptKeyDifficulty.LEAVE_ALONE:
        log.info("Placing key items in vanilla locations.")
        for key_name in key_items_s.KEY_NAMES:
            place_key_item_in_vanilla_location(table, key_name, current_key_locations, item_list)
    else:
        log.info("Placing key items in random locations.")
        for key in key_items_s.KEY_NAMES:
            current_key_locations[key] = "cannot_place"       
        #current_areas = set(["starting"])
        
        if not rand_options.use_lordvessel:
            log.info("Placing Lordvessel in vanilla location.")
            place_key_item_in_vanilla_location(table, "lordvessel", current_key_locations, item_list)
        if not rand_options.use_lord_souls:
            log.info("Placing Lord Souls in vanilla locations.")
            place_key_item_in_vanilla_location(table, "lord_soul_shard_seath", current_key_locations, item_list)
            place_key_item_in_vanilla_location(table, "lord_soul_shard_four_kings", current_key_locations, item_list)
            place_key_item_in_vanilla_location(table, "lord_soul_bed_of_chaos", current_key_locations, item_list)
            place_key_item_in_vanilla_location(table, "lord_soul_nito", current_key_locations, item_list)          

        has_good_trial = False
        while not has_good_trial:
            has_good_trial = True
            log.info("Creating trial key distribution.")
            # Add the additional keys and mark all unplaced keys as placeable,
            #  since all keys are placed at once.
            trial_key_locations = {}
            
            is_speedrun = rand_options.key_placement == rng_opt.RandOptKeyDifficulty.SPEEDRUN_MODE
            if is_speedrun:
                key_names = key_items_s.KEY_NAMES + key_items_s.ADDITIONAL_SPEEDRUN_KEYS
            else:
                key_names = key_items_s.KEY_NAMES
                
            for key_name in key_names:
                if key_items_s.key_placed(key_name, current_key_locations):
                    trial_key_locations[key_name] = current_key_locations[key_name]
                else:
                    trial_key_locations[key_name] = "to_place"
    
            keys_to_place = sorted([key for key in trial_key_locations if trial_key_locations[key] == "to_place"])
            used_loc_ids = set([])
            for key_name in keys_to_place:
                key = find_key_item_by_name(key_name, item_list)
                log.debug("Finding trial location for key " + key_name)
                
                restricted_areas = key_items_s.get_key_restrictions(key_name, rand_options)
                plausible_loc_ids = create_random_placement_list(table, 
                    make_difficulty_order_dict(rand_options.difficulty, key.diff), 
                    key, random_source, item_list)
                pre_possible_loc_ids = [loc_id for loc_id in 
                    plausible_loc_ids if (loc_id not in used_loc_ids and 
                     table.location_dict[loc_id].area in restricted_areas) and
                     not table.location_dict[loc_id].is_transient]
                if (rand_options.key_placement == rng_opt.RandOptKeyDifficulty.RACE_MODE or 
                 rand_options.key_placement == rng_opt.RandOptKeyDifficulty.SPEEDRUN_MODE):
                    possible_loc_ids = [loc_id for loc_id in pre_possible_loc_ids if table.location_dict[loc_id].is_race_key_loc]
                else:
                    possible_loc_ids = pre_possible_loc_ids
                    
                if len(possible_loc_ids) > 0:
                    used_loc_ids.add(possible_loc_ids[0])
                    trial_key_locations[key_name] = table.location_dict[possible_loc_ids[0]]
                else:
                    has_good_trial = False
            if has_good_trial: # Nothing is wrong so far...
                has_good_trial = key_items_s.check_key_locations_are_valid(trial_key_locations, rand_options)
            
            if has_good_trial:
                log.info("Trial succeeded.")
            else:
                log.info("Trial failed.")
        # We have a good trial, so make it permanent.
        for key_name in trial_key_locations:
            if not key_items_s.key_placed(key_name, current_key_locations):
                key = find_key_item_by_name(key_name, item_list)   
                current_key_locations[key_name] = trial_key_locations[key_name]
                loc = current_key_locations[key_name]
                price_overwrite = get_price_for_difficulty(loc.diff, key, random_source)
                if price_overwrite != None and loc.location_id in table.shop_dict:
                    log.info("Placing " + key_name + " at location ID# " + str(loc.location_id) + " with price " + str(price_overwrite))
                else:
                    log.info("Placing " + key_name + " at location ID# " + str(loc.location_id))
                table.place_itemlotpart_at_location(key, loc.location_id, item_list, price = price_overwrite)
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

            
def place_non_key_fixed_items(table, rand_options, random_source, item_list):
    log.info("Placing non-key fixed items.")
    item_ids_to_place = [item_id for item_id in item_list if 
     item_list[item_id].diff in [item_s.ITEM_DIF.EASY, item_s.ITEM_DIF.MEDIUM, 
     item_s.ITEM_DIF.HARD, item_s.ITEM_DIF.SMALL_SOUL, item_s.ITEM_DIF.BIG_SOUL, item_s.ITEM_DIF.BOSS_SOUL, 
     item_s.ITEM_DIF.NPC_EASY, item_s.ITEM_DIF.NPC_MEDIUM, item_s.ITEM_DIF.NPC_HARD,
     item_s.ITEM_DIF.SALABLE_EASY, item_s.ITEM_DIF.SALABLE_MEDIUM, item_s.ITEM_DIF.SALABLE_HARD]]
     
    if rand_options.key_placement != rng_opt.RandOptKeyDifficulty.SPEEDRUN_MODE:
        item_ids_to_place += [item_id for item_id in item_list if 
            (item_list[item_id].diff == item_s.ITEM_DIF.KEY and 
            item_list[item_id].key_name in key_items_s.ADDITIONAL_SPEEDRUN_KEYS)]
     
    if rand_options.fashion_souls:
        # If Fashion Souls is on, stop EASY, MEDIUM, HARD, SMALL_SOUL, BIG_SOUL, BOSS_SOUL
        #  items from following other items.
        for item_id in item_ids_to_place:
            if (item_list[item_id].diff in [item_s.ITEM_DIF.EASY, 
             item_s.ITEM_DIF.MEDIUM, item_s.ITEM_DIF.HARD, 
             item_s.ITEM_DIF.SMALL_SOUL, item_s.ITEM_DIF.BIG_SOUL, 
             item_s.ITEM_DIF.BOSS_SOUL] and not 
             item_s.ITEMS[item_id].always_follow_items):
                item_list[item_id].follow_items = []
    # Remove following items from items_to_place.
    following_items = set(f_item_id for item_id in item_ids_to_place for 
     f_item_id in item_list[item_id].follow_items)
    item_ids_to_place = [item_id for item_id in item_ids_to_place if 
     item_id not in following_items]
    item_ids_to_place.sort(key = lambda item_id: item_list[item_id].get_max_effective_size(), reverse = True)
    
    for item_id in item_ids_to_place:
        item = item_list[item_id]
        
        # Deal with soul consumables, if needed.
        if item.diff in [item_s.ITEM_DIF.SMALL_SOUL, item_s.ITEM_DIF.BIG_SOUL]:
            if rand_options.soul_items_diff == rng_opt.RandOptSoulItemsDifficulty.CONSUMABLE:
                item = transmute_itemlotpart_to_consumable(item, random_source)
        if item.diff == item_s.ITEM_DIF.BOSS_SOUL:
            if rand_options.soul_items_diff == rng_opt.RandOptSoulItemsDifficulty.TRANSPOSE:
                item = transmute_itemlotpart_to_boss_item(item, random_source)
                
        # Fix count on infinitely-sold items.
        if item.diff in [item_s.ITEM_DIF.SALABLE_EASY, item_s.ITEM_DIF.SALABLE_MEDIUM, 
         item_s.ITEM_DIF.SALABLE_HARD]:
             item.items[0].count = -1
        
        # Place item.
        possible_loc_ids = create_random_placement_list(table, 
         make_difficulty_order_dict(rand_options.difficulty, item.diff), item, random_source, item_list)
        if len(possible_loc_ids) > 0:
            loc_id = possible_loc_ids[0]
            price_overwrite = get_price_for_difficulty(table.location_dict[loc_id].diff, item, random_source)
            if price_overwrite != None:
                log.info("Placing ItemLotPart ID# " + str(item_id) + " at location ID# " + str(loc_id) + " with price " + str(price_overwrite))
            else:
                log.info("Placing ItemLotPart ID# " + str(item_id) + " at location ID# " + str(loc_id))
            table.place_itemlotpart_at_location(item, loc_id, item_list, price = price_overwrite)
        else:
            log.warn("Warning: Could not place ItemLotPart ID# " + str(item_id) + " during non-key fixed item placement.")

def place_starting_equipment(table, data_passed_from_chr_init, item_list):
    log.info("Placing starting equipment.")
    for start_class in loc_s.STARTING_ITEM_TABLE:
        for lot_type in ["left_hand", "right_hand", "extra"]:
            if lot_type in loc_s.STARTING_ITEM_TABLE[start_class] and lot_type in data_passed_from_chr_init[start_class]:
                location_id = loc_s.STARTING_ITEM_TABLE[start_class][lot_type]
                item_parts_to_place = data_passed_from_chr_init[start_class][lot_type]
                for item_part in item_parts_to_place:
                    table.place_itemlotpart_at_location(item_part, location_id, item_list)
                
def build_table(rand_options, random_source, chr_init_data):
    # Create a deep copy of the list of items to be modified for this table.
    item_list = copy.deepcopy(item_s.ITEMS)
    
    # Deal with chr_init_data
    if chr_init_data == None:
        chr_inits = [chr_s.VANILLA_CHRS[chr_id].to_chr_init(chr_id , "") for chr_id in chr_s.VANILLA_CHRS]
        given_cip = cip.ChrInitParam(chr_inits)
    else:
        given_cip = cip.ChrInitParam.load_from_file_content(chr_init_data)
    chr_s.randomize_chr_armor(given_cip, rand_options, random_source)
    data_passed_from_chr_init = chr_s.randomize_starting_chr_weapons(given_cip, rand_options, random_source)
    
    for chr_init in given_cip.chr_inits:
        print(chr_init.to_string())
    
    table = item_t.ItemTable(copy.deepcopy(loc_s.LOCATIONS), copy.deepcopy(shop_s.DEFAULT_SHOP_DATA))
    place_ignored_items(table, item_list)
    place_upgrade_items(table, random_source, item_list)
    place_key_items(table, rand_options, random_source, item_list)
    place_starting_equipment(table, data_passed_from_chr_init, item_list)
    place_non_key_fixed_items(table, rand_options, random_source, item_list)
    table.fix_pickup_flags()
    return (table, given_cip)
                
if __name__ == "__main__":
    import random 
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: " + str(sys.argv[0]) + " <seed>")
        sys.exit(1)
    
    seed = sys.argv[1]
    
    #logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    logging.basicConfig(stream=sys.stdout, level=logging.WARN)
    options = rng_opt.RandomizerOptions(
      rng_opt.RandOptDifficulty.EASY, 
      True, 
      rng_opt.RandOptKeyDifficulty.SPEEDRUN_MODE, 
      True, 
      True,
      rng_opt.RandOptSoulItemsDifficulty.SHUFFLE,
      rng_opt.RandOptStartItemsDifficulty.COMBINED_POOL_AND_2H,
      rng_opt.RandOptGameVersion.PTDE,
      False)
    
    rng = random.Random()
    rng.seed(seed)
    (table, _) = build_table(options, rng)
    #result_ilp = table.build_itemlotparam()
    #result_slp = table.build_shoplineup()
    #cheat_string = table.build_cheatsheet(show_event_flags = True)
    hint_string = table.build_hintsheet()
    #ilp_binary_export = result_ilp.export_as_binary()
    #slp_binary_export = result_slp.export_as_binary()
    
    #with open("ItemLotParam.param", 'wb') as f:
    #    f.write(ilp_binary_export)
    #    f.close()
    
    #with open("ShopLineupParam.param", 'wb') as f:
    #    f.write(slp_binary_export)
    #    f.close()
        
    #with open("cheatsheet.txt", "w") as f:
    #    f.write("Seed: " + str(seed) + "\n\n")
    #    f.write(cheat_string)
    #    f.close()
        
    #with open("hintsheet.txt", "w") as f:
    #    f.write(hint_string)
    #    f.close()
    
    #sys.stdout.write("Seed: " + str(seed) + "\n\n")
    #sys.stdout.write(options.as_string())
    #sys.stdout.flush()
    
    sys.stdout.write(hint_string)
    #sys.stdout.write(ilp_binary_export)
    #sys.stdout.write(slp_binary_export)
    #sys.stdout.flush()

