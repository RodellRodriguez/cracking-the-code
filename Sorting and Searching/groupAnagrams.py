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