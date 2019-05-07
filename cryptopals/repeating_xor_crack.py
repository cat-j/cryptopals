import math
import singlebytexor
import frequency
import encrypt

def get_key_length_distances(ciphertext, lower, upper):
    distances = {}

    for length in range(lower, upper+1):
        distance = frequency.blocks_hamming_distance(ciphertext, length)
        distances[length] = distance / length
    
    return distances

# Build a list of subsequences composed of the first, second, ... byte
# of each block_size-long block of ciphertext
# e.g. get_blocks("ilikedogs", 3) = ["iko", "leg", "ids"]
def get_blocks(ciphertext, block_size):
    l = len(ciphertext)
    block_num = math.ceil(l/block_size)
    blocks = [bytearray(b'') for i in range(block_size)]
    
    # i = block byte
    # j = block
    for i in range(block_size):
        for j in range(block_num):
            idx = j*block_size + i
            if idx < l: blocks[i].append(ciphertext[j*block_size + i])
    
    return blocks

# Find the byte that yields the best frequency for each block
def get_xor_bytes(blocks, score_fn):
    l = len(blocks)
    xor_bytes = [None for i in range(l)]
    
    for i in range(l):
        (_, _, xor_bytes[i]) = singlebytexor.decrypt(blocks[i], score_fn)
    
    return bytearray(xor_bytes)

def get_blocks_for_best_distances(ciphertext, distances, best_n=None):
    sorted_d = sorted(distances.items(), key=lambda x: x[1]) # sort by smallest distance
    blocks = []
    if best_n == None: best_n = len(distances)

    for x in sorted_d[:best_n]:
        blocks.append(get_blocks(ciphertext, x[0]))
    
    return blocks

def crack_n(ciphertext, score_fn, lower=1, upper=1, best_n=None):
    distances = get_key_length_distances(ciphertext, lower, upper)
    distance_blocks = get_blocks_for_best_distances(ciphertext, distances, best_n)
    xor_bytes = [get_xor_bytes(blocks, score_fn) for blocks in distance_blocks]
    decrypted = [encrypt.xor_encrypt(ciphertext, key) for key in xor_bytes]
    return decrypted

def crack_one(ciphertext, score_fn, lower=1, upper=1):
    return crack_n(ciphertext, score_fn, lower, upper, 1)[0]

def get_best_crack(cracks, score_fn):
    best_score, best_crack = score_fn.worst_score, None

    for crack in cracks:
        current_score = score_fn.score(crack.decode())
        if score_fn.compare(current_score, best_score):
            best_score, best_crack = current_score, crack
    
    return best_crack

raw_bytes = bytearray.fromhex("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")
cracked = crack_n(raw_bytes, len(raw_bytes)//2, frequency.CharTypeCount(frequency.is_alpha))
crack = get_best_crack(cracked, frequency.CharTypeCount(frequency.is_alpha_space_or_null))
print(crack.decode())