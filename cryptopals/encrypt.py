import binascii
import coreutils

from Crypto.Cipher import AES

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

# usage example
# plaintext = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
# encrypted = xor_encrypt(plaintext, "ICE")
# print(binascii.hexlify(encrypted))