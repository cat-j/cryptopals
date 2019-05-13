import fileutils
import math

from Crypto.Cipher import AES

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

def aes_ecb_decrypt(blocks, key):
    plaintext = bytearray(b'')
    cipher = AES.new(key, AES.MODE_ECB)
    
    for b in blocks:
        plaintext += cipher.decrypt(b)
    
    return plaintext

key = bytearray(b'YELLOW SUBMARINE')
decoded_bytes = fileutils.decode_file_base64("data/7.txt")
blocks = get_blocks(decoded_bytes, key)
plaintext = aes_ecb_decrypt(blocks, key)
print(plaintext.decode())