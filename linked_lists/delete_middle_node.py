'''
Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
that node.

EXAMPLE
lnput:the node c from the linked lista->b->c->d->e->f
Result: nothing is returned, but the new linked list looks like a->b->d->e- >f
'''
'''
So we know that the node that we are given is the middle node and that we
can only have access to that node.

What we need to solve is what does it mean to delete the node? It means we no
longer want the value in the current node, we want the value of the next node to be pointed to
and the current node to longer exist.

So what if we keep the current node but overwrite its current value with the next node's attributes
and then delete that node? We technically don't delete the current node but we effectively accomplish
what we really want to happen: the current value of the node to disappear and for the next node's value
to be pointed to by the prev node.

The drawback to this solution is what if the given node is the last node, but Im assuming that
that wont happen. But if we want to handle that situation then if the true goal is deleting the middle
node then we could just exit the function and dont delete anything
'''

from linked_list import LinkedList


def delete_middle_node(node):
    node.data = node.next.data
    node.next = node.next.next


ll = LinkedList()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(5)
delete_middle_node(ll.head.next.next)
assert ll.get_as_a_list() == [1,2,4,5]
