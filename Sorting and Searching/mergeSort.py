"""
Time: O(nlgn) on average and worst case
Space: Depends

Mergesort divides the array in half recursively until our halves shrink to a size of 1.
Then the halves recursively merge back together. The merging part is the processing heavy portion

Merge portion:
Copies all the elements from the target array segment into a helper array.
This helper array keeps track of the left and right half starting points(called helperLeft and helperRight)
We then iterate thru helper array, copying the smaller element from each half into our original array
At the end we copy any remaining elements from the left half array only into our original array.

Note: We do not need to worry about the remaining elements from the right half array because
Our original array already has them in its array.
"""

def mergeSort(aList):
	print("Starting mergeSort...\n")
	helper = []
	_mergeSort(aList, helper, 0, len(aList)-1)

def _mergeSort(aList, helper, low, high):
	if low < high:
		mid = (low+high)//2
		_mergeSort(aList,helper,low,mid)
		_mergeSort(aList,helper,mid+1,high)
		merge(aList, helper,low,mid,high)

def merge(aList, helper, low, mid, high):
	helper = aList.copy()
	helperLeft, helperRight, current, = low, mid+1, low
	while helperLeft <= mid and helperRight <= high:
		if helper[helperLeft] <= helper[helperRight]:
			aList[current] = helper[helperLeft]
			helperLeft += 1
		else:
			aList[current] = helper[helperRight]
			helperRight += 1
		current += 1
	remaining = mid - helperLeft
	for x in range(0,remaining + 1):
		aList[current+x] = helper[helperLeft+x]
