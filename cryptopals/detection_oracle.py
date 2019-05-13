import encrypt

key = encrypt.get_aes_key(16)
print(key, len(key))