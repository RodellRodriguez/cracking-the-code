'''
A magic index in an array A [ 0 ••• n -1] is defined to be an index such that A[ i] =
i. Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in
array A.
FOLLOW UP
What if the values are not distinct?
'''

'''
Brute force solution is to linearly go through the array and check each value to see if i'th index == i'th value

But because the array is sorted we can use binary search. If A[i] < i then look at only the array with indices > i.
If A[i] > i then look at only the array with indices < i. Whatever array we are observing just check the middle index.

Base case? If array is empty then return False.

The above works for distinct integers. What if the integers are not distinct?
'''

def magic_index(array, start, end):
    if end < start:
        return False
    mid = (end+start)//2
    if array[mid] == mid:
        return mid
    if array[mid] < mid:
        return magic_index(array, mid+1, end)
    else:
        return magic_index(array, 0, mid-1)

array = [-5,-3,0,1,2,3,4,5,8]
assert magic_index(array, 0, len(array)) == 8
