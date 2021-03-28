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

How to do both? We can check both left and right of the current string and keep moving left and right until we find a non-empty string

So if we get an empty string at index x then left = x-1 and right = right + 1

find_non_empty_string:
    left, right = mid-1, mid+1
    While left >= start and right <= end:
        if array[left] not empty:
            mid = left
            break
        if array[right] not empty:
            mid = right
            break
        left -= 1
        right += 1
    if left < start and right > end:
        return -1

Binary search part:
start, end = 0, len(array-1)
while start < end:
    mid = (start+end)//2
    if array[mid] an empty string then do find_non_empty_string portion from above:
    else: do the typical binary search check:
        if target < array[mid]:
            end = mid - 1
        elif target > array[mid]:
            start = mid + 1
        else:
            return mid
return -1


'', '', '', d
'''


def sparse_search(array, target):
    start, end = 0, len(array)-1
    while start < end:
        mid = (start + end)//2
        if len(array[mid]) == 0:
            # check for nearest non empty string
            # Once we do, we found our "mid", if not then search failed
            left, right = mid-1, mid+1
            while left >= start and right <= end:
                if len(array[left]) > 0:
                    mid = left
                    break
                elif len(array[right]) > 0:
                    mid = right
                    break
                left -=1
                right += 1
            if left < start and right > end:
                return -1
        if target < array[mid]:
            end = mid-1
        elif target > array[mid]:
            start = mid+1
        else:
            return mid
    return -1



array = ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]
target = 'at'
assert sparse_search(array, target) == 0
