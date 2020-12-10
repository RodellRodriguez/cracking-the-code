'''
Implement an algorithm to find the kth to last element of a singly linked list.
'''
'''
1 -> 2 -> 3 -> 4 -> 5

0 < k <= N where N is num of nodes
if k = 2 then return 4

desired_node_position = N - k + 1


- Count number of nodes. Call it N
- Create counter = 1
- Start at head and traverse each node, increasing counter by 1 each time. Stop
when the counter == N - k + 1
- Return the node that you're at

You can make this slightly faster by not needing to traverse the ll twice.
You dont need to find out what the length is. If you set p1 =head and p2 and p1 + k-1 nodes away,
then when you iterate both p1 and p2 one node at a time until p2 is at the final node, then p1
will then be at N-k-1'th node which is what we want. The -1 part is dependent on what we want the bounds
of k to be. So if we want  0 < k <= N then we need this -1
'''

from linked_list import LinkedList


def return_kth_to_last(head, k):
    current = head
    runner = head
    for i in range(k-1):
        if not runner:
            return None
        runner = runner.next
    while runner.next:
        current = current.next
        runner = runner.next
    return current.data


ll = LinkedList()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(5)
k = 3
assert return_kth_to_last(ll.head, k) == 3
