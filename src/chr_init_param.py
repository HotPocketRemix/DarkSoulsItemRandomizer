import struct
import sys

def extract_shift_jisz(content, offset):
    extracted = b''
    while content[offset:offset+1] != b'\x00':
        extracted = extracted + content[offset:offset+1]
        offset += 1
    return extracted.decode('shift-jis')


class ChrInit:
    STRUCT_FORMAT = ("<3fi4i4i4i5i3i7i10i2i3h4h3hh10b10b5b7b4b10x")

    def __init__(self, chr_init_id, base_rec_mp, base_rec_sp, red_falldam, soul, wep_r1, wep_r2, 
         wep_l1, wep_l2, armor_head, armor_chest, armor_hand, armor_leg,
         arrow_1, bolt_1, arrow_2, bolt_2, 
         ring_1, ring_2, ring_3, ring_4, ring_5,
         skill_1, skill_2, skill_3,
         spell_1, spell_2, spell_3, spell_4, spell_5, spell_6, spell_7,
         item_1, item_2, item_3, item_4, item_5, item_6, item_7, item_8, item_9, item_10,
         facegen_id, think_id, base_hp, base_mp, base_sp, 
         arrow_1_num, bolt_1_num, arrow_2_num, bolt_2_num, 
         qwc_sb, qwc_mw, qwc_cd, soul_level, 
         base_vit, base_att, base_end, base_str, base_dex, base_int, base_fth, 
         base_luc, base_hum, base_res,
         item_1_num, item_2_num, item_3_num, item_4_num, item_5_num,
         item_6_num, item_7_num, item_8_num, item_9_num, item_10_num,
         body_scale_head, body_scale_chest, body_scale_ab, body_scale_arm, body_scale_leg, 
         gest_0, gest_1, gest_2, gest_3, gest_4, gest_5, gest_6, 
         npc_type, draw_type, sex, covenant, description):
            self.chr_init_id = chr_init_id
            self.base_rec_mp = base_rec_mp
            self.base_rec_sp = base_rec_sp
            self.red_falldam = red_falldam
            self.soul = soul
            self.wep_r1 = wep_r1
            self.wep_r2 = wep_r2
            self.wep_l1 = wep_l1
            self.wep_l2 = wep_l2
            self.armor_head = armor_head
            self.armor_chest = armor_chest
            self.armor_hand = armor_hand
            self.armor_leg = armor_leg
            self.arrow_1 = arrow_1
            self.bolt_1 = bolt_1
            self.arrow_2 = arrow_2
            self.bolt_2 = bolt_2
            self.ring_1 = ring_1
            self.ring_2 = ring_2
            self.ring_3 = ring_3
            self.ring_4 = ring_4
            self.ring_5 = ring_5
            self.skill_1 = skill_1
            self.skill_2 = skill_2
            self.skill_3 = skill_3
            self.spell_1 = spell_1
            self.spell_2 = spell_2
            self.spell_3 = spell_3
            self.spell_4 = spell_4
            self.spell_5 = spell_5
            self.spell_6 = spell_6
            self.spell_7 = spell_7
            self.item_1 = item_1
            self.item_2 = item_2
            self.item_3 = item_3
            self.item_4 = item_4
            self.item_5 = item_5
            self.item_6 = item_6
            self.item_7 = item_7
            self.item_8 = item_8
            self.item_9 = item_9
            self.item_10 = item_10
            self.facegen_id = facegen_id
            self.think_id = think_id
            self.base_hp = base_hp
            self.base_mp = base_mp
            self.base_sp = base_sp
            self.arrow_1_num = arrow_1_num
            self.bolt_1_num = bolt_1_num
            self.arrow_2_num = arrow_2_num
            self.bolt_2_num = bolt_2_num
            self.qwc_sb = qwc_sb
            self.qwc_mw = qwc_mw
            self.qwc_cd = qwc_cd
            self.soul_level = soul_level
            self.base_vit = base_vit
            self.base_att = base_att
            self.base_end = base_end
            self.base_str = base_str
            self.base_dex = base_dex
            self.base_int = base_int
            self.base_fth = base_fth
            self.base_luc = base_luc
            self.base_hum = base_hum
            self.base_res = base_res
            self.item_1_num = item_1_num
            self.item_2_num = item_2_num
            self.item_3_num = item_3_num
            self.item_4_num = item_4_num
            self.item_5_num = item_5_num
            self.item_6_num = item_6_num
            self.item_7_num = item_7_num
            self.item_8_num = item_8_num
            self.item_9_num = item_9_num
            self.item_10_num = item_10_num
            self.body_scale_head = body_scale_head
            self.body_scale_chest = body_scale_chest
            self.body_scale_ab = body_scale_ab
            self.body_scale_arm = body_scale_arm
            self.body_scale_leg = body_scale_leg
            self.gest_0 = gest_0
            self.gest_1 = gest_1
            self.gest_2 = gest_2
            self.gest_3 = gest_3
            self.gest_4 = gest_4
            self.gest_5 = gest_5
            self.gest_6 = gest_6
            self.npc_type = npc_type
            self.draw_type = draw_type
            self.sex = sex
            self.covenant = covenant
            self.description = description
    
    @classmethod
    def from_binary(cls, chr_init_id, data, description):
        return cls(chr_init_id, *struct.unpack_from(cls.STRUCT_FORMAT, 
            data, offset=0), description)
        
    def to_binary(self):
        arg_list = [self.base_rec_mp, self.base_rec_sp, self.red_falldam, 
         self.soul, self.wep_r1, self.wep_r2, self.wep_l1, self.wep_l2, 
         self.armor_head, self.armor_chest, self.armor_hand, self.armor_leg, 
         self.arrow_1, self.bolt_1, self.arrow_2, self.bolt_2, 
         self.ring_1, self.ring_2, self.ring_3, self.ring_4, self.ring_5, 
         self.skill_1, self.skill_2, self.skill_3, self.spell_1, self.spell_2, 
         self.spell_3, self.spell_4, self.spell_5, self.spell_6, self.spell_7, 
         self.item_1, self.item_2, self.item_3, self.item_4, self.item_5, 
         self.item_6, self.item_7, self.item_8, self.item_9, self.item_10, 
         self.facegen_id, self.think_id, self.base_hp, self.base_mp, self.base_sp, 
         self.arrow_1_num, self.bolt_1_num, self.arrow_2_num, self.bolt_2_num, 
         self.qwc_sb, self.qwc_mw, self.qwc_cd, self.soul_level, 
         self.base_vit, self.base_att, self.base_end, self.base_str, 
         self.base_dex, self.base_int, self.base_fth, self.base_luc,
         self.base_hum, self.base_res, 
         self.item_1_num, self.item_2_num, self.item_3_num, self.item_4_num, 
         self.item_5_num, self.item_6_num, self.item_7_num, self.item_8_num, 
         self.item_9_num, self.item_10_num, 
         self.body_scale_head, self.body_scale_chest, self.body_scale_ab, 
         self.body_scale_arm, self.body_scale_leg, 
         self.gest_0, self.gest_1, self.gest_2, self.gest_3, 
         self.gest_4, self.gest_5, self.gest_6, 
         self.npc_type, self.draw_type, self.sex, self.covenant]
        data = struct.pack(self.STRUCT_FORMAT, *arg_list)
        return (self.chr_init_id, data, self.description)
        
    def to_string(self):
        arg_list = [self.chr_init_id, self.description, self.base_rec_mp, 
         self.base_rec_sp, self.red_falldam, 
         self.soul, self.wep_r1, self.wep_r2, self.wep_l1, self.wep_l2, 
         self.armor_head, self.armor_chest, self.armor_hand, self.armor_leg, 
         self.arrow_1, self.bolt_1, self.arrow_2, self.bolt_2, 
         self.ring_1, self.ring_2, self.ring_3, self.ring_4, self.ring_5, 
         self.skill_1, self.skill_2, self.skill_3, self.spell_1, self.spell_2, 
         self.spell_3, self.spell_4, self.spell_5, self.spell_6, self.spell_7, 
         self.item_1, self.item_2, self.item_3, self.item_4, self.item_5, 
         self.item_6, self.item_7, self.item_8, self.item_9, self.item_10, 
         self.facegen_id, self.think_id, self.base_hp, self.base_mp, self.base_sp, 
         self.arrow_1_num, self.bolt_1_num, self.arrow_2_num, self.bolt_2_num, 
         self.qwc_sb, self.qwc_mw, self.qwc_cd, self.soul_level, 
         self.base_vit, self.base_att, self.base_end, self.base_str, 
         self.base_dex, self.base_int, self.base_fth, self.base_luc,
         self.base_hum, self.base_res, 
         self.item_1_num, self.item_2_num, self.item_3_num, self.item_4_num, 
         self.item_5_num, self.item_6_num, self.item_7_num, self.item_8_num, 
         self.item_9_num, self.item_10_num, 
         self.body_scale_head, self.body_scale_chest, self.body_scale_ab, 
         self.body_scale_arm, self.body_scale_leg, 
         self.gest_0, self.gest_1, self.gest_2, self.gest_3, 
         self.gest_4, self.gest_5, self.gest_6, 
         self.npc_type, self.draw_type, self.sex, self.covenant]
        return ("%d %s " + "%d " * 90) % tuple(arg_list)

