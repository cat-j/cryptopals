import binascii

# Decode file as single base64 string
def decode_file_base64(filename):
    lines = open(filename, 'r').read().splitlines()
    decoded_bytes = bytearray(b'')

    for line in lines:
        decoded_bytes += binascii.a2b_base64(line)
    
    return decoded_bytes

# Decode file as several hex strings
def decode_file_hex(filename):
    lines = open(filename, 'r').read().splitlines()
    raw_data = [bytearray.fromhex(l) for l in lines]
    return raw_data