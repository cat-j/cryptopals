import fileutils
import coreutils

def has_equal_blocks(blocks):
    l = len(blocks)
    sorted_blocks = blocks.copy()
    sorted_blocks.sort()
    
    for i in range(l-1):
        if sorted_blocks[i] == sorted_blocks[i+1]:
            return True
    
    return False

def find_aes_ecb(filename):
    raw_data = fileutils.decode_file_hex(filename)

    for line in raw_data:
        blocks = coreutils.get_blocks(line, 16)
        if has_equal_blocks(blocks):
            return blocks
    
    # No patterns found
    return None

aes_encrypted = find_aes_ecb("data/8.txt")
print(aes_encrypted)