import fileutils
import coreutils

def find_aes_ecb(filename):
    raw_data = fileutils.decode_file_hex(filename)
    print(raw_data)

find_aes_ecb("data/8.txt")