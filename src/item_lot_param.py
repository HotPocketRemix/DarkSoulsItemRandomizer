import struct
import sys

def consume_byte(content, offset, byte, length=1):
    for i in range(length-1):
        if content[offset + i:offset + i+1] != byte:
            raise ValueError(("Expected byte '0x%s' at offset " + 
             "0x%x but received byte '0x%s'.") % (byte.hex(), offset+i, 
             content[offset + i:offset + i+1].hex()))
    return offset + length
    
def extract_shift_jisz(content, offset):
    extracted = ''
    while content[offset] != '\x00':
        extracted = extracted + content[offset]
        offset += 1
    return extracted.decode('shift-jis')
    
def unpack_data_to_item_list(data):
    (item_id_1, item_id_2, item_id_3, item_id_4, item_id_5, item_id_6, item_id_7, item_id_8,
     item_cat_1, item_cat_2, item_cat_3, item_cat_4, item_cat_5, item_cat_6, item_cat_7, item_cat_8,
     item_weight_1, item_weight_2, item_weight_3, item_weight_4, item_weight_5, item_weight_6, item_weight_7, item_weight_8,
     item_cumul_1, item_cumul_2, item_cumul_3, item_cumul_4, item_cumul_5, item_cumul_6, item_cumul_7, item_cumul_8,
     item_flag_1, item_flag_2, item_flag_3, item_flag_4, item_flag_5, item_flag_6, item_flag_7, item_flag_8,
     get_item_lot_flag, cumul_num_flag, cumul_num_max, rarity,
     item_count_1, item_count_2, item_count_3, item_count_4, item_count_5, item_count_6, item_count_7, item_count_8,
     packed_luck_byte, packed_cumul_reset_byte) = struct.unpack("@8I 8i 8h 8H 8i i i B B 8B c c", data)
    
    (item_luck_1, item_luck_2, item_luck_3, item_luck_4, item_luck_5, item_luck_6, item_luck_7, item_luck_8) = \
     list(reversed([x == '1' for x in '{0:08b}'.format(ord(packed_luck_byte), 'b')]))
    (item_cumul_reset_1, item_cumul_reset_2, item_cumul_reset_3, item_cumul_reset_4, 
     item_cumul_reset_5, item_cumul_reset_6, item_cumul_reset_7, item_cumul_reset_8) = \
     list(reversed([x == '1' for x in '{0:08b}'.format(ord(packed_cumul_reset_byte), 'b')]))
    item_1 = ItemLotItem(item_cat_1, item_id_1, item_count_1, item_weight_1, item_cumul_1, item_flag_1, item_luck_1, item_cumul_reset_1)
    item_2 = ItemLotItem(item_cat_2, item_id_2, item_count_2, item_weight_2, item_cumul_2, item_flag_2, item_luck_2, item_cumul_reset_2)
    item_3 = ItemLotItem(item_cat_3, item_id_3, item_count_3, item_weight_3, item_cumul_3, item_flag_3, item_luck_3, item_cumul_reset_3)
    item_4 = ItemLotItem(item_cat_4, item_id_4, item_count_4, item_weight_4, item_cumul_4, item_flag_4, item_luck_4, item_cumul_reset_4)
    item_5 = ItemLotItem(item_cat_5, item_id_5, item_count_5, item_weight_5, item_cumul_5, item_flag_5, item_luck_5, item_cumul_reset_5)
    item_6 = ItemLotItem(item_cat_6, item_id_6, item_count_6, item_weight_6, item_cumul_6, item_flag_6, item_luck_6, item_cumul_reset_6)
    item_7 = ItemLotItem(item_cat_7, item_id_7, item_count_7, item_weight_7, item_cumul_7, item_flag_7, item_luck_7, item_cumul_reset_7)
    item_8 = ItemLotItem(item_cat_8, item_id_8, item_count_8, item_weight_8, item_cumul_8, item_flag_8, item_luck_8, item_cumul_reset_8)
    
    return (get_item_lot_flag, cumul_num_flag, cumul_num_max, rarity, 
     [item_1, item_2, item_3, item_4, item_5, item_6, item_7, item_8])

class ItemLotItemType:
    WEAPON = 0x00000000
    ARMOR =  0x10000000
    RING =   0x20000000
    ITEM =   0x40000000
    NONE =   -1 # \xffffffff

class ItemLotItem:
    def __init__(self, item_category = ItemLotItemType.WEAPON, item_id = 0, 
     item_count = 0, item_weight = 0, item_cumul = 0, item_flag = 0, 
     item_luck = False, item_cumul_reset = False):
        self.item_category = item_category
        self.item_id = item_id
        self.item_count = item_count
        self.item_weight = item_weight
        self.item_cumul = item_cumul
        self.item_flag = item_flag
        self.item_luck = item_luck
        self.item_cumul_reset = item_cumul_reset
    
