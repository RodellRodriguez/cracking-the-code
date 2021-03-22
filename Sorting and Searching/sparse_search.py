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

What do we mean by nearest? Do we go forward or backwards?


1. have start, end, mid indices.
2. While start <= end:
    - mid = (start)//end
    - if len(array[mid]) == 0:
        current = mid - 1
        while current >= start:
            if len(array[current]) == 0:
                current -= 1
                continue
            else: we did encounter a value
                if array[current] < input:
                    start = mid +1
                elif array[current] > input:
                    end = current - 1
                else:
                    return current
                break
        if current < start:
            start = mid + 1
    - else:
        if array[mid] < input:
            start = mid +1
        elif array[mid] > input:
            end = mid - 1
        else:
            return mid
'''


def sparse_search(array, target):
    pass


array = ["at", "", '"', "", "ball", "", "", "car", "", '"', "dad", '"', ""]
target = 'at'
assert sparse_search(array, target) == 0
