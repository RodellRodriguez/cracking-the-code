"""
Given a sorted (increasing order) array with unique integer elements, write an
algorithm to create a binary search tree with minimal height.
"""
"""
A binary search tree with minimal height requires that the root is the median number of the
array of elements. This is because if you choose the smallest number possible as the root
then the sub right tree becomes way bigger than the left by the rules of a binary search tree.

So all we need to do is set root as median and all of its subtrees need to take the median of its
resulting arrays.

So if we have array = [1,2,3,4,5,6,7,8,9,10]

                    5
            2               8
        1       3        7      9
                  4     6           10

- If array is empty then return
- Perform binary search on array and take the middle number and set as root
- root's left = the recurse of the same function but with the array of all the numbers
    before the middle number
- root's right = the recurse of the same function but with the array of all the numbers
    after the middle number
"""


class TreeNode():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def minimal_tree(nums):
    if not nums:
        return
    middle = len(nums)/2
    root = TreeNode(nums[middle])
    root.left = minimal_tree(nums[:middle])
    root.right = minimal_tree(nums[middle+1:])
    return root
