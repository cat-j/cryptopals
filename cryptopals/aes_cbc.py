import encrypt
import fileutils

from Crypto.Cipher import AES

raw_bytes = fileutils.decode_file_base64("data/10.txt")
key = bytearray(b"YELLOW SUBMARINE")
iv = bytearray(b"\x00" * AES.block_size)
ciphertext = encrypt.aes_cbc_decrypt(raw_bytes, key, iv)
print(ciphertext.decode())