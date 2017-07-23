import logging
log = logging.getLogger(__name__)

from locations_setup import AREA 

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
 "very_large_ember", "large_magic_ember", "crystal_ember", "cast_light"]

def key_placed(key_name, current_key_locations):
    if key_name not in current_key_locations:
        return False
    key_status = current_key_locations[key_name]
    return not(key_status == "to_place" or key_status == "cannot_place")

# Determines if the given key can be placed in the given location.
#  - key_name should be an element of KEY_NAMES
#  - location should be a Location like those in LOCATIONS
#  - current_key_location should be a dict whose keyset is KEY_NAMES and
#     whose values are drawn from AREA or "to_place" or "cannot_place"
#  - current_areas should be a subset of AREA of currently accessible locations
def is_location_okay_for_key(key_name, location, current_key_locations, current_areas):
    #log.debug("Checking if key '" + key_name + "' can be placed at location ID# " + str(location.location_id))
    if current_key_locations[key_name] != "to_place":
        return False
    if location.is_transient:
        return False
        
    if key_name == "lordvessel":
        # The Lordvessel can only be placed once all the areas before the ones
        #  it opens are accessible.
        if (AREA.TOMB_OF_THE_GIANTS_PRE_LV not in current_areas or # TOMB_OF_THE_GIANTS_POST_LV
         AREA.DEMON_RUINS_NO_LAVA_PRE_LV not in current_areas or # DEMON_RUINS_NO_LAVA_POST_LV
         AREA.NEW_LONDO_POST_SEAL not in current_areas or # NEW_LONDO_POST_LV (Not strictly needed)
         AREA.ANOR_LONDO not in current_areas): # DUKES_PRISON / DUKES_ARCHIVES
             return False
    elif key_name == "key_to_new_londo_ruins":
        # If the Basement Key has been placed, but the Blighttown Key
        #  has not, then no location will work, so that the Depths
        #  path to Blighttown has roughly the same probability as other 
        #  paths.
        # Note: This is not strictly necessary, but increases quality
        #  of experience.
        if (key_placed("basement_key", current_key_locations) and 
         not key_placed("blighttown_key", current_key_locations)):
             return False
    elif key_name == "key_to_the_seal":
        # Same as Key to New Londo Ruins."
        if (key_placed("basement_key", current_key_locations) and 
         not key_placed("blighttown_key", current_key_locations)):
             return False
    elif key_name == "archive_prison_extra_key":
        # The Extra Key must be placed in the Prison, so that softlocks
        #  cannot occur.
        if location.area not in set([AREA.DUKES_PRISON, AREA.DUKES_PRISON_EXTRA,
         AREA.DUKES_PRISON_GIANT_CELL]):
             return False
    elif key_name == "archive_tower_giant_cell_key":
        # If the Giant Door Key has not been placed, restrict to placing
        #  the Giant Cell Key in the Prison, to increase possibilites
        #  of where the Giant Door Key can be placed.
        # Note: This is not strictly necessary, but increases quality
        #  of experience.
        if (current_key_locations["archive_tower_giant_door_key"] == "to_place" and
         location.area not in set([AREA.DUKES_PRISON, AREA.DUKES_PRISON_EXTRA])):
             return False
    elif key_name == "archive_tower_giant_door_key":
        # The Giant Door Key must be placed in the Prison, so that softlocks
        #  cannot occur.
        if location.area not in set([AREA.DUKES_PRISON, AREA.DUKES_PRISON_EXTRA,
         AREA.DUKES_PRISON_GIANT_CELL]):
             return False
    elif key_name == "broken_pendant":
        # Broken Pendant must be placed in an area that requires the
        #  Lordvessel, since otherwise the player may not have it,
        #  and get stuck in the DLC.
        if location.area not in set([AREA.TOMB_OF_THE_GIANTS_POST_LV, 
         AREA.DEMON_RUINS_NO_LAVA_POST_LV, AREA.LOST_IZALITH,
         AREA.DUKES_PRISON, AREA.DUKES_PRISON_EXTRA,
         AREA.DUKES_PRISON_GIANT_CELL, AREA.DUKES_ARCHIVES, 
         AREA.CRYSTAL_CAVE]):
             return False
    
    # If none of the special cases are met, then default to if the
    #  given location is part of the current areas.        
    return (location.area in current_areas)

# Modifies current_key_locations and current_areas as if the area
#  area_to_unlock was unlocked. If area_to_unlock was previously
#  unlocked, then returns True, and if not, returns False.
# Unlocking an area adds it to current_areas, and any of the area's
#  keys that are set to "cannot_place" are set to "to_place".
def unlock_area(area_to_unlock, current_key_locations, current_areas):
    if area_to_unlock in current_areas:
        return False
    else:
        log.debug("Unlocked area " + str(area_to_unlock))
        current_areas.add(area_to_unlock)
        keys_to_place = [area_key for area_key in CONNECTIONS[area_to_unlock] if 
         area_key in current_key_locations and current_key_locations[area_key] == "cannot_place"]
        for key in keys_to_place:
            current_key_locations[key] = "to_place"
        return True