class ChrInitParam:
    RECORD_SIZE = 0xC
    DATA_RECORD_SIZE = 0xF0 
    
    def __init__(self, chr_inits = None):
        if chr_inits == None:
            chr_inits = []
        self.chr_inits = chr_inits
    
    @classmethod
    def load_from_file_content(cls, file_content):
        master_offset = 0
        
        (strings_offset, data_offset, unk, chr_init_count) = struct.unpack_from("<IIHH", file_content, offset=master_offset)
        master_offset = 0x30  # Skip the rest of the header.
        
        chr_inits = []
        for i in range(chr_init_count):
            (chr_init_id, chr_init_data_offset, chr_init_string_offset) = struct.unpack_from("<III", file_content, offset=master_offset)
            master_offset += struct.calcsize("<III")
            
            description = extract_shift_jisz(file_content, chr_init_string_offset)
            chr_init_data = file_content[chr_init_data_offset:chr_init_data_offset + cls.DATA_RECORD_SIZE]
            chr_inits.append(ChrInit.from_binary(chr_init_id, chr_init_data, description))
        return ChrInitParam(chr_inits)
        
    def find_chr_by_id(self, chr_id):
        for chr_init in self.chr_inits:
            if chr_init.chr_init_id == chr_id:
                return chr_init
        return None
        
    def export_as_binary(self):
        num_of_records = len(self.chr_inits)
        records_offset = 0x30
        data_offset = records_offset + num_of_records * self.RECORD_SIZE
        strings_offset = data_offset + num_of_records * self.DATA_RECORD_SIZE
        header = struct.pack("@IIHH", strings_offset, data_offset, 1, num_of_records) 
        header += b"CHARACTER_INIT_PARAM" + b"\x00" + b"\x20" * 11 + b"\x00\x02\x00\x00"
        packed_record = b""
        packed_data = b""
        packed_strings = b""
        current_data_offset = data_offset
        current_strings_offset = strings_offset
        for chr_init in sorted(self.chr_inits, key = lambda c: c.chr_init_id):
            (chr_init_id, data, description) = chr_init.to_binary()
            encoded_description = description.encode('shift-jis') + b"\x00"
            packed_record += struct.pack("@III", chr_init_id, current_data_offset, current_strings_offset)
            packed_data += data
            packed_strings += encoded_description
            current_data_offset += len(data)
            current_strings_offset += len(encoded_description)
        return header + packed_record + packed_data + packed_strings
        
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("No filename specified.")
        sys.exit(0)
        
    with open(sys.argv[1], 'rb') as f:
        file_content = f.read()
        
        data = ChrInitParam.load_from_file_content(file_content)
        for chr_init in data.chr_inits:
            print(chr_init.to_string())
