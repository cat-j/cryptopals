import base64

# @var my_string: ASCII representation of hex bytes without 0x prefix
def str_to_base64(my_string):
    return base64.b64encode(bytes.fromhex(my_string))

def fixed_xor(buf1, buf2):
    return hex(int(buf1, 16) ^ int(buf2, 16))

def get_blocks(ciphertext, key):
    l = len(ciphertext)
    block_size = len(key)
    num_blocks = math.ceil(l // block_size)
    blocks = []

    for i in range(num_blocks):
        lower = i*block_size
        upper = min(l, lower+block_size)
        blocks.append(ciphertext[lower:upper])
    
    return blocks