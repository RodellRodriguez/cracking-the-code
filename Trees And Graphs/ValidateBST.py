"""
4.5:
Implement a function to check if a Binary Tree is a BST
"""

import sys
def checkBST(root):
  return _checkBST(root, -sys.maxsize,sys.maxsize)
  
def _checkBST(root, minVal, maxVal):
  if root:
    if root.val <= minVal or root.val >= maxVal: return False
    if not _checkBST(root.left, minVal, root.val) or not _checkBST(root.right, root.val, maxVal):
      return False
  return True
