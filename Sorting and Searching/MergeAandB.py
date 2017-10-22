"""
You are given 2 sorted arrays A and B where A has a large enough buffer to hold B as well.
Write a method to merge B into A in sorted order
"""

"""
In python you cant create arrays of fixed sizes so I had to do some extra work and create a list
filled with arbitrary values then overwrote the first n values of that list with all of list A's values

The solution is as follows:
We know that A has a large enough buffer to hold B and in order to merge A and B together
We need to take the arrays of A and B and compare each value of A to B then the lower one gets inserted into the array right?
However with this approach that means the resulted value needs to be inserted at the BEGINNING of list A which is bad
Because that means we need to shift all of the current values of list A forward... so why not work backwards?
Meaning compare the last values of list A and list B and append to the end of list A and keep decrementing the indicies.

Keep in mind if list A exhausts all of its values first then we need to ensure list B gets its values written too
Hence the "while end_of_b >= 0:" loop.
"""

def merge_a_and_b(list_a,list_b, size_of_a, size_of_b):
	end_of_a = size_of_a-1
	end_of_b = size_of_b-1
	end_of_merged = size_of_a + size_of_b - 1
	while end_of_a >= 0 and end_of_b >= 0:
		if list_a[end_of_a] > list_b[end_of_b]:
			list_a[end_of_merged] = list_a[end_of_a]
			end_of_a -= 1
			end_of_merged -= 1
		else:
			list_a[end_of_merged] = list_b[end_of_b]
			end_of_b -= 1
			end_of_merged -= 1
	while end_of_b >= 0:
		list_a[end_of_merged] = list_b[end_of_b]
		end_of_merged -= 1
		end_of_b -= 1

def main():
	list_a = [10,15,20,30]
	size_of_a = len(list_a)
	list_b = [3,6,9,12,15,18,21]
	size_of_b = len(list_b)
	print(list_a)
	print(list_b)
	list_a_extended = [i for i in range(0,(size_of_a+ size_of_b))]
	for a in range(0,size_of_a): list_a_extended[a] = list_a[a]
	print(list_a_extended)
	merge_a_and_b(list_a_extended,list_b, size_of_a, size_of_b)
	print(list_a_extended)

main()
