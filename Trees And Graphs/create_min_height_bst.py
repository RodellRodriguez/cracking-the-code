"""
4.3:
Given a sorted(increasing order) array w/ unique integer elements, write an algorithm to create a
BST w/ minimal height
"""

def sortedArrayToBST(nums):
  size = len(nums)
  if size == 0: return None
  if size == 1: return TreeNode(nums[0])
  mid = (size-1)//2
  root = TreeNode(nums[mid])
  root.left = sortedArrayToBST(nums[:mid])
  root.right = sortedArrayToBST(nums[mid+1:])
  return root
