"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    for item in items: 
        print(item)

def get_all_evens(nums):
    even_nums = []
    for num in nums: 
        if num % 2 == 0: 
            even_nums.append(num)


def get_odd_indices(items):
    odd_nums = []
    for num in range(len(items)): 
        if num % 2 != 0: 
            odd_nums.append(num)


def print_as_numbered_list(items):
    i = 1
    for item in items:
        print(f'{i}. {item}')
        i += i 


def get_range(start, stop):
    nums = []
    for num in range(start,stop): 
        nums.append(num)
    return nums 


def censor_vowels(word):
    chars = []
    for letter in word: 
        if letter in "aeiou": 
            chars.append("*")
        else: 
            chars.append(letter)
    return chars.join()


def snake_to_camel(string):
    camel_case = []
    for word in string.split('_'): 
        camel_case.append(word[0].upper+word[1:-1])
    return camel_case.join()


def longest_word_length(words):
    longest = len(words[0])
    for word in words:
        if longest < len(word):
            longest = len(word)
    return longest 


def truncate(string):
    result = []
    for char in string: 
        if len(result) == 0:
            result.append(char)
        if char != result[len(result) - 1]:
            result.append(char)
    return result.join
            


def has_balanced_parens(string):
    parens = 0
    for char in string: 
        if char == '(': 
            parens += 1
        elif char == ')': 
            parens -= 1
    if parens < 0: 
        return False
    else: 
        return True 


def compress(string):
    compressed = []
    cur_char = ""
    char_count = 0 

    for char in string: 
        if char != cur_char: 
            compressed.append(cur_char)
            if char_count > 1: 
                compressed.append(char_count)
            cur_char = char
            char_count = 0
        char_count = 1
    compressed.append(cur_char)
    if char_count > 1: 
        compressed.append(char_count)
    return compressed.join 
