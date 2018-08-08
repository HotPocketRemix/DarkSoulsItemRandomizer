import logging
log = logging.getLogger(__name__)

from ordered_set import OrderedSet
import copy

from locations_setup import AREA
import randomizer_options as rng_opt

KEY_NAMES = ["lordvessel", "key_to_the_seal", "blighttown_key",
 "key_to_depths", "covenant_of_artorias", "rite_of_kindling",
 "orange_charred_ring", "sewer_chamber_key", "large_ember", 
 "mystery_key", "basement_key", "undead_asylum_f2_west_key",
 "annex_key", "watchtower_basement_key", "darkmoon_seance_ring",
 "key_to_new_londo_ruins", "cage_key", "archive_prison_extra_key",
 "archive_tower_giant_cell_key", "archive_tower_giant_door_key",
 "peculiar_doll", "broken_pendant", "crest_key", "crest_of_artorias",
 "residence_key", "dark_ember", "divine_ember", "enchanted_ember",
 "large_divine_ember", "large_flame_ember", "chaos_flame_ember", 
 "very_large_ember", "large_magic_ember", "crystal_ember", "cast_light",
 "lord_soul_shard_seath", "lord_soul_shard_four_kings", 
 "lord_soul_bed_of_chaos", "lord_soul_nito"
]
ADDITIONAL_SPEEDRUN_KEYS = ["purple_cowards_crystal"]

def key_placed(key_name, current_key_locations):
    if key_name not in current_key_locations:
        return False
    key_status = current_key_locations[key_name]
    return not(key_status == "to_place" or key_status == "cannot_place")
       
def check_key_locations_are_valid(current_key_locations, rand_options):
    speedrun = (rand_options.key_placement == rng_opt.RandOptKeyDifficulty.SPEEDRUN_MODE)
    connection_dict = get_connections(rand_options)
        
    # Pretend to start in the Prison with no keys to simulate having to
    #  find the key and escape, to check that this is possible.
    # This is skipped on speedrun mode, because of Duke Skip.
    if not speedrun:
        current_areas = OrderedSet([AREA.DUKES_PRISON])
        current_keys = OrderedSet(["none"])
        for new_key in current_key_locations:
            if current_key_locations[new_key].area == AREA.DUKES_PRISON:
                current_keys.add(new_key)
        has_changed = True 
        while has_changed and AREA.DUKES_ARCHIVES not in current_areas:
            has_changed = False
            for area in current_areas:
                for key in connection_dict[area]:
                    if key in current_keys:
                        for area_to_add in set(connection_dict[area][key]) - current_areas:
                            current_areas.add(area_to_add)
                            for new_key in current_key_locations:
                                if current_key_locations[new_key].area == area_to_add:
                                    current_keys.add(new_key)
                            has_changed = True
        if AREA.DUKES_ARCHIVES not in current_areas:
            return False
            
    # Run the check for real, from the starting area.
    current_areas = OrderedSet(["starting"])
    current_keys = OrderedSet(["none"])
    has_changed = True
    while has_changed:
        has_changed = False
    
        if (not speedrun and AREA.UNDEAD_PARISH in current_areas and
         AREA.QUELAAGS_DOMAIN in current_areas and 
         AREA.SENS_FORTRESS not in current_areas):
             current_areas.add(AREA.SENS_FORTRESS)
             for new_key in current_key_locations:
                if current_key_locations[new_key].area == AREA.SENS_FORTRESS:
                    current_keys.add(new_key)
             has_changed = True
    
        open_kiln = True
        for area in connection_dict:
            if area != AREA.KILN and area not in current_areas:
                open_kiln = False
                
        if not speedrun or "purple_cowards_crystal" not in current_keys:
            for key in ["lord_soul_shard_seath", "lord_soul_shard_four_kings", 
             "lord_soul_bed_of_chaos", "lord_soul_nito"]:
                if key not in current_keys:
                    open_kiln = False
                    
        if open_kiln and AREA.KILN not in current_areas:
            current_areas.add(AREA.KILN)
            has_changed = True

        for area in current_areas:
            for key in connection_dict[area]:
                if key in current_keys:
                    for area_to_add in set(connection_dict[area][key]) - current_areas:
                        current_areas.add(area_to_add)
                        for new_key in current_key_locations:
                            if current_key_locations[new_key].area == area_to_add:
                                current_keys.add(new_key)
                        has_changed = True
    for area in connection_dict:
        if area not in current_areas:
            return False
    return True
    
