import struct
import zlib
import sys
import os

def consume_byte(content, offset, byte, length=1):
    """Consume length bytes from content, starting at offset. If they
     are not all byte, raises a ValueError.
    """
    
    for i in range(length-1):
        if content[offset + i:offset + i+1] != byte:
            raise ValueError(("Expected byte '0x%s' at offset " + 
             "0x%x but received byte '0x%s'.") % (byte.hex(), offset+i, 
             content[offset + i:offset + i+1].hex()))
    return offset + length
    
def appears_dcx(content):
    """Checks if the magic bytes at the start of content indicate that it
    is a .dcx file.
    """
    return content[0:4] == b"DCX\x00"
    
def compress_dcx_content(content):
    """Compress the given uncompressed content into the file data
    of a .dcx file."""
    HEADER_LENGTH = 0x2c
    COMP_HEADER_LENGTH = 0x08
    
    uncomp_size = len(content)
    comp_obj = zlib.compressobj(level=9, wbits=-15)
    compressed_data = comp_obj.compress(content)
    compressed_data += comp_obj.flush()
    comp_size = len(compressed_data) + 2 # Add two to include the \x78\xDA bytes.
    
    return_data = b"DCX\x00" 
    return_data += struct.pack("<I", 0x100) 
    return_data += struct.pack(">III", 0x18, 0x24, 0x24)
    return_data += struct.pack(">I", HEADER_LENGTH)
    return_data += b"DCS\x00"
    return_data += struct.pack(">II", uncomp_size, comp_size)
    return_data += b"DCP\x00DFLT"
    # Begin unknown header portion
    return_data += struct.pack(">I", 0x20)
    return_data += struct.pack("<IIII", 0x09, 0x00, 0x00, 0x00)
    return_data += b"\x00\x01\x01\x00"
    # End unknown header portion
    return_data += b"DCA\x00"
    return_data += struct.pack(">I", COMP_HEADER_LENGTH)
    return_data += b"\x78\xDA"
    return_data += compressed_data
    # Add checksum to file (not strictly needed in DS1, but .dcx includes this).
    return_data += struct.pack(">I", zlib.adler32(content))
    return return_data

def uncompress_dcx_content(content):
    """Decompress the file content from a .dcx file. Returns the uncompressed
    content. Raising ValueError if the header does not match the required format.
    """
    master_offset = 0
    master_offset = consume_byte(content, master_offset, b'D', 1)
    master_offset = consume_byte(content, master_offset, b'C', 1)
    master_offset = consume_byte(content, master_offset, b'X', 1)
    master_offset = consume_byte(content, master_offset, b'\x00', 1)
    
    (req_1,) = struct.unpack_from("<I", content, offset=master_offset)
    master_offset += struct.calcsize("<I")
    (req_2, req_3, req_4) = struct.unpack_from(">III", content, offset=master_offset)
    master_offset += struct.calcsize(">III")
    if req_1 != 0x100:
        raise ValueError("Expected DCX header int 0x100, but received " + hex(req_1))
    if req_2 != 0x18:
        raise ValueError("Expected DCX header int 0x18, but received " + hex(req_2))
    if req_3 != 0x24:
        raise ValueError("Expected DCX header int 0x24, but received " + hex(req_3))
    if req_4 != 0x24:
        raise ValueError("Expected DCX header int 0x24, but received " + hex(req_4))
    
    (header_length,) = struct.unpack_from(">I", content, offset=master_offset)
    master_offset += struct.calcsize(">I")
    
    master_offset = consume_byte(content, master_offset, b'D', 1)
    master_offset = consume_byte(content, master_offset, b'C', 1)
    master_offset = consume_byte(content, master_offset, b'S', 1)
    master_offset = consume_byte(content, master_offset, b'\x00', 1)
    
    (uncomp_size, comp_size) = struct.unpack_from(">II", content, offset=master_offset)
    master_offset += struct.calcsize(">II")
    
    master_offset = consume_byte(content, master_offset, b'D', 1)
    master_offset = consume_byte(content, master_offset, b'C', 1)
    master_offset = consume_byte(content, master_offset, b'P', 1)
    master_offset = consume_byte(content, master_offset, b'\x00', 1)
    master_offset = consume_byte(content, master_offset, b'D', 1)
    master_offset = consume_byte(content, master_offset, b'F', 1)
    master_offset = consume_byte(content, master_offset, b'L', 1)
    master_offset = consume_byte(content, master_offset, b'T', 1)
    
    # Skip the portion of the header whose meaning is unknown.
    master_offset += 0x18
    master_offset = consume_byte(content, master_offset, b'D', 1)
    master_offset = consume_byte(content, master_offset, b'C', 1)
    master_offset = consume_byte(content, master_offset, b'A', 1)
    master_offset = consume_byte(content, master_offset, b'\x00', 1)
    (comp_header_length,) = struct.unpack_from(">I", content, offset=master_offset)
    master_offset += struct.calcsize(">I")
    
    master_offset = consume_byte(content, master_offset, b'0x78', 1)
    master_offset = consume_byte(content, master_offset, b'0xDA', 1)
    comp_size -= 2  # The previous two bytes are included in the compressed data, for some reason.
    
    decomp_obj = zlib.decompressobj(-15)
    return decomp_obj.decompress(content[master_offset:master_offset + comp_size], uncomp_size)
    
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: " + str(sys.argv[0]) + " <DCX File>")
    else:
        filename = sys.argv[1]
        if filename[-4:] == ".dcx":
            uncomp_filename = filename[:-4]
        else:
            uncomp_filename = filename + ".undcx"
        with open(filename, "rb") as f, open(uncomp_filename, "wb") as g:
            file_content = f.read()
            g.write(uncompress_dcx_content(file_content))
            g.close()
            
    

    
    
     

