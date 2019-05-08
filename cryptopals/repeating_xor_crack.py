import math
import binascii
import threading
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

def get_xor_bytes_and_encrypt(blocks, score_fn, ciphertext):
    xor_bytes = get_xor_bytes(blocks, score_fn)
    return encrypt.xor_encrypt(ciphertext, xor_bytes)

def xor_bytes_worker(blocks, score_fn, results_list):
    xor_bytes = get_xor_bytes(blocks, score_fn)
    results_list.append(xor_bytes)
    return

def xor_encrypt_worker(ciphertext, key, results_list):
    plaintext = encrypt.xor_encrypt(ciphertext, key)
    results_list.append(plaintext)
    return

def get_xor_bytes_and_encrypt_worker(blocks, score_fn, ciphertext, results_list):
    decrypted = get_xor_bytes_and_encrypt(blocks, score_fn, ciphertext)
    results_list.append(decrypted)
    return

# Execute worker_fn on num_threads threads
# worker_fn *MUST* be a function that appends the result of its calculations
# to its last argument, thus the check for it being a list
def calculate_multithreaded(num_threads, worker_fn, worker_args_list):
    threads = []

    for i in range(num_threads):
        worker_args = worker_args_list[i]
        assert(type(worker_args[-1]) == list)
        t = threading.Thread(target=worker_fn, args=worker_args)
        threads.append(t)
        t.start()

    for i in range(num_threads):
        threads[i].join()
    
    return

def get_blocks_for_best_distances(ciphertext, distances, best_n=None):
    sorted_d = sorted(distances.items(), key=lambda x: x[1]) # sort by smallest distance
    blocks = []
    if best_n == None: best_n = len(distances)

    for x in sorted_d[:best_n]:
        blocks.append(get_blocks(ciphertext, x[0]))
    
    return blocks

def crack_n(ciphertext, score_fn, lower=1, upper=None, best_n=None, key_and_decrypt=True):
    if upper == None: upper = len(ciphertext) // 2
    
    print("Calculating key length distances...")
    distances = get_key_length_distances(ciphertext, lower, upper)

    print("Calculating blocks...")
    blocks_list = get_blocks_for_best_distances(ciphertext, distances, best_n)
    num_threads = len(blocks_list)
    
    decrypted_list = []

    if key_and_decrypt:
        # Get key and decrypt in a single thread
        print("Calculating keys and decrypting...")
        get_xor_bytes_and_encrypt_worker_args = \
            [(blocks, score_fn, ciphertext, decrypted_list) for blocks in blocks_list]
        calculate_multithreaded(num_threads, worker_fn=get_xor_bytes_and_encrypt_worker, \
            worker_args_list=get_xor_bytes_and_encrypt_worker_args)
    else:
        # One set of threads for calculating keys, one for decrypting
        print("Calculating keys...")
        xor_bytes_list = []
        xor_bytes_worker_args = [(blocks, score_fn, xor_bytes_list) for blocks in blocks_list]
        calculate_multithreaded(num_threads, worker_fn=xor_bytes_worker, \
            worker_args_list=xor_bytes_worker_args)

        print("Decrypting...")
        xor_encrypt_worker_args = [(ciphertext, xor_bytes, decrypted_list) for xor_bytes in xor_bytes_list]
        calculate_multithreaded(num_threads, worker_fn=xor_encrypt_worker, \
            worker_args_list=xor_encrypt_worker_args)
        

    return decrypted_list

def crack_one(ciphertext, score_fn, lower=1, upper=None):
    return crack_n(ciphertext, score_fn, lower, upper, 1)[0]

# Instead of assuming the first element is the best guess,
# analyse the whole list to find the one with the best score
def get_best_crack(cracks, score_fn):
    best_score, best_crack = score_fn.worst_score, None

    for crack in cracks:
        try:
            current_score = score_fn.score(crack.decode())
            if score_fn.compare(current_score, best_score):
                best_score, best_crack = current_score, crack
        except:
            continue
    
    return best_crack

def decode_file(filename):
    lines = open(filename, 'r').read().splitlines()
    decoded_bytes = bytearray(b'')

    for line in lines:
        decoded_bytes += binascii.a2b_base64(line)
    
    return decoded_bytes

def crack_file(filename, score_fn, lower=1, upper=None, best_n=None):
    decoded_bytes = decode_file(filename)
    return crack_n(decoded_bytes, score_fn, lower, upper, best_n)

frequency_distance = frequency.FrequencyDistance
alpha_chars = frequency.CharTypeCount(frequency.is_alpha)
alpha_space_or_null_chars = frequency.CharTypeCount(frequency.is_alpha_space_or_null)
alnum_chars = frequency.CharTypeCount(lambda x: x.isalnum())

cracks = crack_file("data/6.txt", frequency.FrequencyDistance, best_n=40)
crack = get_best_crack(cracks, frequency.FrequencyDistance)

f = open("repeating_xor_crack_log.txt", "+w")
for crack in cracks:
    try:
        f.write("%s\n" % crack.decode())
    except:
        continue
f.close()