def get_key_restrictions(key_name, rand_options):
    speedrun = (rand_options.key_placement == rng_opt.RandOptKeyDifficulty.SPEEDRUN_MODE)
    if speedrun:
        restriction_dict = SPEEDRUN_KEY_RESTRICTIONS
        key_names = KEY_NAMES + ADDITIONAL_SPEEDRUN_KEYS
    else:
        restriction_dict = KEY_RESTRICTIONS
        key_names = KEY_NAMES
    
    if key_name in key_names:
         return restriction_dict.get(key_name, list(CONNECTIONS.keys()))
    else:
        raise KeyError

# Gives a list of locations some keys absolutely must appear in,
#  to speed up the placement algorithm. This does not need to be
#  comprehensive, but helps for keys that can only appear in a
#  smaller set of locations.
KEY_RESTRICTIONS = {
 "archive_prison_extra_key": [AREA.DUKES_PRISON, AREA.DUKES_PRISON_GIANT_CELL],
 "archive_tower_giant_door_key": [AREA.DUKES_PRISON, 
    AREA.DUKES_PRISON_EXTRA, AREA.DUKES_PRISON_GIANT_CELL],
 "broken_pendant": [AREA.TOMB_OF_THE_GIANTS_POST_LV, 
    AREA.DEMON_RUINS_NO_LAVA_POST_LV, AREA.LOST_IZALITH, 
    AREA.DUKES_PRISON, AREA.DUKES_PRISON_EXTRA,
    AREA.DUKES_PRISON_GIANT_CELL, AREA.DUKES_ARCHIVES, AREA.CRYSTAL_CAVE],
}

# No speedrun key restrictions at the moment. 
#  Here in case it's needed at some point.
SPEEDRUN_KEY_RESTRICTIONS = {}

def get_connections(rand_options):
    c = copy.deepcopy(CONNECTIONS)
    if rand_options.key_placement == rng_opt.RandOptKeyDifficulty.SPEEDRUN_MODE:
        c[AREA.UNDEAD_BURG]["none"] += [
            AREA.DEPTHS, # Capra Skip
            AREA.WATCHTOWER_BASEMENT, # Master Key
            AREA.LOWER_UNDEAD_BURG, # Lower Burg Skip
            AREA.UNDEAD_BURG_RESIDENCE # Master Key
        ]
        c[AREA.WATCHTOWER_BASEMENT]["none"] = [
            AREA.UNDEAD_BURG, AREA.DARKROOT_BASIN # Master Key
        ]
        c[AREA.UNDEAD_PARISH]["none"] += [
           AREA.SENS_FORTRESS # Sen's Gate Skip
        ]
        c[AREA.PAINTED_WORLD]["none"] += [
           AREA.PAINTED_WORLD_ANNEX # Annex Jump
        ]
        c[AREA.DARKROOT_FOREST]["purple_cowards_crystal"] = [
           AREA.OOLACILE_TOWNSHIP # Wrong Warp to DLC
        ]
        c[AREA.DARKROOT_BASIN]["none"] += [
           AREA.DARKROOT_GARDEN, # Re-add Sif Ladder
           AREA.VALLEY_OF_DRAKES, # Re-add Valley of Drakes Elevator
           AREA.WATCHTOWER_BASEMENT # Master Key
        ]
        if rand_options.game_version == rng_opt.RandOptGameVersion.PTDE:
            c[AREA.QUELAAGS_DOMAIN]["none"] += [
               AREA.DEMON_RUINS_NO_LAVA_POST_LV # Firesage Drop
            ]
        c[AREA.ANOR_LONDO]["none"] += [
           AREA.DARKMOON_TOMB # Gwynevere can be killed
        ]
        c[AREA.NEW_LONDO_PRE_SEAL]["none"] += [
           AREA.VALLEY_OF_DRAKES, # Master Key
           AREA.NEW_LONDO_POST_LV, # Ingward can be killed
           AREA.NEW_LONDO_POST_SEAL_SKIP, # Seal Skip
        ]
        c[AREA.NEW_LONDO_POST_SEAL_SKIP]["covenant_of_artorias"] += [
           AREA.POST_4K # Four Kings OOB
        ]
        c[AREA.VALLEY_OF_DRAKES]["none"] += [
           AREA.NEW_LONDO_PRE_SEAL # Master Key
        ]
        c[AREA.DUKES_PRISON]["none"] = [
           AREA.DUKES_ARCHIVES # Duke Skip
        ]
    return c

