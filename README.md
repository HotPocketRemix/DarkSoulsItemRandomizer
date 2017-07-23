#Dark Souls Item Randomizer

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
The README contains a full list of all the Race Mode locations.

Soul Items: Determines how the Randomizer treats soul consumables. On "Shuffled", they are treated like any other item. On "Replaced", they are replaced with a random consumable before being shuffled.
This reduces the number of soul consumables in the game, but can make item pickups more interesting, as otherwise you receive many soul consumables, which some players find boring.

Starting Items: Determines what pool of weapons/shields the Randomizer draw from when choosing the player's starting left-hand and right-hand items.

Fashion Souls: If active, the many armor sets in game are split up, and each piece is placed separately.

Senile Gwynevere: If active, the Lordvessel will be shuffled like other key items, and Gwynevere will (usually) give the player a different item in place of the Lordvessel. Not compatible with not shuffling keys.
This options typically makes the game easier, since the player will usually not have to defeat Ornstein & Smough to access the Lordvessel. Depending on other settings, however, the Lordvessel may be placed
in an inconvenient location, which can offset the reduced difficulty slightly.