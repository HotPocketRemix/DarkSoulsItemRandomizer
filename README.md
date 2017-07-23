# Dark Souls Item Randomizer

Instructions:

* Unpack your Dark Souls archive files using UnpackDarkSoulsForModding, which can be found [here](https://github.com/HotPocketRemix/UnpackDarkSoulsForModding). Note that even if you have already unpacked your Dark Souls 
archive files by hand or using a previous version of UDSFM, you will still need to do this step. UDSFM now removes DCX-compression, and the Item Randomizer works on
non-DCX-compressed files only.
* Download `dist/DarkSoulsItemRandomizer.exe`, and place it in `DATA\param\GameParam\`, where `DATA` is your Dark Souls data directory. There should be an
existing file, `GameParam.parambnd` already present.
* Run the Item Randomizer and select your options. When you are ready to randomize your items, click the Export button to automatically write the modified item
configuration to `GameParam.parambnd`. A backup copy, `GameParam.parambnd.bak` will be created if it does not already exist. A directory with the current date/time stamp 
will be created containing information about the item distribution, including a cheatsheet.
* If you want to inspect a certain item distribution, but not modify the current `GameParam.parambnd`, you can instead input a seed and click the "Write Seed Info" button
to generate the same type of folder as above, without modifying the current item distribution. Note that you *must* input a seed for this to work.

To restore the default item distribution:

* Check that `GameParam.parambnd.bak` exists in `DATA\param\GameParam`.
* Delete `GameParam.parambnd` from `DATA\param\GameParam`.
* Re-name `GameParam.parambnd.bak` to `GameParam.parambnd`.

The data/time-stamped directory that is generated contains 5 files:

* `ItemLotParam.param` and `ShopLineupParam.param`. These files are the actual subfiles that are being modified in `GameParam.parambnd` and are
provided for those who wish to inspect them in a .param editor.
* `cheatsheet.txt` contains a list of every location that items can be shuffled to -- with a short description of the location -- and a list of each
shuffled item that is placed at each location. Since NPC drop tables are also shuffled, they are included at the end of the cheatsheet.
* `hintsheet.txt` contains a list of each key item in the game, together with the area that it is located in. If you are stuck, you can use the
hint sheet to give an idea of where a key item is before resorting to using the cheatsheet to find its exact location.
* `seed_info.txt` contains the settings and seed used in the Item Randomizer to produce the item distribution. If you forget the seed/setting you used or want to share the
settings with others, this file has the exact information needed.



Randomizer Settings:

The following is a brief description of each of the Item Randomizer's settings:

Difficulty: Determines how much the Randomizer is biased against you. The more unfair it is, the more it attempts to hide desirable items (good weapons, lighter armor, keys)
in harder-to-reach or less well-known locations.

Key Placement: Determines how the Randomizer places keys. On "Not Shuffled", key items are in their usual locations. On "Shuffled", key items are placed in any locations, provided they do
not lead to a softlock where not all areas can be accessed before defeating Gwyn. On "Race Mode", key items are placed in a restricted set of locations, so that not every location needs
to be checked for a key. The list of locations consists of boss drops, in chests, in Andre statues, dropped by Black Knights, and in some locations where keys are normally:
sold/drop by Andre, sold/drop by Undead Merchant, gift/drop from Gwynevere, gift/drop from Ingward, drop from special Golem in Duke's Archives, drop from second Oolacile Township Mimic.
This README contains a full list of all the Race Mode locations at the end.

Soul Items: Determines how the Randomizer treats soul consumables. On "Shuffled", they are treated like any other item. On "Replaced", they are replaced with a random consumable before being shuffled.
This reduces the number of soul consumables in the game, but can make item pickups more interesting, as otherwise you receive many soul consumables, which some players find boring.

Starting Items: Determines what pool of weapons/shields the Randomizer draw from when choosing the player's starting left-hand and right-hand items.

Fashion Souls: If active, the many armor sets in game are split up, and each piece is placed separately.

Senile Gwynevere: If active, the Lordvessel will be shuffled like other key items, and Gwynevere will (usually) give the player a different item in place of the Lordvessel. Not compatible with not shuffling keys.
This options typically makes the game easier, since the player will usually not have to defeat Ornstein & Smough to access the Lordvessel. Depending on other settings, however, the Lordvessel may be placed
in an inconvenient location, which can offset the reduced difficulty slightly.


Race Mode Possible Key Locations:

    1090: Gwynevere Gift / Drop
    1100: Ingward Gift / Drop
    2500: Gaping Dragon Drop
    2510: Capra Demon Drop
    2520: Crossbreed Priscilla Drop
    2530: Moonlight Butterfly Drop
    2540: Great Gray Wolf, Sif Drop
    2550: Pinwheel Drop
    2570: Chaos Witch Quelaag Drop
    2590: Iron Golem Drop
    2600: Dark Sun Gwyndoling Drop
    2650: Gwyn, Lord of Cinder Drop
    2670: Demon Centipede Drop
    2680: Sanctuary Guardian Drop
    2690: Knight Artorias Drop
    2700: Manus, Father of the Abyss Drop
    2710: Black Dragon Kalameet Drop
    6190: Andre of Astora shop item / drop
    6231: Undead Merchant shop item / drop
 1000500: Depths Chest
 1010450: Undead Burg Chest #1
 1010460: Undead Burg Chest #2
 1020070: Firelink Chest #1
 1020180: Firelink Chest #2
 1020190: Firelink Chest #3
 1020200: Firelink Chest #4
 1100370: Painted World Andre Statue
 1100500: Painted World Chest
 1200140: Darkroot Garden Andre Statue
 1200500: Darkroot Garden Chest #1
 1200510: Darkroot Garden Chest #2
 1210500: Royal Wood Chest #1
 1210510: Oolacile Township Chest #1
 1210520: Oolacile Township Chest #2
 1210540: Oolacile Township Chest #3
 1210550: Royal Wood Chest #2
 1310500: Tomb of the Giants Andre Statue
 1320180: Great Hollow Chest
 1400500: Blighttown Chest #1
 1400510: Blighttown Chest #2
 1400520: Blighttown Chest #3
 1410100: Demon Ruins Chest #1
 1410410: Lost Izalith Chest #1
 1410500: Lost Izalith Chest #2
 1410520: Lost Izalith Chest #3
 1500000: Sen's Fortress Chest #1
 1500020: Sen's Fortress Chest #2
 1500040: Sen's Fortress Chest #3
 1500090: Sen's Fortress Chest #4
 1500100: Sen's Fortress Chest #5
 1510510: Anor Londo Chest #1
 1510520: Anor Londo Chest #2
 1510530: Anor Londo Chest #3
 1510540: Anor Londo Chest #4
 1510560: Anor Londo Chest #5
 1510570: Anor Londo Chest #6
 1510580: Anor Londo Chest #7
 1510590: Anor Londo Chest #8
 1510600: Anor Londo Chest #9
 1510610: Anor Londo Chest #10
 1510620: Anor Londo Chest #11
 1510650: Anor Londo Chest #12
 1510660: Anor Londo Chest #13
 1510670: Anor Londo Chest #14
 1510680: Anor Londo Chest #15
 1510690: Anor Londo Chest #16
 1600290: New Londo Ruins Chest #1
 1600500: New Londo Ruins Chest #2
 1600510: New Londo Ruins Chest #3
 1700020: The Duke's Archives Chest #1
 1700050: The Duke's Archives Chest #2
 1700510: The Duke's Archives Chest #3
 1700520: The Duke's Archives Chest #4
 1700530: The Duke's Archives Chest #5
 1700540: The Duke's Archives Chest #6
 1700560: The Duke's Archives Chest #7
 1700580: The Duke's Archives Chest #8
 1700590: The Duke's Archives Chest #9
 1700600: The Duke's Archives Chest #10
 1700630: The Duke's Archives Chest #11
27100200: The Duke's Archives Special Golem
27803001: Oolacile Township 2nd Mimic
27900000: Undead Burg Black Knight
27900100: Undead Parish Black Knight
27901000: Darkroot Basin Black Knight
27902000: Catacombs Black Knight
27903000: Tomb of the Giants Black Knight