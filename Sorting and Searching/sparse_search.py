'''
Given a sorted array of strings that is interspersed with empty strings, write a
method to find the location of a given string.
EXAMPLE
Input: ball, {"at", "", '"', "", "ball", "", "", "car", "", '"', "dad", '"', ""}
Output:4
'''
'''
Searching for a string in a sorted string typically implies a binary search.
Do a binary search and if it's an empty string then search for the nearest non empty string

What do we mean by nearest? Do we go forward or backwards? What if we do both?
'''


def sparse_search(array, target):



array = ["at", "", '"', "", "ball", "", "", "car", "", '"', "dad", '"', ""]
target = 'dad'
assert sparse_search(array, target) == 0
