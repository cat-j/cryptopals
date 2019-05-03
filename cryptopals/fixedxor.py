raw_bytes_1 = int("1c0111001f010100061a024b53535009181c", 16)
raw_bytes_2 = int("686974207468652062756c6c277320657965", 16)
xord = raw_bytes_1 ^ raw_bytes_2
print(hex(xord))