CONNECTIONS = {
 AREA.DEPTHS: {
    "blighttown_key": [AREA.BLIGHTTOWN], 
    "sewer_chamber_key": [], 
    "key_to_depths": [AREA.LOWER_UNDEAD_BURG]},
 AREA.LOWER_UNDEAD_BURG: {
    "key_to_depths": [AREA.DEPTHS], 
    "none": [AREA.UNDEAD_BURG, AREA.FIRELINK],
    "residence_key": [AREA.LOWER_UNDEAD_BURG_RESIDENCE]},
 AREA.LOWER_UNDEAD_BURG_RESIDENCE: {},
 AREA.UNDEAD_BURG: {
    "none": [AREA.FIRELINK, AREA.UNDEAD_PARISH], 
    "watchtower_basement_key": [AREA.WATCHTOWER_BASEMENT], 
    "basement_key": [AREA.LOWER_UNDEAD_BURG],
    "residence_key": [AREA.UNDEAD_BURG_RESIDENCE]},
 AREA.UNDEAD_BURG_RESIDENCE: {
    "none": [AREA.UNDEAD_BURG]},
 AREA.WATCHTOWER_BASEMENT: {"watchtower_basement_key": [AREA.UNDEAD_BURG, AREA.DARKROOT_BASIN]},
 AREA.UNDEAD_PARISH: {
    "none": [AREA.UNDEAD_BURG, AREA.FIRELINK, 
        AREA.UNDEAD_ASYLUM, AREA.DARKROOT_FOREST],
    "mystery_key": [],
    "logic": [AREA.SENS_FORTRESS]},
 AREA.FIRELINK: {
    "none": [AREA.UNDEAD_BURG, AREA.CATACOMBS, AREA.NEW_LONDO_PRE_SEAL],
    "logic": [AREA.KILN]},
 AREA.PAINTED_WORLD: {
    "none": [AREA.ANOR_LONDO], 
    "annex_key": [AREA.PAINTED_WORLD_ANNEX]},
 AREA.PAINTED_WORLD_ANNEX: {
    "none": [AREA.PAINTED_WORLD]},
 AREA.DARKROOT_GARDEN: {
    "none": [AREA.DARKROOT_BASIN]},
 AREA.DARKROOT_FOREST: {
    "none": [AREA.DARKROOT_BASIN, AREA.UNDEAD_PARISH],
    "crest_of_artorias": [AREA.DARKROOT_GARDEN]},
 AREA.DARKROOT_BASIN: {
    "none": [AREA.DARKROOT_FOREST],
    #"none": [AREA.DARKROOT_GARDEN, AREA.DARKROOT_FOREST, AREA.VALLEY_OF_DRAKES],
    # Remove Valley of Drakes, since otherwise there is a (key-based) 
    #  unbroken path from Firelink to Blighttown and beyond, which is
    #  too challenging.
    # Remove Darkroot Garden, as otherwise the Crest of Artorias is useless,
    #  and usually is placed very late.
    "watchtower_basement_key": [AREA.WATCHTOWER_BASEMENT],
    "broken_pendant": [AREA.OOLACILE_SANCTUARY]},
 AREA.OOLACILE_SANCTUARY: {
    "none": [AREA.ROYAL_WOOD]},
 AREA.ROYAL_WOOD: {
    "none": [AREA.OOLACILE_TOWNSHIP]},
 AREA.OOLACILE_TOWNSHIP: {
    "none": [AREA.ROYAL_WOOD, AREA.CHASM_OF_THE_ABYSS],
    "crest_key": [AREA.KALAMEET_FIGHT],
    "cast_light": [AREA.OOLACILE_HIDDEN]},
 AREA.OOLACILE_HIDDEN: {
    "cast_light": [AREA.OOLACILE_TOWNSHIP]},
 AREA.KALAMEET_FIGHT: {
    "none": [AREA.ROYAL_WOOD]},
 AREA.CHASM_OF_THE_ABYSS: {
    "none": [AREA.ROYAL_WOOD, AREA.OOLACILE_TOWNSHIP]},
 AREA.CATACOMBS: {
    "none": [AREA.FIRELINK, AREA.TOMB_OF_THE_GIANTS_PRE_LV]},
 AREA.TOMB_OF_THE_GIANTS_PRE_LV: {
    "none": [AREA.CATACOMBS],
    "lordvessel": [AREA.TOMB_OF_THE_GIANTS_POST_LV]},
 AREA.TOMB_OF_THE_GIANTS_POST_LV: {
    "lordvessel": [AREA.TOMB_OF_THE_GIANTS_PRE_LV],
    "lord_soul_nito": []},
 AREA.GREAT_HOLLOW: {
    "none": [AREA.BLIGHTTOWN, AREA.ASH_LAKE]},
 AREA.ASH_LAKE: {
    "none": [AREA.GREAT_HOLLOW]},
 AREA.BLIGHTTOWN: {
    "none": [AREA.VALLEY_OF_DRAKES, AREA.GREAT_HOLLOW, AREA.QUELAAGS_DOMAIN]},
 AREA.QUELAAGS_DOMAIN: {
    "none": [AREA.BLIGHTTOWN, AREA.DEMON_RUINS_NO_LAVA_PRE_LV]},
 AREA.DEMON_RUINS_NO_LAVA_PRE_LV: {
    "none": [AREA.QUELAAGS_DOMAIN],
    "lordvessel": [AREA.DEMON_RUINS_NO_LAVA_POST_LV],
    "orange_charred_ring": [AREA.DEMON_RUINS_LAVA]},
 AREA.DEMON_RUINS_NO_LAVA_POST_LV: {
    "none": [AREA.QUELAAGS_DOMAIN],
    "lordvessel": [AREA.DEMON_RUINS_NO_LAVA_PRE_LV],
    "orange_charred_ring": [AREA.LOST_IZALITH]},
 AREA.DEMON_RUINS_LAVA: {
    "orange_charred_ring": [AREA.DEMON_RUINS_NO_LAVA_PRE_LV]},
 AREA.LOST_IZALITH: {
    "none": [AREA.DEMON_RUINS_NO_LAVA_PRE_LV],
    "lord_soul_bed_of_chaos": []},
 AREA.SENS_FORTRESS: {
    "none": [AREA.ANOR_LONDO],
    "cage_key": [AREA.SENS_CAGE],
    "logic": [AREA.UNDEAD_PARISH]},
 AREA.SENS_CAGE: {
    "cage_key": [AREA.SENS_FORTRESS]},
 AREA.ANOR_LONDO: {
    "none": [AREA.SENS_FORTRESS],
    "peculiar_doll": [AREA.PAINTED_WORLD],
    "darkmoon_seance_ring": [AREA.DARKMOON_TOMB],
    "lordvessel": [AREA.DUKES_PRISON]},
 AREA.DARKMOON_TOMB: {
    "none": [AREA.ANOR_LONDO]},
 AREA.NEW_LONDO_PRE_SEAL: {
    "none": [AREA.FIRELINK],
    "key_to_new_londo_ruins": [AREA.VALLEY_OF_DRAKES],
    "lordvessel": [AREA.NEW_LONDO_POST_LV],
    "key_to_the_seal": [AREA.NEW_LONDO_POST_SEAL]},
 AREA.NEW_LONDO_POST_LV: {
    "none": [AREA.NEW_LONDO_PRE_SEAL]},
 AREA.NEW_LONDO_POST_SEAL: {
    "none": [AREA.VALLEY_OF_DRAKES, AREA.NEW_LONDO_PRE_SEAL, AREA.NEW_LONDO_POST_SEAL_SKIP],
    "covenant_of_artorias": [AREA.POST_4K]},
 AREA.NEW_LONDO_POST_SEAL_SKIP: {
    "none": [],
    "covenant_of_artorias": []},
 AREA.VALLEY_OF_DRAKES: {
    "none": [AREA.BLIGHTTOWN, AREA.DARKROOT_BASIN],
    "key_to_new_londo_ruins": [AREA.NEW_LONDO_PRE_SEAL]},
 AREA.POST_4K: {
    "logic": [AREA.KILN],
    "lord_soul_shard_four_kings": []},
 AREA.DUKES_PRISON: {
    "archive_tower_giant_door_key": [AREA.DUKES_ARCHIVES],
    "archive_tower_giant_cell_key": [AREA.DUKES_PRISON_GIANT_CELL],
    "archive_prison_extra_key": [AREA.DUKES_PRISON_EXTRA]},
 AREA.DUKES_PRISON_EXTRA: {
    "archive_prison_extra_key": [AREA.DUKES_PRISON]},
 AREA.DUKES_PRISON_GIANT_CELL: {
    "archive_tower_giant_cell_key": [AREA.DUKES_PRISON]},
 AREA.DUKES_ARCHIVES: {
    "none": [AREA.CRYSTAL_CAVE],
    "lordvessel": [AREA.ANOR_LONDO]},
 AREA.CRYSTAL_CAVE: {
    "none": [AREA.DUKES_ARCHIVES],
    "lord_soul_shard_seath": []},
 AREA.KILN: {},
 AREA.UNDEAD_ASYLUM: {
    "none": [AREA.FIRELINK],
    "undead_asylum_f2_west_key": [AREA.UNDEAD_ASYLUM_F2_WEST]},
 AREA.UNDEAD_ASYLUM_F2_WEST: {
    "none": [AREA.FIRELINK]},
 "starting": {
    "none": [AREA.UNDEAD_ASYLUM]},
}
