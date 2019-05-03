ENGLISH_ALPHABET = "abcdefghijklmnopqrstuvwxyz"

ENGLISH_ALPHABET_LETTERS = 26

# defined here so we won't have to read a .csv every time
# unless there's a dramatic shift in English morphology in the near future,
# this will probably just remain static so there's nothing really wrong
# with hardcoding it
ENGLISH_LETTER_FREQUENCIES = {
    'a': 0.08167,
    'b': 0.01492,
    'c': 0.02782,
    'd': 0.04253,
    'e': 0.12702,
    'f': 0.02228,
    'g': 0.02015,
    'h': 0.06094,
    'i': 0.06966,
    'j': 0.00153,
    'k': 0.00772,
    'l': 0.04025,
    'm': 0.02406,
    'n': 0.06749,
    'o': 0.07507,
    'p': 0.01929,
    'q': 0.00095,
    'r': 0.05987,
    's': 0.06327,
    't': 0.09056,
    'u': 0.02758,
    'v': 0.00978,
    'w': 0.02360,
    'x': 0.00150,
    'y': 0.01974,
    'z': 0.00074
}

def get_empty_dict():
    result = {}
    for i in range(ENGLISH_ALPHABET_LETTERS):
        result[chr(ord('a') + i)] = 0
    return result

def analyse_frequencies(my_string):
    # count character appearances
    appearances = get_empty_dict()
    l = len(my_string)
    if l == 0:
        return appearances
        
    lowercase_string = my_string.lower()

    for c in lowercase_string:
        if (ord(c) >= ord('a') and ord(c) <= ord('z')):
            appearances[c] += 1

    # calculate frequencies
    frequencies = {}
    for k, v in appearances.items():
        frequencies[k] = v / l
    
    return frequencies

# @var my_dict: dictionary containing character frequencies in a string
def dict_frequency_distance(my_dict):
    return sum([abs(my_dict[k] - ENGLISH_LETTER_FREQUENCIES[k]) for k in ENGLISH_ALPHABET])

def frequency_distance(my_string):
    frequencies = analyse_frequencies(my_string)
    return dict_frequency_distance(frequencies)

def is_alpha(ch):
    return ((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z'))

def count_alpha_chars(my_string):
    return sum([(1 if is_alpha(ch) else 0) for ch in my_string])