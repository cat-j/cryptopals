import singlebytexor
import frequency
import fileutils

def find_single_byte_xor(filename):
    raw_data = fileutils.decode_file_hex(filename)
    best_score, best_string = 0, ""

    for r in raw_data:
        current_score, current_string = singlebytexor.alpha_chars_decrypt(r)
        if current_score > best_score:
            best_score, best_string = current_score, current_string

    return best_string

print(find_single_byte_xor("data/4.txt"))