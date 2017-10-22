"""
Implementing iterative and recursive way of performing Binary Search of a sorted array
"""

def binarySearchIterative(arr, target):
	if arr:
		low, high = 0, len(arr)-1
		while low <= high:
			mid = (low+high)//2
			if arr[mid] < target: low = mid+1
			elif arr[mid] > target: high = mid-1
			else: return arr[mid]
	#Failed to find the target
	return -1 

def binarySearchRecursive(arr, target, low, high):
	if arr:
		if low <= high:
			mid = (low+high)//2
			if arr[mid] < target: return binarySearchRecursive(arr,target,mid+1,high)
			elif arr[mid] > target: return binarySearchRecursive(arr,target,low, mid-1)
			else: return arr[mid]
	return -1
