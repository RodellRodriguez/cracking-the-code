"""
4.1: 
Check if binary tree is balanced. Balanced here means the heights of the twoo subtrees of any node does not
Differ by more than one
"""

def getHeight(root):
  if not root: return 0
  leftHeight = getHeight(root.left)
  if leftHeight == -1: return -1
  rightHeight = getHeight(root.right)
  ifrightHeight == -1: return -1
  if abs(leftHeight - rightHeight) > 1: return -1
  return max(leftHeight, rightHeight) + 1
 
def isBalanced(root):
  if getHeight(root) == -1: return False
  return True
