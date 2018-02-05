import Tkinter as tk
import tkMessageBox as tkMB
import random
import hashlib
import sys
import os
import datetime
import shutil
import webbrowser
import requests
from distutils.version import LooseVersion

import randomizer_options as rngopts
import randomize_item_table
import bnd_rebuilder

import logging
log = logging.getLogger(__name__)

MAX_SEED_LENGTH = 64

VERSION_NUM = "0.2.1"

DESC_DICT = {
    "diff": {rngopts.RandOptDifficulty.EASY: "* Perfectly fair. Items have an equal chance to be placed anywhere.\n\n", 
        rngopts.RandOptDifficulty.MEDIUM: "* Slightly biased. Desirable items are not placed in plain view.\n\n", 
        rngopts.RandOptDifficulty.HARD: "* Heavily biased. Desirable items are hidden, and are rarely in early areas.\n\n"},
    "key_diff": {rngopts.RandOptKeyDifficulty.LEAVE_ALONE: ("* Key items are placed in their usual locations.\n" + 
            "  For a player who wants random items without needing to hunt for keys.\n" + 
            "  Some key locations may contain additional items in some seeds.\n\n"),
        rngopts.RandOptKeyDifficulty.RANDOMIZE: ("* Key items are shuffled into the item pool and placed in random locations.\n" + 
            "  For a player who wishes to explore all of Lordran. Average run is ~10hrs.\n" + 
            "  Players will typically need to pick up many items in search of keys.\n\n"),
        rngopts.RandOptKeyDifficulty.RACE_MODE: (
            "* Key items are shuffled but can be placed only in certain locations.\n" + 
            "  Good for races / short runs. Average run is ~4hrs. See README for list of \n" + 
            "  locations to check. Read this list ahead of time to know where to check.\n\n"),
        rngopts.RandOptKeyDifficulty.SPEEDRUN_MODE: (
            "* Key items are shuffled but can be placed only in certain locations.\n" +
            "  May require skips and glitches to complete. SOFTLOCKING IS POSSIBLE.\n" +
            "  See README for list of locations to check. Read this list ahead of time.\n\n")},
    "souls_diff": {rngopts.RandOptSoulItemsDifficulty.SHUFFLE: "* Soul items are shuffled into the item pool like other items.\n\n",
        rngopts.RandOptSoulItemsDifficulty.CONSUMABLE: "* Lesser soul items are replaced with a random consumable before shuffling.\n\n",
        rngopts.RandOptSoulItemsDifficulty.TRANSPOSE:  "* Boss souls have a 75% chance to be transposed to one of their boss items.\n\n"},
    "start_items": {rngopts.RandOptStartItemsDifficulty.SHIELD_AND_1H: ("* Player starts with random class-usable (L) shield & (R) weapon.\n" + 
            "  The weapon is usable one-handed with base stats.\n\n"),
        rngopts.RandOptStartItemsDifficulty.SHIELD_AND_2H: ("* Player starts with random class-usable (L) shield & (R) weapon.\n" + 
            "  The weapon may need to be two-handed to be usable with base stats.\n\n"),
        rngopts.RandOptStartItemsDifficulty.COMBINED_POOL_AND_2H: ("* Player starts with random class-usable (L) shield OR weapon & (R) weapon.\n" + 
            "  The weapon(s) may need to be two-handed to be usable with base stats.\n\n")},
    "fashion": {True: "* Armor sets ARE NOT kept together during shuffling.\n   Players will typically need to mix-and-match armor pieces.\n\n",
        False: "* Armor sets ARE kept together during shuffling.\n   Players will be able to find full sets of armor at once.\n\n"},
    "use_lv": {True: "* The Lordvessel IS included in the randomized keys.\n   Difficulty ranges from much easier (in Firelink) to harder (in TotG).\n\n",
        False: "* The Lordvessel IS NOT included in the randomized keys.\n   Difficulty is standard. Lordvessel is given by Gwynevere in Anor Londo.\n\n"},
    "use_lord_souls": {True: "* The 4 Lord Souls ARE included in the randomized keys.\n   Difficulty ranges from much easier to much harder.", 
        False: "* The 4 Lord Souls ARE NOT included in the randomized keys.\n   Difficulty is standard. Lord Souls are dropped by their normal bosses."}
}
DESC_ORDER = ["diff", "key_diff", "souls_diff", "start_items", "fashion", "use_lv", "use_lord_souls"]



def resource_path(rel_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, rel_path)

