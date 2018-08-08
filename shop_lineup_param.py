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
    while content[offset] != b'\x00':
        extracted = extracted + content[offset]
        offset += 1
    return extracted.decode('shift-jis')

class ShopLineItemType:
    WEAPON =     0
    ARMOR =      1
    RING =       2
    ITEM =       3
    SHOP_SPELL = 4
    NONE =      -1

class ShopLineup:
    def __init__(self, lineup_id, item_type, item_id, cost, sell_quantity, 
     event_flag, mtrl_id, qwc_id, shop_type, description):
         self.lineup_id = lineup_id
         self.item_type = item_type
         self.item_id = item_id
         self.cost = cost
         self.sell_quantity = sell_quantity
         self.event_flag = event_flag
         self.mtrl_id = mtrl_id
         self.qwc_id = qwc_id
         self.shop_type = shop_type
         self.description = description
        
    @classmethod
    def from_binary(cls, lineup_id, data, description):
        (item_id, cost, mtrl_id, event_flag, qwc_id, sell_quantity, 
         shop_type, item_type, _, _) = struct.unpack("@iiiiihBb II", data)
        return cls(lineup_id, item_type, item_id, cost, sell_quantity, 
         event_flag, mtrl_id, qwc_id, shop_type, description)
         
    def to_binary(self):       
        arg_list = [self.item_id, self.cost, self.mtrl_id, self.event_flag, 
         self.qwc_id, self.sell_quantity, self.shop_type, self.item_type]        
        data = struct.pack("@iiiiihBb", *arg_list) + b"\x00" * 8
        return (self.lineup_id, data, self.description)
        
    def as_string(self):
        return "Id: %d (%d %d %d %d %d %d %d %d): %s" % (self.lineup_id,
         self.item_id, self.cost, self.mtrl_id, self.event_flag, 
         self.qwc_id, self.sell_quantity, self.shop_type, self.item_type,
         self.description)

RECORD_SIZE = 0xC
DATA_RECORD_SIZE = 0x20 

class ShopLineupParam:
    def __init__(self, shop_lineups = None):
        if shop_lineups == None:
            shop_lineups = []
        self.shop_lineups = shop_lineups
    
    @classmethod
    def load_from_file_content(cls, file_content):
        master_offset = 0
        
        (strings_offset, data_offset, unk1, unk2, shop_lineup_count) = struct.unpack_from("<IHHHH", file_content, offset=master_offset)
        
        master_offset = 0x30  # Skip the rest of the header.
        
        shop_lineups = []
        for i in range(shop_lineup_count):
            (lineup_id, lineup_data_offset, lineup_string_offset) = struct.unpack_from("<III", file_content, offset=master_offset)           
            master_offset += struct.calcsize("<III")
            
            description = extract_shift_jisz(file_content, lineup_string_offset)
            lineup_data = file_content[lineup_data_offset:lineup_data_offset + DATA_RECORD_SIZE]
            
            shop_lineups.append(ShopLineup.from_binary(lineup_id, lineup_data, description))
        return ShopLineupParam(shop_lineups)
             
    def export_as_binary(self):
        num_of_records = len(self.shop_lineups)
        records_offset = 0x30
        data_offset = records_offset + num_of_records * RECORD_SIZE
        strings_offset = data_offset + num_of_records * DATA_RECORD_SIZE
        header = struct.pack("@IHHHH", strings_offset, data_offset, 1, 1, num_of_records) + b"SHOP_LINEUP_PARAM" + b"\x00" + b"\x20" * 14 + b"\x00\x02\x00\x00"
        packed_record = b""
        packed_data = b""
        packed_strings = b""
        current_data_offset = data_offset
        current_strings_offset = strings_offset
        for lineup in sorted(self.shop_lineups, key = lambda lineup: lineup.lineup_id):
            (lineup_id, data, description) = lineup.to_binary()
            encoded_description = description.encode('shift-jis') + b"\x00"
            packed_record += struct.pack("@III", lineup_id, current_data_offset, current_strings_offset)
            packed_data += data
            packed_strings += encoded_description
            current_data_offset += len(data)
            current_strings_offset += len(encoded_description)
        return header + packed_record + packed_data + packed_strings
            
    def as_string(self):
        return "\n".join([lineup.as_string() for lineup in sorted(self.shop_lineups, key = lambda lineup: lineup.lineup_id)])
            
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("No filename specified.")
        sys.exit(0)
        
    with open(sys.argv[1], 'rb') as f:
        file_content = f.read()
        
        data = ShopLineupParam.load_from_file_content(file_content)
        print(data.as_string())
