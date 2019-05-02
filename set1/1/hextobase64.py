import base64

ascii_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
raw_bytes = bytes.fromhex(ascii_string)
encoded = base64.b64encode(raw_bytes)
print(encoded)