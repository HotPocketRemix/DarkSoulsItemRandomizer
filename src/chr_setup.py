import logging
log = logging.getLogger(__name__)

import random
from enum import Enum
import math

import chr_init_param as cip
import randomizer_options as rng_opt
import items_setup as item_s


class ChrInitStats:
    def __init__(self, soul_level, vita, attu, ende, stre, dext, inte, fith, luck, humn, resi):
        self.soul_level = soul_level
        self.vita = vita
        self.attu = attu
        self.ende = ende 
        self.stre = stre
        self.dext = dext
        self.inte = inte
        self.fith = fith
        self.luck = luck
        self.humn = humn
        self.resi = resi

class ChrInitWeapons:
    def __init__(self, right_primary, right_secondary, left_primary, left_secondary):
        self.right_primary = right_primary
        self.right_secondary = right_secondary
        self.left_primary = left_primary
        self.left_secondary = left_secondary
        
class ChrInitArmor:
    def __init__(self, head, chest, hand, legs):
        self.head = head
        self.chest = chest
        self.hand = hand
        self.legs = legs

class ChrInitArrows:
    def __init__(self, arrow_primary, arrow_primary_count, 
     arrow_secondary, arrow_secondary_count, bolt_primary, 
     bolt_primary_count, bolt_secondary, bolt_secondary_count):
        self.arrow_primary = arrow_primary
        self.arrow_primary_count = arrow_primary_count
        self.arrow_secondary = arrow_secondary
        self.arrow_secondary_count = arrow_secondary_count
        self.bolt_primary = bolt_primary
        self.bolt_primary_count = bolt_primary_count
        self.bolt_secondary = bolt_secondary
        self.bolt_secondary_count = bolt_secondary_count

class ChrInitRings:
    def __init__(self, ring1 = -1, ring2 = -1, ring3 = -1, ring4 = -1, ring5 = -1):
        self.ring1 = ring1
        self.ring2 = ring2
        self.ring3 = ring3
        self.ring4 = ring4
        self.ring5 = ring5

class ChrInitSkills:
    def __init__(self, skill1 = -1, skill2 = -1, skill3 = -1):
        self.skill1 = skill1
        self.skill2 = skill2
        self.skill3 = skill3
        
class ChrInitSpells:
    def __init__(self, spell1 = -1, spell2 = -1, spell3 = -1,
     spell4 = -1, spell5 = -1, spell6 = -1, spell7 = -1):
        self.spell1 = spell1
        self.spell2 = spell2
        self.spell3 = spell3
        self.spell4 = spell4
        self.spell5 = spell5
        self.spell6 = spell6
        self.spell7 = spell7

class ChrInitItems:
    def __init__(self, item1 = -1, item1_count = 0, item2 = -1,
     item2_count = 0, item3 = -1, item3_count = 0, item4 = -1, 
     item4_count = 0, item5 = -1, item5_count = 0, item6 = -1, 
     item6_count = 0, item7 = -1, item7_count = 0, item8 = -1, 
     item8_count = 0, item9 = -1, item9_count = 0, item10 = -1, 
     item10_count = 0):
        self.item1 = item1
        self.item1_count = item1_count
        self.item2 = item2
        self.item2_count = item2_count
        self.item3 = item3
        self.item3_count = item3_count
        self.item4 = item4
        self.item4_count = item4_count
        self.item5 = item5
        self.item5_count = item5_count
        self.item6 = item6
        self.item6_count = item6_count
        self.item7 = item7
        self.item7_count = item7_count
        self.item8 = item8
        self.item8_count = item8_count
        self.item9 = item9
        self.item9_count = item9_count
        self.item10 = item10
        self.item10_count = item10_count

class ChrInitBodyScale:
    def __init__(self, head_scale, chest_scale, ab_scale, arm_scale, leg_scale):
        self.head_scale = head_scale
        self.chest_scale = chest_scale
        self.ab_scale = ab_scale
        self.arm_scale = arm_scale
        self.leg_scale = leg_scale

class ChrInitGestures:
    def __init__(self, gesture0, gesture1, gesture2, gesture3, gesture4, 
     gesture5, gesture6):
        self.gesture0 = gesture0
        self.gesture1 = gesture1
        self.gesture2 = gesture2
        self.gesture3 = gesture3
        self.gesture4 = gesture4
        self.gesture5 = gesture5
        self.gesture6 = gesture6
    

class ChrInitEntry:
    def __init__(self, stats, weapons, armor, arrows, rings, skills, spells, 
     items, facegen_id, think_id, npc_type, draw_type, sex, body_scale, 
     covenant, gestures, souls = 0, base_hp = 0, base_mp = 0, 
     base_rec_mp = 0, base_sp = 0, base_rec_sp = 0, red_falldam = 0, 
     qwc_sb = 0, qwc_mw = 0, qwc_cd = 0):
        if arrows == None:
            self.arrows = ChrInitArrows(-1, 0, -1, 0, -1, 0, -1, 0)
        else:
            self.arrows = arrows
        
        if rings == None:
            self.rings = ChrInitRings(-1, -1, -1, -1, -1)
        else:
            self.rings = rings
            
        if skills == None:
            self.skills = ChrInitSkills(-1, -1, -1)
        else:
            self.skills = skills
            
        if spells == None:
            self.spells = ChrInitSpells(-1, -1, -1, -1, -1, -1, -1)
        else:
            self.spells = spells
            
        if items == None:
            self.items = ChrInitItems(-1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 
             -1, 0, -1, 0, -1, 0, -1, 0, -1, 0)
        else:
            self.items = items
            
        if body_scale == None:
            self.body_scale = ChrInitBodyScale(0, 0, 0, 0, 0)
        else:
            self.body_scale = body_scale
        
        self.stats = stats
        self.weapons = weapons
        self.armor = armor
        self.base_hp = base_hp
        self.base_mp = base_mp
        self.base_rec_mp = base_rec_mp
        self.base_sp = base_sp
        self.base_rec_sp = base_rec_sp
        self.red_falldam = red_falldam
        self.qwc_sb = qwc_sb
        self.qwc_mw = qwc_mw
        self.qwc_cd = qwc_cd
        self.facegen_id = facegen_id
        self.think_id = think_id
        self.npc_type = npc_type
        self.draw_type = draw_type
        self.sex = sex
        self.covenant = covenant
        self.gestures = gestures
        self.souls = souls

    def to_chr_init(self, chr_init_id, description):
        return cip.ChrInit(chr_init_id, self.base_rec_mp, self.base_rec_sp,
         self.red_falldam, self.souls, self.weapons.right_primary,
         self.weapons.right_secondary, self.weapons.left_primary, self.weapons.left_secondary,
         self.armor.head, self.armor.chest, self.armor.hand, self.armor.legs, 
         self.arrows.arrow_primary, self.arrows.bolt_primary,
         self.arrows.arrow_secondary, self.arrows.bolt_secondary,
         self.rings.ring1, self.rings.ring2, self.rings.ring3, 
         self.rings.ring4, self.rings.ring5, self.skills.skill1, 
         self.skills.skill2, self.skills.skill3, self.spells.spell1,
         self.spells.spell2, self.spells.spell3, self.spells.spell4, 
         self.spells.spell5, self.spells.spell6, self.spells.spell7,
         self.items.item1, self.items.item2, self.items.item3, 
         self.items.item4, self.items.item5, self.items.item6, 
         self.items.item7, self.items.item8, self.items.item9, 
         self.items.item10, self.facegen_id, self.think_id, self.base_hp,
         self.base_mp, self.base_sp, self.arrows.arrow_primary_count,
         self.arrows.bolt_primary_count, self.arrows.arrow_secondary_count,
         self.arrows.bolt_secondary_count, self.qwc_sb, self.qwc_mw, 
         self.qwc_cd, self.stats.soul_level, self.stats.vita, 
         self.stats.attu, self.stats.ende, self.stats.stre, self.stats.dext,
         self.stats.inte, self.stats.fith, self.stats.luck,
         self.stats.humn, self.stats.resi, self.items.item1_count, 
         self.items.item2_count, self.items.item3_count, 
         self.items.item4_count, self.items.item5_count, 
         self.items.item6_count, self.items.item7_count, 
         self.items.item8_count, self.items.item9_count, 
         self.items.item10_count, self.body_scale.head_scale,
         self.body_scale.chest_scale, self.body_scale.ab_scale, 
         self.body_scale.arm_scale, self.body_scale.leg_scale,
         self.gestures.gesture0, self.gestures.gesture1, 
         self.gestures.gesture2, self.gestures.gesture3, 
         self.gestures.gesture4, self.gestures.gesture5, 
         self.gestures.gesture6, self.npc_type, self.draw_type, self.sex,
         self.covenant, description)        

