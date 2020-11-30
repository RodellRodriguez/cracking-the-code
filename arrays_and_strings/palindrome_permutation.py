'''
Given a string, write a function to check if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards and backwards. A permutation
is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.

EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat", "atco cta", etc.)
'''

'''
So given a string, a permutation of a palindrome is if we can rearrange the letters
in the phrase to make another palindrome. Ignore casing of letters and spacing

Brute Force Solution:
    - Create every possible permutation and for each permutation check if it's a palindrome
    - Takes way too long

What are the properties of a palindrome?
    - Reads the same way forward and backwards. This means that the num of letters in a palindrome are a multiple
of 2 except for 1 letter if the num of letteres in the palindrome is odd. That 1 letter must have an odd number of repetitions.
If its not odd then all num of letters are a multiple of 2.

Input: 'Tact Coooa'
Output: taoco coat

Better Solution
    - Create a hash table of letter counts
    - Then establish if str has even or odd length
    - If even then all letter counts in the hash table must be even
        - Return False if this fails
    - Else all the letter counts must be even except for one letter count
        - Return False if this fails
    - Return True
    - Time Complexity: O(N)
    - Space Complxity: O(N)

'''


def palindrome_permutation(str):
    letter_count = {}
    str = str.lower().replace(' ', '')
    for letter in str:
        letter_count[letter] = letter_count.get(letter, 0) + 1
    if len(str) % 2 == 0:
        # parity_of_string = 'even'
        for count in letter_count.values():
            # If it finds any odd number then not permutation
            if count % 2 != 0:
                return False
    else:
        # parity_of_string = 'odd'
        num_of_odd_count = 0
        for count in letter_count.values():
            if count % 2 != 0:
                num_of_odd_count += 1
                if num_of_odd_count > 1:
                    return False
    return True


str = 'Tact Coa'
assert palindrome_permutation(str) == True
