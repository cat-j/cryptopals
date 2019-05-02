import binascii
import importlib.util
spec = importlib.util.spec_from_file_location("utils", "./utils.py")
utils = importlib.util.module_from_spec(spec)
spec.loader.exec_module(utils)

raw_bytes_1 = int("1c0111001f010100061a024b53535009181c", 16)
raw_bytes_2 = int("686974207468652062756c6c277320657965", 16)
xord = raw_bytes_1 ^ raw_bytes_2
print(hex(xord))