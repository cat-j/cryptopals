import math
import frequency

def get_key_length_distances(ciphertext, lower, upper):
    distances = {}

    for length in range(lower, upper+1):
        distance = frequency.blocks_hamming_distance(ciphertext, length)
        distances[length] = distance / length
    
    return distances