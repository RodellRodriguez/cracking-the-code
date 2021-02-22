"""
4.4:
Given a binary tree, design an algorithm which creates a Linked List of all the nodes
At each depth. E.g. if you have a tree with depth D you'll have D linked lists
"""

#My solution utilizes a BFS approach. There is a solution utilizing DFS but I haven't solved it that way
#Will be using a Python list as a "linked list". The concept is all the same

def linkedListAtEachDepth(root):
  queue = [root]
  res = []
  while queue:
    nextQueue, linkedList = [], []
    for node in queue:
      linkedList.append(node)
      if node.left: nextQueue.append(node.left)
      if node.right: nextQueue.append(node.right)
    queue = nextQueue
    res.append(linkedList)
  return res
      
