'''
Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
before all nodes greater than or equal to x. If x is contained within the list, the values of x only need
to be after the elements less than x (see below). The partition element x can appear anywhere in the
"right partition"; it does not need to appear between the left and right partitions.
EXAMPLE
Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition= 5]
Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
'''
'''
3 -> 2 -> 1
5 -> 8 -> 5 -> 10

First solution is to have two linked lists, one for all of the nodes that come before the partition
and then the nodes that have the values that are equal to or greater than the partition. And then
connect the first linked list to the second linked list

Although the run time will be the same, we can simplify the code of the first solution by thinking
about this 2nd solution where we have a head pointer and a tail pointer that both point to head node.
Now we iterate through each node:
    - if node < parition:
        prepend that node to head and the new head becomes that new node
    - else we know this node >= partition so:
        append that node to tail and then the new tail becomes that new node
Set tail's next to null to end the linked list
'''

from linked_list import LinkedList


def parition(linked_list, partition):
    tail = linked_list.head
    current = linked_list.head
    next = current.next
    while next:
        # if there's a next then we look at the node and then save the next node
        current = next
        next = next.next
        if current.data < partition:
            current.next = linked_list.head
            linked_list.head  = current
        else: # current.data >= partition
            tail.next = current
            tail = current
    tail.next = None
    return linked_list.head


ll = LinkedList()
ll.insert(3)
ll.insert(5)
ll.insert(2)
ll.insert(1)
ll.insert(7)
ll.insert(0)
parition(ll, 5)
assert ll.get_as_a_list() == [0,1,2,3,5,7]
