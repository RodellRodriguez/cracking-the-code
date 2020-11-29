'''
Given two strings, write a method to decide if one is a permutation of the
other.
'''

'''
Do we assume lower case chars only? Let's assume that.
What about whitespace? I'll assume no whitespace
Input: a, b where a and b are strings
Output: True/False

First we can check if the strings are the same length. If diff length then False

First solution:
    - Sort both strings in alphabetical order
    - Iterate through both strings at the same time and compare each letter to each other. If at any point
    the characters are different then return False
    - Return True if the for loop completes
    - Time Complexity: O(n*lgn). The sorting is the main bottleneck
    - Space Compleity: Depends on the sorting algorithm used

Faster Solution:
    - Create a hash table h where the key is each letter in string a and the value is the number of times that letter
    occurs in a
    - Iterate through b and for each letter look up its value in h:
        - If key doesn't exist then return False
        - Else if the count is 0 then return False
        - Else we see that the count is > 0 so decrement the count and continue loop
    - Get all of the values of h and if any values are > 0 then return False. This accounts for the situation
    where a had diff letters than b
    - Return True
    - Time Complexity is O(N) where N is the length of either string
    - Space Complexity is O(N) where N is the length of either string
'''


def is_permutation(a, b):
    if len(a) != len(b):
        return False
    letter_count = {}
    # Get a count of the num of letters in a
    for a_letter in a:
        letter_count[a_letter] = letter_count.get(a_letter, 0) + 1
    # Check if all letters in b exist in a
    for b_letter in b:
        if letter_count.get(b_letter, 0) == 0:
            return False
        else:
            letter_count[b_letter] -= 1
    # Check if there were any letters that are in a that weren't in b
    if [count for count in letter_count.values() if count != 0]:
        return False
    # We're good, it's a permutation
    return True


a = 'hello'
b = 'loelh'
print(is_permutation(a,b)) # True
a = 's'
b = 'asdad'
print(is_permutation(a,b)) # False
a = 'wearamask'
b = 'masibwear'
print(is_permutation(a,b)) # False