VANILLA_CHRS = {
 1:	   ChrInitEntry(ChrInitStats(  1, 18, 14, 22, 19, 15, 14,  8, 13,  5, 17), ChrInitWeapons( 201005, 1330000, 1452000,      -1), ChrInitArmor( 390000,  391000,  392000,  393000), None, ChrInitRings(100), None, ChrInitSpells(4000, 4100), ChrInitItems(201, 5), 31, 0, 0, 0, 1, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 2:	   ChrInitEntry(ChrInitStats(  0, 14, 18, 50, 12, 11,  8,  9, 11,  3, 15), ChrInitWeapons( 201000,  351000, 1456000, 1330000), ChrInitArmor( 350000,  351000,  352000,  353000), None, ChrInitRings(100), None, ChrInitSpells(4000, 4300, 3550), ChrInitItems(200, 1), -1, 0, 0, 0, 1, None, 1, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 3:	   ChrInitEntry(ChrInitStats(  1, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99), ChrInitWeapons( 201015,      -1, 1450015,      -1), ChrInitArmor( 210000,  211000,  212000,  213000), None, ChrInitRings(138, 148), None, None, ChrInitItems(106, 1, 100, 1, 101, 1, 113, 1, 102, 1, 114, 1, 109, 10, 103, 1, 108, 1, 373, 10), 6270, 0, 0, 0, 1, None, 0, ChrInitGestures(0, 1, 2, 3, 4, 5, 8), 10000000),
 4:	   ChrInitEntry(ChrInitStats(  1, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99), ChrInitWeapons( 201015,      -1, 1450015,      -1), ChrInitArmor( 210000,  211000,  212000,  213000), None, ChrInitRings(138, 148), None, None, ChrInitItems(106, 1, 100, 1, 101, 1, 113, 1, 102, 1, 114, 1, 109, 10, 103, 1, 108, 1, 373, 10), 6270, 0, 0, 0, 1, None, 1, ChrInitGestures(0, 1, 2, 3, 4, 5, 8), 10000000),
 5:	   ChrInitEntry(ChrInitStats(  1, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99), ChrInitWeapons( 201015,      -1, 1450015,      -1), ChrInitArmor( 210000,  211000,  212000,  213000), None, ChrInitRings(138, 148), None, None, ChrInitItems(106, 1, 100, 1, 101, 1, 113, 1, 102, 1, 114, 1, 109, 10, 103, 1, 108, 1, 373, 10), 6270, 0, 0, 0, 1, None, 2, ChrInitGestures(0, 1, 2, 3, 4, 5, 8), 10000000),
 6:    ChrInitEntry(ChrInitStats(  1, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99), ChrInitWeapons( 201015,      -1, 1450015,      -1), ChrInitArmor( 210000,  211000,  212000,  213000), None, ChrInitRings(138, 148), None, None, ChrInitItems(106, 1, 100, 1, 101, 1, 113, 1, 102, 1, 114, 1, 109, 10, 103, 1, 108, 1, 373, 10), 6270, 0, 0, 0, 1, None, 3, ChrInitGestures(0, 1, 2, 3, 4, 5, 8), 10000000),
 7:    ChrInitEntry(ChrInitStats(  1, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99), ChrInitWeapons( 201015,      -1, 1450015,      -1), ChrInitArmor( 210000,  211000,  212000,  213000), None, ChrInitRings(138, 139), None, None, ChrInitItems(106, 1, 100, 1, 101, 1, 113, 1, 102, 1, 114, 1, 109, 10, 103, 1, 108, 1, 373, 10), 6270, 0, 0, 0, 1, None, 4, ChrInitGestures(0, 1, 2, 3, 4, 5, 8), 10000000),
 8:    ChrInitEntry(ChrInitStats(  1, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99), ChrInitWeapons( 201015,      -1, 1450015,      -1), ChrInitArmor( 210000,  211000,  212000,  213000), None, ChrInitRings(138, 139), None, None, ChrInitItems(106, 1, 100, 1, 101, 1, 113, 1, 102, 1, 114, 1, 109, 10, 103, 1, 108, 1, 373, 10), 6270, 0, 0, 0, 1, None, 5, ChrInitGestures(0, 1, 2, 3, 4, 5, 8), 10000000),
 9:    ChrInitEntry(ChrInitStats(  1, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99), ChrInitWeapons( 201015,      -1, 1450015,      -1), ChrInitArmor( 210000,  211000,  212000,  213000), None, ChrInitRings(138, 139), None, None, ChrInitItems(106, 1, 100, 1, 101, 1, 113, 1, 102, 1, 114, 1, 109, 10, 103, 1, 108, 1, 373, 10), 6270, 0, 0, 0, 1, None, 6, ChrInitGestures(0, 1, 2, 3, 4, 5, 8), 10000000),
 10:   ChrInitEntry(ChrInitStats(  1, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99), ChrInitWeapons( 201015,      -1, 1450015,      -1), ChrInitArmor( 210000,  211000,  212000,  213000), None, ChrInitRings(103), None, None, ChrInitItems(106, 1, 100, 1, 101, 1, 113, 1, 102, 1, 114, 1, 109, 10, 103, 1, 108, 1, 373, 10), 6270, 0, 0, 0, 1, None, 7, ChrInitGestures(0, 1, 2, 3, 4, 5, 8), 10000000),
 11:   ChrInitEntry(ChrInitStats(  1, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99), ChrInitWeapons( 201015,      -1, 1450015,      -1), ChrInitArmor( 210000,  211000,  212000,  213000), None, ChrInitRings(102), None, None, ChrInitItems(106, 1, 100, 1, 101, 1, 113, 1, 102, 1, 114, 1, 109, 10, 103, 1, 108, 1, 373, 10), 6270, 0, 0, 0, 1, None, 8, ChrInitGestures(0, 1, 2, 3, 4, 5, 8), 10000000),
 12:   ChrInitEntry(ChrInitStats(  1, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99), ChrInitWeapons( 201015,      -1, 1450015,      -1), ChrInitArmor( 210000,  211000,  212000,  213000), None, ChrInitRings(138, 139), None, None, ChrInitItems(106, 1, 100, 1, 101, 1, 113, 1, 102, 1, 114, 1, 109, 10, 103, 1, 112, 1), 6270, 0, 0, 0, 1, None, 9, ChrInitGestures(0, 1, 2, 3, 4, 5, 8), 10000000),
 100:  ChrInitEntry(ChrInitStats(  0, 50, 50, 99, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons(9012000, 9011000, 9014000, 9010000), ChrInitArmor( 660000,  661000,  662000,  663000), None, None, None, None, ChrInitItems(-1, 1), -1, 0, 0, 0, 1, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 1000000),
 101:  ChrInitEntry(ChrInitStats(  0, 50, 50, 99, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons(1253000, 9016000,      -1,      -1), ChrInitArmor( 700000,  701000,  702000,  703000), ChrInitArrows(-1, 0, -1, 0, 2102000, 99, -1, 0), None, None, None, ChrInitItems(-1, 1), -1, 0, 0, 0, 1, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 1000000),
 1000: ChrInitEntry(ChrInitStats(  0, 21,  8, 21, 18, 18,  7,  9, 11,  5, 10), ChrInitWeapons( 201000,  300000, 1450000, 1200000), ChrInitArmor( 210000,  211000,  212000,  213000), ChrInitArrows(2000000, 50, -1, 0, -1, 0, -1, 0), None, None, None, None, -1, 0, 0, 0, 1, None, 7, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 50000),
 1001: ChrInitEntry(ChrInitStats(  0, 14, 20, 24, 12,  8, 20,  5, 10,  5, 10), ChrInitWeapons(1300000,  701000, 1404000,      -1), ChrInitArmor( 230000,  231000,  232000,  233000), None, None, None, ChrInitSpells(4000, 6100, 3100), None, -1, 0, 0, 0, 1, None, 6, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 50000),
 1002: ChrInitEntry(ChrInitStats(  0, 16, 14, 28, 20,  7, 15,  8,  5,  5, 10), ChrInitWeapons( 350000, 1300000, 1501000,      -1), ChrInitArmor(  10000,   11000,   12000,   13000), None, None, None, None, None, -1, 0, 0, 0, 0, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 50000),
 1003: ChrInitEntry(ChrInitStats(  0, 14,  8, 13, 14, 11,  8,  8, 10,  5, 10), ChrInitWeapons( 801000,      -1, 1501000, 1300000), ChrInitArmor( 240000,  241000,  242000,  243000), None, None, None, ChrInitSpells(3550), None, -1, 10100, 0, 0, 1, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 50000),
 1010: ChrInitEntry(ChrInitStats(  0, 20, 12, 24, 18, 15,  7,  9, 11,  5, 10), ChrInitWeapons( 201000, 1050000, 1501000, 1300000), ChrInitArmor( 210000,  211000,  212000,  213000), None, None, None, None, None, -1, 0, 0, 0, 1, ChrInitBodyScale(100, 100, 100, 100, 100), 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 50000),
 1011: ChrInitEntry(ChrInitStats(  0, 16, 16, 28, 15, 12,  5, 18,  6,  5, 10), ChrInitWeapons( 801000,      -1, 1450000, 1300000), ChrInitArmor( 180000,  181000,  182000,  183000), None, None, None, None, None, -1, 0, 0, 0, 1, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 50000),
 1012: ChrInitEntry(ChrInitStats(  0, 14, 24, 16, 12, 12, 25,  3, 10,  5, 10), ChrInitWeapons(1300000,  201000, 1404000,      -1), ChrInitArmor( 220000,  221000,  222000,  223000), None, None, None, None, None, -1, 0, 0, 0, 1, ChrInitBodyScale(-100, -100, -100, -100, -100), 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 50000),
 1030: ChrInitEntry(ChrInitStats(  0, 20, 14, 19, 18, 15,  7,  9,  8,  3,  6), ChrInitWeapons( 800000, 1000000, 1450000, 1300000), ChrInitArmor(  50000,   51000,   52000,   53000), None, None, None, None, None, -1, 0, 0, 0, 1, ChrInitBodyScale(-100, -100, -100, -100, -100), 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 50000),
 1031: ChrInitEntry(ChrInitStats(  0, 14, 21, 15, 14, 17, 20,  3,  5,  2,  8), ChrInitWeapons( 201000, 1050000, 1404000, 1300000), ChrInitArmor(  60000,   61000,   62000,   63000), None, ChrInitRings(128), None, ChrInitSpells(3550), None, -1, 0, 0, 0, 1, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 50000),
 1032: ChrInitEntry(ChrInitStats(  0, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99), ChrInitWeapons( 350000, 1100000, 1501000, 1300000), ChrInitArmor(  70000,   71000,   72000,   73000), None, None, None, None, None, -1, 0, 0, 0, 1, ChrInitBodyScale(100, 100, 100, 100, 100), 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 50000),
 1040: ChrInitEntry(ChrInitStats(  0, 15,  9, 12, 12, 11,  8,  8, 10,  3, 10), ChrInitWeapons( 201000, 1100000, 1452000,      -1), ChrInitArmor( 210000,  211000,  212000,  213000), None, None, None, None, None, 1, 0, 0, 0, 1, ChrInitBodyScale(0, 100, 0, 100, 0), 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 1041: ChrInitEntry(ChrInitStats(  0, 12, 10, 13, 11, 12,  9,  8, 12,  2, 11), ChrInitWeapons( 401000, 1000000, 1201000, 1402000), ChrInitArmor( 240000,  241000,  242000,  243000), ChrInitArrows(2000000, 30, 2003000, 10, -1, 0, -1, 0), ChrInitRings(100), None, None, None, 1, 0, 0, 0, 1, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 1042: ChrInitEntry(ChrInitStats(  0,  9, 15, 10,  9, 11, 15,  6, 11,  3,  9), ChrInitWeapons(1300000,  701000, 1402000,      -1), ChrInitArmor( 230000,  231000,  232000,  233000), None, ChrInitRings(100, 2), None, ChrInitSpells(4020, 4360, 3550, 6100), None, 1, 0, 0, 0, 1, ChrInitBodyScale(100, 100, 0, 100, 0), 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 1043: ChrInitEntry(ChrInitStats(  0, 17, 20, 18, 14, 12, 13, 14, 13,  5, 14), ChrInitWeapons( 202000,  802000, 1450000, 1360000), ChrInitArmor(  10000,   11000,   12000,   13000), None, ChrInitRings(100, 2), None, ChrInitSpells(5000, 5300, 5500), None, 1, 0, 0, 0, 1, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 1050: ChrInitEntry(ChrInitStats(  1, 14,  4, 10, 16,  9,  2,  6,  7,  3, 10), ChrInitWeapons( 201000, 1000000, 1450000,      -1), ChrInitArmor( 210000,  211000,  212000,  213000), None, None, None, None, ChrInitItems(201, 5), 30, 0, 0, 0, 1, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 1051: ChrInitEntry(ChrInitStats(  1, 12, 12, 12, 12,  8,  5, 10,  4,  5,  6), ChrInitWeapons( 202000, 1360000, 1452000,      -1), ChrInitArmor( 390000,  391000,  392000,  393000), None, None, None, ChrInitSpells(5300, 5000), ChrInitItems(201, 5, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 5000, 1, 5300, 1), 31, 0, 0, 0, 1, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 1052: ChrInitEntry(ChrInitStats(  1,  8, 15,  6,  7, 12, 13,  5,  6,  3,  9), ChrInitWeapons(1300000,  100000, 1460000,      -1), ChrInitArmor( 220000,  221000,  222000,  223000), None, None, None, ChrInitSpells(3300, 3000), ChrInitItems(201, 5, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 3000, 1, 3300, 1, 2603, 1), 32, 0, 0, 0, 0, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 1053: ChrInitEntry(ChrInitStats(  1,  9, 12,  9,  8, 11, 16,  5,  5,  2,  7), ChrInitWeapons(1330000,  700000, 1403000,      -1), ChrInitArmor( 230000,  231000,  232000,  233000), None, None, None, ChrInitSpells(4000), ChrInitItems(201, 5, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 4000, 1, 2603, 1), 33, 0, 0, 0, 1, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 1054: ChrInitEntry(ChrInitStats(  1, 14,  4, 10, 16,  9,  2,  6,  7,  0, 10), ChrInitWeapons( 203000,      -1,      -1,      -1), ChrInitArmor( 210000,  211000,  212000,  213000), None, None, None, None, None, 30, 0, 0, 4, 1, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 1055: ChrInitEntry(ChrInitStats(  1, 12, 12, 12, 12,  8,  5, 10,  4,  0,  6), ChrInitWeapons( 203000,      -1,      -1,      -1), ChrInitArmor( 390000,  391000,  392000,  393000), None, None, None, ChrInitSpells(5300, 5000), ChrInitItems(-1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 5000, 1, 5300, 1), 31, 0, 0, 4, 1, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 1056: ChrInitEntry(ChrInitStats(  1,  8, 15,  6,  7, 12, 13,  5,  6,  0,  9), ChrInitWeapons( 203000,      -1,      -1,      -1), ChrInitArmor( 220000,  221000,  222000,  223000), None, None, None, ChrInitSpells(3300, 3000), ChrInitItems(-1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 3000, 1, 3300, 1, 2603, 1), 32, 0, 0, 4, 0, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 1057: ChrInitEntry(ChrInitStats(  1,  9, 12,  9,  8, 11, 16,  5,  5,  0,  7), ChrInitWeapons( 203000,      -1,      -1,      -1), ChrInitArmor( 230000,  231000,  232000,  233000), None, None, None, ChrInitSpells(4000), ChrInitItems(-1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 4000, 1, 2603, 1), 33, 0, 0, 4, 1, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 2000: ChrInitEntry(ChrInitStats(  4, 11,  8, 12, 13, 13,  9,  9, 10,  0, 11), ChrInitWeapons( 212000,      -1,      -1,      -1), ChrInitArmor( 210000,  211000,  212000,  213000), None, None, None, None, ChrInitItems(-1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 103, 1, 117, 1), -1, 0, 0, 4, 1, None, 0, ChrInitGestures(0, 1, 2, 3, 4, 5, 8), 0),
 2001: ChrInitEntry(ChrInitStats(  5, 14, 10, 10, 11, 11,  9, 11, 10,  0, 10), ChrInitWeapons( 212000,      -1,      -1,      -1), ChrInitArmor( 390000,  391000,  392000,  393000), None, None, None, None, ChrInitItems(-1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 103, 1, 117, 1), -1, 0, 0, 4, 1, None, 1, ChrInitGestures(0, 1, 2, 3, 4, 5, 13), 0),
 2002: ChrInitEntry(ChrInitStats(  3, 10, 11, 10, 10, 14, 11,  8, 10,  0, 12), ChrInitWeapons( 212000,      -1,      -1,      -1), ChrInitArmor( 360000,  361000,  362000,  363000), None, None, None, None, ChrInitItems(-1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 103, 1, 117, 1), -1, 0, 0, 4, 1, None, 0, ChrInitGestures(0, 1, 2, 3, 4, 5, 8), 0),
 2003: ChrInitEntry(ChrInitStats(  5,  9, 11,  9,  9, 15, 12, 11, 10,  0, 10), ChrInitWeapons( 212000,      -1,      -1,      -1), ChrInitArmor( 300000,  301000,  302000,  303000), None, None, None, None, ChrInitItems(2100, 1, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 103, 1, 117, 1), -1, 0, 0, 4, 1, None, 0, ChrInitGestures(0, 1, 2, 3, 4, 5, 8), 0),
 2004: ChrInitEntry(ChrInitStats(  4, 12,  8, 14, 14,  9,  8, 10, 10,  0, 11), ChrInitWeapons( 212000,      -1,      -1,      -1), ChrInitArmor(  50000,   51000,   52000,   53000), None, None, None, None, ChrInitItems(-1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 103, 1, 117, 1), -1, 0, 0, 4, 1, None, 0, ChrInitGestures(0, 1, 2, 3, 4, 5, 8), 0),
 2005: ChrInitEntry(ChrInitStats(  4, 11,  9, 11, 12, 14,  9,  9, 10,  0, 11), ChrInitWeapons( 212000,      -1,      -1,      -1), ChrInitArmor( 900000,  241000,  242000,  243000), None, None, None, None, ChrInitItems(-1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 103, 1, 117, 1), -1, 0, 0, 4, 1, None, 0, ChrInitGestures(0, 1, 2, 3, 4, 5, 8), 0),
 2006: ChrInitEntry(ChrInitStats(  3,  8, 15,  8,  9, 11, 15,  8, 10,  0,  8), ChrInitWeapons( 212000,      -1,      -1,      -1), ChrInitArmor( 220000,  221000,  222000,  223000), None, None, None, ChrInitSpells(3000), ChrInitItems(3000, 1, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 103, 1, 117, 1), -1, 0, 0, 4, 1, None, 0, ChrInitGestures(0, 1, 2, 3, 4, 5, 8), 0),
 2007: ChrInitEntry(ChrInitStats(  1, 10, 12, 11, 12,  9, 10,  8, 10,  0, 12), ChrInitWeapons( 212000,      -1,      -1,      -1), ChrInitArmor( 230000,  231000,  232000,  233000), None, None, None, ChrInitSpells(4000), ChrInitItems(4000, 1, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 103, 1, 117, 1), -1, 0, 0, 4, 1, None, 0, ChrInitGestures(0, 1, 2, 3, 4, 5, 8), 0),
 2008: ChrInitEntry(ChrInitStats(  2, 11, 11,  9, 12,  8,  8, 14, 10,  0, 11), ChrInitWeapons( 212000,      -1,      -1,      -1), ChrInitArmor( 900000,  311000,  312000,  313000), None, None, None, ChrInitSpells(5000), ChrInitItems(5000, 1, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 103, 1, 117, 1), -1, 0, 0, 4, 1, None, 1, ChrInitGestures(0, 1, 2, 3, 4, 5, 13), 0),
 2009: ChrInitEntry(ChrInitStats(  6, 11, 11, 11, 11, 11, 11, 11, 10,  0, 11), ChrInitWeapons( 212000,      -1,      -1,      -1), ChrInitArmor( 900000,  901000,  902000,  903000), None, None, None, None, ChrInitItems(-1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 103, 1, 117, 1), -1, 0, 0, 4, 1, None, 0, ChrInitGestures(0, 1, 2, 3, 4, 5, 8), 0),
 2020: ChrInitEntry(ChrInitStats(  1, 15,  6, 11, 12, 13,  6,  5,  7,  1, 10), ChrInitWeapons( 201000, 1250000, 1450000,      -1), ChrInitArmor( 210000,  211000,  212000,  213000), ChrInitArrows(-1, 0, -1, 0, 2100000, 20, -1, 0), None, None, None, ChrInitItems(201, 5, 100, 1, 106, 1, -1, 0, 2607, 1), 30, 0, 0, 0, 1, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 2021: ChrInitEntry(ChrInitStats(  1, 13, 12, 12, 14,  6,  4, 10,  4,  1, 11), ChrInitWeapons( 202000, 1000000, 1452000, 1360000), ChrInitArmor( 390000,  391000,  392000,  393000), None, None, None, ChrInitSpells(5000, 5300), ChrInitItems(201, 5, 100, 1, 106, 1, -1, 0, 2607, 1, 5000, 1, 5300, 1), 31, 0, 0, 0, 1, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 2022: ChrInitEntry(ChrInitStats(  1,  7, 15,  9,  8, 10, 16,  5,  5,  1,  9), ChrInitWeapons(1300000,  100000, 1460000,      -1), ChrInitArmor(     -1,  221000,  222000,  223000), None, None, None, ChrInitSpells(3000, 3300), ChrInitItems(201, 5, 100, 1, 106, 1, -1, 0, 2607, 1, 3000, 1, 3300, 1), 32, 0, 0, 0, 0, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 2023: ChrInitEntry(ChrInitStats(  1,  9, 13,  9, 10,  7, 12,  3, 13,  1,  9), ChrInitWeapons(1330000,  700000, 1408000, 1200000), ChrInitArmor( 230000,  231000,  232000,  233000), ChrInitArrows(2000000, 20, -1, 0, -1, 0, -1, 0), None, None, ChrInitSpells(4000, 4310), ChrInitItems(201, 5, 109, 1, 106, 1, -1, 0, 2607, 1, 4000, 1, 4310, 1), 33, 0, 0, 0, 1, None, 6, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 2024: ChrInitEntry(ChrInitStats( 40, 20, 14, 16, 21, 17,  6, 16,  5,  1, 10), ChrInitWeapons( 206001,  301001, 1472000, 1360000), ChrInitArmor( 160000,  161000,  162000,  163000), None, ChrInitRings(100), None, ChrInitSpells(6000, 5500), ChrInitItems(201, 5, 100, 1, 106, 1, -1, 0, 2607, 1, 6000, 1, 5500, 1), 34, 0, 0, 0, 1, None, 2, ChrInitGestures(5, 0, 4, 7, 3, 1, 2), 0),
 2025: ChrInitEntry(ChrInitStats(  1,  8,  7, 10, 13, 12,  7,  5,  8,  1, 10), ChrInitWeapons( 310000, 1105000, 1474000,      -1), ChrInitArmor( 320000,  321000,  322000,  323000), None, None, None, None, ChrInitItems(201, 5, 102, 1, 106, 1, -1, 0, 2607, 1), 30, 0, 0, 0, 1, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 2100: ChrInitEntry(ChrInitStats(  0, 50, 50, 99, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons(     -1,      -1,      -1,      -1), ChrInitArmor( 900000,  901000,  902000,  903000), None, None, None, None, None, 2, 0, 0, 0, 1, None, 0, ChrInitGestures(-1, -1, -1, -1, -1, -1, -1), 50000),
 2101: ChrInitEntry(ChrInitStats(  0, 50, 50, 99, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons(     -1,      -1,      -1,      -1), ChrInitArmor( 900000,  901000,  902000,  903000), None, None, None, None, None, 1, 0, 0, 0, 1, ChrInitBodyScale(-50, -50, -50, -50, -50), 0, ChrInitGestures(-1, -1, -1, -1, -1, -1, -1), 50000),
 2102: ChrInitEntry(ChrInitStats(  0, 50, 50, 99, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons(     -1,      -1,      -1,      -1), ChrInitArmor( 900000,  901000,  902000,  903000), None, None, None, None, None, 1, 0, 0, 0, 1, ChrInitBodyScale(-100, -100, -100, -100, -100), 0, ChrInitGestures(-1, -1, -1, -1, -1, -1, -1), 50000),
 2103: ChrInitEntry(ChrInitStats(  0, 50, 50, 99, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons(     -1,      -1,      -1,      -1), ChrInitArmor( 900000,  901000,  902000,  903000), None, None, None, None, None, 2, 0, 0, 0, 1, ChrInitBodyScale(50, 50, 50, 50, 50), 0, ChrInitGestures(-1, -1, -1, -1, -1, -1, -1), 50000),
 2104: ChrInitEntry(ChrInitStats(  0, 50, 50, 99, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons(     -1,      -1,      -1,      -1), ChrInitArmor( 900000,  901000,  902000,  903000), None, None, None, None, None, 2, 0, 0, 0, 1, ChrInitBodyScale(100, 100, 100, 100, 100), 0, ChrInitGestures(-1, -1, -1, -1, -1, -1, -1), 50000),
 2105: ChrInitEntry(ChrInitStats(  0, 50, 50, 99, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons(     -1,      -1,      -1,      -1), ChrInitArmor( 900000,  901000,  902000,  903000), None, None, None, None, None, 3, 0, 0, 0, 1, ChrInitBodyScale(0, 100, 0, 100, 0), 0, ChrInitGestures(-1, -1, -1, -1, -1, -1, -1), 50000),
 2106: ChrInitEntry(ChrInitStats(  0, 50, 50, 99, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons(     -1,      -1,      -1,      -1), ChrInitArmor( 900000,  901000,  902000,  903000), None, None, None, None, None, 3, 0, 0, 0, 1, ChrInitBodyScale(0, 0, 100, 0, 100), 0, ChrInitGestures(-1, -1, -1, -1, -1, -1, -1), 50000),
 2107: ChrInitEntry(ChrInitStats(  0, 50, 50, 99, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons(     -1,      -1,      -1,      -1), ChrInitArmor( 900000,  901000,  902000,  903000), None, None, None, None, None, 3, 0, 0, 0, 1, ChrInitBodyScale(100, 0, 0, 0, 0), 0, ChrInitGestures(-1, -1, -1, -1, -1, -1, -1), 50000),
 2108: ChrInitEntry(ChrInitStats(  0, 50, 50, 99, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons(     -1,      -1,      -1,      -1), ChrInitArmor( 900000,  901000,  902000,  903000), None, None, None, None, None, 3, 0, 0, 0, 1, ChrInitBodyScale(-100, 0, 0, 0, 0), 0, ChrInitGestures(-1, -1, -1, -1, -1, -1, -1), 50000),
 2200: ChrInitEntry(ChrInitStats(  0, 50, 50, 99, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons(     -1,      -1,      -1,      -1), ChrInitArmor( 900000,  901000,  902000,  903000), None, None, None, None, None, 2, 0, 0, 0, 1, None, 0, ChrInitGestures(-1, -1, -1, -1, -1, -1, -1), 50000),
 2201: ChrInitEntry(ChrInitStats(  0, 50, 50, 99, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons(     -1,      -1,      -1,      -1), ChrInitArmor( 900000,  901000,  902000,  903000), None, None, None, None, None, 1, 0, 0, 0, 1, ChrInitBodyScale(-50, -50, -50, -50, -50), 0, ChrInitGestures(-1, -1, -1, -1, -1, -1, -1), 50000),
 2202: ChrInitEntry(ChrInitStats(  0, 50, 50, 99, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons(     -1,      -1,      -1,      -1), ChrInitArmor( 900000,  901000,  902000,  903000), None, None, None, None, None, 1, 0, 0, 0, 1, ChrInitBodyScale(-100, -100, -100, -100, -100), 0, ChrInitGestures(-1, -1, -1, -1, -1, -1, -1), 50000),
 2203: ChrInitEntry(ChrInitStats(  0, 50, 50, 99, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons(     -1,      -1,      -1,      -1), ChrInitArmor( 900000,  901000,  902000,  903000), None, None, None, None, None, 2, 0, 0, 0, 1, ChrInitBodyScale(50, 50, 50, 50, 50), 0, ChrInitGestures(-1, -1, -1, -1, -1, -1, -1), 50000),
 2204: ChrInitEntry(ChrInitStats(  0, 50, 50, 99, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons(     -1,      -1,      -1,      -1), ChrInitArmor( 900000,  901000,  902000,  903000), None, None, None, None, None, 2, 0, 0, 0, 1, ChrInitBodyScale(100, 100, 100, 100, 100), 0, ChrInitGestures(-1, -1, -1, -1, -1, -1, -1), 50000),
 2205: ChrInitEntry(ChrInitStats(  0, 50, 50, 99, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons(     -1,      -1,      -1,      -1), ChrInitArmor( 900000,  901000,  902000,  903000), None, None, None, None, None, 3, 0, 0, 0, 1, ChrInitBodyScale(0, 100, 0, 100, 0), 0, ChrInitGestures(-1, -1, -1, -1, -1, -1, -1), 50000),
 2206: ChrInitEntry(ChrInitStats(  0, 50, 50, 99, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons(     -1,      -1,      -1,      -1), ChrInitArmor( 900000,  901000,  902000,  903000), None, None, None, None, None, 3, 0, 0, 0, 1, ChrInitBodyScale(0, 0, 100, 0, 100), 0, ChrInitGestures(-1, -1, -1, -1, -1, -1, -1), 50000),
 2207: ChrInitEntry(ChrInitStats(  0, 50, 50, 99, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons(     -1,      -1,      -1,      -1), ChrInitArmor( 900000,  901000,  902000,  903000), None, None, None, None, None, 3, 0, 0, 0, 1, ChrInitBodyScale(100, 0, 0, 0, 0), 0, ChrInitGestures(-1, -1, -1, -1, -1, -1, -1), 50000),
 2208: ChrInitEntry(ChrInitStats(  0, 50, 50, 99, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons(     -1,      -1,      -1,      -1), ChrInitArmor( 900000,  901000,  902000,  903000), None, None, None, None, None, 3, 0, 0, 0, 1, ChrInitBodyScale(-100, 0, 0, 0, 0), 0, ChrInitGestures(-1, -1, -1, -1, -1, -1, -1), 50000),
 2300: ChrInitEntry(ChrInitStats(  0, 50, 50, 99, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons(     -1,      -1,      -1,      -1), ChrInitArmor( 900000,  901000,  902000,  903000), None, None, None, None, None, 1000, 0, 0, 0, 1, ChrInitBodyScale(50, 50, 50, 50, 50), 0, ChrInitGestures(-1, -1, -1, -1, -1, -1, -1), 50000),
 2301: ChrInitEntry(ChrInitStats(  0, 50, 50, 99, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons(     -1,      -1,      -1,      -1), ChrInitArmor( 900000,  901000,  902000,  903000), None, None, None, None, None, 1001, 0, 0, 0, 1, ChrInitBodyScale(50, 50, 50, 50, 50), 0, ChrInitGestures(-1, -1, -1, -1, -1, -1, -1), 50000),
 2302: ChrInitEntry(ChrInitStats(  0, 50, 50, 99, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons(     -1,      -1,      -1,      -1), ChrInitArmor( 900000,  901000,  902000,  903000), None, None, None, None, None, 1002, 0, 0, 0, 1, ChrInitBodyScale(50, 50, 50, 50, 50), 0, ChrInitGestures(-1, -1, -1, -1, -1, -1, -1), 50000),
 2303: ChrInitEntry(ChrInitStats(  0, 50, 50, 99, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons(     -1,      -1,      -1,      -1), ChrInitArmor( 900000,  901000,  902000,  903000), None, None, None, None, None, 1003, 0, 0, 0, 1, ChrInitBodyScale(50, 50, 50, 50, 50), 0, ChrInitGestures(-1, -1, -1, -1, -1, -1, -1), 50000),
 2304: ChrInitEntry(ChrInitStats(  0, 50, 50, 99, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons(     -1,      -1,      -1,      -1), ChrInitArmor( 900000,  901000,  902000,  903000), None, None, None, None, None, 1004, 0, 0, 0, 1, ChrInitBodyScale(50, 50, 50, 50, 50), 0, ChrInitGestures(-1, -1, -1, -1, -1, -1, -1), 50000),
 2305: ChrInitEntry(ChrInitStats(  0, 50, 50, 99, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons(     -1,      -1,      -1,      -1), ChrInitArmor( 900000,  901000,  902000,  903000), None, None, None, None, None, 1005, 0, 0, 0, 1, ChrInitBodyScale(50, 50, 50, 50, 50), 0, ChrInitGestures(-1, -1, -1, -1, -1, -1, -1), 50000),
 2306: ChrInitEntry(ChrInitStats(  0, 50, 50, 99, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons(     -1,      -1,      -1,      -1), ChrInitArmor( 900000,  901000,  902000,  903000), None, None, None, None, None, 1006, 0, 0, 0, 1, ChrInitBodyScale(50, 50, 50, 50, 50), 0, ChrInitGestures(-1, -1, -1, -1, -1, -1, -1), 50000),
 2307: ChrInitEntry(ChrInitStats(  0, 50, 50, 99, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons(     -1,      -1,      -1,      -1), ChrInitArmor( 900000,  901000,  902000,  903000), None, None, None, None, None, 1007, 0, 0, 0, 1, ChrInitBodyScale(50, 50, 50, 50, 50), 0, ChrInitGestures(-1, -1, -1, -1, -1, -1, -1), 50000),
 2308: ChrInitEntry(ChrInitStats(  0, 50, 50, 99, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons(     -1,      -1,      -1,      -1), ChrInitArmor( 900000,  901000,  902000,  903000), None, None, None, None, None, 1008, 0, 0, 0, 1, ChrInitBodyScale(50, 50, 50, 50, 50), 0, ChrInitGestures(-1, -1, -1, -1, -1, -1, -1), 50000),
 2309: ChrInitEntry(ChrInitStats(  0, 50, 50, 99, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons(     -1,      -1,      -1,      -1), ChrInitArmor( 900000,  901000,  902000,  903000), None, None, None, None, None, 1009, 0, 0, 0, 1, ChrInitBodyScale(50, 50, 50, 50, 50), 0, ChrInitGestures(-1, -1, -1, -1, -1, -1, -1), 50000),
 2310: ChrInitEntry(ChrInitStats(  0, 50, 50, 99, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons(     -1,      -1,      -1,      -1), ChrInitArmor( 900000,  901000,  902000,  903000), None, None, None, None, None, 2000, 0, 0, 0, 0, ChrInitBodyScale(50, 50, 50, 50, 50), 0, ChrInitGestures(-1, -1, -1, -1, -1, -1, -1), 50000),
 2311: ChrInitEntry(ChrInitStats(  0, 50, 50, 99, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons(     -1,      -1,      -1,      -1), ChrInitArmor( 900000,  901000,  902000,  903000), None, None, None, None, None, 2001, 0, 0, 0, 0, ChrInitBodyScale(50, 50, 50, 50, 50), 0, ChrInitGestures(-1, -1, -1, -1, -1, -1, -1), 50000),
 2312: ChrInitEntry(ChrInitStats(  0, 50, 50, 99, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons(     -1,      -1,      -1,      -1), ChrInitArmor( 900000,  901000,  902000,  903000), None, None, None, None, None, 2002, 0, 0, 0, 0, ChrInitBodyScale(50, 50, 50, 50, 50), 0, ChrInitGestures(-1, -1, -1, -1, -1, -1, -1), 50000),
 2313: ChrInitEntry(ChrInitStats(  0, 50, 50, 99, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons(     -1,      -1,      -1,      -1), ChrInitArmor( 900000,  901000,  902000,  903000), None, None, None, None, None, 2003, 0, 0, 0, 0, ChrInitBodyScale(50, 50, 50, 50, 50), 0, ChrInitGestures(-1, -1, -1, -1, -1, -1, -1), 50000),
 2314: ChrInitEntry(ChrInitStats(  0, 50, 50, 99, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons(     -1,      -1,      -1,      -1), ChrInitArmor( 900000,  901000,  902000,  903000), None, None, None, None, None, 2004, 0, 0, 0, 0, ChrInitBodyScale(50, 50, 50, 50, 50), 0, ChrInitGestures(-1, -1, -1, -1, -1, -1, -1), 50000),
 2315: ChrInitEntry(ChrInitStats(  0, 50, 50, 99, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons(     -1,      -1,      -1,      -1), ChrInitArmor( 900000,  901000,  902000,  903000), None, None, None, None, None, 2005, 0, 0, 0, 0, ChrInitBodyScale(50, 50, 50, 50, 50), 0, ChrInitGestures(-1, -1, -1, -1, -1, -1, -1), 50000),
 2316: ChrInitEntry(ChrInitStats(  0, 50, 50, 99, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons(     -1,      -1,      -1,      -1), ChrInitArmor( 900000,  901000,  902000,  903000), None, None, None, None, None, 2006, 0, 0, 0, 0, ChrInitBodyScale(50, 50, 50, 50, 50), 0, ChrInitGestures(-1, -1, -1, -1, -1, -1, -1), 50000),
 2317: ChrInitEntry(ChrInitStats(  0, 50, 50, 99, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons(     -1,      -1,      -1,      -1), ChrInitArmor( 900000,  901000,  902000,  903000), None, None, None, None, None, 2007, 0, 0, 0, 0, ChrInitBodyScale(50, 50, 50, 50, 50), 0, ChrInitGestures(-1, -1, -1, -1, -1, -1, -1), 50000),
 2318: ChrInitEntry(ChrInitStats(  0, 50, 50, 99, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons(     -1,      -1,      -1,      -1), ChrInitArmor( 900000,  901000,  902000,  903000), None, None, None, None, None, 2008, 0, 0, 0, 0, ChrInitBodyScale(50, 50, 50, 50, 50), 0, ChrInitGestures(-1, -1, -1, -1, -1, -1, -1), 50000),
 2319: ChrInitEntry(ChrInitStats(  0, 50, 50, 99, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons(     -1,      -1,      -1,      -1), ChrInitArmor( 900000,  901000,  902000,  903000), None, None, None, None, None, 2009, 0, 0, 0, 0, ChrInitBodyScale(50, 50, 50, 50, 50), 0, ChrInitGestures(-1, -1, -1, -1, -1, -1, -1), 50000),
 2400: ChrInitEntry(ChrInitStats(  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0), ChrInitWeapons(      0,       0,       0,       0), ChrInitArmor(      0,       0,       0,       0), ChrInitArrows(0, 0, 0, 0, 0, 0, 0, 0), ChrInitRings(0, 0, 0, 0, 0), ChrInitSkills(0, 0, 0), ChrInitSpells(0, 0, 0, 0, 0, 0, 0), ChrInitItems(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 0, 0, 0, 0, 0, None, 0, ChrInitGestures(0, 0, 0, 0, 0, 0, 0), 0),
 2401: ChrInitEntry(ChrInitStats(  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0), ChrInitWeapons(      0,       0,       0,       0), ChrInitArmor(      0,       0,       0,       0), ChrInitArrows(0, 0, 0, 0, 0, 0, 0, 0), ChrInitRings(0, 0, 0, 0, 0), ChrInitSkills(0, 0, 0), ChrInitSpells(0, 0, 0, 0, 0, 0, 0), ChrInitItems(240, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 0, 0, 0, 0, 0, None, 0, ChrInitGestures(0, 0, 0, 0, 0, 0, 0), 0),
 2402: ChrInitEntry(ChrInitStats(  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0), ChrInitWeapons(      0,       0,       0,       0), ChrInitArmor(      0,       0,       0,       0), ChrInitArrows(0, 0, 0, 0, 0, 0, 0, 0), ChrInitRings(0, 0, 0, 0, 0), ChrInitSkills(0, 0, 0), ChrInitSpells(0, 0, 0, 0, 0, 0, 0), ChrInitItems(297, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 0, 0, 0, 0, 0, None, 0, ChrInitGestures(0, 0, 0, 0, 0, 0, 0), 0),
 2403: ChrInitEntry(ChrInitStats(  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0), ChrInitWeapons(      0,       0,       0,       0), ChrInitArmor(      0,       0,       0,       0), ChrInitArrows(0, 0, 0, 0, 0, 0, 0, 0), ChrInitRings(0, 0, 0, 0, 0), ChrInitSkills(0, 0, 0), ChrInitSpells(0, 0, 0, 0, 0, 0, 0), ChrInitItems(501, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 0, 0, 0, 0, 0, None, 0, ChrInitGestures(0, 0, 0, 0, 0, 0, 0), 0),
 2404: ChrInitEntry(ChrInitStats(  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0), ChrInitWeapons(      0,       0,       0,       0), ChrInitArmor(      0,       0,       0,       0), ChrInitArrows(0, 0, 0, 0, 0, 0, 0, 0), ChrInitRings(0, 0, 0, 0, 0), ChrInitSkills(0, 0, 0), ChrInitSpells(0, 0, 0, 0, 0, 0, 0), ChrInitItems(371, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 0, 0, 0, 0, 0, None, 0, ChrInitGestures(0, 0, 0, 0, 0, 0, 0), 0),
 2405: ChrInitEntry(ChrInitStats(  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0), ChrInitWeapons(      0,       0,       0,       0), ChrInitArmor(      0,       0,       0,       0), ChrInitArrows(0, 0, 0, 0, 0, 0, 0, 0), ChrInitRings(0, 0, 0, 0, 0), ChrInitSkills(0, 0, 0), ChrInitSpells(0, 0, 0, 0, 0, 0, 0), ChrInitItems(376, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 0, 0, 0, 0, 0, None, 0, ChrInitGestures(0, 0, 0, 0, 0, 0, 0), 0),
 2406: ChrInitEntry(ChrInitStats(  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0), ChrInitWeapons(      0,       0,       0,       0), ChrInitArmor(      0,       0,       0,       0), ChrInitArrows(0, 0, 0, 0, 0, 0, 0, 0), ChrInitRings(0, 0, 0, 0, 0), ChrInitSkills(0, 0, 0), ChrInitSpells(0, 0, 0, 0, 0, 0, 0), ChrInitItems(2100, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 0, 0, 0, 0, 0, None, 0, ChrInitGestures(0, 0, 0, 0, 0, 0, 0), 0),
 2407: ChrInitEntry(ChrInitStats(  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0), ChrInitWeapons(      0,       0,       0,       0), ChrInitArmor(      0,       0,       0,       0), ChrInitArrows(0, 0, 0, 0, 0, 0, 0, 0), ChrInitRings(111, 0, 0, 0, 0), ChrInitSkills(0, 0, 0), ChrInitSpells(0, 0, 0, 0, 0, 0, 0), ChrInitItems(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 0, 0, 0, 0, 0, None, 0, ChrInitGestures(0, 0, 0, 0, 0, 0, 0), 0),
 2408: ChrInitEntry(ChrInitStats(  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0), ChrInitWeapons(      0,       0,       0,       0), ChrInitArmor(      0,       0,       0,       0), ChrInitArrows(0, 0, 0, 0, 0, 0, 0, 0), ChrInitRings(137, 0, 0, 0, 0), ChrInitSkills(0, 0, 0), ChrInitSpells(0, 0, 0, 0, 0, 0, 0), ChrInitItems(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 0, 0, 0, 0, 0, None, 0, ChrInitGestures(0, 0, 0, 0, 0, 0, 0), 0),
 3000: ChrInitEntry(ChrInitStats(  4, 11,  8, 12, 13, 13,  9,  9, 10,  0, 11), ChrInitWeapons( 201000,      -1, 1450000,      -1), ChrInitArmor( 210000,  211000,  212000,  213000), None, None, None, None, ChrInitItems(-1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 103, 1, 117, 1), -1, 0, 0, 0, 1, None, 0, ChrInitGestures(0, 1, 2, 3, 4, 5, 8), 0),
 3001: ChrInitEntry(ChrInitStats(  5, 14, 10, 10, 11, 11,  9, 11, 10,  0, 10), ChrInitWeapons( 202000,      -1, 1452000,      -1), ChrInitArmor( 390000,  391000,  392000,  393000), None, None, None, None, ChrInitItems(-1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 103, 1, 117, 1), -1, 0, 0, 0, 1, None, 1, ChrInitGestures(0, 1, 2, 3, 4, 5, 13), 0),
 3002: ChrInitEntry(ChrInitStats(  3, 10, 11, 10, 10, 14, 11,  8, 10,  0, 12), ChrInitWeapons( 400000,      -1, 1408000,      -1), ChrInitArmor( 360000,  361000,  362000,  363000), None, None, None, None, ChrInitItems(-1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 103, 1, 117, 1), -1, 0, 0, 0, 1, None, 0, ChrInitGestures(0, 1, 2, 3, 4, 5, 8), 0),
 3003: ChrInitEntry(ChrInitStats(  5,  9, 11,  9,  9, 15, 12, 11, 10,  0, 10), ChrInitWeapons( 103000,      -1, 1404000,      -1), ChrInitArmor( 300000,  301000,  302000,  303000), None, None, None, None, ChrInitItems(2100, 1, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 103, 1, 117, 1), -1, 0, 0, 0, 1, None, 0, ChrInitGestures(0, 1, 2, 3, 4, 5, 8), 0),
 3004: ChrInitEntry(ChrInitStats(  4, 12,  8, 14, 14,  9,  8, 10, 10,  0, 11), ChrInitWeapons( 701000,      -1, 1462000,      -1), ChrInitArmor(  50000,   51000,   52000,   53000), None, None, None, None, ChrInitItems(-1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 103, 1, 117, 1), -1, 0, 0, 0, 1, None, 0, ChrInitGestures(0, 1, 2, 3, 4, 5, 8), 0),
 3005: ChrInitEntry(ChrInitStats(  4, 11,  9, 11, 12, 14,  9,  9, 10,  0, 11), ChrInitWeapons( 200000, 1200000, 1402000,      -1), ChrInitArmor( 900000,  241000,  242000,  243000), ChrInitArrows(2000000, 30, -1, 0, -1, 0, -1, 0), None, None, None, ChrInitItems(-1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 103, 1, 117, 1), -1, 0, 0, 0, 1, None, 0, ChrInitGestures(0, 1, 2, 3, 4, 5, 8), 0),
 3006: ChrInitEntry(ChrInitStats(  3,  8, 15,  8,  9, 11, 15,  8, 10,  0,  8), ChrInitWeapons( 100000, 1300000, 1403000,      -1), ChrInitArmor( 220000,  221000,  222000,  223000), None, None, None, ChrInitSpells(3000), ChrInitItems(3000, 1, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 103, 1, 117, 1), -1, 0, 0, 0, 1, None, 0, ChrInitGestures(0, 1, 2, 3, 4, 5, 8), 0),
 3007: ChrInitEntry(ChrInitStats(  1, 10, 12, 11, 12,  9, 10,  8, 10,  0, 12), ChrInitWeapons( 700000, 1330000, 1406000,      -1), ChrInitArmor( 230000,  231000,  232000,  233000), None, None, None, ChrInitSpells(4000), ChrInitItems(4000, 1, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 103, 1, 117, 1), -1, 0, 0, 0, 1, None, 0, ChrInitGestures(0, 1, 2, 3, 4, 5, 8), 0),
 3008: ChrInitEntry(ChrInitStats(  2, 11, 11,  9, 12,  8,  8, 14, 10,  0, 11), ChrInitWeapons( 801000, 1361000, 1400000,      -1), ChrInitArmor( 900000,  311000,  312000,  313000), None, None, None, ChrInitSpells(5000), ChrInitItems(5000, 1, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 103, 1, 117, 1), -1, 0, 0, 0, 1, None, 1, ChrInitGestures(0, 1, 2, 3, 4, 5, 13), 0),
 3009: ChrInitEntry(ChrInitStats(  6, 11, 11, 11, 11, 11, 11, 11, 10,  0, 11), ChrInitWeapons( 800000,      -1, 1409000,      -1), ChrInitArmor( 900000,  901000,  902000,  903000), None, None, None, None, ChrInitItems(-1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 103, 1, 117, 1), -1, 0, 0, 0, 1, None, 0, ChrInitGestures(0, 1, 2, 3, 4, 5, 8), 0),
 6000: ChrInitEntry(ChrInitStats( 35, 16, 12, 20, 20, 14,  9, 14,  1,  5, 15), ChrInitWeapons( 206003, 1365000, 1472003,      -1), ChrInitArmor( 160002,  161002,  162002,  163002), None, ChrInitRings(139), None, ChrInitSpells(15500, 15010), None, 6000, 0, 2, 0, 1, ChrInitBodyScale(0, 70, 10, 30, 0), 3, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6002: ChrInitEntry(ChrInitStats( 75, 24, 12, 23, 30, 25, 10, 14,  1,  5, 22), ChrInitWeapons( 206012, 1365000, 1472012,      -1), ChrInitArmor( 160010,  161010,  162010,  163010), None, ChrInitRings(139), None, ChrInitSpells(15500, 15010), None, 6000, 0, 2, 0, 1, ChrInitBodyScale(0, 70, 10, 30, 0), 3, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6003: ChrInitEntry(ChrInitStats( 95, 25, 12, 25, 40, 30, 11, 14,  1,  5, 23), ChrInitWeapons( 206015, 1365000, 1472015,      -1), ChrInitArmor( 160010,  161010,  162010,  163010), None, ChrInitRings(139), None, ChrInitSpells(15500, 15010), None, 6000, 0, 2, 0, 1, ChrInitBodyScale(0, 70, 10, 30, 0), 3, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6004: ChrInitEntry(ChrInitStats( 95, 25, 12, 25, 40, 30, 11, 14,  1,  5, 23), ChrInitWeapons( 206015, 1365000, 1472015,      -1), ChrInitArmor( 190000,  161010,  162010,  163010), None, ChrInitRings(139), None, ChrInitSpells(15500, 15010), None, 6001, 0, 0, 0, 1, ChrInitBodyScale(50, 70, 10, 30, 0), 3, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6010: ChrInitEntry(ChrInitStats( 75, 17, 11, 21, 26, 32, 13, 24,  1,  0, 16), ChrInitWeapons( 602012,      -1,  101012, 1366000), ChrInitArmor( 450005,  451005,  452005,  453005), None, None, None, ChrInitSpells(15910), None, 6010, 0, 2, 0, 0, ChrInitBodyScale(-40, -20, -50, -30, -40), 8, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6020: ChrInitEntry(ChrInitStats(  1,  1,  1,  1,  1,  1,  1,  1,  1,  0,  1), ChrInitWeapons( 209008,      -1, 1456005,      -1), ChrInitArmor( 350006,  351006,  352006,  353006), None, None, None, None, None, 6020, 0, 2, 0, 1, ChrInitBodyScale(-20, 20, -30, 0, -10), 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6021: ChrInitEntry(ChrInitStats( 55, 20,  9, 16, 26, 27,  9, 16,  1,  0, 17), ChrInitWeapons( 209008,      -1, 1456005,      -1), ChrInitArmor(2350006, 2351006, 2352006, 2353006), None, None, None, None, None, 6021, 0, 0, 4, 1, ChrInitBodyScale(-20, 20, -30, 0, -10), 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6030: ChrInitEntry(ChrInitStats( 65, 17, 22, 17, 11, 16, 41, 12,  1,  0, 14), ChrInitWeapons(1303000,  400010, 1403010,      -1), ChrInitArmor( 380005,  381005,  382008,  383008), None, None, None, ChrInitSpells(13010, 13030, 13040, 13060), None, 6030, 0, 2, 0, 1, ChrInitBodyScale(100, -100, 50, -100, -100), 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6031: ChrInitEntry(ChrInitStats( 85, 17, 22, 18, 12, 17, 55, 12,  1,  0, 17), ChrInitWeapons(1303000,  400014, 1403014,      -1), ChrInitArmor( 380005,  381005,  382010,  383010), None, None, None, ChrInitSpells(13010, 13030, 13050, 13070), None, 6030, 0, 2, 0, 1, ChrInitBodyScale(100, -100, 50, -100, -100), 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6032: ChrInitEntry(ChrInitStats( 85, 17, 22, 18, 12, 17, 55, 12,  1,  0, 17), ChrInitWeapons(1306000,  400014, 1403014,      -1), ChrInitArmor( 380005,      -1,      -1,      -1), None, None, None, ChrInitSpells(13010, 13030, 13050, 13070, 13700), None, 6030, 0, 2, 0, 1, ChrInitBodyScale(100, -100, 50, -100, -100), 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6040: ChrInitEntry(ChrInitStats( 45, 14, 15, 17, 13, 16, 30,  9,  1,  3, 16), ChrInitWeapons(1300000,  600006, 1403006,      -1), ChrInitArmor( 640004,  641004,  642004,  643004), None, None, None, ChrInitSpells(13000, 13020), None, 6040, 0, 2, 0, 1, ChrInitBodyScale(-20, 20, -10, -10, -10), 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6041: ChrInitEntry(ChrInitStats( 65, 18, 15, 19, 13, 16, 42,  9,  1,  0, 18), ChrInitWeapons(1300000,  600010, 1403010,      -1), ChrInitArmor(2640008, 2641008, 2642008, 2643008), None, ChrInitRings(123), None, ChrInitSpells(13000, 13020), None, 6041, 0, 0, 4, 1, ChrInitBodyScale(-20, 20, -10, -10, -10), 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6050: ChrInitEntry(ChrInitStats(  5,  9, 15, 10,  9, 11, 18, 10,  1,  0,  8), ChrInitWeapons(     -1,      -1,      -1,      -1), ChrInitArmor( 330000,  331000,  332000,  333000), None, ChrInitRings(116), None, None, None, 6050, 0, 2, 0, 0, ChrInitBodyScale(-20, -30, -40, -60, -40), 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6051: ChrInitEntry(ChrInitStats(  5,  9, 15, 10,  9, 11, 18, 10,  1,  0,  8), ChrInitWeapons(     -1,      -1,      -1,      -1), ChrInitArmor( 330000,  331000,  332000,  333000), None, ChrInitRings(116), None, None, None, 6050, 0, 2, 0, 0, ChrInitBodyScale(-20, -30, -40, -60, -40), 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6070: ChrInitEntry(ChrInitStats(  5,  8, 13, 12,  8,  9, 14, 19,  1, 12,  7), ChrInitWeapons(1363000,      -1,      -1,      -1), ChrInitArmor( 410000,  411000,  412000,  413000), None, None, None, ChrInitSpells(15010), None, 6070, 0, 2, 0, 0, ChrInitBodyScale(-30, 50, -30, -50, 30), 1, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6071: ChrInitEntry(ChrInitStats(  5,  8, 13, 12,  8,  9, 14, 19,  1,  0,  7), ChrInitWeapons(1363000,      -1,      -1,      -1), ChrInitArmor(2410000, 2411000, 2412000, 2413000), None, None, None, ChrInitSpells(15010), None, 6071, 0, 0, 4, 0, ChrInitBodyScale(-30, 50, -30, -50, 30), 1, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6080: ChrInitEntry(ChrInitStats( 25, 11, 13, 14, 13, 14, 11, 17,  1,  2, 17), ChrInitWeapons( 802000, 1362000, 1451000,      -1), ChrInitArmor(     -1,  651000,  652000,  653000), None, None, None, ChrInitSpells(15020, 15300), None, 6080, 0, 2, 0, 1, ChrInitBodyScale(100, -30, 50, -40, 60), 1, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6090: ChrInitEntry(ChrInitStats( 25, 13, 11, 15, 15, 13, 10, 15,  1,  5, 18), ChrInitWeapons( 801014, 1362000, 1477014,      -1), ChrInitArmor(     -1,  181010,  182010,  183010), None, None, None, ChrInitSpells(15300), None, 6090, 0, 2, 0, 1, ChrInitBodyScale(0, 20, -10, 20, 10), 1, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6091: ChrInitEntry(ChrInitStats( 85, 21, 13, 28, 18, 21, 16, 30,  1,  0, 23), ChrInitWeapons( 801014, 1362000, 1477014,      -1), ChrInitArmor(     -1, 2181010, 2182010, 2183010), None, None, None, ChrInitSpells(15300), None, 6091, 0, 0, 4, 1, ChrInitBodyScale(0, 20, -10, 20, 10), 1, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6100: ChrInitEntry(ChrInitStats( 25, 15, 11, 12, 19, 13,  8, 17,  1,  3, 15), ChrInitWeapons( 702014, 1362000, 1477014,      -1), ChrInitArmor( 180010,  181010,  182010,  183010), None, None, None, ChrInitSpells(15040), None, 6100, 0, 2, 0, 1, ChrInitBodyScale(-50, 100, 0, 100, 50), 1, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6101: ChrInitEntry(ChrInitStats( 85, 26, 13, 22, 26, 18, 14, 26,  1,  0, 25), ChrInitWeapons( 702014, 1362000, 1477014,      -1), ChrInitArmor(2180010, 2181010, 2182010, 2183010), None, None, None, ChrInitSpells(15040), None, 6101, 0, 0, 4, 1, ChrInitBodyScale(-50, 100, 0, 100, 50), 1, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6130: ChrInitEntry(ChrInitStats( 55, 17, 16, 20, 16, 17, 26,  9,  1,  5, 19), ChrInitWeapons(1330800,  700008, 1406008,      -1), ChrInitArmor( 230006,  231006,  232006,  233006), None, None, None, ChrInitSpells(14000, 14010, 14100), None, 6130, 0, 2, 0, 1, ChrInitBodyScale(30, 30, 30, -30, -40), 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6131: ChrInitEntry(ChrInitStats( 55, 17, 16, 20, 16, 17, 26,  9,  1,  0, 19), ChrInitWeapons(1330800,  700008, 1406008,      -1), ChrInitArmor(2230006, 2231006, 2232006, 2233006), None, None, None, ChrInitSpells(14000, 14010, 14100), None, 6131, 0, 0, 4, 1, ChrInitBodyScale(30, 30, 30, -30, -40), 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6170: ChrInitEntry(ChrInitStats( 95, 16, 30, 23,  9, 10, 62, 13,  1,  0, 17), ChrInitWeapons(1332500,      -1,      -1,      -1), ChrInitArmor( 460000,  461000,  462000,  463000), None, None, None, ChrInitSpells(14020, 14040, 14110), None, 6170, 0, 2, 0, 0, ChrInitBodyScale(-50, -20, -60, -60, -30), 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6180: ChrInitEntry(ChrInitStats( 45, 15, 17, 16, 13, 14, 29, 11,  1,  4, 15), ChrInitWeapons(1302000,      -1,  102005,      -1), ChrInitArmor( 140004,  141004,  142004,  143004), None, None, None, ChrInitSpells(13020, 13030, 13610), None, 6180, 0, 2, 0, 1, ChrInitBodyScale(30, -20, -20, -20, -20), 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6220: ChrInitEntry(ChrInitStats(  5, 14, 11, 12, 13, 11,  8,  9,  1,  0, 12), ChrInitWeapons(     -1,      -1,      -1,      -1), ChrInitArmor( 370000,  371000,  372000,  373000), None, None, None, None, None, 6220, 0, 2, 0, 1, ChrInitBodyScale(30, -40, -30, 50, -30), 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6250: ChrInitEntry(ChrInitStats( 65, 23, 11, 26, 32, 16,  9,  9,  1,  0, 24), ChrInitWeapons( 351010,      -1, 1501010,      -1), ChrInitArmor( 490008,  491008,  492008,  493008), None, ChrInitRings(100), None, None, None, 6250, 0, 2, 0, 1, ChrInitBodyScale(100, 100, 0, 100, 0), 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6260: ChrInitEntry(ChrInitStats( 65, 19, 13, 22, 29, 23, 13, 14,  1,  0, 17), ChrInitWeapons( 205000,  304000, 1471005,      -1), ChrInitArmor( 110000,  111000,  112000,  113000), None, None, None, None, None, 6260, 0, 2, 0, 1, ChrInitBodyScale(40, 20, -20, -30, 20), 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6270: ChrInitEntry(ChrInitStats( 65, 20, 14, 24, 26, 25, 11,  8,  1,  0, 22), ChrInitWeapons( 201010,      -1, 1450010,      -1), ChrInitArmor(     -1,  171008,  172008,  173008), None, None, None, None, None, 6270, 0, 2, 0, 1, ChrInitBodyScale(40, -30, 20, -30, -30), 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6271: ChrInitEntry(ChrInitStats( 65, 20, 14, 24, 26, 25, 11,  8,  1,  0, 22), ChrInitWeapons( 201010,      -1, 1450010,      -1), ChrInitArmor(     -1, 2171008, 2172008, 2173008), None, None, None, None, None, 6271, 0, 0, 4, 1, ChrInitBodyScale(40, -30, 20, -30, -30), 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6280: ChrInitEntry(ChrInitStats( 95, 28,  8, 26, 44, 31,  8,  9,  1,  4, 26), ChrInitWeapons( 350015,      -1, 1475015,      -1), ChrInitArmor(  10005,   11005,   12005,   13005), None, ChrInitRings(147), None, None, None, 6280, 0, 2, 0, 1, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6281: ChrInitEntry(ChrInitStats( 95, 28,  8, 26, 44, 31,  8,  9,  1,  4, 26), ChrInitWeapons( 350015,      -1, 1475015,      -1), ChrInitArmor(  10005,   11005,   12005,   13005), None, ChrInitRings(147), None, None, None, 6280, 0, 2, 0, 1, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6282: ChrInitEntry(ChrInitStats( 95, 28,  8, 26, 44, 31,  8,  9,  1,  4, 26), ChrInitWeapons( 350015,      -1, 1475015,      -1), ChrInitArmor(  10005,   11005,   12005,   13005), None, ChrInitRings(147), None, None, None, 6280, 0, 2, 0, 1, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6283: ChrInitEntry(ChrInitStats( 95, 28,  8, 26, 44, 31,  8,  9,  1,  4, 26), ChrInitWeapons( 350015,      -1, 1475015,      -1), ChrInitArmor(  10005,   11005,   12005,   13005), None, ChrInitRings(147), None, None, None, 6280, 0, 2, 0, 1, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6284: ChrInitEntry(ChrInitStats( 95, 28,  8, 26, 44, 31,  8,  9,  1,  4, 26), ChrInitWeapons( 350015,      -1, 1475015,      -1), ChrInitArmor(  10005,   11005,   12005,   13005), None, ChrInitRings(147), None, None, None, 6280, 0, 2, 0, 1, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6290: ChrInitEntry(ChrInitStats(105, 25, 10, 28, 47, 34,  9, 11,  1, 10, 26), ChrInitWeapons( 300015,      -1, 1475015,      -1), ChrInitArmor(  10005,   11005,   12005,   13005), None, ChrInitRings(147), None, None, None, 6290, 0, 2, 0, 0, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6291: ChrInitEntry(ChrInitStats(105, 25, 10, 28, 47, 34,  9, 11,  1, 10, 26), ChrInitWeapons( 300015,      -1, 1475015,      -1), ChrInitArmor(  10005,   11005,   12005,   13005), None, ChrInitRings(147), None, None, None, 6290, 0, 2, 0, 0, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6300: ChrInitEntry(ChrInitStats( 45, 17,  9, 16, 23, 27,  8, 12,  1,  8, 18), ChrInitWeapons( 402006,      -1,  402006,  101006), ChrInitArmor( 100004,  101004,  102004,  103004), None, ChrInitRings(143, 101), None, None, None, 6300, 0, 2, 0, 1, ChrInitBodyScale(-20, 20, -10, 10, 0), 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6301: ChrInitEntry(ChrInitStats( 75, 21, 11, 24, 33, 29, 10, 12,  1,  8, 20), ChrInitWeapons( 402012,      -1,  402012,  101012), ChrInitArmor( 100005,  101005,  102005,  103005), None, ChrInitRings(143, 101), None, None, None, 6300, 0, 2, 0, 1, ChrInitBodyScale(-20, 20, -10, 10, 0), 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6310: ChrInitEntry(ChrInitStats( 75, 17,  9, 27, 37, 35,  8,  8,  1,  0, 19), ChrInitWeapons( 451012,      -1, 1461012,      -1), ChrInitArmor( 280005,  281005,  282005,  283005), None, None, None, None, None, 6310, 0, 2, 0, 1, None, 7, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6320: ChrInitEntry(ChrInitStats( 85, 21,  9, 29, 34, 33,  9,  9,  1,  7, 26), ChrInitWeapons(1001014,      -1, 1500014,      -1), ChrInitArmor(     -1,  301010,  302010,  303010), None, None, None, None, None, 6320, 0, 2, 0, 1, ChrInitBodyScale(10, -20, -60, -40, -70), 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6321: ChrInitEntry(ChrInitStats( 85, 21,  9, 29, 34, 33,  9,  9,  1,  7, 26), ChrInitWeapons(1001014,      -1, 1500014,      -1), ChrInitArmor(     -1,  301010,  302010,  303010), None, None, None, None, None, 6320, 0, 2, 0, 1, ChrInitBodyScale(10, -20, -60, -40, -70), 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6370: ChrInitEntry(ChrInitStats( 35, 13, 15, 12, 17, 18, 17, 15,  1,  0, 13), ChrInitWeapons( 603003, 1367000,  101003,      -1), ChrInitArmor( 150002,  151002,  152002,  153002), None, None, None, ChrInitSpells(15010, 15700, 15810), None, 6370, 0, 2, 0, 1, ChrInitBodyScale(-10, 20, -10, 20, 10), 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6390: ChrInitEntry(ChrInitStats( 65, 20,  9, 28, 34, 21,  8,  9,  1,  0, 21), ChrInitWeapons( 351010,      -1, 9003010,      -1), ChrInitArmor(  70005,   71005,   72005,   73005), None, ChrInitRings(100), None, None, None, 6390, 0, 2, 0, 1, ChrInitBodyScale(50, 100, 0, 50, 0), 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6420: ChrInitEntry(ChrInitStats( 75, 18, 14, 34, 27, 29, 12,  8,  1,  0, 18), ChrInitWeapons( 500012, 1331200, 1404012,      -1), ChrInitArmor(  60005,   61005,   62005,   63005), None, ChrInitRings(128, 124), None, ChrInitSpells(14050, 14400), None, 6420, 0, 2, 0, 1, ChrInitBodyScale(-50, -50, -50, -50, -50), 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6490: ChrInitEntry(ChrInitStats( 75, 21,  9, 26, 31, 27,  9,  9,  1,  0, 28), ChrInitWeapons(1050012,      -1, 1401012,      -1), ChrInitArmor(     -1,  211010,  212010,  213010), None, None, None, None, None, 6490, 0, 2, 1, 1, ChrInitBodyScale(-10, 0, 30, 0, 50), 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6500: ChrInitEntry(ChrInitStats( 75, 17, 21, 22, 11, 10, 45, 16,  1,  0, 18), ChrInitWeapons(1302000,      -1, 1408012,      -1), ChrInitArmor(     -1,  141005,  142005,  143005), None, None, None, ChrInitSpells(13020, 13030, 13610), None, 6500, 0, 2, 1, 1, ChrInitBodyScale(-20, -20, -20, -20, -20), 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6510: ChrInitEntry(ChrInitStats( 65, 20, 10, 24, 34, 24, 10,  8,  1,  0, 20), ChrInitWeapons( 351010,      -1, 9003010,      -1), ChrInitArmor(  70005,   71005,   72005,   73005), None, ChrInitRings(100), None, None, None, 6390, 0, 2, 0, 1, ChrInitBodyScale(50, 100, 0, 50, 0), 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6511: ChrInitEntry(ChrInitStats( 95, 24, 10, 30, 41, 31, 11,  9,  1,  0, 24), ChrInitWeapons( 351015,      -1, 9003015,      -1), ChrInitArmor(  70005,   71005,   72005,   73005), None, ChrInitRings(100), None, None, None, 6390, 0, 0, 0, 1, ChrInitBodyScale(50, 100, 0, 50, 0), 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6520: ChrInitEntry(ChrInitStats( 45, 13, 20, 18, 10, 12, 31, 12,  1,  0, 14), ChrInitWeapons(1301000,      -1, 1406006,      -1), ChrInitArmor( 340002,  341002,  342002,  343002), None, ChrInitRings(138), None, ChrInitSpells(13020, 13030, 13040, 13550), None, 6410, 0, 2, 0, 0, ChrInitBodyScale(-50, -50, -50, -50, -50), 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6521: ChrInitEntry(ChrInitStats( 85, 19, 22, 21, 13, 14, 42, 15,  1,  0, 24), ChrInitWeapons(1301000,      -1, 1406014,      -1), ChrInitArmor( 340005,  341005,  342005,  343005), None, ChrInitRings(138), None, ChrInitSpells(13020, 13030, 13040, 13550), None, 6410, 0, 2, 0, 0, ChrInitBodyScale(-50, -50, -50, -50, -50), 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6530: ChrInitEntry(ChrInitStats( 55, 18,  8, 19, 26, 19,  8,  8,  1,  8, 34), ChrInitWeapons( 703008,      -1, 1409008,      -1), ChrInitArmor( 560006,      -1,      -1,      -1), None, ChrInitRings(125), None, None, None, 6530, 0, 2, 0, 0, ChrInitBodyScale(0, 0, 100, 0, 100), 4, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6531: ChrInitEntry(ChrInitStats( 55, 18,  8, 19, 26, 19,  8,  8,  1,  8, 34), ChrInitWeapons( 703008,      -1, 1409008,      -1), ChrInitArmor( 560006,      -1,      -1,      -1), None, ChrInitRings(125), None, None, None, 6530, 0, 2, 0, 0, ChrInitBodyScale(0, 0, 100, 0, 100), 4, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6540: ChrInitEntry(ChrInitStats( 35, 16, 12, 20, 20, 14,  9, 14,  1,  5, 15), ChrInitWeapons( 206003, 1365000, 1472003,      -1), ChrInitArmor( 160002,  161002,  162002,  163002), None, ChrInitRings(139), None, ChrInitSpells(15500, 15010), None, 6000, 0, 2, 0, 1, ChrInitBodyScale(0, 70, 10, 30, 0), 3, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6541: ChrInitEntry(ChrInitStats( 45, 19, 12, 20, 24, 14,  9, 14,  1,  5, 18), ChrInitWeapons( 206006, 1365000, 1472006,      -1), ChrInitArmor( 160004,  161004,  162004,  163004), None, ChrInitRings(139), None, ChrInitSpells(15500, 15010), None, 6000, 0, 2, 0, 1, ChrInitBodyScale(0, 70, 10, 30, 0), 3, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6542: ChrInitEntry(ChrInitStats( 75, 24, 12, 23, 30, 25, 10, 14,  1,  5, 22), ChrInitWeapons( 206012, 1365000, 1472012,      -1), ChrInitArmor( 160010,  161010,  162010,  163010), None, ChrInitRings(139), None, ChrInitSpells(15500, 15010), None, 6000, 0, 2, 0, 1, ChrInitBodyScale(0, 70, 10, 30, 0), 3, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6543: ChrInitEntry(ChrInitStats( 95, 25, 12, 25, 40, 30, 11, 14,  1,  5, 23), ChrInitWeapons( 206015, 1365000, 1472015,      -1), ChrInitArmor( 160010,  161010,  162010,  163010), None, ChrInitRings(139), None, ChrInitSpells(15500, 15010), None, 6000, 0, 2, 0, 1, ChrInitBodyScale(0, 70, 10, 30, 0), 3, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6544: ChrInitEntry(ChrInitStats(105, 27, 12, 28, 43, 31, 12, 14,  1,  5, 23), ChrInitWeapons( 206015, 1365000, 1472015,      -1), ChrInitArmor( 160010,  161010,  162010,  163010), None, ChrInitRings(139), None, ChrInitSpells(15500, 15010), None, 6000, 0, 2, 0, 1, ChrInitBodyScale(0, 70, 10, 30, 0), 3, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6550: ChrInitEntry(ChrInitStats( 45, 11, 13, 13, 34,  8,  9, 30,  1,  3, 12), ChrInitWeapons( 851005, 1361000, 9001006,      -1), ChrInitArmor(  20001,   21001,   22001,   23001), None, ChrInitRings(100), None, ChrInitSpells(15010, 15310), None, 6550, 0, 2, 0, 1, ChrInitBodyScale(20, 50, 20, 50, 20), 1, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6551: ChrInitEntry(ChrInitStats( 85, 17, 14, 22, 50, 12,  9, 30,  1,  3, 16), ChrInitWeapons( 851005, 1361000, 9001014,      -1), ChrInitArmor(  20005,   21005,   22005,   23005), None, ChrInitRings(100), None, ChrInitSpells(15010, 15310), None, 6550, 0, 2, 0, 1, ChrInitBodyScale(20, 50, 20, 50, 20), 1, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6560: ChrInitEntry(ChrInitStats( 45, 15,  9, 25, 26, 24,  9,  9,  1,  0, 13), ChrInitWeapons( 207006,      -1, 1470006,      -1), ChrInitArmor( 200000,  201000,  202000,  203000), None, None, None, None, None, 6560, 0, 2, 0, 1, ChrInitBodyScale(-70, -70, -70, -70, -70), 4, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6561: ChrInitEntry(ChrInitStats( 95, 17,  9, 35, 45, 41,  9,  9,  1,  0, 15), ChrInitWeapons( 207015,      -1, 1470015,      -1), ChrInitArmor( 200005,  201005,  202005,  203005), None, None, None, None, None, 6560, 0, 2, 0, 1, ChrInitBodyScale(-70, -70, -70, -70, -70), 4, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6562: ChrInitEntry(ChrInitStats( 95, 17,  9, 35, 45, 41,  9,  9,  1,  0, 15), ChrInitWeapons( 207015,      -1, 1470015,      -1), ChrInitArmor( 200005,  201005,  202005,  203005), None, None, None, None, None, 6560, 0, 2, 0, 1, ChrInitBodyScale(-70, -70, -70, -70, -70), 4, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6570: ChrInitEntry(ChrInitStats(100, 17, 16, 26, 19, 24, 59,  8,  1,  0, 16), ChrInitWeapons(1601015,      -1, 1332500,      -1), ChrInitArmor( 290005,  291005,  292005,  293005), None, None, None, ChrInitSpells(14500, 14510, 14520), None, 6570, 0, 2, 0, 1, ChrInitBodyScale(100, -20, -20, -20, -20), 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6580: ChrInitEntry(ChrInitStats( 95, 28,  9, 35, 50, 15,  8,  8,  1,  0, 27), ChrInitWeapons( 854005,      -1, 1505005,      -1), ChrInitArmor( 440000,  441000,  442000,  443000), None, ChrInitRings(100), None, None, None, 6580, 0, 0, 0, 1, ChrInitBodyScale(0, 50, 20, 30, 50), 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6590: ChrInitEntry(ChrInitStats( 45, 17,  9, 16, 23, 27,  8, 12,  1,  8, 18), ChrInitWeapons( 402006,      -1,  402006,  101006), ChrInitArmor( 100004,  101004,  102004,  103004), None, ChrInitRings(143, 101), None, None, None, 6300, 0, 2, 0, 1, ChrInitBodyScale(-20, 20, -10, 10, 0), 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6591: ChrInitEntry(ChrInitStats( 45, 17,  9, 16, 23, 27,  8, 12,  1,  8, 18), ChrInitWeapons( 402006,      -1,  402006,  101006), ChrInitArmor( 100004,  101004,  102004,  103004), None, ChrInitRings(143, 101), None, None, None, 6300, 0, 2, 0, 1, ChrInitBodyScale(-20, 20, -10, 10, 0), 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6600: ChrInitEntry(ChrInitStats( 65, 17,  9, 27, 34, 30,  9,  9,  1,  0, 15), ChrInitWeapons( 604010, 1201010, 1405010,      -1), ChrInitArmor( 350008,  351008,  352008,  353008), ChrInitArrows(2000000, 999, -1, 0, -1, 0, -1, 0), None, None, None, None, 6600, 0, 0, 0, 1, ChrInitBodyScale(0, 60, 50, 60, -50), 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6610: ChrInitEntry(ChrInitStats( 85, 18,  8, 25, 40, 44,  8,  8,  1,  0, 19), ChrInitWeapons( 304000,      -1, 1471005,      -1), ChrInitArmor( 130000,  131000,  132000,  133000), None, None, None, None, None, 6610, 0, 0, 0, 1, ChrInitBodyScale(0, -100, -100, -50, -50), 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6620: ChrInitEntry(ChrInitStats( 95, 16, 26, 26, 13, 14, 57,  8,  1,  0, 20), ChrInitWeapons(1332500,      -1,      -1,      -1), ChrInitArmor( 460000,  461000,  462000,  463000), None, None, None, ChrInitSpells(14500, 14510, 14520), None, 6620, 0, 0, 0, 0, ChrInitBodyScale(-70, -70, -70, -70, -70), 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6640: ChrInitEntry(ChrInitStats( 75, 21,  9, 28, 33, 21, 10, 12,  1,  3, 26), ChrInitWeapons( 351012,      -1, 1501012,      -1), ChrInitArmor( 490010,  491010,  492010,  493010), None, ChrInitRings(100), None, None, None, 6640, 0, 0, 0, 1, ChrInitBodyScale(0, 100, 0, 100, 0), 8, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6650: ChrInitEntry(ChrInitStats( 75, 19, 10, 32, 27, 28,  8,  9,  1,  3, 27), ChrInitWeapons( 204012,      -1, 1455012,      -1), ChrInitArmor( 510010,  511010,  512010,  513010), None, None, None, None, None, 6650, 0, 0, 0, 1, ChrInitBodyScale(-10, -10, -10, -10, -10), 8, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6700: ChrInitEntry(ChrInitStats(  5,  9, 15, 10,  9, 11, 18, 10,  1,  0,  8), ChrInitWeapons(     -1,      -1,      -1,      -1), ChrInitArmor( 330000,  331000,  332000,  333000), None, ChrInitRings(116), None, None, None, 6050, 0, 2, 0, 0, ChrInitBodyScale(-20, -30, -40, -60, -40), 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6740: ChrInitEntry(ChrInitStats(100, 25, 14, 48, 22, 46, 25, 18,  1,  0, 21), ChrInitWeapons(     -1, 9011005,      -1, 9010005), ChrInitArmor( 670005,  671005,  672005,  673005), None, ChrInitRings(117), None, None, ChrInitItems(290, 99, 296, 99), 6740, 0, 2, 0, 0, ChrInitBodyScale(-10, -20, -30, -20, -30), 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6801: ChrInitEntry(ChrInitStats( 80, 24,  8, 23, 38, 29,  9,  9,  1,  0, 25), ChrInitWeapons( 701013,      -1, 1462013,      -1), ChrInitArmor(  50010,   51010,   52010,   53010), None, None, None, None, None, 6801, 0, 0, 0, 1, ChrInitBodyScale(50, 100, 100, 50, 0), 7, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6802: ChrInitEntry(ChrInitStats( 75, 22, 10, 26, 24, 35,  8, 12,  1,  0, 23), ChrInitWeapons( 301012,      -1, 1451012,      -1), ChrInitArmor( 390010,  391010,  392010,  393010), None, ChrInitRings(124), None, None, None, 6802, 0, 0, 0, 0, ChrInitBodyScale(-50, -50, -50, -50, -50), 7, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6803: ChrInitEntry(ChrInitStats( 75, 19, 11, 25, 23, 41,  9, 11,  1,  0, 21), ChrInitWeapons(1202012,  401012, 1402012,      -1), ChrInitArmor( 240010,  241010,  242010,  243010), ChrInitArrows(2000000, 999, -1, 0, -1, 0, -1, 0), ChrInitRings(124), None, None, None, 6803, 0, 0, 0, 0, ChrInitBodyScale(-50, -50, -50, 0, 0), 7, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6804: ChrInitEntry(ChrInitStats( 75, 17, 21, 20, 13, 14, 42, 13,  1,  0, 20), ChrInitWeapons(1300000,  200012, 1403012,      -1), ChrInitArmor(     -1,  221010,  222010,  223010), None, None, None, ChrInitSpells(13000, 13020), None, 6804, 0, 0, 0, 1, ChrInitBodyScale(70, 70, 0, 70, 70), 7, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6805: ChrInitEntry(ChrInitStats( 75, 19, 15, 15, 13, 16, 27, 35,  1,  0, 20), ChrInitWeapons( 801012, 1361000, 1400012,      -1), ChrInitArmor(     -1,  311010,  312010,  313010), None, None, None, ChrInitSpells(15030), None, 6805, 0, 0, 0, 0, ChrInitBodyScale(-100, -100, -100, -100, -100), 7, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 6806: ChrInitEntry(ChrInitStats( 75, 19, 10, 35, 21, 35,  9, 10,  1,  0, 21), ChrInitWeapons( 103012,      -1, 1404012,      -1), ChrInitArmor( 500010,  501010,      -1,  503010), None, ChrInitRings(124), None, None, None, 6806, 0, 0, 0, 1, ChrInitBodyScale(-50, -20, -20, -20, -20), 7, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 7100: ChrInitEntry(ChrInitStats( 45, 16,  9, 22, 26, 23,  9,  9, 10,  0, 16), ChrInitWeapons( 201006,      -1, 1450006,      -1), ChrInitArmor( 210000,  211000,  212000,  213000), None, None, None, None, None, -1, 0, 0, 0, 1, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 7110: ChrInitEntry(ChrInitStats(  5,  9, 11, 12, 10, 15, 11, 11, 10,  0, 11), ChrInitWeapons( 103000,      -1, 1404000,      -1), ChrInitArmor( 300000,  301000,  302000,  303000), None, None, None, None, None, -1, 0, 0, 0, 0, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 7111: ChrInitEntry(ChrInitStats( 35, 14, 11, 19, 17, 23, 11, 11, 10,  0, 14), ChrInitWeapons( 103003,      -1, 1404003,      -1), ChrInitArmor( 300000,  301000,  302000,  303000), None, None, None, None, None, -1, 0, 0, 0, 0, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 7120: ChrInitEntry(ChrInitStats(100, 20, 12, 33, 30, 34, 31,  8, 10,  0, 17), ChrInitWeapons( 303015, 1361000, 1408015,      -1), ChrInitArmor( 360000,  361000,  362000,  363000), None, None, None, ChrInitSpells(5700, 5810), None, -1, 0, 0, 0, 1, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 7130: ChrInitEntry(ChrInitStats( 45, 16,  9, 21, 24, 26,  9,  9, 10,  0, 16), ChrInitWeapons( 200006, 1200006, 1402006,      -1), ChrInitArmor(     -1,  241000,  242000,  243000), ChrInitArrows(2003000, 999, -1, 0, -1, 0, -1, 0), None, None, None, None, 6300, 0, 0, 0, 1, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 7131: ChrInitEntry(ChrInitStats( 75, 16,  9, 31, 34, 36,  9,  9, 10,  0, 16), ChrInitWeapons( 200012, 1200012, 1402012,      -1), ChrInitArmor(     -1,  241000,  242000,  243000), ChrInitArrows(2003000, 999, -1, 0, -1, 0, -1, 0), None, None, None, None, 6300, 0, 0, 0, 1, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 7140: ChrInitEntry(ChrInitStats( 45, 22, 11, 16, 18,  8,  8, 26, 10,  0, 21), ChrInitWeapons( 801006, 1361000, 1400006,      -1), ChrInitArmor(     -1,  311000,  312000,  313000), None, None, None, ChrInitSpells(5000, 5300), None, 6560, 0, 0, 0, 1, None, 1, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 7150: ChrInitEntry(ChrInitStats( 85, 32, 11, 21, 23,  8,  8, 36, 10,  0, 31), ChrInitWeapons( 802014, 1361000, 1400014,      -1), ChrInitArmor( 180000,  181000,  182000,  183000), None, None, None, ChrInitSpells(5010, 5310), None, -1, 0, 0, 0, 1, None, 1, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 7160: ChrInitEntry(ChrInitStats( 85, 11, 11, 34, 70, 11, 11, 11, 10,  0, 11), ChrInitWeapons(     -1,      -1,      -1,      -1), ChrInitArmor(     -1,      -1,      -1,      -1), None, None, None, None, ChrInitItems(377, 1, 378, 1), -1, 0, 0, 0, 1, None, 5, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 7170: ChrInitEntry(ChrInitStats( 55, 16, 11, 25, 20, 29, 11,  8, 10,  0, 20), ChrInitWeapons( 401008, 1330008, 1408008,      -1), ChrInitArmor( 360000,  361000,  362000,  363000), None, None, None, ChrInitSpells(4010), None, -1, 0, 0, 0, 1, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 7180: ChrInitEntry(ChrInitStats( 95, 17, 14, 36, 42, 34, 10,  8, 10,  0, 19), ChrInitWeapons( 700015, 1330015, 1406015,      -1), ChrInitArmor( 230000,  231000,  232000,  233000), None, None, None, ChrInitSpells(4220, 4210), None, -1, 0, 0, 0, 0, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 7190: ChrInitEntry(ChrInitStats( 65, 16,  9, 31, 37, 23,  9,  9, 10,  0, 16), ChrInitWeapons(1001010,      -1, 1450010, 1251010), ChrInitArmor( 210000,  211000,  212000,  213000), ChrInitArrows(-1, 0, -1, 0, 2101000, 999, -1, 0), None, None, None, None, -1, 0, 0, 0, 1, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 7200: ChrInitEntry(ChrInitStats( 75, 34, 14, 20, 26, 26,  9, 11, 10,  0, 20), ChrInitWeapons( 301012, 1361000, 1452012,      -1), ChrInitArmor( 390000,  391000,  392000,  393000), None, None, None, ChrInitSpells(5040), None, -1, 0, 0, 0, 1, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 7210: ChrInitEntry(ChrInitStats( 85, 22,  8, 34, 47, 21,  8,  9, 10,  0, 21), ChrInitWeapons( 750014,      -1, 1462014,      -1), ChrInitArmor(  50000,   51000,   52000,   53000), None, None, None, None, ChrInitItems(293, 99), -1, 0, 0, 0, 0, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 7220: ChrInitEntry(ChrInitStats( 85, 18, 22, 24, 15, 17, 48,  8, 10,  0, 18), ChrInitWeapons( 201014,      -1, 1403014, 1300000), ChrInitArmor( 220000,  221000,  222000,  223000), None, None, None, ChrInitSpells(3110, 3000, 3020), None, -1, 0, 0, 0, 1, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 7230: ChrInitEntry(ChrInitStats(150, 40, 11, 50, 61, 11, 11, 11, 10,  0, 40), ChrInitWeapons( 850015,      -1, 1409015,      -1), ChrInitArmor(     -1,      -1,      -1,      -1), None, None, None, None, None, -1, 0, 0, 0, 1, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 7240: ChrInitEntry(ChrInitStats( 55, 20, 11, 25, 31, 11, 11, 11, 10,  0, 20), ChrInitWeapons( 901008,      -1, 901008,       -1), ChrInitArmor(     -1,      -1,      -1,      -1), None, None, None, None, None, -1, 0, 0, 0, 1, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 8000: ChrInitEntry(ChrInitStats(  0, 50, 50, 99, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons(     -1,      -1,      -1,      -1), ChrInitArmor( 210000,  211000,  212000,  213000), None, ChrInitRings(100), None, None, None, -1, 0, 0, 0, 1, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 8001: ChrInitEntry(ChrInitStats(  0, 50, 50, 99, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons(     -1,      -1,      -1,      -1), ChrInitArmor( 230000,  231000,  232000,  233000), None, ChrInitRings(100), None, None, None, -1, 0, 0, 0, 1, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 8002: ChrInitEntry(ChrInitStats(  0, 50, 50, 99, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons(     -1,      -1,      -1,      -1), ChrInitArmor( 140000,  141000,  142000,  143000), None, ChrInitRings(100), None, None, None, -1, 0, 0, 0, 1, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 8003: ChrInitEntry(ChrInitStats(  0, 50, 50, 99, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons(     -1,      -1,      -1,      -1), ChrInitArmor( 170000,  171000,  172000,  173000), None, ChrInitRings(100), None, None, None, -1, 0, 0, 0, 0, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 8004: ChrInitEntry(ChrInitStats(  0, 50, 50, 99, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons(     -1,      -1,      -1,      -1), ChrInitArmor(     -1,  241000,  242000,  243000), None, ChrInitRings(100), None, None, None, -1, 0, 0, 0, 1, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 8005: ChrInitEntry(ChrInitStats(  0, 50, 50, 99, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons(     -1,      -1,      -1,      -1), ChrInitArmor(  10000,   11000,   12000,   13000), None, ChrInitRings(100), None, None, None, -1, 0, 0, 0, 1, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 8006: ChrInitEntry(ChrInitStats(  0, 50, 50, 99, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons(     -1,      -1,      -1,      -1), ChrInitArmor(     -1,  401000,  402000,  403000), None, ChrInitRings(100), None, None, None, 300, 0, 0, 0, 0, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 8007: ChrInitEntry(ChrInitStats(  0, 50, 50, 99, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons( 202000,      -1, 1456000,      -1), ChrInitArmor( 350000,  351000,  352000,  353000), None, None, None, None, None, -1, 0, 0, 0, 1, None, 1, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 8008: ChrInitEntry(ChrInitStats(  0, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99), ChrInitWeapons( 350000, 1100000, 1501000, 1300000), ChrInitArmor(  70000,   71000,   72000,   73000), None, None, None, None, None, -1, 0, 0, 0, 1, ChrInitBodyScale(100, 100, 100, 100, 100), 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 8500: ChrInitEntry(ChrInitStats(  0, 15,  7, 12, 14,  9,  6, 10,  8,  3, 10), ChrInitWeapons( 201000, 1107000, 1450000,      -1), ChrInitArmor( 210000,  211000,  212000,  213000), None, None, None, None, ChrInitItems(200, 1, 312, 20, 292, 5, 310, 4, 273, 5, 100, 1, 101, 1, 102, 1, 103, 1), -1, 0, 0, 0, 1, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 8501: ChrInitEntry(ChrInitStats(  0, 11,  8, 11, 11, 12,  9,  8, 11,  3, 10), ChrInitWeapons( 701000, 1201000, 1404000,      -1), ChrInitArmor( 240000,  241000,  242000,  243000), ChrInitArrows(2000000, 20, -1, 0, -1, 0, -1, 0), None, None, None, ChrInitItems(200, 1, 312, 20, 292, 5, 294, 8, 273, 5, 100, 1, 101, 1, 102, 1, 103, 1), -1, 0, 0, 0, 1, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 8502: ChrInitEntry(ChrInitStats(  0,  8, 14, 10,  9,  8, 15,  9,  8,  3, 10), ChrInitWeapons( 202000, 1330000, 1402000,      -1), ChrInitArmor( 230000,  231000,  232000,  233000), None, None, None, ChrInitSpells(4000, 4300), ChrInitItems(200, 1, -1, 0, 312, 20, 294, 8, 273, 5, 100, 1, 101, 1, 102, 1, 103, 1), -1, 0, 0, 0, 1, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 8600: ChrInitEntry(ChrInitStats(  3, 12,  9, 12, 13, 13,  9,  9, 10,  3, 11), ChrInitWeapons( 201000, 1000000, 1450000, 1200000), ChrInitArmor( 210000,  211000,  212000,  213000), ChrInitArrows(2000000, 20, -1, 0, -1, 0, -1, 0), None, None, None, ChrInitItems(-1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 201, 20, 103, 1, 117, 1), 6000, 0, 0, 0, 1, None, 0, ChrInitGestures(0, 1, 2, 3, 4, 5, 8), 0),
 8601: ChrInitEntry(ChrInitStats(  3, 15, 10, 10, 16, 11,  9,  7, 10,  3, 10), ChrInitWeapons( 202000,  300000, 1452000,      -1), ChrInitArmor( 390000,  391000,  392000,  393000), None, None, None, None, ChrInitItems(-1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 201, 20, 103, 1, 117, 1), 6020, 0, 0, 0, 1, None, 1, ChrInitGestures(0, 1, 2, 3, 4, 5, 13), 0),
 8602: ChrInitEntry(ChrInitStats(  3,  9, 15,  8,  9, 11, 16,  8, 10,  3,  8), ChrInitWeapons(1300000,  100000, 1403000,      -1), ChrInitArmor( 220000,  221000,  222000,  223000), None, None, None, ChrInitSpells(3000), ChrInitItems(3000, 1, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 201, 20, 103, 1, 117, 1), 6410, 0, 0, 0, 0, None, 0, ChrInitGestures(0, 1, 2, 3, 4, 5, 8), 0),
 8603: ChrInitEntry(ChrInitStats(  3, 11, 12, 11, 12,  9, 11,  8, 10,  3, 12), ChrInitWeapons(1330000,  700000, 1406000,      -1), ChrInitArmor( 230000,  231000,  232000,  233000), None, None, None, ChrInitSpells(4000), ChrInitItems(4000, 1, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 201, 20, 103, 1, 117, 1), 6130, 0, 0, 0, 1, None, 0, ChrInitGestures(0, 1, 2, 3, 4, 5, 8), 0),
 8604: ChrInitEntry(ChrInitStats(  3, 12, 11, 10, 12,  8,  8, 15, 10,  3, 10), ChrInitWeapons(1361000,  801000, 1400000,      -1), ChrInitArmor( 900000,  311000,  312000,  313000), None, None, None, ChrInitSpells(5000), ChrInitItems(5000, 1, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 201, 20, 103, 1, 117, 1), 6090, 0, 0, 0, 1, None, 1, ChrInitGestures(0, 1, 2, 3, 4, 5, 13), 0),
 8610: ChrInitEntry(ChrInitStats( 13, 14,  9, 14, 15, 15,  9,  9, 10,  3, 13), ChrInitWeapons( 201003, 1000003, 1450003, 1200003), ChrInitArmor( 210001,  211001,  212001,  213001), ChrInitArrows(2000000, 30, -1, 0, -1, 0, -1, 0), None, None, None, ChrInitItems(-1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 202, 1, 103, 1, 117, 1), 6000, 0, 0, 0, 1, None, 0, ChrInitGestures(0, 1, 2, 3, 4, 5, 8), 0),
 8611: ChrInitEntry(ChrInitStats( 13, 19, 10, 13, 13, 11,  9, 11, 10,  3, 12), ChrInitWeapons( 202003,  300003, 1452003,      -1), ChrInitArmor( 390001,  391001,  392001,  393001), None, None, None, None, ChrInitItems(-1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 202, 1, 103, 1, 117, 1), 6020, 0, 0, 0, 1, None, 1, ChrInitGestures(0, 1, 2, 3, 4, 5, 13), 0),
 8612: ChrInitEntry(ChrInitStats( 13, 11, 17, 10,  9, 11, 20,  8, 10,  3,  8), ChrInitWeapons(1300000,  100003, 1403003,      -1), ChrInitArmor( 220001,  221001,  222001,  223001), None, None, None, ChrInitSpells(3010, 3000, -1, -1, -1, -1, -1), ChrInitItems(3010, 1, 3000, 1, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 202, 1, 103, 1, 117, 1), 6410, 0, 0, 0, 0, None, 0, ChrInitGestures(0, 1, 2, 3, 4, 5, 8), 0),
 8613: ChrInitEntry(ChrInitStats( 13, 13, 14, 12, 14,  9, 13,  8, 10,  3, 13), ChrInitWeapons(1330300,  700003, 1406003,      -1), ChrInitArmor( 230001,  231001,  232001,  233001), None, None, None, ChrInitSpells(4010, 4000, -1, -1, -1, -1, -1), ChrInitItems(4010, 1, 4000, 1, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 202, 1, 103, 1, 117, 1), 6130, 0, 0, 0, 1, None, 0, ChrInitGestures(0, 1, 2, 3, 4, 5, 8), 0),
 8614: ChrInitEntry(ChrInitStats( 13, 14, 13, 12, 12,  8,  8, 19, 10,  3, 10), ChrInitWeapons(1361000,  801003, 1400003,      -1), ChrInitArmor( 900001,  311001,  312001,  313001), None, None, None, ChrInitSpells(5020, 5000, -1, -1, -1, -1, -1), ChrInitItems(5020, 1, 5000, 1, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 202, 1, 103, 1, 117, 1), 6090, 0, 0, 0, 1, None, 1, ChrInitGestures(0, 1, 2, 3, 4, 5, 13), 0),
 8620: ChrInitEntry(ChrInitStats( 19, 15,  9, 15, 17, 16,  9,  9, 10,  3, 14), ChrInitWeapons( 201005, 1000005, 1450005, 1200005), ChrInitArmor( 210003,  211003,  212003,  213003), ChrInitArrows(2000000, 50, -1, 0, -1, 0, -1, 0), None, None, None, ChrInitItems(-1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 202, 1, 103, 1, 117, 1), 6000, 0, 0, 0, 1, None, 0, ChrInitGestures(0, 1, 2, 3, 4, 5, 8), 0),
 8621: ChrInitEntry(ChrInitStats( 19, 18, 10, 14, 18, 11,  9, 11, 10,  3, 13), ChrInitWeapons( 202005,  300005, 1452005,      -1), ChrInitArmor( 390003,  391003,  392003,  393003), None, None, None, None, ChrInitItems(-1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 202, 1, 103, 1, 117, 1), 6020, 0, 0, 0, 1, None, 1, ChrInitGestures(0, 1, 2, 3, 4, 5, 13), 0),
 8622: ChrInitEntry(ChrInitStats( 19, 12, 18, 11,  9, 11, 22,  8, 10,  3,  9), ChrInitWeapons(1300000,  100005, 1403005,      -1), ChrInitArmor( 220003,  221003,  222003,  223003), None, None, None, ChrInitSpells(3010, 3000), ChrInitItems(3010, 1, 3000, 1, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 202, 1, 103, 1, 117, 1), 6410, 0, 0, 0, 0, None, 0, ChrInitGestures(0, 1, 2, 3, 4, 5, 8), 0),
 8623: ChrInitEntry(ChrInitStats( 19, 14, 15, 13, 15,  9, 14,  8, 10,  3, 14), ChrInitWeapons(1330500,  700005, 1406005,      -1), ChrInitArmor( 230003,  231003,  232003,  233003), None, None, None, ChrInitSpells(4010, 4000), ChrInitItems(4010, 1, 4000, 1, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 202, 1, 103, 1, 117, 1), 6130, 0, 0, 0, 1, None, 0, ChrInitGestures(0, 1, 2, 3, 4, 5, 8), 0),
 8624: ChrInitEntry(ChrInitStats( 19, 15, 14, 13, 12,  8,  8, 21, 10,  3, 11), ChrInitWeapons(1361000,  801005, 1400005,      -1), ChrInitArmor( 900003,  311003,  312003,  313003), None, None, None, ChrInitSpells(5020, 5000), ChrInitItems(5020, 1, 5000, 1, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 202, 1, 103, 1, 117, 1), 6090, 0, 0, 0, 1, None, 1, ChrInitGestures(0, 1, 2, 3, 4, 5, 13), 0),
 8630: ChrInitEntry(ChrInitStats( 34, 18,  9, 18, 20, 19,  9,  9, 10,  3, 17), ChrInitWeapons( 201007, 1000007, 1450007, 1200007), ChrInitArmor( 210004,  211004,  212004,  213004), ChrInitArrows(2000000, 70, -1, 0, -1, 0, -1, 0), None, None, None, ChrInitItems(-1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 202, 1, 103, 1, 117, 1), 6000, 0, 0, 0, 1, None, 0, ChrInitGestures(0, 1, 2, 3, 4, 5, 8), 0),
 8631: ChrInitEntry(ChrInitStats( 34, 25, 10, 17, 20, 11,  9, 11, 10,  3, 16), ChrInitWeapons( 202007,  300007, 1452007,      -1), ChrInitArmor( 390004,  391004,  392004,  393004), None, None, None, None, ChrInitItems(-1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 202, 1, 103, 1, 117, 1), 6020, 0, 0, 0, 1, None, 1, ChrInitGestures(0, 1, 2, 3, 4, 5, 13), 0),
 8632: ChrInitEntry(ChrInitStats( 34, 15, 21, 13,  9, 11, 28,  8, 10,  3, 10), ChrInitWeapons(1300000,  100007, 1403007,      -1), ChrInitArmor( 220004,  221004,  222004,  223004), None, None, None, ChrInitSpells(3030, 3010, 3000), ChrInitItems(3030, 1, 3010, 1, 3000, 1, -1, 0, -1, 0, -1, 0, -1, 0, 202, 1, 103, 1, 117, 1), 6410, 0, 0, 0, 0, None, 0, ChrInitGestures(0, 1, 2, 3, 4, 5, 8), 0),
 8633: ChrInitEntry(ChrInitStats( 34, 17, 18, 15, 16,  9, 19,  8, 10,  3, 15), ChrInitWeapons(1330700,  700007, 1406007,      -1), ChrInitArmor( 230004,  231004,  232004,  233004), None, None, None, ChrInitSpells(4020, 4010, 4000), ChrInitItems(4020, 1, 4010, 1, 4000, 1, -1, 0, -1, 0, -1, 0, -1, 0, 202, 1, 103, 1, 117, 1), 6130, 0, 0, 0, 1, None, 0, ChrInitGestures(0, 1, 2, 3, 4, 5, 8), 0),
 8634: ChrInitEntry(ChrInitStats( 34, 18, 17, 15, 12,  8,  8, 27, 10,  3, 12), ChrInitWeapons(1361000,  801007, 1400007,      -1), ChrInitArmor( 900004,  311004,  312004,  313004), None, None, None, ChrInitSpells(5520, 5020, 5000), ChrInitItems(5520, 1, 5020, 1, 5000, 1, -1, 0, -1, 0, -1, 0, -1, 0, 202, 1, 103, 1, 117, 1), 6090, 0, 0, 0, 1, None, 3, ChrInitGestures(0, 1, 2, 3, 4, 5, 13), 0),
 8640: ChrInitEntry(ChrInitStats( 42, 20,  9, 19, 21, 21,  9,  9, 10,  3, 19), ChrInitWeapons( 201009, 1000009, 1450009, 1200009), ChrInitArmor( 210005,  211005,  212005,  213005), ChrInitArrows(2000000, 90, -1, 0, -1, 0, -1, 0), None, None, None, ChrInitItems(-1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 204, 1, 103, 1, 117, 1), 6000, 0, 0, 0, 1, None, 0, ChrInitGestures(0, 1, 2, 3, 4, 5, 8), 0),
 8641: ChrInitEntry(ChrInitStats( 42, 28, 10, 18, 22, 11,  9, 11, 10,  3, 18), ChrInitWeapons( 202009,  300009, 1452009,      -1), ChrInitArmor( 390005,  391005,  392005,  393005), None, None, None, None, ChrInitItems(-1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 204, 1, 103, 1, 117, 1), 6020, 0, 0, 0, 1, None, 1, ChrInitGestures(0, 1, 2, 3, 4, 5, 13), 0),
 8642: ChrInitEntry(ChrInitStats( 42, 16, 23, 13,  9, 11, 32,  8, 10,  3, 11), ChrInitWeapons(1300000,  100008, 1403008,      -1), ChrInitArmor( 220005,  221005,  222005,  223005), None, None, None, ChrInitSpells(3030, 3010, 3000), ChrInitItems(3030, 1, 3010, 1, 3000, 1, -1, 0, -1, 0, -1, 0, -1, 0, 204, 1, 103, 1, 117, 1), 6410, 0, 0, 0, 0, None, 0, ChrInitGestures(0, 1, 2, 3, 4, 5, 8), 0),
 8643: ChrInitEntry(ChrInitStats( 42, 18, 20, 15, 18,  9, 21,  8, 10,  3, 16), ChrInitWeapons(1330800,  700008, 1406008,      -1), ChrInitArmor( 230005,  231005,  232005,  233005), None, None, None, ChrInitSpells(4020, 4010, 4000), ChrInitItems(4020, 1, 4010, 1, 4000, 1, -1, 0, -1, 0, -1, 0, -1, 0, 204, 1, 103, 1, 117, 1), 6130, 0, 0, 0, 1, None, 0, ChrInitGestures(0, 1, 2, 3, 4, 5, 8), 0),
 8644: ChrInitEntry(ChrInitStats( 42, 19, 19, 15, 12,  8,  8, 31, 10,  3, 13), ChrInitWeapons(1361000,  801008, 1400008,      -1), ChrInitArmor( 900005,  311005,  312005,  313005), None, None, None, ChrInitSpells(5010, 5520, 5020, 5000), ChrInitItems(5010, 1, 5520, 1, 5020, 1, 5000, 1, -1, 0, -1, 0, -1, 0, 204, 1, 103, 1, 117, 1), 6090, 0, 0, 0, 1, None, 3, ChrInitGestures(0, 1, 2, 3, 4, 5, 13), 0),
 8650: ChrInitEntry(ChrInitStats( 50, 21,  9, 21, 23, 23,  9,  9, 10,  3, 20), ChrInitWeapons( 201010, 1000010, 1450010, 1200010), ChrInitArmor( 210006,  211006,  212006,  213006), ChrInitArrows(2001000, 20, 2000000, 50, -1, 0, -1, 0), None, None, None, ChrInitItems(-1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 204, 1, 103, 1, 117, 1), 6000, 0, 0, 0, 1, None, 0, ChrInitGestures(0, 1, 2, 3, 4, 5, 8), 0),
 8651: ChrInitEntry(ChrInitStats( 50, 29, 10, 20, 25, 11,  9, 11, 10,  3, 20), ChrInitWeapons( 202010,  300010, 1452010,      -1), ChrInitArmor( 390006,  391006,  392006,  393006), None, None, None, None, ChrInitItems(-1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 204, 1, 103, 1, 117, 1), 6020, 0, 0, 0, 1, None, 1, ChrInitGestures(0, 1, 2, 3, 4, 5, 13), 0),
 8652: ChrInitEntry(ChrInitStats( 50, 18, 24, 14,  9, 11, 35,  8, 10,  3, 12), ChrInitWeapons(1300000,  100010, 1403010,      -1), ChrInitArmor( 220006,  221006,  222006,  223006), None, None, None, ChrInitSpells(3060, 3030, 3010, 3000), ChrInitItems(3060, 1, 3030, 1, 3010, 1, 3000, 1, -1, 0, -1, 0, -1, 0, 204, 1, 103, 1, 117, 1), 6410, 0, 0, 0, 0, None, 0, ChrInitGestures(0, 1, 2, 3, 4, 5, 8), 0),
 8653: ChrInitEntry(ChrInitStats( 50, 20, 21, 16, 19,  9, 23,  8, 10,  3, 17), ChrInitWeapons(1331000,  700010, 1406010,      -1), ChrInitArmor( 230006,  231006,  232006,  233006), None, None, None, ChrInitSpells(4030, 4020, 4010, 4000), ChrInitItems(4030, 1, 4020, 1, 4010, 1, 4000, 1, -1, 0, -1, 0, -1, 0, 204, 1, 103, 1, 117, 1), 6130, 0, 0, 0, 1, None, 0, ChrInitGestures(0, 1, 2, 3, 4, 5, 8), 0),
 8654: ChrInitEntry(ChrInitStats( 50, 21, 20, 16, 12,  8,  8, 34, 10,  3, 14), ChrInitWeapons(1361000,  801010, 1400010,      -1), ChrInitArmor( 900006,  311006,  312006,  313006), None, None, None, ChrInitSpells(5010, 5520, 5020, 5000), ChrInitItems(5010, 1, 5520, 1, 5020, 1, 5000, 1, -1, 0, -1, 0, -1, 0, 204, 1, 103, 1, 117, 1), 6090, 0, 0, 0, 1, None, 3, ChrInitGestures(0, 1, 2, 3, 4, 5, 13), 0),
 8660: ChrInitEntry(ChrInitStats( 56, 22,  9, 22, 24, 24,  9,  9, 10,  3, 22), ChrInitWeapons( 201012, 1000012, 1450012, 1200012), ChrInitArmor( 210007,  211007,  212007,  213007), ChrInitArrows(2001000, 30, 2000000, 70, -1, 0, -1, 0), None, None, None, ChrInitItems(-1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 206, 1, 103, 1, 117, 1), 6000, 0, 0, 0, 1, None, 0, ChrInitGestures(0, 1, 2, 3, 4, 5, 8), 0),
 8661: ChrInitEntry(ChrInitStats( 56, 32, 10, 21, 26, 11,  9, 11, 10,  3, 21), ChrInitWeapons( 202012,  300012, 1452012,      -1), ChrInitArmor( 390007,  391007,  392007,  393007), None, None, None, None, ChrInitItems(-1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 206, 1, 103, 1, 117, 1), 6020, 0, 0, 0, 1, None, 1, ChrInitGestures(0, 1, 2, 3, 4, 5, 13), 0),
 8662: ChrInitEntry(ChrInitStats( 56, 19, 26, 15,  9, 11, 37,  8, 10,  3, 12), ChrInitWeapons(1300000,  100012, 1403012,      -1), ChrInitArmor( 220007,  221007,  222007,  223007), None, None, None, ChrInitSpells(3060, 3030, 3010, 3000), ChrInitItems(3060, 1, 3030, 1, 3010, 1, 3000, 1, -1, 0, -1, 0, -1, 0, 206, 1, 103, 1, 117, 1), 6410, 0, 0, 0, 0, None, 0, ChrInitGestures(0, 1, 2, 3, 4, 5, 8), 0),
 8663: ChrInitEntry(ChrInitStats( 56, 21, 23, 17, 20,  9, 24,  8, 10,  3, 17), ChrInitWeapons(1331200,  700012, 1406012,      -1), ChrInitArmor( 230007,  231007,  232007,  233007), None, None, None, ChrInitSpells(4030, 4020, 4010, 4000), ChrInitItems(4030, 1, 4020, 1, 4010, 1, 4000, 1, -1, 0, -1, 0, -1, 0, 206, 1, 103, 1, 117, 1), 6130, 0, 0, 0, 1, None, 0, ChrInitGestures(0, 1, 2, 3, 4, 5, 8), 0),
 8664: ChrInitEntry(ChrInitStats( 56, 22, 22, 17, 12,  8,  8, 36, 10,  3, 14), ChrInitWeapons(1361000,  801012, 1400012,      -1), ChrInitArmor( 900007,  311007,  312007,  313007), None, None, None, ChrInitSpells(5010, 5520, 5020, 5000), ChrInitItems(5010, 1, 5520, 1, 5020, 1, 5000, 1, -1, 0, -1, 0, -1, 0, 206, 1, 103, 1, 117, 1), 6090, 0, 0, 0, 1, None, 3, ChrInitGestures(0, 1, 2, 3, 4, 5, 13), 0),
 8670: ChrInitEntry(ChrInitStats( 63, 24,  9, 24, 25, 25,  9,  9, 10,  3, 23), ChrInitWeapons( 201014, 1000014, 1450014, 1200014), ChrInitArmor( 210008,  211008,  212008,  213008), ChrInitArrows(2001000, 50, 2000000, 90, -1, 0, -1, 0), None, None, None, ChrInitItems(-1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 206, 1, 103, 1, 117, 1), 6000, 0, 0, 0, 1, None, 0, ChrInitGestures(0, 1, 2, 3, 4, 5, 8), 0),
 8671: ChrInitEntry(ChrInitStats( 63, 34, 10, 23, 28, 11,  9, 11, 10,  3, 22), ChrInitWeapons( 202014,  300014, 1452014,      -1), ChrInitArmor( 390008,  391008,  392008,  393008), None, None, None, None, ChrInitItems(-1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 206, 1, 103, 1, 117, 1), 6020, 0, 0, 0, 1, None, 1, ChrInitGestures(0, 1, 2, 3, 4, 5, 13), 0),
 8672: ChrInitEntry(ChrInitStats( 63, 21, 27, 15,  9, 11, 40,  8, 10,  3, 13), ChrInitWeapons(1300000,  100013, 1403013,      -1), ChrInitArmor( 220008,  221008,  222008,  223008), None, None, None, ChrInitSpells(3060, 3030, 3010, 3000), ChrInitItems(3060, 1, 3030, 1, 3010, 1, 3000, 1, -1, 0, -1, 0, -1, 0, 206, 1, 103, 1, 117, 1), 6410, 0, 0, 0, 0, None, 0, ChrInitGestures(0, 1, 2, 3, 4, 5, 8), 0),
 8673: ChrInitEntry(ChrInitStats( 63, 23, 24, 17, 20,  9, 27,  8, 10,  3, 18), ChrInitWeapons(1331300,  700013, 1406013,      -1), ChrInitArmor( 230008,  231008,  232008,  233008), None, None, None, ChrInitSpells(4030, 4020, 4010, 4000), ChrInitItems(4030, 1, 4020, 1, 4010, 1, 4000, 1, -1, 0, -1, 0, -1, 0, 206, 1, 103, 1, 117, 1), 6130, 0, 0, 0, 1, None, 0, ChrInitGestures(0, 1, 2, 3, 4, 5, 8), 0),
 8674: ChrInitEntry(ChrInitStats( 63, 24, 23, 17, 12,  8,  8, 39, 10,  3, 15), ChrInitWeapons(1361000,  801013, 1400013,      -1), ChrInitArmor( 900008,  311008,  312008,  313008), None, None, None, ChrInitSpells(5010, 5520, 5020, 5000), ChrInitItems(5010, 1, 5520, 1, 5020, 1, 5000, 1, -1, 0, -1, 0, -1, 0, 206, 1, 103, 1, 117, 1), 6090, 0, 0, 0, 1, None, 3, ChrInitGestures(0, 1, 2, 3, 4, 5, 13), 0),
 8680: ChrInitEntry(ChrInitStats( 71, 25,  9, 25, 27, 27,  9,  9, 10,  3, 25), ChrInitWeapons( 201015, 1000015, 1450015, 1200015), ChrInitArmor( 210010,  211010,  212010,  213010), ChrInitArrows(2001000, 70, 2000000, 99, -1, 0, -1, 0), None, None, None, ChrInitItems(-1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 209, 10, 103, 1, 117, 1), 6000, 0, 0, 0, 1, None, 0, ChrInitGestures(0, 1, 2, 3, 4, 5, 8), 0),
 8681: ChrInitEntry(ChrInitStats( 71, 36, 10, 24, 31, 11,  9, 11, 10,  3, 24), ChrInitWeapons( 202015,  300015, 1452015,      -1), ChrInitArmor( 390010,  391010,  392010,  393010), None, None, None, None, ChrInitItems(-1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 209, 10, 103, 1, 117, 1), 6020, 0, 0, 0, 1, None, 1, ChrInitGestures(0, 1, 2, 3, 4, 5, 13), 0),
 8682: ChrInitEntry(ChrInitStats( 71, 22, 29, 16,  9, 11, 43,  8, 10,  3, 14), ChrInitWeapons(1300000,  100015, 1403015,      -1), ChrInitArmor( 220010,  221010,  222010,  223010), None, None, None, ChrInitSpells(3070, 3060, 3030, 3010, 3000), ChrInitItems(3070, 1, 3060, 1, 3030, 1, 3010, 1, 3000, 1, -1, 0, -1, 0, 209, 10, 103, 1, 117, 1), 6410, 0, 0, 0, 0, None, 0, ChrInitGestures(0, 1, 2, 3, 4, 5, 8), 0),
 8683: ChrInitEntry(ChrInitStats( 71, 24, 26, 18, 21,  9, 29,  8, 10,  3, 19), ChrInitWeapons(1331500,  700015, 1406015,      -1), ChrInitArmor( 230010,  231010,  232010,  233010), None, None, None, ChrInitSpells(4030, 4020, 4010, 4000), ChrInitItems(4030, 1, 4020, 1, 4010, 1, 4000, 1, -1, 0, -1, 0, -1, 0, 209, 10, 103, 1, 117, 1), 6130, 0, 0, 0, 1, None, 0, ChrInitGestures(0, 1, 2, 3, 4, 5, 8), 0),
 8684: ChrInitEntry(ChrInitStats( 71, 25, 25, 18, 12,  8,  8, 42, 10,  3, 16), ChrInitWeapons(1361000,  801015, 1400015,      -1), ChrInitArmor( 900010,  311010,  312010,  313010), None, None, None, ChrInitSpells(5010, 5520, 5020, 5000), ChrInitItems(5010, 1, 5520, 1, 5020, 1, 5000, 1, -1, 0, -1, 0, -1, 0, 209, 10, 103, 1, 117, 1), 6090, 0, 0, 0, 1, None, 3, ChrInitGestures(0, 1, 2, 3, 4, 5, 13), 0),
 8690: ChrInitEntry(ChrInitStats( 79, 27,  9, 27, 29, 28,  9,  9, 10,  3, 26), ChrInitWeapons( 201015, 1000015, 1450015, 1200015), ChrInitArmor( 210010,  211010,  212010,  213010), ChrInitArrows(2001000, 90, 2000000, 99, -1, 0, -1, 0), None, None, None, ChrInitItems(-1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 211, 10, 103, 1, 117, 1), 6000, 0, 0, 0, 1, None, 0, ChrInitGestures(0, 1, 2, 3, 4, 5, 8), 0),
 8691: ChrInitEntry(ChrInitStats( 79, 38, 10, 26, 34, 11,  9, 11, 10,  3, 25), ChrInitWeapons( 202015,  300015, 1452015,      -1), ChrInitArmor( 390010,  391010,  392010,  393010), None, None, None, None, ChrInitItems(-1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 211, 10, 103, 1, 117, 1), 6020, 0, 0, 0, 1, None, 1, ChrInitGestures(0, 1, 2, 3, 4, 5, 13), 0),
 8692: ChrInitEntry(ChrInitStats( 79, 24, 30, 17,  9, 11, 46,  8, 10,  3, 15), ChrInitWeapons(1300000,  100015, 1403015,      -1), ChrInitArmor( 220010,  221010,  222010,  223010), None, None, None, ChrInitSpells(3070, 3060, 3030, 3010, 3000), ChrInitItems(3070, 1, 3060, 1, 3030, 1, 3010, 1, 3000, 1, -1, 0, -1, 0, 211, 10, 103, 1, 117, 1), 6410, 0, 0, 0, 0, None, 0, ChrInitGestures(0, 1, 2, 3, 4, 5, 8), 0),
 8693: ChrInitEntry(ChrInitStats( 79, 26, 27, 19, 22,  9, 31,  8, 10,  3, 20), ChrInitWeapons(1331500,  700015, 1406015,      -1), ChrInitArmor( 230010,  231010,  232010,  233010), None, None, None, ChrInitSpells(4030, 4020, 4010, 4000), ChrInitItems(4030, 1, 4020, 1, 4010, 1, 4000, 1, -1, 0, -1, 0, -1, 0, 211, 10, 103, 1, 117, 1), 6130, 0, 0, 0, 1, None, 0, ChrInitGestures(0, 1, 2, 3, 4, 5, 8), 0),
 8694: ChrInitEntry(ChrInitStats( 79, 27, 26, 19, 12,  8,  8, 45, 10,  3, 17), ChrInitWeapons(1361000,  801015, 1400015,      -1), ChrInitArmor( 900010,  311010,  312010,  313010), None, None, None, ChrInitSpells(5010, 5520, 5020, 5000), ChrInitItems(5010, 1, 5520, 1, 5020, 1, 5000, 1, -1, 0, -1, 0, -1, 0, 211, 10, 103, 1, 117, 1), 6090, 0, 0, 0, 1, None, 3, ChrInitGestures(0, 1, 2, 3, 4, 5, 13), 0),
 9000: ChrInitEntry(ChrInitStats(  0, 50, 50, 99, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons( 306000,  354000, 1455000,  852000), ChrInitArmor( 100000,  111000,  292000,  103000), ChrInitArrows(2000000, 50, -1, 0, 2100000, 50, -1, 0), ChrInitRings(100, 138), None, ChrInitSpells(3550, 5500, 4300, 3100, 5400, 5300), ChrInitItems(240, 50, 200, 1, 1000, 99, -1, 0, -1, 0, 106, 1, 100, 1, 101, 1, 102, 1), -1, 0, 0, 0, 1, None, 0, ChrInitGestures(5, 0, 4, 7, 3, 1, 2), 50000),
 9001: ChrInitEntry(ChrInitStats(  0, 50, 50, 99, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons( 201015, 1201015, 1450015, 1300000), ChrInitArmor( 900000,  901000,  902000,  213010), ChrInitArrows(2000000, 99, 2003000, 99, -1, 0, -1, 0), ChrInitRings(100), None, ChrInitSpells(3550, 5500, 4300, 3500, 5400, 5300), ChrInitItems(240, 99, 200, 1, 1000, 99, 280, 99, -1, 0, -1, 0, 100, 1, 101, 1, 102, 1), -1, 0, 0, 0, 1, None, 0, ChrInitGestures(5, 0, 4, 7, 3, 1, 2), 50000),
 9002: ChrInitEntry(ChrInitStats(  0, 50, 50, 99, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons( 201000,  200000, 1450000, 1300000), ChrInitArmor( 900000,  901000,  902000,  213000), None, ChrInitRings(100), None, ChrInitSpells(3550, 5500, 4300, 3500, 5400, 5300), ChrInitItems(240, 50, 200, 1, 1000, 99, -1, 0, -1, 0, -1, 0, 100, 1, 101, 1, 102, 1), 8, 0, 0, 0, 0, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 50000),
 9005: ChrInitEntry(ChrInitStats(  0, 50, 50, 99, 50, 50, 50, 50,  1, 50, 50), ChrInitWeapons(1330000,      -1, 1330000,      -1), ChrInitArmor( 900000,  901000,  902000,  213000), None, None, None, None, ChrInitItems(240, 50, 200, 1, 310, 50, 350, 50, -1, 0, -1, 0, 100, 1, 101, 1, 102, 1), 4, 0, 0, 0, 1, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 50000),
 9006: ChrInitEntry(ChrInitStats(  0, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons( 201000, 1201000, 1450000, 1250000), ChrInitArmor( 170000,  171000,  172000,  173000), ChrInitArrows(2000000, 30, 2003000, 10, 2100000, 30, 2101000, 10), ChrInitRings(114), None, None, ChrInitItems(240, 50, 200, 1, 310, 50, 350, 50, -1, 0, -1, 0, 100, 1, 101, 1, 102, 1), 3104, 0, 0, 0, 1, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 50000),
 9007: ChrInitEntry(ChrInitStats(  0, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons( 201000, 1150000, 1450000, 1300000), ChrInitArmor( 170000,  171000,  172000,  173000), None, ChrInitRings(114), None, None, ChrInitItems(240, 50, 200, 1, 310, 50, 350, 50, -1, 0, -1, 0, 100, 1, 101, 1, 102, 1), -1, 0, 0, 0, 1, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 50000),
 9008: ChrInitEntry(ChrInitStats(  0, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons(1200000,  201000, 1404000, 1300000), ChrInitArmor( 220000,  221000,  222000,  223000), ChrInitArrows(2000000, 99, -1, 0, 2100000, 99, -1, 0), ChrInitRings(100), None, ChrInitSpells(3550, 5500, 4300, 3100, 5400, 5300), ChrInitItems(240, 50, 200, 1, 310, 50, 350, 50, -1, 0, -1, 0, 100, 1, 101, 1, 102, 1), -1, 0, 0, 0, 1, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 50000),
 9010: ChrInitEntry(ChrInitStats(  0, 10, 10, 10, 10, 10, 10, 10, 10,  3, 10), ChrInitWeapons( 201000, 1200000, 1450000, 1300000), ChrInitArmor( 210000,  211000,  212000,  213000), ChrInitArrows(2000000, 99, -1, 0, -1, 0, -1, 0), None, None, ChrInitSpells(3000), ChrInitItems(240, 50, 200, 1, 310, 50, 100, 1, -1, 0, -1, 0, -1, 0, -1, 0, 101, 1), -1, 0, 0, 0, 1, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 9011: ChrInitEntry(ChrInitStats(  0, 14,  8, 13, 14, 11,  8,  8, 10,  5, 10), ChrInitWeapons( 802000,      -1, 1501000, 1300000), ChrInitArmor( 240000,  241000,  242000,  243000), None, None, None, None, None, -1, 502, 0, 0, 1, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 50000),
 9012: ChrInitEntry(ChrInitStats(  0, 50, 50, 99, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons( 300000,  100000,  850000, 1200000), ChrInitArmor( 900000,  901000,  902000,  213000), ChrInitArrows(2000000, 99, -1, 0, -1, 0, -1, 0), None, None, None, ChrInitItems(240, 50, -1, 0, 310, 50, 311, 50, 312, 50, -1, 0, 100, 1, 101, 1, 102, 1), -1, 0, 0, 0, 1, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 50000),
 9013: ChrInitEntry(ChrInitStats(  0, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons( 405000,      -1,  405000, 1404000), ChrInitArmor( 250000,  251000,  252000,  253000), None, None, None, None, ChrInitItems(240, 50, -1, 0, 310, 50, 350, 50, 200, 1, -1, 0, 100, 1, 101, 1, 102, 1), -1, 0, 0, 0, 1, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 50000),
 9014: ChrInitEntry(ChrInitStats(  0, 50, 50, 99, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons( 201000,  201400, 1450000, 1450400), ChrInitArmor( 900000,  901000,  902000,  213000), None, ChrInitRings(100), None, ChrInitSpells(3550, 5500, 4300, 3500, 5400, 5300), ChrInitItems(240, 50, -1, 0, 1000, 99, -1, 0, 200, 1, -1, 0, 100, 1, 101, 1, 312, 99), -1, 0, 0, 0, 1, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 50000),
 9015: ChrInitEntry(ChrInitStats(  0, 14, 28, 99, 12, 11, 21, 25, 11,  3, 15), ChrInitWeapons( 201000, 1200000, 1456000, 1330000), ChrInitArmor( 350000,  351000,  352000,  353000), ChrInitArrows(2000000, 99, 2003000, 99, -1, 0, -1, 0), ChrInitRings(100), None, ChrInitSpells(4000, 4100), ChrInitItems(100, 1, 101, 1, 102, 1, 103, 1), -1, 0, 0, 0, 1, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 0),
 9016: ChrInitEntry(ChrInitStats(  0, 50, 50, 99, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons( 201000,  201700, 1450000, 1300000), ChrInitArmor( 900000,  901000,  902000,  213000), None, ChrInitRings(100), None, ChrInitSpells(3550, 5500, 4300, 3500, 5400, 5300), ChrInitItems(240, 50, 314, 50, 1000, 99, -1, 0, -1, 0, -1, 0, 100, 1, 101, 1, 102, 1), -1, 0, 0, 0, 1, None, 0, ChrInitGestures(5, 0, 4, 7, 3, 1, 2), 50000),
 9017: ChrInitEntry(ChrInitStats(  1, 50, 50, 99, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons( 200015, 1300000, 1404000, 1200000), ChrInitArmor( 220000,  221000,  222000,  223000), ChrInitArrows(2001000, 999, 2000000, 999, -1, 0, -1, 0), ChrInitRings(100, 114), None, ChrInitSpells(3030, 3010, 3050, 3070, 3110, 3310, 3610), ChrInitItems(100, 1, 101, 1, 102, 1, 103, 1, 106, 1, 109, 1, 215, 10, 240, 99, 350, 99), 2000, 0, 0, 0, 0, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 500000),
 9018: ChrInitEntry(ChrInitStats(  0, 50, 50, 99, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons( 201000,      -1, 1450000,      -1), ChrInitArmor( 900000,  901000,  902000,  213000), None, ChrInitRings(100), None, ChrInitSpells(3550, 5500, 4300, 3500, 5400, 5300), ChrInitItems(377, 1, 378, 1, 330, 99, 280, 99, -1, 0, -1, 0, 100, 1, 101, 1, 102, 1), -1, 0, 0, 0, 1, None, 0, ChrInitGestures(5, 0, 4, 7, 3, 1, 2), 50000),
 9100: ChrInitEntry(ChrInitStats(  0, 50, 99, 99, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons(1300000,  201000, 1300000, 1450000), ChrInitArmor( 900000,  901000,  902000,  213000), None, ChrInitRings(114, 2), None, ChrInitSpells(3000, 3010, 3020, 3030, 3040, 3050), ChrInitItems(240, 50, -1, 0, 1000, 99, 106, 1, 103, 1, -1, 0, 100, 1, 101, 1, 102, 1), 2, 0, 0, 0, 1, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 50000),
 9101: ChrInitEntry(ChrInitStats(  0, 50, 99, 99, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons(1300000,  201000, 1300000, 1450000), ChrInitArmor( 900000,  901000,  902000,  213000), None, ChrInitRings(114, 2), None, ChrInitSpells(3060, 3070, 3100, 3110, 3120, 3300, 3310), ChrInitItems(240, 50, -1, 0, 1000, 99, 106, 1, 103, 1, -1, 0, 100, 1, 101, 1, 102, 1), 2, 0, 0, 0, 1, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 50000),
 9102: ChrInitEntry(ChrInitStats(  0, 50, 99, 99, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons(1300000,  201000, 1300000, 1450000), ChrInitArmor( 900000,  901000,  902000,  213000), None, ChrInitRings(114, 2), None, ChrInitSpells(3400, 3410, 3500, 3510, 3520, 3530), ChrInitItems(240, 50, -1, 0, 1000, 99, 106, 1, 103, 1, -1, 0, 100, 1, 101, 1, 102, 1), 2, 0, 0, 0, 1, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 50000),
 9103: ChrInitEntry(ChrInitStats(  0, 50, 99, 99, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons(1300000,  201000, 1300000, 1450000), ChrInitArmor( 900000,  901000,  902000,  213000), None, ChrInitRings(114, 2), None, ChrInitSpells(3540, 3550, 3600, 3610, 3700), ChrInitItems(240, 50, -1, 0, 1000, 99, 106, 1, 103, 1, -1, 0, 100, 1, 101, 1, 102, 1), 2, 0, 0, 0, 1, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 50000),
 9104: ChrInitEntry(ChrInitStats(  0, 50, 99, 99, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons(1330000,  201000, 1330000, 1450000), ChrInitArmor( 900000,  901000,  902000,  213000), None, ChrInitRings(114, 2), None, ChrInitSpells(4000, 4010, 4020, 4030, 4040, 4050, 4060), ChrInitItems(240, 50, -1, 0, 1000, 99, 106, 1, 103, 1, -1, 0, 100, 1, 101, 1, 102, 1), 2, 0, 0, 0, 1, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 50000),
 9105: ChrInitEntry(ChrInitStats(  0, 50, 99, 99, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons(1330000,  201000, 1330000, 1450000), ChrInitArmor( 900000,  901000,  902000,  213000), None, ChrInitRings(114, 2), None, ChrInitSpells(4100, 4110, 4200, 4210, 4220), ChrInitItems(240, 50, -1, 0, 1000, 99, 106, 1, 103, 1, -1, 0, 100, 1, 101, 1, 102, 1), 2, 0, 0, 0, 1, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 50000),
 9106: ChrInitEntry(ChrInitStats(  0, 50, 99, 99, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons(1330000,  201000, 1330000, 1450000), ChrInitArmor( 900000,  901000,  902000,  213000), None, ChrInitRings(114, 2), None, ChrInitSpells(4300, 4310, 4320, 4360, 4400), ChrInitItems(240, 50, -1, 0, 1000, 99, 106, 1, 103, 1, -1, 0, 100, 1, 101, 1, 102, 1), 2, 0, 0, 0, 1, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 50000),
 9107: ChrInitEntry(ChrInitStats(  0, 50, 99, 99, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons(1330000,  201000, 1330000, 1450000), ChrInitArmor( 900000,  901000,  902000,  213000), None, ChrInitRings(114, 2), None, ChrInitSpells(4500, 4510, 4520), ChrInitItems(240, 50, -1, 0, 1000, 99, 106, 1, 103, 1, -1, 0, 100, 1, 101, 1, 102, 1), 2, 0, 0, 0, 1, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 50000),
 9108: ChrInitEntry(ChrInitStats(  0, 50, 99, 99, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons(1360000,  201000, 1360000, 1450000), ChrInitArmor( 900000,  901000,  902000,  213000), None, ChrInitRings(114, 2), None, ChrInitSpells(5000, 5010, 5020, 5030, 5040, 5050), ChrInitItems(240, 50, -1, 0, 1000, 99, 106, 1, 103, 1, -1, 0, 100, 1, 101, 1, 102, 1), 2, 0, 0, 0, 1, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 50000),
 9109: ChrInitEntry(ChrInitStats(  0, 50, 99, 99, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons(1360000,  201000, 1360000, 1450000), ChrInitArmor( 900000,  901000,  902000,  213000), None, ChrInitRings(114, 2), None, ChrInitSpells(5100, 5110, 5200, 5210, 5300, 5310, 5320), ChrInitItems(240, 50, -1, 0, 1000, 99, 106, 1, 103, 1, -1, 0, 100, 1, 101, 1, 102, 1), 2, 0, 0, 0, 1, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 50000),
 9110: ChrInitEntry(ChrInitStats(  0, 50, 99, 99, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons(1360000,  201000, 1360000, 1450000), ChrInitArmor( 900000,  901000,  902000,  213000), None, ChrInitRings(114, 2), None, ChrInitSpells(5400, 5500, 5510, 5520, 5600, 5610), ChrInitItems(240, 50, -1, 0, 1000, 99, 106, 1, 103, 1, -1, 0, 100, 1, 101, 1, 102, 1), 2, 0, 0, 0, 1, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 50000),
 9111: ChrInitEntry(ChrInitStats(  0, 50, 99, 99, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons(1360000,  201000, 1360000, 1450000), ChrInitArmor( 900000,  901000,  902000,  213000), None, ChrInitRings(114, 2), None, ChrInitSpells(5700, 5800, 5810, 5900, 5910), ChrInitItems(240, 50, -1, 0, 1000, 99, 106, 1, 103, 1, -1, 0, 100, 1, 101, 1, 102, 1), 2, 0, 0, 0, 1, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 50000),
 9112: ChrInitEntry(ChrInitStats(  0, 50, 99, 99, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons(1300000, 1330000, 1300000, 1330000), ChrInitArmor( 900000,  901000,  902000,  213000), None, ChrInitRings(114, 2), None, ChrInitSpells(3710, 3720, 3730, 3740, 4530), ChrInitItems(240, 50, -1, 0, 1000, 99, 106, 1, 103, 1, -1, 0, 100, 1, 101, 1, 102, 1), 2, 0, 0, 0, 1, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 50000),
 9120: ChrInitEntry(ChrInitStats(  0, 50, 99, 99, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons( 211000,  306000, 1450000, 1300000), ChrInitArmor( 900000,  901000,  902000,  213000), None, ChrInitRings(114, 2), None, None, ChrInitItems(240, 50, 280, 99, 1000, 99, 106, 1, 103, 1, -1, 0, 100, 1, 101, 1, 102, 1), 2, 0, 0, 0, 1, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 50000),
 9121: ChrInitEntry(ChrInitStats(  0, 50, 99, 99, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons( 309000,  354000, 1450000, 1300000), ChrInitArmor( 900000,  901000,  902000,  213000), None, ChrInitRings(114, 2), None, None, ChrInitItems(240, 50, 280, 99, 1000, 99, 106, 1, 103, 1, -1, 0, 100, 1, 101, 1, 102, 1), 2, 0, 0, 0, 1, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 50000),
 9122: ChrInitEntry(ChrInitStats(  0, 50, 99, 99, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons( 704000,  752000, 1450000, 1300000), ChrInitArmor( 900000,  901000,  902000,  213000), None, ChrInitRings(114, 2), None, None, ChrInitItems(240, 50, 280, 99, 1000, 99, 106, 1, 103, 1, -1, 0, 100, 1, 101, 1, 102, 1), 2, 0, 0, 0, 1, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 50000),
 9123: ChrInitEntry(ChrInitStats(  0, 50, 99, 99, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons( 851000,  904000, 1450000,  904000), ChrInitArmor( 900000,  901000,  902000,  213000), None, ChrInitRings(114, 2), None, None, ChrInitItems(240, 50, 280, 99, 1000, 99, 106, 1, 103, 1, -1, 0, 100, 1, 101, 1, 102, 1), 2, 0, 0, 0, 1, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 50000),
 9124: ChrInitEntry(ChrInitStats(  0, 50, 99, 99, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons(1004000, 1051000, 1450000, 1450000), ChrInitArmor( 900000,  901000,  902000,  213000), None, ChrInitRings(114, 2), None, None, ChrInitItems(240, 50, 280, 99, 1000, 99, 106, 1, 103, 1, -1, 0, 100, 1, 101, 1, 102, 1), 2, 0, 0, 0, 1, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 50000),
 9125: ChrInitEntry(ChrInitStats(  0, 50, 99, 99, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons(1411000, 1505000, 1411000, 1505000), ChrInitArmor( 900000,  901000,  902000,  213000), None, ChrInitRings(114, 2), None, None, ChrInitItems(240, 50, 280, 99, 1000, 99, 106, 1, 103, 1, -1, 0, 100, 1, 101, 1, 102, 1), 2, 0, 0, 0, 1, None, 0, ChrInitGestures(5, 0, 4, 6, 3, 1, 2), 50000),
 9130: ChrInitEntry(ChrInitStats(  5, 13,  9, 13, 13, 13,  9,  9, 10,  3, 11), ChrInitWeapons( 201000,  401000,  602000,  801000), ChrInitArmor( 210000,  211000,  212000,  213000), None, None, None, None, ChrInitItems(-1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 200, 1, 103, 1, 117, 1), 6000, 0, 0, 0, 1, None, 0, ChrInitGestures(0, 1, 2, 3, 4, 5, 8), 0),
 9131: ChrInitEntry(ChrInitStats( 15, 14,  9, 14, 17, 16,  9,  9, 10,  3, 12), ChrInitWeapons( 201003,  401003,  602003,  801003), ChrInitArmor( 210002,  211002,  212002,  213002), None, None, None, None, ChrInitItems(-1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 200, 1, 103, 1, 117, 1), 6000, 0, 0, 0, 1, None, 0, ChrInitGestures(0, 1, 2, 3, 4, 5, 8), 0),
 9132: ChrInitEntry(ChrInitStats( 25, 15,  9, 15, 21, 19,  9,  9, 10,  3, 13), ChrInitWeapons( 201006,  401006,  602006,  801006), ChrInitArmor( 210004,  211004,  212004,  213004), None, None, None, None, ChrInitItems(-1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 200, 1, 103, 1, 117, 1), 6000, 0, 0, 0, 1, None, 0, ChrInitGestures(0, 1, 2, 3, 4, 5, 8), 0),
 9133: ChrInitEntry(ChrInitStats( 35, 16,  9, 16, 25, 22,  9,  9, 10,  3, 14), ChrInitWeapons( 201008,  401008,  602008,  801008), ChrInitArmor( 210006,  211006,  212006,  213006), None, None, None, None, ChrInitItems(-1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 200, 1, 103, 1, 117, 1), 6000, 0, 0, 0, 1, None, 0, ChrInitGestures(0, 1, 2, 3, 4, 5, 8), 0),
 9134: ChrInitEntry(ChrInitStats( 45, 17,  9, 17, 29, 25,  9,  9, 10,  3, 15), ChrInitWeapons( 201010,  401010,  602010,  801010), ChrInitArmor( 210008,  211008,  212008,  213008), None, None, None, None, ChrInitItems(-1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 200, 1, 103, 1, 117, 1), 6000, 0, 0, 0, 1, None, 0, ChrInitGestures(0, 1, 2, 3, 4, 5, 8), 0),
 9135: ChrInitEntry(ChrInitStats( 55, 18,  9, 17, 33, 29,  9,  9, 10,  3, 16), ChrInitWeapons( 201012,  401012,  602012,  801012), ChrInitArmor( 210010,  211010,  212010,  213010), None, None, None, None, ChrInitItems(-1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 200, 1, 103, 1, 117, 1), 6000, 0, 0, 0, 1, None, 0, ChrInitGestures(0, 1, 2, 3, 4, 5, 8), 0),
 9136: ChrInitEntry(ChrInitStats( 65, 18,  9, 18, 37, 33,  9,  9, 10,  3, 17), ChrInitWeapons( 201014,  401014,  602014,  801014), ChrInitArmor( 210010,  211010,  212010,  213010), None, None, None, None, ChrInitItems(-1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 200, 1, 103, 1, 117, 1), 6000, 0, 0, 0, 1, None, 0, ChrInitGestures(0, 1, 2, 3, 4, 5, 8), 0),
 9137: ChrInitEntry(ChrInitStats( 75, 19,  9, 19, 41, 37,  9,  9, 10,  3, 17), ChrInitWeapons( 201015,  401015,  602015,  801015), ChrInitArmor( 210010,  211010,  212010,  213010), None, None, None, None, ChrInitItems(-1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 200, 1, 103, 1, 117, 1), 6000, 0, 0, 0, 1, None, 0, ChrInitGestures(0, 1, 2, 3, 4, 5, 8), 0),
 9140: ChrInitEntry(ChrInitStats(  0, 50, 50, 99, 50, 50, 50, 50, 50, 50, 50), ChrInitWeapons( 310000,  201000,  100000, 1201000), ChrInitArmor(     -1, 2171008, 2172008, 2173008), ChrInitArrows(2000000, 999, 2003000, 999, -1, 0, -1, 0), None, None, None, ChrInitItems(377, 1, 310, 99, 201, 15, 100, 1, 101, 1, 103, 1, 117, 1), 6270, 0, 0, 0, 1, None, 5, ChrInitGestures(0, 1, 2, 3, 4, 5, 8), 50000)
} 

class CharacterArmorLinks:
    def __init__(self, head_list, chest_list, arms_list, legs_list, 
     is_npc = True, has_hat = True, special_hat = False):
        if head_list == None:
            self.head_list = []
        else:
            self.head_list = head_list
        
        if chest_list == None:
            self.chest_list = []
        else:
            self.chest_list = chest_list
            
        if arms_list == None:
            self.arms_list = []
        else:
            self.arms_list = arms_list
            
        if legs_list == None:
            self.legs_list = []
        else:
            self.legs_list = legs_list
            
        self.is_npc = is_npc
        self.has_hat = has_hat
        self.special_hat = special_hat
        
    @classmethod
    def from_same_list(cls, same_list, is_npc = True, has_hat = True, 
     special_hat = False):
        return CharacterArmorLinks(same_list, same_list, same_list, 
         same_list, is_npc, has_hat, special_hat)

CHR_ARMOR_LINKS = [
 CharacterArmorLinks.from_same_list([(2000, 0), (3000, 0)], is_npc = False), # Starting Class Warrior
 CharacterArmorLinks.from_same_list([(2001, 0), (3001, 0)], is_npc = False), # Starting Class Knight
 CharacterArmorLinks.from_same_list([(2002, 0), (3002, 0)], is_npc = False), # Starting Class Wanderer
 CharacterArmorLinks.from_same_list([(2003, 0), (3003, 0)], is_npc = False), # Starting Class Thief
 CharacterArmorLinks.from_same_list([(2004, 0), (3004, 0)], is_npc = False), # Starting Class Bandit
 CharacterArmorLinks.from_same_list([(2005, 0), (3005, 0)], is_npc = False, has_hat = False), # Starting Class Hunter
 CharacterArmorLinks.from_same_list([(2006, 0), (3006, 0)], is_npc = False), # Starting Class Sorcerer
 CharacterArmorLinks.from_same_list([(2007, 0), (3007, 0)], is_npc = False), # Starting Class Pyromancer
 CharacterArmorLinks.from_same_list([(2008, 0), (3008, 0)], is_npc = False, has_hat = False), # Starting Class Cleric
 CharacterArmorLinks([(2009, 0), (3009, 0)], None, None, None, is_npc = False, special_hat = True), # Starting Class Deprived
 CharacterArmorLinks([(6000, 2), (6002, 10), (6003, 10), (6540, 2), (6542, 10), (6543, 10), (6544, 10)], 
                     [(6000, 2), (6002, 10), (6003, 10), (6004, 10), (6540, 2), (6542, 10), (6543, 10), (6544, 10)], 
                     [(6000, 2), (6002, 10), (6003, 10), (6004, 10), (6540, 2), (6542, 10), (6543, 10), (6544, 10)], 
                     [(6000, 2), (6002, 10), (6003, 10), (6004, 10), (6540, 2), (6542, 10), (6543, 10), (6544, 10)]),  # Solaire
 CharacterArmorLinks([(6004, 10)], None, None, None, special_hat = True), # Solaire's Sunlight Maggot
 CharacterArmorLinks.from_same_list([(6010, 10)]), # Darkmoon Knightess
 CharacterArmorLinks.from_same_list([(6020, 6), (6021, 0)]), # Oscar
 CharacterArmorLinks([(6030, 10), (6031, 10), (6032, 10)],
                     [(6030, 10), (6031, 10)],
                     [(6030, 8), (6031, 10)],
                     [(6030, 8), (6031, 10)]), # Logan
 CharacterArmorLinks.from_same_list([(6040, 4), (6041, 0)]), # Griggs
 CharacterArmorLinks.from_same_list([(6050, 0), (6051, 0), (6700, 0)]), # Dusk
 CharacterArmorLinks.from_same_list([(6070, 0), (6071, 0)]), # Rhea
 CharacterArmorLinks.from_same_list([(6080, 0)], has_hat = False), # Petrus
 CharacterArmorLinks.from_same_list([(6090, 10), (6091, 0)], has_hat = False), # Vince
 CharacterArmorLinks.from_same_list([(6100, 10), (6101, 0)]), # Nico
 CharacterArmorLinks.from_same_list([(6130, 6), (6131, 0)]), # Laurentius
 CharacterArmorLinks.from_same_list([(6170, 10)]), # Quelana
 CharacterArmorLinks.from_same_list([(6180, 8)]), # Ingward
 CharacterArmorLinks.from_same_list([(6220, 0)]), # Rickert
 CharacterArmorLinks.from_same_list([(6250, 8)]), # Crestfallen Merchant
 CharacterArmorLinks.from_same_list([(6260, 0)]), # Domhnall
 CharacterArmorLinks.from_same_list([(6270, 8), (6271, 0)], has_hat = False), # Crestfallen Warrior
 CharacterArmorLinks.from_same_list([(6280, 10), (6281, 10), (6282, 10), (6283, 10), (6284, 10)]), # Siegmeyer
 CharacterArmorLinks.from_same_list([(6290, 10), (6291, 10)]), # Sieglinde
 CharacterArmorLinks.from_same_list([(6300, 8), (6301, 10), (6591, 8)]), # Lautrec
 CharacterArmorLinks.from_same_list([(6310, 10)]), # Shiva
 CharacterArmorLinks.from_same_list([(6320, 10), (6321, 10)], has_hat = False), # Patches
 CharacterArmorLinks.from_same_list([(6370, 4)]), # Oswald
 CharacterArmorLinks.from_same_list([(6420, 10)]), # Ninja
 CharacterArmorLinks.from_same_list([(6490, 10)]), # Lautrec's Pike Friend
 CharacterArmorLinks.from_same_list([(6500, 10)]), # Lautrec's Mage Friend
 CharacterArmorLinks.from_same_list([(6510, 10)]), # Tarkus
 CharacterArmorLinks.from_same_list([(6520, 4), (6521, 10)]), # Beatrice
 CharacterArmorLinks([(6530, 6), (6531, 6)], None, None, None, special_hat = True), # Mildred
 CharacterArmorLinks.from_same_list([(6550, 2), (6551, 10)]), # Leeroy
 CharacterArmorLinks.from_same_list([(6560, 0), (6561, 10), (6562, 10)]), # Kirk
 CharacterArmorLinks.from_same_list([(6570, 10)]), # Jeremiah
 CharacterArmorLinks.from_same_list([(6580, 10)]), # Havel
 CharacterArmorLinks.from_same_list([(6600, 8)]), # Ricard
 CharacterArmorLinks.from_same_list([(6610, 10)]), # Crystal Knight
 CharacterArmorLinks.from_same_list([(6620, 10)]), # Daughter of Chaos
 CharacterArmorLinks.from_same_list([(6640, 10)]), # Berenike Darkmoon
 CharacterArmorLinks.from_same_list([(6650, 10)]), # Balder Darkmoon
 CharacterArmorLinks.from_same_list([(6740, 10)]), # Ciaran
 CharacterArmorLinks.from_same_list([(6801, 10)]), # Forest Bandit
 CharacterArmorLinks.from_same_list([(6802, 10)]), # Forest Knight
 CharacterArmorLinks.from_same_list([(6803, 10)]), # Pharis
 CharacterArmorLinks.from_same_list([(6804, 10)], has_hat = False), # Forest Mage
 CharacterArmorLinks.from_same_list([(6805, 10)], has_hat = False), # Forest Cleric
 CharacterArmorLinks.from_same_list([(6806, 10)]) # Forest Thief
]

class CharacterArmorSet:
    UPGRADE_NORMAL = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    UPGRADE_UNIQUE = [0, 0, 1, 1, 2, 2, 3, 4, 4, 5, 5]
    UPGRADE_NONE   = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]    
    
    def __init__(self, head_armor, chest_armor, arm_armor, leg_armor,
     head_upgrades, chest_upgrades, arm_upgrades, leg_upgrades, 
     npc_usable = True, player_usable = True, special_hat = False):
        self.head_armor = head_armor
        self.chest_armor = chest_armor
        self.arm_armor = arm_armor
        self.leg_armor = leg_armor
        self.head_upgrades = head_upgrades
        self.chest_upgrades = chest_upgrades
        self.arm_upgrades = arm_upgrades
        self.leg_upgrades = leg_upgrades
        self.npc_usable = npc_usable
        self.player_usable = player_usable
        self.special_hat = special_hat
        
    @classmethod
    def from_use_single_upgrade(cls, head_armor, chest_armor, 
     arm_armor, leg_armor, upgrades, npc_usable = True, 
     player_usable = True, special_hat = False):
         return CharacterArmorSet(head_armor, chest_armor, arm_armor, 
          leg_armor, upgrades, upgrades, upgrades, upgrades, npc_usable, 
          player_usable, special_hat)

ARMOR_SETS = [
 CharacterArmorSet.from_use_single_upgrade( 10000,  11000,  12000,  13000, CharacterArmorSet.UPGRADE_UNIQUE),
 CharacterArmorSet.from_use_single_upgrade( 20000,  21000,  22000,  23000, CharacterArmorSet.UPGRADE_UNIQUE),
 CharacterArmorSet.from_use_single_upgrade( 40000,  41000,  42000,  43000, CharacterArmorSet.UPGRADE_UNIQUE),
 CharacterArmorSet.from_use_single_upgrade( 50000,  51000,  52000,  53000, CharacterArmorSet.UPGRADE_NORMAL),
 CharacterArmorSet.from_use_single_upgrade( 60000,  61000,  62000,  63000, CharacterArmorSet.UPGRADE_UNIQUE),
 CharacterArmorSet.from_use_single_upgrade( 70000,  71000,  72000,  73000, CharacterArmorSet.UPGRADE_UNIQUE),
 CharacterArmorSet.from_use_single_upgrade( 80000,  81000,  82000,  83000, CharacterArmorSet.UPGRADE_NONE),
 CharacterArmorSet.from_use_single_upgrade( 90000,  91000,  92000,  93000, CharacterArmorSet.UPGRADE_NONE),
 CharacterArmorSet.from_use_single_upgrade(100000, 101000, 102000, 103000, CharacterArmorSet.UPGRADE_UNIQUE),
 CharacterArmorSet.from_use_single_upgrade(110000, 111000, 112000, 113000, CharacterArmorSet.UPGRADE_NONE),
 CharacterArmorSet.from_use_single_upgrade(120000, 121000, 122000, 123000, CharacterArmorSet.UPGRADE_NONE),
 CharacterArmorSet.from_use_single_upgrade(130000, 131000, 132000, 133000, CharacterArmorSet.UPGRADE_NONE),
 CharacterArmorSet.from_use_single_upgrade(140000, 141000, 142000, 143000, CharacterArmorSet.UPGRADE_UNIQUE),
 CharacterArmorSet.from_use_single_upgrade(150000, 151000, 152000, 153000, CharacterArmorSet.UPGRADE_UNIQUE),
 CharacterArmorSet.from_use_single_upgrade(160000, 161000, 162000, 163000, CharacterArmorSet.UPGRADE_NORMAL),
 CharacterArmorSet.from_use_single_upgrade(170000, 171000, 172000, 173000, CharacterArmorSet.UPGRADE_NORMAL),
 CharacterArmorSet.from_use_single_upgrade(180000, 181000, 182000, 183000, CharacterArmorSet.UPGRADE_NORMAL),
 CharacterArmorSet.from_use_single_upgrade(190000,     -1,     -1,     -1, CharacterArmorSet.UPGRADE_NONE, special_hat = True),
 CharacterArmorSet.from_use_single_upgrade(200000, 201000, 202000, 203000, CharacterArmorSet.UPGRADE_UNIQUE),
 CharacterArmorSet.from_use_single_upgrade(210000, 211000, 212000, 213000, CharacterArmorSet.UPGRADE_NORMAL),
 CharacterArmorSet.from_use_single_upgrade(220000, 221000, 222000, 223000, CharacterArmorSet.UPGRADE_NORMAL),
 CharacterArmorSet.from_use_single_upgrade(230000, 231000, 232000, 233000, CharacterArmorSet.UPGRADE_NORMAL),
 CharacterArmorSet.from_use_single_upgrade(240000, 241000, 242000, 243000, CharacterArmorSet.UPGRADE_NORMAL),
 CharacterArmorSet.from_use_single_upgrade(250000, 251000, 252000, 253000, CharacterArmorSet.UPGRADE_UNIQUE),
 CharacterArmorSet.from_use_single_upgrade(270000, 271000, 272000, 273000, CharacterArmorSet.UPGRADE_NONE),
 CharacterArmorSet.from_use_single_upgrade(280000, 281000, 282000, 283000, CharacterArmorSet.UPGRADE_UNIQUE),
 CharacterArmorSet.from_use_single_upgrade(290000, 291000, 292000, 293000, CharacterArmorSet.UPGRADE_UNIQUE),
 CharacterArmorSet.from_use_single_upgrade(300000, 301000, 302000, 303000, CharacterArmorSet.UPGRADE_NORMAL),
 CharacterArmorSet.from_use_single_upgrade(310000, 311000, 312000, 313000, CharacterArmorSet.UPGRADE_NORMAL),
 CharacterArmorSet.from_use_single_upgrade(320000, 321000, 322000, 323000, CharacterArmorSet.UPGRADE_UNIQUE),
 CharacterArmorSet(330000, 331000, 332000, 333000, CharacterArmorSet.UPGRADE_NONE, CharacterArmorSet.UPGRADE_UNIQUE,
  CharacterArmorSet.UPGRADE_UNIQUE, CharacterArmorSet.UPGRADE_UNIQUE),
 CharacterArmorSet.from_use_single_upgrade(340000, 341000, 342000, 343000, CharacterArmorSet.UPGRADE_UNIQUE),
 CharacterArmorSet.from_use_single_upgrade(350000, 351000, 352000, 353000, CharacterArmorSet.UPGRADE_NORMAL),
 CharacterArmorSet.from_use_single_upgrade(360000, 361000, 362000, 363000, CharacterArmorSet.UPGRADE_NORMAL),
 CharacterArmorSet.from_use_single_upgrade(370000, 371000, 372000, 373000, CharacterArmorSet.UPGRADE_NORMAL, player_usable = False),
 CharacterArmorSet(380000, 381000, 382000, 383000, CharacterArmorSet.UPGRADE_UNIQUE, CharacterArmorSet.UPGRADE_UNIQUE,
  CharacterArmorSet.UPGRADE_NORMAL, CharacterArmorSet.UPGRADE_NORMAL),
 CharacterArmorSet.from_use_single_upgrade(390000, 391000, 392000, 393000, CharacterArmorSet.UPGRADE_NORMAL),
 CharacterArmorSet.from_use_single_upgrade(400000, 401000, 402000, 403000, CharacterArmorSet.UPGRADE_NORMAL),
 CharacterArmorSet.from_use_single_upgrade(410000, 411000, 412000, 413000, CharacterArmorSet.UPGRADE_NORMAL),
 CharacterArmorSet.from_use_single_upgrade(420000, 421000, 422000, 423000, CharacterArmorSet.UPGRADE_UNIQUE),
 CharacterArmorSet.from_use_single_upgrade(440000, 441000, 442000, 443000, CharacterArmorSet.UPGRADE_NONE),
 CharacterArmorSet.from_use_single_upgrade(450000, 451000, 452000, 453000, CharacterArmorSet.UPGRADE_UNIQUE),
 CharacterArmorSet.from_use_single_upgrade(460000, 461000, 462000, 463000, CharacterArmorSet.UPGRADE_NONE),
 CharacterArmorSet.from_use_single_upgrade(470000, 471000, 472000, 473000, CharacterArmorSet.UPGRADE_NONE),
 CharacterArmorSet.from_use_single_upgrade(480000, 481000,     -1, 483000, CharacterArmorSet.UPGRADE_NORMAL),
 CharacterArmorSet.from_use_single_upgrade(490000, 491000, 492000, 493000, CharacterArmorSet.UPGRADE_NORMAL),
 CharacterArmorSet.from_use_single_upgrade(500000, 501000,     -1, 503000, CharacterArmorSet.UPGRADE_NORMAL),
 CharacterArmorSet.from_use_single_upgrade(510000, 511000, 512000, 513000, CharacterArmorSet.UPGRADE_NORMAL),
 CharacterArmorSet.from_use_single_upgrade(520000, 521000,     -1, 523000, CharacterArmorSet.UPGRADE_NORMAL),
 CharacterArmorSet.from_use_single_upgrade(530000, 531000, 532000, 533000, CharacterArmorSet.UPGRADE_UNIQUE),
 CharacterArmorSet.from_use_single_upgrade(540000, 541000, 542000, 543000, CharacterArmorSet.UPGRADE_NONE),
 CharacterArmorSet.from_use_single_upgrade(550000, 551000, 552000, 553000, CharacterArmorSet.UPGRADE_NONE),
 CharacterArmorSet.from_use_single_upgrade(560000,     -1,     -1,     -1, CharacterArmorSet.UPGRADE_NORMAL, special_hat = True),
 CharacterArmorSet.from_use_single_upgrade(570000,     -1,     -1,     -1, CharacterArmorSet.UPGRADE_NONE, special_hat = True, npc_usable = False),
 CharacterArmorSet.from_use_single_upgrade(580000,     -1,     -1,     -1, CharacterArmorSet.UPGRADE_NORMAL, special_hat = True),
 CharacterArmorSet.from_use_single_upgrade(590000,     -1,     -1,     -1, CharacterArmorSet.UPGRADE_NONE, special_hat = True),
 CharacterArmorSet.from_use_single_upgrade(600000,     -1,     -1,     -1, CharacterArmorSet.UPGRADE_NONE, special_hat = True),
 CharacterArmorSet.from_use_single_upgrade(610000,     -1,     -1,     -1, CharacterArmorSet.UPGRADE_NONE, special_hat = True),
 CharacterArmorSet.from_use_single_upgrade(620000,     -1,     -1,     -1, CharacterArmorSet.UPGRADE_UNIQUE, special_hat = True),
 CharacterArmorSet.from_use_single_upgrade(630000,     -1,     -1,     -1, CharacterArmorSet.UPGRADE_UNIQUE, special_hat = True),
 CharacterArmorSet.from_use_single_upgrade(640000, 641000, 642000, 643000, CharacterArmorSet.UPGRADE_NORMAL),
 CharacterArmorSet.from_use_single_upgrade(650000, 651000, 652000, 653000, CharacterArmorSet.UPGRADE_NORMAL, player_usable = False),
 CharacterArmorSet.from_use_single_upgrade(660000, 661000, 662000, 663000, CharacterArmorSet.UPGRADE_UNIQUE),
 CharacterArmorSet.from_use_single_upgrade(670000, 671000, 672000, 673000, CharacterArmorSet.UPGRADE_UNIQUE),
 CharacterArmorSet.from_use_single_upgrade(680000, 681000, 682000, 683000, CharacterArmorSet.UPGRADE_UNIQUE),
 CharacterArmorSet.from_use_single_upgrade(690000, 691000, 692000, 693000, CharacterArmorSet.UPGRADE_NONE),
 CharacterArmorSet.from_use_single_upgrade(700000, 701000, 702000, 703000, CharacterArmorSet.UPGRADE_UNIQUE),
 CharacterArmorSet.from_use_single_upgrade(710000,     -1,     -1,     -1, CharacterArmorSet.UPGRADE_NONE, special_hat = True),
 CharacterArmorSet.from_use_single_upgrade(720000,     -1,     -1,     -1, CharacterArmorSet.UPGRADE_NONE, special_hat = True)
]

def randomize_chr_armor(chr_init_param, rand_options, random_source):
    NO_HAT_CHANCE_USUAL = 0.05   # Chance to not have a hat for a character that normally has a hat.
    NO_HAT_CHANCE_HATLESS = 0.60 # Chance to not have a hat for a character that does not normally have a hat.
    
    for links in CHR_ARMOR_LINKS:
        head_list = links.head_list
        chest_list = links.chest_list
        arms_list = links.arms_list
        legs_list = links.legs_list
        
        if links.is_npc and not rand_options.randomize_npc_armor:
            continue
        
        if not rand_options.fashion_souls or links.special_hat:
            armor_sets = [s for s in ARMOR_SETS if (
             (not links.is_npc or s.npc_usable) and 
             (links.is_npc or s.player_usable) and 
             (links.special_hat == s.special_hat))
            ]
            
            head_choice = random_source.choice(armor_sets)
            chest_choice = head_choice
            arms_choice = head_choice
            legs_choice = head_choice
        else:
            head_armor_sets = [s for s in ARMOR_SETS if (
             (not links.is_npc or s.npc_usable) and 
             (links.is_npc or s.player_usable))
            ]
            other_armor_sets = [s for s in head_armor_sets if not s.special_hat]
            
            head_choice = random_source.choice(head_armor_sets)
            chest_choice = random_source.choice(other_armor_sets)
            arms_choice = random_source.choice(other_armor_sets)
            legs_choice = random_source.choice(other_armor_sets)
        
        not_uses_hat = ((links.has_hat and random_source.random() < NO_HAT_CHANCE_USUAL) or
            (not links.has_hat and random_source.random() < NO_HAT_CHANCE_HATLESS))
        for (chr_id, upgrade_level) in head_list:
            chr_init = chr_init_param.find_chr_by_id(chr_id)
            if chr_init == None:
                log.warn("Attempted to randomize head armor of chr #" + str(chr_id) + 
                 " but was not found in chr_init_param!")
                continue
            head_to_use = -1
            if head_choice.head_armor != -1:
                head_to_use = head_choice.head_armor + head_choice.head_upgrades[upgrade_level]
            if not_uses_hat:
                head_to_use = -1
            if head_to_use == -1 and not links.is_npc:
                head_to_use = 900000
            chr_init.armor_head = head_to_use
        for (chr_id, upgrade_level) in chest_list:
            chr_init = chr_init_param.find_chr_by_id(chr_id)
            if chr_init == None:
                log.warn("Attempted to randomize chest armor of chr #" + str(chr_id) + 
                 " but was not found in chr_init_param!")
                continue
            chest_to_use = -1
            if chest_choice.chest_armor != -1:
                chest_to_use = chest_choice.chest_armor + chest_choice.chest_upgrades[upgrade_level]
            if chest_to_use == -1 and not links.is_npc:
                chest_to_use = 901000
            chr_init.armor_chest = chest_to_use
        for (chr_id, upgrade_level) in arms_list:
            chr_init = chr_init_param.find_chr_by_id(chr_id)
            if chr_init == None:
                log.warn("Attempted to randomize arm armor of chr #" + str(chr_id) + 
                 " but was not found in chr_init_param!")
                continue
            arms_to_use = -1
            if arms_choice.arm_armor != -1:
                arms_to_use = arms_choice.arm_armor + arms_choice.arm_upgrades[upgrade_level]
            if arms_to_use == -1 and not links.is_npc:
                arms_to_use = 902000
            chr_init.armor_hand = arms_to_use
        for (chr_id, upgrade_level) in legs_list:
            chr_init = chr_init_param.find_chr_by_id(chr_id)
            if chr_init == None:
                log.warn("Attempted to randomize leg armor of chr #" + str(chr_id) + 
                 " but was not found in chr_init_param!")
                continue
            legs_to_use = -1
            if legs_choice.leg_armor != -1:
                legs_to_use = legs_choice.leg_armor + legs_choice.leg_upgrades[upgrade_level]
            if legs_to_use == -1 and not links.is_npc:
                legs_to_use = 903000
            chr_init.armor_leg = legs_to_use



class StartingClassWeaponShield:
    class POOL(Enum):
        RIGHT_HAND = 0 # In right-hand pool, and left-hand pool when expanded.
        LEFT_HAND = 1 # In only left-hand pool (and when expanded).
        BOTH = 2 # In both pools always.
        LEFT_ONLY_EXPANDED = 3 # In left-hand pool *only* when pool is expanded.
    
    def __init__(self, req_str, req_dex, req_int, req_fth, two_handable, pool):
        self.req_str = req_str
        self.req_dex = req_dex
        self.req_int = req_int
        self.req_fth = req_fth
        self.two_handable = two_handable
        self.pool = pool
        
    def can_be_used(self, base_str, base_dex, base_int, base_fth, is_two_handing, is_offhand, use_expanded_offhand):
        if not is_offhand and self.pool not in [StartingClassWeaponShield.POOL.RIGHT_HAND, StartingClassWeaponShield.POOL.BOTH]:
            return False
        if is_offhand and not use_expanded_offhand and self.pool not in [StartingClassWeaponShield.POOL.LEFT_HAND, StartingClassWeaponShield.POOL.BOTH]:
            return False
        if is_two_handing and self.two_handable:
            passed_str_req = (self.req_str <= math.floor(base_str*1.5))
        else:
            passed_str_req = (self.req_str <= base_str)
        passed_dex_req = (self.req_dex <= base_dex)
        passed_int_req = (self.req_int <= base_int)
        passed_fth_req = (self.req_fth <= base_fth)
        return (passed_str_req and passed_dex_req and passed_int_req and passed_fth_req)
        
STARTING_WEAPONS_AND_SHIELDS = {
 100000: StartingClassWeaponShield(5, 8, 0, 0, True, StartingClassWeaponShield.POOL.RIGHT_HAND),
 101000: StartingClassWeaponShield(5, 14, 0, 0, True, StartingClassWeaponShield.POOL.RIGHT_HAND),
 102000: StartingClassWeaponShield(5, 0, 0, 0, True, StartingClassWeaponShield.POOL.RIGHT_HAND),
 103000: StartingClassWeaponShield(6, 12, 0, 0, True, StartingClassWeaponShield.POOL.RIGHT_HAND),
 200000: StartingClassWeaponShield(8, 10, 0, 0, True, StartingClassWeaponShield.POOL.RIGHT_HAND),
 201000: StartingClassWeaponShield(10, 10, 0, 0, True, StartingClassWeaponShield.POOL.RIGHT_HAND),
 202000: StartingClassWeaponShield(10, 10, 0, 0, True, StartingClassWeaponShield.POOL.RIGHT_HAND),
 203000: StartingClassWeaponShield(8, 8, 0, 0, True, StartingClassWeaponShield.POOL.LEFT_ONLY_EXPANDED),
 204000: StartingClassWeaponShield(10, 14, 0, 0, True, StartingClassWeaponShield.POOL.RIGHT_HAND),
 205000: StartingClassWeaponShield(16, 10, 0, 0, True, StartingClassWeaponShield.POOL.RIGHT_HAND),
 206000: StartingClassWeaponShield(12, 12, 0, 0, True, StartingClassWeaponShield.POOL.RIGHT_HAND),
 207000: StartingClassWeaponShield(10, 10, 0, 0, True, StartingClassWeaponShield.POOL.RIGHT_HAND),
 211000: StartingClassWeaponShield(16, 10, 0, 0, True, StartingClassWeaponShield.POOL.RIGHT_HAND),
 212000: StartingClassWeaponShield(6, 6, 0, 0, True, StartingClassWeaponShield.POOL.LEFT_ONLY_EXPANDED),
 300000: StartingClassWeaponShield(16, 10, 0, 0, True, StartingClassWeaponShield.POOL.RIGHT_HAND),
 301000: StartingClassWeaponShield(16, 10, 0, 0, True, StartingClassWeaponShield.POOL.RIGHT_HAND),
 303000: StartingClassWeaponShield(16, 14, 0, 0, True, StartingClassWeaponShield.POOL.RIGHT_HAND),
 400000: StartingClassWeaponShield(7, 13, 0, 0, True, StartingClassWeaponShield.POOL.RIGHT_HAND),
 401000: StartingClassWeaponShield(9, 13, 0, 0, True, StartingClassWeaponShield.POOL.RIGHT_HAND),
 402000: StartingClassWeaponShield(9, 14, 0, 0, True, StartingClassWeaponShield.POOL.RIGHT_HAND),
 403000: StartingClassWeaponShield(7, 0, 0, 0, True, StartingClassWeaponShield.POOL.RIGHT_HAND),
 406000: StartingClassWeaponShield(11, 13, 0, 0, True, StartingClassWeaponShield.POOL.RIGHT_HAND),
 500000: StartingClassWeaponShield(14, 14, 0, 0, True, StartingClassWeaponShield.POOL.RIGHT_HAND),
 600000: StartingClassWeaponShield(5, 12, 0, 0, True, StartingClassWeaponShield.POOL.RIGHT_HAND),
 601000: StartingClassWeaponShield(7, 12, 0, 0, True, StartingClassWeaponShield.POOL.RIGHT_HAND),
 602000: StartingClassWeaponShield(10, 12, 0, 0, True, StartingClassWeaponShield.POOL.RIGHT_HAND),
 700000: StartingClassWeaponShield(8, 8, 0, 0, True, StartingClassWeaponShield.POOL.RIGHT_HAND),
 701000: StartingClassWeaponShield(12, 8, 0, 0, True, StartingClassWeaponShield.POOL.RIGHT_HAND),
 705000: StartingClassWeaponShield(14, 14, 0, 0, True, StartingClassWeaponShield.POOL.RIGHT_HAND),
 800000: StartingClassWeaponShield(10, 0, 0, 0, True, StartingClassWeaponShield.POOL.RIGHT_HAND),
 801000: StartingClassWeaponShield(12, 0, 0, 0, True, StartingClassWeaponShield.POOL.RIGHT_HAND),
 802000: StartingClassWeaponShield(11, 0, 0, 0, True, StartingClassWeaponShield.POOL.RIGHT_HAND),
 803000: StartingClassWeaponShield(11, 10, 0, 0, True, StartingClassWeaponShield.POOL.RIGHT_HAND),
 804000: StartingClassWeaponShield(14, 0, 0, 0, True, StartingClassWeaponShield.POOL.RIGHT_HAND),
 809000: StartingClassWeaponShield(12, 0, 0, 0, True, StartingClassWeaponShield.POOL.RIGHT_HAND),
 810000: StartingClassWeaponShield(14, 0, 0, 0, True, StartingClassWeaponShield.POOL.RIGHT_HAND),
 811000: StartingClassWeaponShield(16, 0, 0, 0, True, StartingClassWeaponShield.POOL.RIGHT_HAND),
 812000: StartingClassWeaponShield(14, 0, 0, 0, True, StartingClassWeaponShield.POOL.RIGHT_HAND),
 901000: StartingClassWeaponShield(5, 8, 0, 0, False, StartingClassWeaponShield.POOL.RIGHT_HAND),
 902000: StartingClassWeaponShield(6, 14, 0, 0, False, StartingClassWeaponShield.POOL.RIGHT_HAND),
 904000: StartingClassWeaponShield(0, 0, 0, 0, False, StartingClassWeaponShield.POOL.BOTH),
 1000000: StartingClassWeaponShield(11, 10, 0, 0, True, StartingClassWeaponShield.POOL.RIGHT_HAND),
 1001000: StartingClassWeaponShield(13, 15, 0, 0, True, StartingClassWeaponShield.POOL.RIGHT_HAND),
 1002000: StartingClassWeaponShield(13, 12, 0, 0, True, StartingClassWeaponShield.POOL.RIGHT_HAND),
 1003000: StartingClassWeaponShield(12, 10, 0, 0, True, StartingClassWeaponShield.POOL.RIGHT_HAND),
 1052000: StartingClassWeaponShield(12, 0, 14, 0, True, StartingClassWeaponShield.POOL.RIGHT_HAND),
 1100000: StartingClassWeaponShield(16, 12, 0, 0, True, StartingClassWeaponShield.POOL.RIGHT_HAND),
 1102000: StartingClassWeaponShield(16, 14, 0, 0, True, StartingClassWeaponShield.POOL.RIGHT_HAND),
 1103000: StartingClassWeaponShield(16, 12, 0, 0, True, StartingClassWeaponShield.POOL.RIGHT_HAND),
 1106000: StartingClassWeaponShield(15, 12, 0, 0, True, StartingClassWeaponShield.POOL.RIGHT_HAND),
 1107000: StartingClassWeaponShield(14, 12, 0, 0, True, StartingClassWeaponShield.POOL.RIGHT_HAND),
 1150000: StartingClassWeaponShield(14, 14, 0, 0, True, StartingClassWeaponShield.POOL.RIGHT_HAND),
 1151000: StartingClassWeaponShield(16, 14, 0, 0, True, StartingClassWeaponShield.POOL.RIGHT_HAND),
 1600000: StartingClassWeaponShield(7, 14, 0, 0, True, StartingClassWeaponShield.POOL.RIGHT_HAND),
 1396000: StartingClassWeaponShield(5, 0, 0, 0, False, StartingClassWeaponShield.POOL.LEFT_HAND),
 1400000: StartingClassWeaponShield(6, 0, 0, 0, False, StartingClassWeaponShield.POOL.LEFT_HAND),
 1401000: StartingClassWeaponShield(7, 0, 0, 0, False, StartingClassWeaponShield.POOL.LEFT_HAND),
 1402000: StartingClassWeaponShield(7, 0, 0, 0, False, StartingClassWeaponShield.POOL.LEFT_HAND),
 1403000: StartingClassWeaponShield(5, 0, 0, 0, False, StartingClassWeaponShield.POOL.LEFT_HAND),
 1404000: StartingClassWeaponShield(8, 11, 0, 0, False, StartingClassWeaponShield.POOL.LEFT_HAND),
 1405000: StartingClassWeaponShield(7, 13, 0, 0, False, StartingClassWeaponShield.POOL.LEFT_HAND),
 1406000: StartingClassWeaponShield(6, 0, 0, 0, False, StartingClassWeaponShield.POOL.LEFT_HAND),
 1408000: StartingClassWeaponShield(6, 0, 0, 0, False, StartingClassWeaponShield.POOL.LEFT_HAND),
 1409000: StartingClassWeaponShield(7, 0, 0, 0, False, StartingClassWeaponShield.POOL.LEFT_HAND),
 1410000: StartingClassWeaponShield(6, 0, 0, 0, False, StartingClassWeaponShield.POOL.LEFT_HAND),
 1411000: StartingClassWeaponShield(10, 0, 0, 0, False, StartingClassWeaponShield.POOL.LEFT_HAND),
 1450000: StartingClassWeaponShield(8, 0, 0, 0, False, StartingClassWeaponShield.POOL.LEFT_HAND),
 1451000: StartingClassWeaponShield(10, 0, 0, 0, False, StartingClassWeaponShield.POOL.LEFT_HAND),
 1452000: StartingClassWeaponShield(10, 0, 0, 0, False, StartingClassWeaponShield.POOL.LEFT_HAND),
 1453000: StartingClassWeaponShield(10, 0, 0, 0, False, StartingClassWeaponShield.POOL.LEFT_HAND),
 1454000: StartingClassWeaponShield(11, 0, 0, 0, False, StartingClassWeaponShield.POOL.LEFT_HAND),
 1455000: StartingClassWeaponShield(12, 0, 0, 0, False, StartingClassWeaponShield.POOL.LEFT_HAND),
 1456000: StartingClassWeaponShield(10, 0, 0, 0, False, StartingClassWeaponShield.POOL.LEFT_HAND),
 1457000: StartingClassWeaponShield(10, 0, 0, 0, False, StartingClassWeaponShield.POOL.LEFT_HAND),
 1460000: StartingClassWeaponShield(6, 0, 0, 0, False, StartingClassWeaponShield.POOL.LEFT_HAND),
 1461000: StartingClassWeaponShield(14, 0, 0, 0, False, StartingClassWeaponShield.POOL.LEFT_HAND),
 1462000: StartingClassWeaponShield(10, 0, 0, 0, False, StartingClassWeaponShield.POOL.LEFT_HAND),
 1470000: StartingClassWeaponShield(10, 12, 0, 0, False, StartingClassWeaponShield.POOL.LEFT_HAND),
 1471000: StartingClassWeaponShield(14, 0, 0, 0, False, StartingClassWeaponShield.POOL.LEFT_HAND),
 1472000: StartingClassWeaponShield(12, 0, 0, 0, False, StartingClassWeaponShield.POOL.LEFT_HAND),
 1473000: StartingClassWeaponShield(14, 0, 0, 0, False, StartingClassWeaponShield.POOL.LEFT_HAND),
 1475000: StartingClassWeaponShield(11, 14, 0, 0, False, StartingClassWeaponShield.POOL.LEFT_HAND),
 1476000: StartingClassWeaponShield(6, 0, 0, 0, False, StartingClassWeaponShield.POOL.LEFT_HAND),
 1477000: StartingClassWeaponShield(10, 0, 0, 0, False, StartingClassWeaponShield.POOL.LEFT_HAND),
 1478000: StartingClassWeaponShield(12, 0, 0, 0, False, StartingClassWeaponShield.POOL.LEFT_HAND),
 9002000: StartingClassWeaponShield(10, 0, 0, 0, False, StartingClassWeaponShield.POOL.LEFT_HAND),
 9016000: StartingClassWeaponShield(15, 12, 0, 0, True, StartingClassWeaponShield.POOL.RIGHT_HAND),
 9019000: StartingClassWeaponShield(15, 10, 0, 0, True, StartingClassWeaponShield.POOL.RIGHT_HAND),
}


CLASS_TO_CHR_INIT = {
 "warrior":    (3000, 2000),
 "knight":     (3001, 2001),
 "wanderer":   (3002, 2002),
 "thief":      (3003, 2003),
 "bandit":     (3004, 2004),
 "hunter":     (3005, 2005),
 "sorcerer":   (3006, 2006),
 "pyromancer": (3007, 2007),
 "cleric":     (3008, 2008),
 "deprived":   (3009, 2009)
}

class StartingClassData:
    class CHR_INIT(Enum):
        WEP_R1  = 0
        WEP_R2  = 1
        WEP_L1  = 2
        WEP_L2  = 3
        ARROW_1 = 4
        SPELL_1 = 5
        ITEM_1  = 6
        
    CHR_INIT_FIELD = {
        CHR_INIT.WEP_R1: ("wep_r1", "right_hand"),
        CHR_INIT.WEP_R2: ("wep_r2", "extra"),
        CHR_INIT.WEP_L1: ("wep_l1", "left_hand"),
        CHR_INIT.WEP_L2: ("wep_l2", "extra"),
        CHR_INIT.ARROW_1: ("arrow_1", "extra"),
        CHR_INIT.SPELL_1: ("spell_1", "extra"),
        CHR_INIT.ITEM_1: ("item_1", "extra")
    }
        
    def __init__(self, class_name, item_type, item, chr_init_fields, item_quantity = 1, should_pass_to_items = True):
        self.class_name = class_name
        self.item_type = item_type
        self.item = item
        self.chr_init_fields = chr_init_fields
        self.item_quantity = item_quantity
        self.should_pass_to_items = should_pass_to_items

EXTRA_DATA = [
 StartingClassData("hunter", item_s.ITEM_TYPE.WEAPON, 1200000, [StartingClassData.CHR_INIT.WEP_R2]),
 StartingClassData("hunter", item_s.ITEM_TYPE.WEAPON, 1201000, [StartingClassData.CHR_INIT.WEP_R2]),
 StartingClassData("hunter", item_s.ITEM_TYPE.WEAPON, 1204000, [StartingClassData.CHR_INIT.WEP_R2]),
 StartingClassData("hunter", item_s.ITEM_TYPE.WEAPON, 2000000, [StartingClassData.CHR_INIT.ARROW_1], 30),
 StartingClassData("hunter", item_s.ITEM_TYPE.WEAPON, 2001000, [StartingClassData.CHR_INIT.ARROW_1], 30),
 StartingClassData("hunter", item_s.ITEM_TYPE.WEAPON, 2002000, [StartingClassData.CHR_INIT.ARROW_1], 30),
 StartingClassData("hunter", item_s.ITEM_TYPE.WEAPON, 2003000, [StartingClassData.CHR_INIT.ARROW_1], 30),
 StartingClassData("hunter", item_s.ITEM_TYPE.WEAPON, 2004000, [StartingClassData.CHR_INIT.ARROW_1], 30),
 StartingClassData("hunter", item_s.ITEM_TYPE.WEAPON, 2005000, [StartingClassData.CHR_INIT.ARROW_1], 30),
 StartingClassData("hunter", item_s.ITEM_TYPE.WEAPON, 2006000, [StartingClassData.CHR_INIT.ARROW_1], 30),
 StartingClassData("sorcerer", item_s.ITEM_TYPE.WEAPON, 1300000, [StartingClassData.CHR_INIT.WEP_R2]),
 StartingClassData("sorcerer", item_s.ITEM_TYPE.WEAPON, 1301000, [StartingClassData.CHR_INIT.WEP_R2]),
 StartingClassData("sorcerer", item_s.ITEM_TYPE.WEAPON, 1305000, [StartingClassData.CHR_INIT.WEP_R2]),
 StartingClassData("sorcerer", item_s.ITEM_TYPE.WEAPON, 1308000, [StartingClassData.CHR_INIT.WEP_R2]),
 StartingClassData("sorcerer", item_s.ITEM_TYPE.WEAPON, 9018000, [StartingClassData.CHR_INIT.WEP_R2]),
 StartingClassData("sorcerer", item_s.ITEM_TYPE.ITEM, 3000, [StartingClassData.CHR_INIT.SPELL_1, StartingClassData.CHR_INIT.ITEM_1], should_pass_to_items = False),
 StartingClassData("sorcerer", item_s.ITEM_TYPE.ITEM, 3010, [StartingClassData.CHR_INIT.SPELL_1, StartingClassData.CHR_INIT.ITEM_1], should_pass_to_items = False),
 StartingClassData("sorcerer", item_s.ITEM_TYPE.ITEM, 3020, [StartingClassData.CHR_INIT.SPELL_1, StartingClassData.CHR_INIT.ITEM_1], should_pass_to_items = False),
 StartingClassData("sorcerer", item_s.ITEM_TYPE.ITEM, 3100, [StartingClassData.CHR_INIT.SPELL_1, StartingClassData.CHR_INIT.ITEM_1], should_pass_to_items = False),
 StartingClassData("sorcerer", item_s.ITEM_TYPE.ITEM, 3300, [StartingClassData.CHR_INIT.SPELL_1, StartingClassData.CHR_INIT.ITEM_1], should_pass_to_items = False),
 StartingClassData("sorcerer", item_s.ITEM_TYPE.ITEM, 3400, [StartingClassData.CHR_INIT.SPELL_1, StartingClassData.CHR_INIT.ITEM_1], should_pass_to_items = False),
 StartingClassData("sorcerer", item_s.ITEM_TYPE.ITEM, 3410, [StartingClassData.CHR_INIT.SPELL_1, StartingClassData.CHR_INIT.ITEM_1], should_pass_to_items = False),
 StartingClassData("sorcerer", item_s.ITEM_TYPE.ITEM, 3500, [StartingClassData.CHR_INIT.SPELL_1, StartingClassData.CHR_INIT.ITEM_1], should_pass_to_items = False),
 StartingClassData("sorcerer", item_s.ITEM_TYPE.ITEM, 3510, [StartingClassData.CHR_INIT.SPELL_1, StartingClassData.CHR_INIT.ITEM_1], should_pass_to_items = False),
 StartingClassData("sorcerer", item_s.ITEM_TYPE.ITEM, 3520, [StartingClassData.CHR_INIT.SPELL_1, StartingClassData.CHR_INIT.ITEM_1], should_pass_to_items = False),
 StartingClassData("sorcerer", item_s.ITEM_TYPE.ITEM, 3530, [StartingClassData.CHR_INIT.SPELL_1, StartingClassData.CHR_INIT.ITEM_1], should_pass_to_items = False),
 StartingClassData("sorcerer", item_s.ITEM_TYPE.ITEM, 3540, [StartingClassData.CHR_INIT.SPELL_1, StartingClassData.CHR_INIT.ITEM_1], should_pass_to_items = False),
 StartingClassData("sorcerer", item_s.ITEM_TYPE.ITEM, 3550, [StartingClassData.CHR_INIT.SPELL_1, StartingClassData.CHR_INIT.ITEM_1], should_pass_to_items = False),
 StartingClassData("pyromancer", item_s.ITEM_TYPE.WEAPON, 1330000, [StartingClassData.CHR_INIT.WEP_R2]),
 StartingClassData("pyromancer", item_s.ITEM_TYPE.WEAPON, 1330100, [StartingClassData.CHR_INIT.WEP_R2]),
 StartingClassData("pyromancer", item_s.ITEM_TYPE.WEAPON, 1330200, [StartingClassData.CHR_INIT.WEP_R2]),
 StartingClassData("pyromancer", item_s.ITEM_TYPE.ITEM, 4000, [StartingClassData.CHR_INIT.SPELL_1, StartingClassData.CHR_INIT.ITEM_1], should_pass_to_items = False),
 StartingClassData("pyromancer", item_s.ITEM_TYPE.ITEM, 4010, [StartingClassData.CHR_INIT.SPELL_1, StartingClassData.CHR_INIT.ITEM_1], should_pass_to_items = False),
 StartingClassData("pyromancer", item_s.ITEM_TYPE.ITEM, 4100, [StartingClassData.CHR_INIT.SPELL_1, StartingClassData.CHR_INIT.ITEM_1], should_pass_to_items = False),
 StartingClassData("pyromancer", item_s.ITEM_TYPE.ITEM, 4200, [StartingClassData.CHR_INIT.SPELL_1, StartingClassData.CHR_INIT.ITEM_1], should_pass_to_items = False),
 StartingClassData("pyromancer", item_s.ITEM_TYPE.ITEM, 4210, [StartingClassData.CHR_INIT.SPELL_1, StartingClassData.CHR_INIT.ITEM_1], should_pass_to_items = False),
 StartingClassData("pyromancer", item_s.ITEM_TYPE.ITEM, 4300, [StartingClassData.CHR_INIT.SPELL_1, StartingClassData.CHR_INIT.ITEM_1], should_pass_to_items = False),
 StartingClassData("pyromancer", item_s.ITEM_TYPE.ITEM, 4310, [StartingClassData.CHR_INIT.SPELL_1, StartingClassData.CHR_INIT.ITEM_1], should_pass_to_items = False),
 StartingClassData("pyromancer", item_s.ITEM_TYPE.ITEM, 4360, [StartingClassData.CHR_INIT.SPELL_1, StartingClassData.CHR_INIT.ITEM_1], should_pass_to_items = False),
 StartingClassData("pyromancer", item_s.ITEM_TYPE.ITEM, 4400, [StartingClassData.CHR_INIT.SPELL_1, StartingClassData.CHR_INIT.ITEM_1], should_pass_to_items = False),
 StartingClassData("cleric", item_s.ITEM_TYPE.WEAPON, 1360000, [StartingClassData.CHR_INIT.WEP_R2]),
 StartingClassData("cleric", item_s.ITEM_TYPE.WEAPON, 1361000, [StartingClassData.CHR_INIT.WEP_R2]),
 StartingClassData("cleric", item_s.ITEM_TYPE.WEAPON, 1362000, [StartingClassData.CHR_INIT.WEP_R2]),
 StartingClassData("cleric", item_s.ITEM_TYPE.WEAPON, 1365000, [StartingClassData.CHR_INIT.WEP_R2]),
 StartingClassData("cleric", item_s.ITEM_TYPE.ITEM, 5000, [StartingClassData.CHR_INIT.SPELL_1, StartingClassData.CHR_INIT.ITEM_1], should_pass_to_items = False),
 StartingClassData("cleric", item_s.ITEM_TYPE.ITEM, 5020, [StartingClassData.CHR_INIT.SPELL_1, StartingClassData.CHR_INIT.ITEM_1], should_pass_to_items = False),
 StartingClassData("cleric", item_s.ITEM_TYPE.ITEM, 5300, [StartingClassData.CHR_INIT.SPELL_1, StartingClassData.CHR_INIT.ITEM_1], should_pass_to_items = False),
 StartingClassData("cleric", item_s.ITEM_TYPE.ITEM, 5400, [StartingClassData.CHR_INIT.SPELL_1, StartingClassData.CHR_INIT.ITEM_1], should_pass_to_items = False),
 StartingClassData("cleric", item_s.ITEM_TYPE.ITEM, 5600, [StartingClassData.CHR_INIT.SPELL_1, StartingClassData.CHR_INIT.ITEM_1], should_pass_to_items = False)
]

def create_starting_class_weapon_data(chr_init_param, rand_options):
    return_list = []
    
    is_two_handing = (rand_options.start_items_diff in [rng_opt.RandOptStartItemsDifficulty.SHIELD_AND_2H, rng_opt.RandOptStartItemsDifficulty.COMBINED_POOL_AND_2H])
    use_expanded_offhand = (rand_options.start_items_diff == rng_opt.RandOptStartItemsDifficulty.COMBINED_POOL_AND_2H)
    
    for class_name in CLASS_TO_CHR_INIT:
        (_, start_class_init_id) = CLASS_TO_CHR_INIT[class_name]
        start_class_init = chr_init_param.find_chr_by_id(start_class_init_id)
        for wep_shield_id in STARTING_WEAPONS_AND_SHIELDS:
            wep_shield = STARTING_WEAPONS_AND_SHIELDS[wep_shield_id]
            if wep_shield.can_be_used(start_class_init.base_str, 
             start_class_init.base_dex, start_class_init.base_int,
             start_class_init.base_fth, is_two_handing, False, False):
                return_list.append(StartingClassData(class_name, item_s.ITEM_TYPE.WEAPON, wep_shield_id, [StartingClassData.CHR_INIT.WEP_R1]))
            if wep_shield.can_be_used(start_class_init.base_str, 
             start_class_init.base_dex, start_class_init.base_int,
             start_class_init.base_fth, False, True, use_expanded_offhand):
                return_list.append(StartingClassData(class_name, item_s.ITEM_TYPE.WEAPON, wep_shield_id, [StartingClassData.CHR_INIT.WEP_L1]))
    return return_list

def randomize_starting_chr_weapons(chr_init_param, rand_options, random_source):
    starting_class_weapon_data = create_starting_class_weapon_data(chr_init_param, rand_options)
    joined_data = starting_class_weapon_data + EXTRA_DATA
    
    data_passed_to_items = {}
    for class_name in CLASS_TO_CHR_INIT:
        data_passed_to_items[class_name] = {}
        (display_class_init_id, start_class_init_id) = CLASS_TO_CHR_INIT[class_name]
        display_class_init = chr_init_param.find_chr_by_id(display_class_init_id)
        start_class_init = chr_init_param.find_chr_by_id(start_class_init_id)
        
        used_set = set([])
        for field in StartingClassData.CHR_INIT:
            if field in used_set:
                continue
            else:
                choice_list = [d for d in joined_data if 
                 (d.class_name == class_name) and
                 (field in d.chr_init_fields)]
                if len(choice_list) == 0:
                    continue
                else:
                    choice = random_source.choice(choice_list)
                    for linked_field in choice.chr_init_fields:
                        # TODO: Quantity is not correctly set in the chr_init.
                        (chr_init_field_to_use, data_passed_field) = StartingClassData.CHR_INIT_FIELD[linked_field]
                        setattr(display_class_init, chr_init_field_to_use, choice.item)
                        if choice.should_pass_to_items:
                            item_to_pass = item_s.ItemLotPart(item_s.ITEM_DIF.EASY, 4, 
                             [item_s.ItemLotEntry(choice.item_type, choice.item, count = choice.item_quantity)])
                            if data_passed_field in data_passed_to_items[class_name]:
                                data_passed_to_items[class_name][data_passed_field].append(item_to_pass)
                            else:
                                data_passed_to_items[class_name][data_passed_field] = [item_to_pass]
                        else:
                            setattr(start_class_init, chr_init_field_to_use, choice.item)
                        used_set.add(linked_field)
    return data_passed_to_items
    
    
if __name__ == "__main__":
    # Build vanilla ChrItemParam
    chr_inits = [VANILLA_CHRS[chr_id].to_chr_init(chr_id , "") for chr_id in VANILLA_CHRS]
    vanilla_cip = cip.ChrInitParam(chr_inits)

    # Set up randomizer options and randomize armor in table.
    rand_options = rng_opt.RandomizerOptions(
     rng_opt.RandOptDifficulty.EASY, 
     False, 
     rng_opt.RandOptKeyDifficulty.SPEEDRUN_MODE, 
     True, 
     True,
     rng_opt.RandOptSoulItemsDifficulty.SHUFFLE,
     rng_opt.RandOptStartItemsDifficulty.SHIELD_AND_1H,
     rng_opt.RandOptGameVersion.PTDE,
     False)
     
    random_source = random.Random()
    randomize_chr_armor(vanilla_cip, rand_options, random_source)
    passed_data = randomize_starting_chr_weapons(vanilla_cip, rand_options, random_source)
    # Print results.
    for chr_init in vanilla_cip.chr_inits:
        print(chr_init.to_string())
    passed_data_as_string = "\n\n["
    for class_name in passed_data:
        passed_data_as_string += class_name + ": ["
        class_data = passed_data[class_name]
        for data_type in class_data:
            passed_data_as_string += data_type + ": "
            passed_data_of_type = class_data[data_type]
            for item_lot_part in passed_data_of_type:
                passed_data_as_string += "[" + ", ".join([str(e.item_id) for e in item_lot_part.items]) + "] "
        passed_data_as_string += "] "
    print(passed_data_as_string)
            