class ItemLot:
    def __init__(self, lot_id, get_item_lot_flag, cumul_num_flag, 
     cumul_num_max, rarity, item_list, description):
        if len(item_list) > 8:
            raise ValueError("ItemLot cannot have more than 8 items. " +
             "Received " + str(len(item_list)) + " items in Lot #" + 
             str(lot_id) + ".")
        item_list += [ItemLotItem() for _ in range(8 - len(item_list))]
        
        self.lot_id = lot_id
        self.get_item_lot_flag = get_item_lot_flag
        self.cumul_num_flag = cumul_num_flag
        self.cumul_num_max = cumul_num_max
        self.rarity = rarity
        self.item_list = item_list
        self.description = description
        
    @classmethod
    def from_binary(cls, lot_id, data, description):
        (get_item_lot_flag, cumul_num_flag, cumul_num_max, 
         rarity, item_list) = unpack_data_to_item_list(data)
        return cls(lot_id, get_item_lot_flag, cumul_num_flag, 
         cumul_num_max, rarity, item_list, description)
         
    def to_binary(self):
        item_id_list = [item.item_id for item in self.item_list]
        item_cat_list = [item.item_category for item in self.item_list]
        item_weight_list = [item.item_weight for item in self.item_list]
        item_cumul_list = [item.item_cumul for item in self.item_list]
        item_flag_list = [item.item_flag for item in self.item_list]
        item_extra_list = [self.get_item_lot_flag, self.cumul_num_flag, self.cumul_num_max, self.rarity]
        item_count_list = [item.item_count for item in self.item_list]
        
        item_luck_list = [item.item_luck for item in self.item_list]
        packed_luck_byte = chr(sum([item_luck_list[i] * 2**i for i in range(7)]))
        item_cumul_reset_list = [item.item_cumul_reset for item in self.item_list]
        packed_cumul_reset_byte = chr(sum([item_cumul_reset_list[i] * 2**i for i in range(7)]))
        item_packed_list = [packed_luck_byte.encode("ascii"), packed_cumul_reset_byte.encode("ascii")]
        
        arg_list = (item_id_list + item_cat_list + item_weight_list + 
         item_cumul_list + item_flag_list + item_extra_list + 
         item_count_list + item_packed_list)
        
        data = struct.pack("@8I 8i 8h 8H 8i i i B B 8B c c", *arg_list)        
        return (self.lot_id, data, self.description)

class ItemLotParam:
    RECORD_SIZE = 0xC
    DATA_RECORD_SIZE = 0x94
    
    def __init__(self, item_lots = None):
        if item_lots == None:
            item_lots = []
        self.item_lots = item_lots
        
    def has_used_lot_id(self, lot_id):
        return len([item_lot for item_lot in self.item_lots if item_lot.lot_id == lot_id]) > 0
    
    @classmethod
    def load_from_file_content(cls, file_content):
        master_offset = 0
        
        (strings_offset, data_offset, unk, item_lot_count) = struct.unpack_from("<IIHH", file_content, offset=master_offset)
        
        master_offset = 0x30  # Skip the rest of the header.
        
        item_lots = []
        for i in range(item_lot_count):
            (item_lot_id, item_lot_data_offset, item_lot_string_offset) = struct.unpack_from("<III", file_content, offset=master_offset)           
            master_offset += struct.calcsize("<III")
            
            description = extract_shift_jisz(file_content, item_lot_string_offset)
            item_lot_data = file_content[item_lot_data_offset:item_lot_data_offset + cls.DATA_RECORD_SIZE]
            
            item_lots.append(ItemLot.from_binary(item_lot_id, item_lot_data, description))
        return ItemLotParam(item_lots)
             
    def export_as_binary(self):
        num_of_records = len(self.item_lots)
        records_offset = 0x30
        data_offset = records_offset + num_of_records * self.RECORD_SIZE
        strings_offset = data_offset + num_of_records * self.DATA_RECORD_SIZE
        header = struct.pack("@IIHH", strings_offset, data_offset, 2, num_of_records) + b"ITEMLOT_PARAM_ST" + b"\x00" + b"\x20" * 15 + b"\x00\x02\x00\x00"
        packed_record = b""
        packed_data = b""
        packed_strings = b""
        current_data_offset = data_offset
        current_strings_offset = strings_offset
        for item_lot in sorted(self.item_lots, key = lambda lot: lot.lot_id):
            (lot_id, data, description) = item_lot.to_binary()
            encoded_description = description.encode('shift-jis') + b"\x00"
            packed_record += struct.pack("@III", lot_id, current_data_offset, current_strings_offset)
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
        
        data = ItemLotParam.load_from_file_content(file_content)
        #print(data.export_cheatsheet(filter_only_treasure = True))
        sys.stdout.write(data.export_as_binary())
        sys.stdout.flush()
        
        
        
        
            

            
            

 
