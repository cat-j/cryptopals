import math
import frequency

# @var ciphertext: hex-encoded string as a byte array
# @var key: single-char key as an int
def decrypt_single_key(ciphertext, key):
    return "".join([chr(b ^ key) for b in ciphertext])

def decrypt(ciphertext, score_fn):
    best_score, best_plaintext, best_key = score_fn.worst_score, None, None

    for key in range(256):
        current_plaintext = decrypt_single_key(ciphertext, key)
        current_score = score_fn.score(current_plaintext)
        if score_fn.compare(current_score, best_score):
            best_score, best_plaintext, best_key = current_score, current_plaintext, key
    
    return (best_score, best_plaintext, best_key)

# usage example:
# raw_bytes = bytearray.fromhex("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")
# print(decrypt(raw_bytes, frequency.CharTypeCount(frequency.is_alpha_space_or_null)))