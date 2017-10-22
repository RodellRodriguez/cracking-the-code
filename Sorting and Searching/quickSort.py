"""
Runtime: O(nlgn) on avg, O(n^2) worst case
Space: O(lgn)

Picks a random element as the "pivot" and partitions the array such that all numbers
LESS than the pivot are placed before the pivot and all elements GREATER than the pivot
Are placed after the pivot.

The Quick sort algorithm partitions the array as explained and 
Recursively partitions the left half and the right half via pivots

The partitioning can be performed efficiently thru a series of swaps. The speed of this
sorting algorithm is dependent on the choice of the pivot. 
The best pivot is the median of the array (if the array was sorted).
The worst pivot is the smallest or largest value of the array.
So how do we choose the pivot? A safe choice is 
Choosing the middle index of our Left and Right trackers

Partitioning:
The first time that we partition, we select our left tracker as index 0
And we choose our right tracker as the last index of the array.
As explained, we choose the middle index as the pivot.
While the left tracker is less than or equal to the right tracker (not the value in the array, their indicies):
  You advance left tracker to the right until the value of the array at that index is no longer less than
  The value of the array at the pivot's index.
  Then, you decrement the right tracker to the left until the value of the array at that index is no longer
  Greater than the value of the array at the pivot's index.
  Finally check if left tracker's index is still less than or equal to the right tracker's index
  If so then swap the values of in the array of left and right tracker. 
  Then advance the left tracker index by one and decrement the right tracker index by one
  Repeat while loop
Return the left tracker index

After partitioning that very first time now we have two halves so we recursively partition
The left and right halves.

"""

def quickSort(arr, left, right):
	index = partition(arr, left, right)
	mid = index-1 
	if left < mid: quickSort(arr,left,mid)
	if right > mid + 1: quickSort(arr, mid+1, right)

def partition(arr, left, right):
#Choosing the median of the left and right indicies as the pivot.
#It usually gives a better performance than choosing the first element as the pivot
#If an array is nearly sorted then choosing the first element as pivot is BAD
	pivot = arr[(left+right)//2]
	while left <= right:
		while arr[left] < pivot: left += 1
		while arr[right] > pivot: right -= 1
		if left <= right:
			swap(arr, left, right)
			left += 1
			right -= 1
	return left

def swap(arr, left, right):
	#This is the pythonic way of swapping
	#Otherwise you would do this manually and create a temp	variable
	arr[left], arr[right] = arr[right], arr[left]
