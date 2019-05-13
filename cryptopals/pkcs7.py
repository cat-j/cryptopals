import coreutils

block = bytearray(b"YELLOW SUBMARINE")
padded = coreutils.pkcs7(block, 20)
print(padded)