"""
4.6:
Write an algorithm to find the next node (in order successor) of a given node in a BST.
You may assume that each node has a link to its parent
"""

"""
1.) Check if that node has a right subtree
2.) If the node has a right subtree then find the left most leaf of that subtree
And return that leaf. Otherwise proceed to step 3
3.) If the node does not have a right subtree then this gets tricky.
This scenario means that its successor must be a node higher up in the BST. 
How high? You keep going up the BST until you find the node that is the
LEFT child of its parent. That means you finally found a parent that is GREATER than the
Node were interested in. Return that parent node.
"""

def inOrderSucc(root, node):
  if root:
    succ = findLeftLeaf(node.right)
    if succ: return succ
    temp = node
    parent = node.parent
    while parent and parent.right == temp:
      temp = parent
      parent = parent.parent
    return parent
  return None