class Placeholder_State(object):
     __slots__ = 'normal_color', 'normal_font', 'placeholder_text', 'placeholder_color', 'placeholder_font', 'with_placeholder'
     
class DescriptionState():
    NORMAL = "normal"
    DEEMPH = "deemph"
    EMPH = "emph"
    
    def __init__(self, desc_specifiers, text_area):
        self.text_area = text_area
        self.desc_specifiers = desc_specifiers
        
    def write_state_to_area(self):
        self.text_area.config(state="normal")
        self.text_area.delete(1.0, "end")
        
        for desc_part in DESC_ORDER:
            (desc_part_value, desc_part_format) = self.desc_specifiers[desc_part]
            text_part = DESC_DICT[desc_part][desc_part_value]
            self.text_area.insert("end", text_part, desc_part_format)
        self.text_area.tag_config(DescriptionState.NORMAL, foreground="black")
        self.text_area.tag_config(DescriptionState.DEEMPH, foreground="grey")
        self.text_area.tag_config(DescriptionState.EMPH, foreground="red2")
        self.text_area.config(state="disabled")

class MainGUI:
    def __init__(self):
        self.seed_rng = random.Random()
        self.has_hovered_desc = False
        self.root = tk.Tk()
        self.root.title("Dark Souls Item Randomizer v" + VERSION_NUM)
        self.root.resizable(False, False)
        img = tk.PhotoImage(file=resource_path('favicon.gif'))
        self.root.call('wm', 'iconphoto', self.root._w, img)
    
        tk.Label(self.root, text="Seed:").grid(row=0, column=0, sticky='E', padx=2)
        self.seed_string = tk.StringVar()
        self.seed_string.set("")
        self.seed_string.trace('w', lambda name, index, mode: self.seed_changed())
        self.seed_entry = tk.Entry(self.root, font="TkFixedFont", textvariable=self.seed_string, width=70)
        self.entry_state = self.add_placeholder_to(self.seed_entry, 'Type a seed (or leave blank for a random seed)')
        self.seed_entry.grid(row=0, column=1, ipady=2, ipadx=1, padx=2, sticky='EW')
        self.msg_area = tk.Text(self.root, width=76, height=19, state="disabled", background=self.root.cget('background'), wrap="word")
        self.msg_area.grid(row=1, column=0, columnspan=2, rowspan=9, padx=2, pady=2)
        self.msg_quit_button = tk.Button(self.root, text="Quit", command=self.quit_button)
        self.msg_quit_button.grid(row=5, column=1, rowspan=2)
        self.msg_continue_button = tk.Button(self.root, text="Continue", command=self.continue_button)
        self.msg_continue_button.grid(row=3, column=1, rowspan=2)
        self.back_button = tk.Button(self.root, text="Back", command=self.back_button)
        self.back_button.grid(row=3, column=1, rowspan=2)
        self.desc_area = tk.Text(self.root, width=76, height=19, state="disabled", background=self.root.cget('background'), wrap="word")
        self.desc_area.grid(row=1, column=0, columnspan=2, rowspan=9, padx=2, pady=2)
        tk.Label(self.root, text="Made by HotPocketRemix      ").grid(row=0, column=2, columnspan=2, sticky='E', padx=2)
        self.sellout_button = tk.Button(self.root, text="$", bg="pale goldenrod",
         padx=2, pady=2, command=self.lift_sellout_area)
        self.sellout_button.grid(row=0, column=3, padx=2, sticky='E')
        
        self.diff_frame = tk.LabelFrame(text="Difficulty:")
        self.diff_frame.grid(row=1, column=2, rowspan=1, sticky='NS', padx=2)
        self.diff = tk.IntVar()
        self.diff.set(rngopts.RandOptDifficulty.EASY)
        self.diff.trace('w', lambda name, index, mode: self.update())
        self.diff_rbutton1 = tk.Radiobutton(self.diff_frame, 
         text=rngopts.RandOptDifficulty.as_string(rngopts.RandOptDifficulty.EASY), 
         variable=self.diff, value=rngopts.RandOptDifficulty.EASY, width=10, anchor=tk.W)
        self.diff_rbutton2 = tk.Radiobutton(self.diff_frame, 
         text=rngopts.RandOptDifficulty.as_string(rngopts.RandOptDifficulty.MEDIUM), 
         variable=self.diff, value=rngopts.RandOptDifficulty.MEDIUM, width=10, anchor=tk.W)
        self.diff_rbutton3 = tk.Radiobutton(self.diff_frame, 
         text=rngopts.RandOptDifficulty.as_string(rngopts.RandOptDifficulty.HARD), 
         variable=self.diff, value=rngopts.RandOptDifficulty.HARD, width=10, anchor=tk.W)
        self.diff_rbutton1.grid(row=0, column=0, sticky='W')
        self.diff_rbutton2.grid(row=1, column=0, sticky='W')
        self.diff_rbutton3.grid(row=2, column=0, sticky='W')
        self.setup_hover_events(self.diff_rbutton1, {"diff": rngopts.RandOptDifficulty.EASY})
        self.setup_hover_events(self.diff_rbutton2, {"diff": rngopts.RandOptDifficulty.MEDIUM})
        self.setup_hover_events(self.diff_rbutton3, {"diff": rngopts.RandOptDifficulty.HARD})
        
        self.key_diff_frame = tk.LabelFrame(text="Key Placement:")
        self.key_diff_frame.grid(row=2, column=2, rowspan=4, sticky='NS', padx=2)
        self.key_diff = tk.IntVar()
        self.key_diff.set(rngopts.RandOptKeyDifficulty.RANDOMIZE)
        self.key_diff.trace('w', lambda name, index, mode: self.update())
        self.key_diff_rbutton1 = tk.Radiobutton(self.key_diff_frame, 
         text=rngopts.RandOptKeyDifficulty.as_string(rngopts.RandOptKeyDifficulty.LEAVE_ALONE), 
         variable=self.key_diff, value=rngopts.RandOptKeyDifficulty.LEAVE_ALONE, width=10, anchor=tk.W)
        self.key_diff_rbutton2 = tk.Radiobutton(self.key_diff_frame, 
         text=rngopts.RandOptKeyDifficulty.as_string(rngopts.RandOptKeyDifficulty.RANDOMIZE), 
         variable=self.key_diff, value=rngopts.RandOptKeyDifficulty.RANDOMIZE, width=10, anchor=tk.W)
        self.key_diff_rbutton3 = tk.Radiobutton(self.key_diff_frame, 
         text=rngopts.RandOptKeyDifficulty.as_string(rngopts.RandOptKeyDifficulty.RACE_MODE), 
         variable=self.key_diff, value=rngopts.RandOptKeyDifficulty.RACE_MODE, width=10, anchor=tk.W)
        self.key_diff_rbutton4 = tk.Radiobutton(self.key_diff_frame, 
         text=rngopts.RandOptKeyDifficulty.as_string(rngopts.RandOptKeyDifficulty.SPEEDRUN_MODE), 
         variable=self.key_diff, value=rngopts.RandOptKeyDifficulty.SPEEDRUN_MODE, width=10, anchor=tk.W)
        self.key_diff_rbutton1.grid(row=0, column=0, sticky='W')
        self.key_diff_rbutton2.grid(row=1, column=0, sticky='W')
        self.key_diff_rbutton3.grid(row=2, column=0, sticky='W')
        self.key_diff_rbutton4.grid(row=3, column=0, sticky='W')
        self.setup_hover_events(self.key_diff_rbutton1, {"key_diff": rngopts.RandOptKeyDifficulty.LEAVE_ALONE, "use_lv": False, "use_lord_souls": False})
        self.setup_hover_events(self.key_diff_rbutton2, {"key_diff": rngopts.RandOptKeyDifficulty.RANDOMIZE})
        self.setup_hover_events(self.key_diff_rbutton3, {"key_diff": rngopts.RandOptKeyDifficulty.RACE_MODE})
        self.setup_hover_events(self.key_diff_rbutton4, {"key_diff": rngopts.RandOptKeyDifficulty.SPEEDRUN_MODE, "diff": rngopts.RandOptDifficulty.EASY})
        
        self.soul_frame = tk.LabelFrame(text="Soul Items:")
        self.soul_frame.grid(row=6, column=2, rowspan=5, sticky='NS', padx=2, pady=2)
        self.soul_diff = tk.IntVar()
        self.soul_diff.set(rngopts.RandOptSoulItemsDifficulty.SHUFFLE)
        self.soul_diff.trace('w', lambda name, index, mode: self.update())
        self.soul_diff_rbutton1 = tk.Radiobutton(self.soul_frame, 
         text=rngopts.RandOptSoulItemsDifficulty.as_string(rngopts.RandOptSoulItemsDifficulty.SHUFFLE), 
         variable=self.soul_diff, value=rngopts.RandOptSoulItemsDifficulty.SHUFFLE, width=10, anchor=tk.W)
        self.soul_diff_rbutton2 = tk.Radiobutton(self.soul_frame, 
         text=rngopts.RandOptSoulItemsDifficulty.as_string(rngopts.RandOptSoulItemsDifficulty.CONSUMABLE), 
         variable=self.soul_diff, value=rngopts.RandOptSoulItemsDifficulty.CONSUMABLE, width=10, anchor=tk.W)
        self.soul_diff_rbutton3 = tk.Radiobutton(self.soul_frame, 
         text=rngopts.RandOptSoulItemsDifficulty.as_string(rngopts.RandOptSoulItemsDifficulty.TRANSPOSE), 
         variable=self.soul_diff, value=rngopts.RandOptSoulItemsDifficulty.TRANSPOSE, width=10, anchor=tk.W)
        self.soul_diff_rbutton1.grid(row=0, column=0, sticky='W')
        self.soul_diff_rbutton2.grid(row=1, column=0, sticky='W')
        self.soul_diff_rbutton3.grid(row=2, column=0, sticky='W')
        self.setup_hover_events(self.soul_diff_rbutton1, {"souls_diff": rngopts.RandOptSoulItemsDifficulty.SHUFFLE})
        self.setup_hover_events(self.soul_diff_rbutton2, {"souls_diff": rngopts.RandOptSoulItemsDifficulty.CONSUMABLE})
        self.setup_hover_events(self.soul_diff_rbutton3, {"souls_diff": rngopts.RandOptSoulItemsDifficulty.TRANSPOSE})
        
        self.start_items_frame = tk.LabelFrame(text="Starting Items:")
        self.start_items_frame.grid(row=1, column=3, sticky='NS', padx=2)
        self.start_items_diff = tk.IntVar()
        self.start_items_diff.set(rngopts.RandOptStartItemsDifficulty.SHIELD_AND_2H)
        self.start_items_diff.trace('w', lambda name, index, mode: self.update())
        self.start_items_rbutton1 = tk.Radiobutton(self.start_items_frame, 
         text=rngopts.RandOptStartItemsDifficulty.as_string(rngopts.RandOptStartItemsDifficulty.SHIELD_AND_1H), 
         variable=self.start_items_diff, value=rngopts.RandOptStartItemsDifficulty.SHIELD_AND_1H, width=20, anchor=tk.W)
        self.start_items_rbutton2 = tk.Radiobutton(self.start_items_frame, 
         text=rngopts.RandOptStartItemsDifficulty.as_string(rngopts.RandOptStartItemsDifficulty.SHIELD_AND_2H), 
         variable=self.start_items_diff, value=rngopts.RandOptStartItemsDifficulty.SHIELD_AND_2H, width=20, anchor=tk.W)
        self.start_items_rbutton3 = tk.Radiobutton(self.start_items_frame, 
         text=rngopts.RandOptStartItemsDifficulty.as_string(rngopts.RandOptStartItemsDifficulty.COMBINED_POOL_AND_2H), 
         variable=self.start_items_diff, value=rngopts.RandOptStartItemsDifficulty.COMBINED_POOL_AND_2H, width=20, anchor=tk.W)
        self.start_items_rbutton1.grid(row=0, column=0, sticky='W')
        self.start_items_rbutton2.grid(row=1, column=0, sticky='W')
        self.start_items_rbutton3.grid(row=2, column=0, sticky='W')
        self.setup_hover_events(self.start_items_rbutton1, {"start_items": rngopts.RandOptStartItemsDifficulty.SHIELD_AND_1H})
        self.setup_hover_events(self.start_items_rbutton2, {"start_items": rngopts.RandOptStartItemsDifficulty.SHIELD_AND_2H})
        self.setup_hover_events(self.start_items_rbutton3, {"start_items": rngopts.RandOptStartItemsDifficulty.COMBINED_POOL_AND_2H})
        
        self.fashion_bool = tk.BooleanVar()
        self.fashion_bool.set(True)
        self.fashion_bool.trace('w', lambda name, index, mode: self.update())
        self.fashion_check = tk.Checkbutton(self.root, text="Fashion Souls", 
         variable=self.fashion_bool, onvalue=True, offvalue=False, padx=2,
         width=20, anchor=tk.W)
        self.fashion_check.grid(row=2, column=3, sticky='W')
        self.setup_hover_events(self.fashion_check, {"fashion": None}, no_emph = True)
        
        self.use_lordvessel = tk.BooleanVar()
        self.use_lordvessel.set(False)
        self.use_lordvessel.trace('w', lambda name, index, mode: self.update())
        self.lv_check = tk.Checkbutton(self.root, text="Senile Gwynevere", 
         variable=self.use_lordvessel, onvalue=True, offvalue=False, padx=2,
         width=20, anchor=tk.W)
        self.lv_check.grid(row=3, column=3, sticky='W')
        self.setup_hover_events(self.lv_check, {"use_lv": None}, no_emph = True)
        
        self.use_lord_souls = tk.BooleanVar()
        self.use_lord_souls.set(False)
        self.use_lordvessel.trace('w', lambda name, index, mode: self.update())
        self.lord_soul_check = tk.Checkbutton(self.root, text="Senile Primordial Serpents", 
         variable=self.use_lord_souls, onvalue=True, offvalue=False, padx=2,
         width=20, anchor=tk.W)
        self.lord_soul_check.grid(row=4, column=3, sticky='W')
        self.setup_hover_events(self.lord_soul_check, {"use_lord_souls": None}, no_emph = True)
        
        self.export_button = tk.Button(self.root, text="Scramble Items &\nExport to GameParam", 
         padx=10, pady=10, command=self.export_to_gameparam)
        self.export_button.grid(row=5, rowspan=3, column=3, padx=2, sticky='EW')
        
        self.cheat_button = tk.Button(self.root, text="Write Seed Info &\nCheatsheet / Hintsheet", command=self.export_seed_info)
        self.cheat_button.grid(row=8, rowspan=2, column=3, sticky='EW', padx=2, pady=2)
        
        self.update_desc()
        self.check_for_new_version()
        
    def quit_button(self):
        self.root.destroy()
        
    def continue_button(self):
        self.msg_quit_button.lower()
        self.msg_continue_button.lower()
        self.msg_area.lower()
        
    def back_button(self):
        self.msg_quit_button.lower()
        self.back_button.lower()
        self.msg_area.lower()
        
    def lift_msg_area(self):
        self.msg_area.lift()
        self.msg_continue_button.lift()
        self.msg_quit_button.lift()
        
    def lift_sellout_area(self):
        self.msg_continue_button.lower()
        self.msg_area.config(state="normal")
        self.msg_area.delete(1.0, "end")
        self.msg_area.insert("end", "\n\n")
        self.msg_area.insert("end", "If you are interested in supporting the author, please consider donating at\n\n               ")
        self.msg_area.insert("end", r"https://twitch.streamlabs.com/hotpocketremix/", "hyperlink")
        self.msg_area.insert("end", "\n\n       Donations are not required, but are much appreciated. \`[T]/")
        self.msg_area.tag_config("hyperlink", foreground="blue", underline=1)
        self.msg_area.tag_bind("hyperlink", "<Enter>", lambda _: self.hyperlink_enter())
        self.msg_area.tag_bind("hyperlink", "<Leave>", lambda _: self.hyperlink_leave())
        self.msg_area.tag_bind("hyperlink", "<Button-1>", lambda _: self.hyperlink_click())
        self.msg_area.config(state="disabled")
        self.msg_area.lift()
        self.back_button.lift()
        
    def hyperlink_enter(self):
        self.msg_area.config(cursor="hand2")
    
    def hyperlink_leave(self):
        self.msg_area.config(cursor="")
        
    def hyperlink_click(self):
        webbrowser.open_new_tab(r"https://twitch.streamlabs.com/hotpocketremix/")
        
    def get_current_desc_state(self):
        desc_specifiers = {
            "diff": (self.diff.get(), DescriptionState.NORMAL),
            "key_diff": (self.key_diff.get(), DescriptionState.NORMAL),
            "souls_diff": (self.soul_diff.get(), DescriptionState.NORMAL),
            "start_items": (self.start_items_diff.get(), DescriptionState.NORMAL),
            "fashion": (self.fashion_bool.get(), DescriptionState.NORMAL),
            "use_lv": (self.use_lordvessel.get(), DescriptionState.NORMAL),
            "use_lord_souls": (self.use_lord_souls.get(), DescriptionState.NORMAL)
        }
        return DescriptionState(desc_specifiers, self.desc_area)
        
    def update_desc_with_fade(self, overwrite_desc_specifiers):
        current_state = self.get_current_desc_state()
        current_desc_specifiers = current_state.desc_specifiers
        for k in current_desc_specifiers:
            if k in overwrite_desc_specifiers:
                current_desc_specifiers[k] = overwrite_desc_specifiers[k]
            else:
                (current_val, current_tag) = current_desc_specifiers[k] 
                current_desc_specifiers[k] = (current_val, DescriptionState.DEEMPH)
        current_state.write_state_to_area()

    def update_desc_for_hover(self, hovered_parts, no_emph = False):
        overwrite_desc_specifiers = {}
        current_state = self.get_current_desc_state()
        for part in hovered_parts:
            if no_emph:
                # Only NORMAL the currently shown desc part, rather
                #  than EMPH the to-be-shown desc part.
                overwrite_desc_specifiers[part] = (current_state.desc_specifiers[part][0], DescriptionState.NORMAL)
            else:
                if hovered_parts[part] == current_state.desc_specifiers[part][0]:
                    overwrite_desc_specifiers[part] = (hovered_parts[part], DescriptionState.NORMAL)
                else:
                    overwrite_desc_specifiers[part] = (hovered_parts[part], DescriptionState.EMPH)
        self.update_desc_with_fade(overwrite_desc_specifiers)
        self.has_hovered_desc = True
        
    def setup_hover_events(self, hover_object, hovered_parts, no_emph = False):
        hover_object.bind("<Enter>", lambda _: self.update_desc_for_hover(hovered_parts, no_emph))
        hover_object.bind("<Leave>", lambda _: self.update_desc(respect_current_hover = False))
        hover_object.bind("<Return>", lambda _: self.update_desc(respect_current_hover = False))
        hover_object.bind("<space>", lambda _: self.update_desc(respect_current_hover = False))
        hover_object.configure(command = lambda: self.update_desc_for_hover(hovered_parts, no_emph))
        
    def update_desc(self, respect_current_hover = True):
        if not (respect_current_hover and self.has_hovered_desc):
            self.has_hovered_desc = False
            self.get_current_desc_state().write_state_to_area()
            
    def update(self):
        if self.key_diff.get() == rngopts.RandOptKeyDifficulty.LEAVE_ALONE:
            self.use_lordvessel.set(False)
            self.use_lord_souls.set(False)
            self.lv_check.config(state="disabled")
            self.lord_soul_check.config(state="disabled")
        else:
            self.lv_check.config(state="normal")
            self.lord_soul_check.config(state="normal")
            
        if self.key_diff.get() == rngopts.RandOptKeyDifficulty.SPEEDRUN_MODE:
            self.diff.set(rngopts.RandOptDifficulty.EASY)
            self.diff_rbutton1.config(state="disabled")
            self.diff_rbutton2.config(state="disabled")
            self.diff_rbutton3.config(state="disabled")
        else:
            self.diff_rbutton1.config(state="normal")
            self.diff_rbutton2.config(state="normal")
            self.diff_rbutton3.config(state="normal")
        self.update_desc()
        
    def build_item_table(self):
        options = rngopts.RandomizerOptions(self.diff.get(), self.fashion_bool.get(), 
         self.key_diff.get(), self.use_lordvessel.get(), self.use_lord_souls.get(), 
         self.soul_diff.get(), self.start_items_diff.get())

        rng = random.Random()
        rng.seed(int(hashlib.sha256(self.seed_string.get()).hexdigest(), 16))
        return (options, randomize_item_table.build_table(options, rng))
    
    def get_new_seed(self):
        new_hex_seed = hashlib.sha256(str(self.seed_rng.random())).hexdigest()
        # Swap some letters in the hexadecimal seed to be more easily readable.
        #  Useful for distinguishing letters on-stream, and for those with
        #  impaired vision.
        
        SUBS_DICT = {'0': 'b','1': 'c', '2': 'f', '3': 'i', '4': 'j', 
         '5': 'k', '6': 'p', '7': 'q', '8': 'r', '9': 'v', 'a': 'x', 
         'b': 'y', 'c': 'z', 'd': '2', 'e': '4', 'f': '5'}
        
        self.seed_string.set(''.join([SUBS_DICT.get(c, '') for c in new_hex_seed]))
        self.seed_entry.config(fg = self.entry_state.normal_color, font=self.entry_state.normal_font)
        self.entry_state.with_placeholder = False

    def seed_changed(self):
        self.limit_seed_length()
        value = self.seed_string.get()
        self.seed_entry.config(bg = "white")
        
    def is_seed_empty(self):
        seed = self.seed_string.get()
        return seed is None or len(seed) < 1 or self.entry_state.with_placeholder
        
    def export_seed_info(self, use_table=None):
        if self.is_seed_empty():
            self.seed_entry.config(bg = "light salmon")
            return
        
        new_dir_name = "random-seed-" + datetime.datetime.today().strftime("%Y-%m-%d--%H-%M-%S-%f")
        new_dirpath = os.path.join(os.getcwd(), new_dir_name)
        try: 
            os.makedirs(new_dirpath)
        except OSError:
            if not os.path.isdir(new_dirpath):
                raise
        
        if use_table:
            (options, table) = use_table
        else:
            (options, table) = self.build_item_table()
        
        result_ilp = table.build_itemlotparam()
        ilp_binary_export = result_ilp.export_as_binary()
        result_slp = table.build_shoplineup()
        slp_binary_export = result_slp.export_as_binary()
        cheat_string = table.build_cheatsheet(show_event_flags = False)
        hint_string = table.build_hintsheet()
        seed_info = "Seed: " + str(self.seed_string.get()) + "\n\n" + options.as_string()
        
        ITEMLOT_FILEPATH = os.path.join(new_dirpath, "ItemLotParam.param")
        SHOPLINEUP_FILEPATH = os.path.join(new_dirpath, "ShopLineupParam.param")
        CHEATSHEET_FILEPATH = os.path.join(new_dirpath, "cheatsheet.txt")
        HINTSHEET_FILEPATH = os.path.join(new_dirpath, "hintsheet.txt")
        SEEDINFO_FILEPATH = os.path.join(new_dirpath, "seed_info.txt")
        
        with open(ITEMLOT_FILEPATH, 'wb') as f:
            f.write(ilp_binary_export)
        with open(SHOPLINEUP_FILEPATH, 'wb') as f:
            f.write(slp_binary_export)
        with open(CHEATSHEET_FILEPATH, 'w') as f:
            f.write(cheat_string)
        with open(HINTSHEET_FILEPATH, 'w') as f:
            f.write(hint_string)
        with open(SEEDINFO_FILEPATH, 'w') as f:
            f.write(seed_info)
            
        if not use_table:
            self.msg_continue_button.lower()
            self.msg_area.config(state="normal")
            self.msg_area.delete(1.0, "end")
            self.msg_area.insert("end", "\n")
            self.msg_area.insert("end", "SUCCESS", "yay")
            self.msg_area.insert("end", "! The information for this seed has been exported in the directory\n  " + 
            new_dir_name + "\n\nClick \"Back\" to begin again, or click \"Quit\" to exit.")
            self.msg_area.tag_config("yay", foreground="green")
            self.msg_area.config(state="disabled")
            self.msg_area.lift()
            self.back_button.lift()
            self.msg_quit_button.lift()
            
        return new_dir_name
        
    def export_to_gameparam(self):
        GAMEPARAM_FILEPATH = os.path.join(os.getcwd(), "GameParam.parambnd")
        GAMEPARAMBAK_FILEPATH = os.path.join(os.getcwd(), "GameParam.parambnd.bak")
        
        if not os.path.isfile(GAMEPARAM_FILEPATH):
            self.msg_area.config(state="normal")
            self.msg_area.delete(1.0, "end")
            self.msg_area.insert("end", "\n\n")
            self.msg_area.insert("end", "ERROR", "error_red")
            self.msg_area.insert("end", ": GameParam.parambnd is missing or cannot be opened." + 
             " Check that this program is in the correct directory and GameParam.parambnd is present and try again.\n\n" +
             "Click \"Continue\" to continue in seed-information-only mode, or" + 
             " click \"Quit\" to exit.")
            self.msg_area.tag_config("error_red", foreground="red")
            self.msg_area.config(state="disabled")
            self.export_button.config(state = "disabled")
            self.lift_msg_area()
        else:
            with open(GAMEPARAM_FILEPATH, "rb") as f:
                content = f.read()
            try:
                content_list = bnd_rebuilder.unpack_bnd(content)
            except:
                self.msg_area.config(state="normal")
                self.msg_area.delete(1.0, "end")
                self.msg_area.insert("end", "\n\n")
                self.msg_area.insert("end", "ERROR", "error_red")
                self.msg_area.insert("end", ": GameParam.parambnd is malformed or corrupted and cannot be" + 
                 " parsed to export randomized items. If possible, restore GameParam.parambnd from a backup copy.\n\n" +
                 "Click \"Continue\" to continue in seed-information-only mode, or" + 
                 " click \"Quit\" to exit.")
                self.msg_area.tag_config("error_red", foreground="red")
                self.msg_area.config(state="disabled")
                self.export_button.config(state = "disabled")
                self.lift_msg_area()
            
            # Back up GameParam.parambnd if needed.
            if not os.path.isfile(GAMEPARAMBAK_FILEPATH):
                shutil.copy2(GAMEPARAM_FILEPATH, GAMEPARAMBAK_FILEPATH)
                
            if self.is_seed_empty():
                self.get_new_seed()

            (options, table) = self.build_item_table()
            result_ilp = table.build_itemlotparam()
            ilp_binary_export = result_ilp.export_as_binary()
            result_slp = table.build_shoplineup()
            slp_binary_export = result_slp.export_as_binary()
            
            for index, (file_id, filepath, filedata) in enumerate(content_list):
                if filepath == "N:\FRPG\data\INTERROOT_win32\param\GameParam\ItemLotParam.param":
                    content_list[index] = (file_id, filepath, ilp_binary_export)
                if filepath == "N:\FRPG\data\INTERROOT_win32\param\GameParam\ShopLineupParam.param":
                    content_list[index] = (file_id, filepath, slp_binary_export)
            new_content = bnd_rebuilder.repack_bnd(content_list)
            with open(GAMEPARAM_FILEPATH, "wb") as f:
                f.write(new_content)
            seed_folder = self.export_seed_info((options, table))
                
            self.msg_continue_button.lower()
            self.msg_area.config(state="normal")
            self.msg_area.delete(1.0, "end")
            self.msg_area.insert("end", "\n\n")
            self.msg_area.insert("end", "SUCCESS", "yay")
            self.msg_area.insert("end", "! GameParam.parambnd has been modified successfully.\n\n" +
            "The information for this seed has been exported in the directory\n  " + 
            seed_folder + "\n\nClick \"Back\" to begin again, or click \"Quit\" to exit.")
            self.msg_area.tag_config("yay", foreground="green")
            self.msg_area.config(state="disabled")
            self.msg_area.lift()
            self.back_button.lift()
            self.msg_quit_button.lift()
                
            
        
    def limit_seed_length(self):
        value = self.seed_string.get()
        if len(value) > MAX_SEED_LENGTH: 
            self.seed_string.set(value[:MAX_SEED_LENGTH])
            
    def add_placeholder_to(self, entry, placeholder, color="grey", font=None):
        normal_color = entry.cget("fg")
        normal_font = entry.cget("font")
        
        if font is None:
            font = normal_font

        state = Placeholder_State()
        state.normal_color=normal_color
        state.normal_font=normal_font
        state.placeholder_color=color
        state.placeholder_font=font
        state.placeholder_text = placeholder
        state.with_placeholder=True

        def on_focusin(event, entry=entry, state=state):
            if state.with_placeholder:
                entry.delete(0, "end")
                entry.config(fg = state.normal_color, font=state.normal_font)
                state.with_placeholder = False

        def on_focusout(event, entry=entry, state=state):
            if entry.get() == '':
                entry.insert(0, state.placeholder_text)
                entry.config(fg = state.placeholder_color, font=state.placeholder_font)
                state.with_placeholder = True

        entry.insert(0, placeholder)
        entry.config(fg = color, font=font)

        entry.bind('<FocusIn>', on_focusin, add="+")
        entry.bind('<FocusOut>', on_focusout, add="+")
        
        entry.placeholder_state = state
        return state
        
    def check_for_new_version(self):
        CHECK_VERSION_URL = r'https://raw.githubusercontent.com/HotPocketRemix/DarkSoulsItemRandomizer/master/version.txt'
        try:
            r = requests.get(CHECK_VERSION_URL, timeout=2)
            if r.status_code == requests.codes.ok:
                page_content = r.content
                page_version_num = page_content.split('\n')[0].strip()
                if LooseVersion(page_version_num) > LooseVersion(VERSION_NUM):
                    self.back_button.lower()
                    self.msg_area.config(state="normal")
                    self.msg_area.delete(1.0, "end")
                    self.msg_area.insert("end", "\n\n")
                    self.msg_area.insert("end", "ATTENTION", "error_red")
                    self.msg_area.insert("end", "! There is a new version of the Item Randomizer available.\n\n" +
                    "It is recommended that you update to the newest version. Old versions\n" + 
                    "will NOT be supported and may have bugs fixed in the latest release." +
                    "\n\nClick \"Continue\" to use the current version anyway, or click \"Quit\" to exit.")
                    self.msg_area.tag_config("error_red", foreground="red")
                    self.msg_area.lift()
                    self.msg_continue_button.lift()
                    self.msg_quit_button.lift()
        except:
            pass


if __name__ == "__main__":
    logging.basicConfig(stream=sys.stdout, level=logging.WARN)
    maingui = MainGUI()
    maingui.root.mainloop()
    
