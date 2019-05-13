import fileutils
import coreutils
import math

from Crypto.Cipher import AES

def aes_ecb_decrypt(blocks, key):
    plaintext = bytearray(b'')
    cipher = AES.new(key, AES.MODE_ECB)
    
    for b in blocks:
        plaintext += cipher.decrypt(b)
    
    return plaintext

key = bytearray(b'YELLOW SUBMARINE')
decoded_bytes = fileutils.decode_file_base64("data/7.txt")
blocks = coreutils.get_blocks(decoded_bytes, key)
plaintext = aes_ecb_decrypt(blocks, key)
print(plaintext.decode())