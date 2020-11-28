'''
Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?
'''

'''
- Our inputs can be lower/upper case characters and numbers, symbols
- Out output is True/False

Brute Force:
    - Call string 's'
    - For each letter x in s, compare x to all of the characters after it in s
    - If we find a match then return False. If we never find a match then return True
    - If N is num of characters in S then the time complexity is O(N^2). Space complexity is O(1)

Faster solution:
    - Use Hash Table as a lookup table
    - For each letter x in s, check if x is in the hash table and if not then add an entry to the hash Table
        - If the letter is in the hash table then return False
    - Return True if we never find a match in the Hash Table
    - If N is num of characters in S then the time complexity is now O(N). Space Complexity is O(1) still because there's a ceiling
    on the number of unique characters we can have
'''


def is_unique(str):
    look_up = {}
    for letter in str:
        if letter in look_up:
            return False
        else:
            look_up[letter] = True
    return True


input = 'pool'
print(is_unique(input))
