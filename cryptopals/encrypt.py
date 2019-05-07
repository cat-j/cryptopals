import binascii

def xor_encrypt(plaintext, key):
    key_length = len(key)
    i = 0
    ciphertext = bytearray(b'')
    
    for b in plaintext:
        ciphertext.append(b ^ key[i%key_length])
        i += 1

    return ciphertext

# usage example
# plaintext = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
# encrypted = xor_encrypt(plaintext, "ICE")
# print(binascii.hexlify(encrypted))