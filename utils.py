import base64

# @var my_string: ASCII representation of hex bytes without 0x prefix
def str_to_base64(my_string):
    return base64.b64encode(bytes.fromhex(my_string))