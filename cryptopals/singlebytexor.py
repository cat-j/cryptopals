import math
import frequency

# @var ciphertext: hex-encoded string as a byte array
# @var key: single-char key as an int
def decrypt_single_key(ciphertext, key):
    return "".join([chr(b ^ key) for b in ciphertext])

# TODO: document and refactor the next 2 functions

# @var ciphertext: hex-encoded string as a byte array
def frequency_decrypt(ciphertext):
    best_score, best_plaintext = math.inf, ""

    for key in range(256):
        current_plaintext = decrypt_single_key(ciphertext, key)
        current_score = frequency.frequency_distance(current_plaintext)
        if current_score < best_score:
            best_score, best_plaintext = current_score, current_plaintext
    
    return (best_score, best_plaintext)

def alpha_chars_decrypt(ciphertext):
    best_score, best_plaintext = 0, ""
    l = len(ciphertext)

    for key in range(256):
        current_plaintext = decrypt_single_key(ciphertext, key)
        current_score = frequency.count_alpha_chars(current_plaintext)
        current_score = current_score / l
        if current_score > best_score:
            best_score, best_plaintext = current_score, current_plaintext
        
    return (best_score, best_plaintext)

def ascii_chars_decrypt(ciphertext):
    best_score, best_plaintext = 0, ""
    l = len(ciphertext)

    for key in range(256):
        current_plaintext = decrypt_single_key(ciphertext, key)
        current_score = frequency.count_ascii_chars(current_plaintext)
        current_score = current_score / l
        if current_score > best_score:
            best_score, best_plaintext = current_score, current_plaintext
        
    return (best_score, best_plaintext)

# raw_bytes = bytearray.fromhex("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")
# print(alpha_chars_decrypt(raw_bytes))