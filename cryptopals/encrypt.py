import binascii
import coreutils

from Crypto.Cipher import AES
from random import randrange

def xor_encrypt(plaintext, key):
    key_length = len(key)
    i = 0
    ciphertext = bytearray(b'')
    
    for b in plaintext:
        ciphertext.append(b ^ key[i%key_length])
        i += 1

    return ciphertext

def aes_cbc_decrypt(ciphertext, key, iv):
    block_size = len(key)
    blocks = coreutils.get_blocks(ciphertext, block_size)
    num_blocks = len(blocks)
    previous_block, current_block = coreutils.pkcs7(iv, block_size), None
    plaintext = bytearray(b'')
    cipher = AES.new(key, AES.MODE_ECB)

    for i in range(num_blocks):
        current_block = coreutils.pkcs7(blocks[i], block_size)
        decrypted_block = cipher.decrypt(current_block)
        plaintext += xor_encrypt(decrypted_block, previous_block)
        previous_block = current_block
    
    return plaintext

def get_random_bytes():
    num_bytes = randrange(5, 11)
    random_bytes = bytearray(b'')

    for i in range(num_bytes):
        byte = randrange(256)
        random_bytes += bytes([byte])
    
    return random_bytes

def get_aes_key(size):
    assert(size == 16 or size == 24 or size == 32)
    key = bytearray(b'')
    
    for i in range(size):
        byte = randrange(256)
        key += bytes([byte])
    
    return key

def encryption_oracle(data):
    mode = randrange(2)
    start_bytes = get_random_bytes()
    end_bytes = get_random_bytes()
    print(start_bytes)
    print(end_bytes)

# usage example
# plaintext = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
# encrypted = xor_encrypt(plaintext, "ICE")
# print(binascii.hexlify(encrypted))