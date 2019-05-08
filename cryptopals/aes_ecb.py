import fileutils
import math

from cryptography.hazmat.primitives.aead import AESCCM

def aes_ecb_decrypt(ciphertext, key):
    l = len(ciphertext)
    block_size = len(key)
    num_blocks = math.ceil(l // block_size)
    plaintext = bytearray(b'')

    for i in range(num_blocks):
        lower = i*block_size
        upper = min(l, lower+block_size)
        block = ciphertext[lower:upper]
        # plaintext += cryptography.hazmat.primitives.ciphers.aead

key = bytearray(b'YELLOW SUBMARINE')
decoded_bytes = fileutils.decode_file_base64("data/7.txt")
aes_ecb_decrypt(decoded_bytes, key)