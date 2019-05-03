import singlebytexor

def find_single_byte_xor(filename):
    lines = open(filename, 'r').read().splitlines()
    raw_data = [bytearray.fromhex(l) for l in lines]
    decrypted = [singlebytexor.frequency_decrypt(r) for r in raw_data]
    print(decrypted)

find_single_byte_xor("data/4.txt")