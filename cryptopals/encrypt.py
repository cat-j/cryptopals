import binascii

def xor_encrypt(plaintext, key):
    plaintext_bytes = bytes(plaintext, "utf-8")
    key_bytes = bytes(key, "utf-8")
    key_length = len(key)
    i = 0
    ciphertext = bytearray(b'')
    
    for b in plaintext_bytes:
        ciphertext.append(b ^ key_bytes[i%key_length])
        i += 1

    return ciphertext

plaintext = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
encrypted = xor_encrypt(plaintext, "ICE")
print(binascii.hexlify(encrypted))