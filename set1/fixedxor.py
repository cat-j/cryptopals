import importlib.util
spec = importlib.util.spec_from_file_location("utils", "./utils.py")
utils = importlib.util.module_from_spec(spec)
spec.loader.exec_module(utils)

raw_bytes = bytearray.fromhex("1c0111001f010100061a024b53535009181c")
print(raw_bytes)