"""
11.2:
Write a method to sort an array of strings so that all the anagrams are next to each
other
"""

"""
1. Create an empty hash table
2. For loop: For every string from the input array:
	2a. Sort the string and store it as "key" then find if key exists in the hash table's keys
	2b. If the key does not exist then create a new entry in the hash table using that sorted string
	As the key and the new value will be an empty list
	2c. Add the original string to the list of its corresponding sorted string in the hash table
3. Loop through every string in the hash table and overwrite our originaly inpur array with the strings
from the hash table. Since the hash table's entries are organized via anagrams then the way the
Array will be overwritten will be such that all the same anagrams will be grouped together
"""

def groupAnagrams(arr):
	myDict = {}
	for string in arr:
		key = sortString(string)
		if key not in myDict: myDict[key] = []
		myDict[key].append(string)

	i = 0
	for key,value in myDict.items():
		for string in value:
			arr[i] = string
			i += 1

def sortString(string):
	return ''.join(sorted(string))

def main():
	test = ["bat","cop","hbat","tab","bath","poc"]
	print(test)
	groupAnagrams(test)
	print(test)

main()