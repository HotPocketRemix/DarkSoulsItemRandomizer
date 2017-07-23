
class RandOptDifficulty:
    EASY = 0
    MEDIUM = 1
    HARD = 2
    
    @classmethod
    def as_string(cls, diff):
        if diff == cls.EASY:
            return "Fair"
        elif diff == cls.MEDIUM:
            return "Unfair"
        elif diff == cls.HARD:
            return "Very Unfair"
        else:
            return ""

class RandOptKeyDifficulty:
    LEAVE_ALONE = 0
    RANDOMIZE = 1
    RACE_MODE = 2
    
    @classmethod
    def as_string(cls, diff):
        if diff == cls.LEAVE_ALONE:
            return "Not Shuffled"
        elif diff == cls.RANDOMIZE:
            return "Shuffled"
        elif diff == cls.RACE_MODE:
            return "Race Mode"
        else:
            return ""
    
class RandOptStartItemsDifficulty:
    SHIELD_AND_1H = 0
    SHIELD_AND_2H = 1
    COMBINED_POOL_AND_2H = 2
    
    @classmethod
    def as_string(cls, diff):
        if diff == cls.SHIELD_AND_1H:
            return "Shield & 1H Weapon"
        elif diff == cls.SHIELD_AND_2H:
            return "Shield & 1/2H Weapon"
        elif diff == cls.COMBINED_POOL_AND_2H:
            return "Shield/Weapon & Weapon"
        else:
            return ""
            
    
class RandOptSoulItemsDifficulty:
    SHUFFLE = 0
    CONSUMABLE = 1
    
    @classmethod
    def as_string(cls, diff):
        if diff == cls.SHUFFLE:
            return "Shuffled"
        elif diff == cls.CONSUMABLE:
            return "Replaced"
        else:
            return ""

class RandomizerOptions:
    def __init__(self, difficulty, fashion_souls, key_placement, 
     use_lordvessel, soul_items_diff, start_items_diff):
         self.difficulty = difficulty
         self.fashion_souls = fashion_souls
         self.key_placement = key_placement
         self.use_lordvessel = use_lordvessel
         self.soul_items_diff = soul_items_diff
         self.start_items_diff = start_items_diff
         
    def bool_option_to_string(self, b):
        if b:
            return "On"
        else:
            return "Off"
         
    def as_string(self):
        return_string = "Randomizer Settings:\n"
        return_string += "  Difficulty: " + RandOptDifficulty.as_string(self.difficulty) + "\n"
        return_string += "  Fashion Souls: " + self.bool_option_to_string(self.fashion_souls) + "\n"
        return_string += "  Key Difficulty: " + RandOptKeyDifficulty.as_string(self.key_placement) + "\n"
        return_string += "  Senile Gwynevere: " + self.bool_option_to_string(self.use_lordvessel) + "\n"
        return_string += "  Soul Items: " + RandOptSoulItemsDifficulty.as_string(self.soul_items_diff) + "\n"
        return_string += "  Starting Items: " + RandOptStartItemsDifficulty.as_string(self.start_items_diff) + "\n"
        return return_string
        
