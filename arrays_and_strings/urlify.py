'''
Write a method to replace all spaces in a string with '%20'. You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string. (Note: If implementing in Java, please use a character array so that you can
perform this operation in place.)

EXAMPLE
Input: "Mr John Smith     ", 13
Output: "Mr%20John%20Smith"
'''

'''
What if there are consecutive white spaces? I'm assuming we replace literally each white space with '%20'
We can't include the white space at the end of the string to be replaced since that's the extra space alotted for the replacement
    - We could use a function that strips trailing white space
'''


def urlify(str):
    return str.strip().replace(' ', '%20')


input = 'Mr John Smith'
assert urlify(input) == 'Mr%20John%20Smith'