# Modifies current_key_locations and current_areas to update them
#  when keys are placed. Returns True if a modification was made,
#  and False if not. Should be iterated until it returns False.
def unlock_locations_and_keys(current_key_locations, current_areas):
    has_changed = False
    
    # Sen's Fortress is added when both Bell areas are unlocked.
    if AREA.UNDEAD_PARISH in current_areas and AREA.QUELAAGS_DOMAIN in current_areas:
        has_changed = unlock_area(AREA.SENS_FORTRESS, current_key_locations, 
         current_areas) or has_changed
        
    # Kiln of the First Flame is unlocked after all other areas are.
    open_kiln = True
    for area in CONNECTIONS:
        if area != AREA.KILN and area not in current_areas:
            open_kiln = False
    if open_kiln:
        has_changed = unlock_area(AREA.KILN, current_key_locations, 
         current_areas) or has_changed

    for area in sorted(tuple(current_areas)):
        for key in CONNECTIONS[area]:
            if key == "none" or (key_placed(key, current_key_locations) and
             current_key_locations[key].area in current_areas):
                for area_to_add in CONNECTIONS[area][key]:
                    has_changed = unlock_area(area_to_add, current_key_locations, 
                     current_areas) or has_changed
    return has_changed

def update_locations_and_keys(current_key_locations, current_areas):
    modification_made = True
    while modification_made:
        modification_made = unlock_locations_and_keys(current_key_locations, current_areas)
              
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
 AREA.WATCHTOWER_BASEMENT: {
    "watchtower_basement_key": [AREA.UNDEAD_BURG, AREA.DARKROOT_BASIN]},
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
    "none": [AREA.OOLACILE_SANCTUARY, AREA.OOLACILE_TOWNSHIP]},
 AREA.OOLACILE_TOWNSHIP: {
    "none": [AREA.ROYAL_WOOD, AREA.CHASM_OF_THE_ABYSS],
    "crest_key": [AREA.KALAMEET_FIGHT],
    "cast_light": [AREA.OOLACILE_HIDDEN]},
 AREA.OOLACILE_HIDDEN: {
    "cast_light": [AREA.OOLACILE_TOWNSHIP]},
 AREA.KALAMEET_FIGHT: {
    "none": [AREA.ROYAL_WOOD]},
 AREA.CHASM_OF_THE_ABYSS: {
    "none": [AREA.OOLACILE_TOWNSHIP]},
 AREA.CATACOMBS: {
    "none": [AREA.FIRELINK, AREA.TOMB_OF_THE_GIANTS_PRE_LV]},
 AREA.TOMB_OF_THE_GIANTS_PRE_LV: {
    "none": [AREA.CATACOMBS],
    "lordvessel": [AREA.TOMB_OF_THE_GIANTS_POST_LV]},
 AREA.TOMB_OF_THE_GIANTS_POST_LV: {
    "lordvessel": [AREA.TOMB_OF_THE_GIANTS_PRE_LV]},
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
    "none": [AREA.DEMON_RUINS_NO_LAVA_PRE_LV]},
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
    "none": [AREA.VALLEY_OF_DRAKES, AREA.NEW_LONDO_PRE_SEAL],
    "covenant_of_artorias": [AREA.POST_4K]},
 AREA.VALLEY_OF_DRAKES: {
    "none": [AREA.BLIGHTTOWN, AREA.DARKROOT_BASIN],
    "key_to_new_londo_ruins": [AREA.NEW_LONDO_PRE_SEAL]},
 AREA.POST_4K: {
    "logic": [AREA.KILN]},
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
    "none": [AREA.DUKES_ARCHIVES]},
 AREA.KILN: {
    # Essential items that can go in any non-transient location but are
    #  not truly keys are placed after all actual keys.
    "rite_of_kindling": [],
    "large_ember": [], 
    "dark_ember": [],
    "divine_ember": [],
    "enchanted_ember": [],
    "large_divine_ember" : [],
    "large_flame_ember": [],
    "chaos_flame_ember": [],
    "very_large_ember": [],
    "large_magic_ember": [],
    "crystal_ember": []},
 AREA.UNDEAD_ASYLUM: {
    "none": [AREA.FIRELINK],
    "undead_asylum_f2_west_key": [AREA.UNDEAD_ASYLUM_F2_WEST]},
 AREA.UNDEAD_ASYLUM_F2_WEST: {
    "none": [AREA.FIRELINK]},
 "starting": {
    "none": [AREA.UNDEAD_ASYLUM]}
}
                    
