'''
Write code to remove duplicates from an unsorted linked list.
FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?
'''
'''
So this will be a space vs time tradeoff. We can achieve this is O(N) time compelxity but with
O(N) space complexity if we utilize a hash table to keep track of seen values in a linked list.
If we encounter a value in the LL that exists in hash table then delete that node, otherwise
keep that node but add the value to the hash table

If we priority space complexity then we can reduce the space complxity to O(1) but increase
time complxity to O(N^2) by creating a second pointer to traverse the LL to search for any duplicates
for every node we come across.


'''

from linked_list import LinkedList


def remove_dups_time_efficient(head):
    if not head or not head.next:
        return
    duplicate_lookup = {}
    current_node = head
    prev = None
    while current_node:
        if current_node.data in duplicate_lookup:
            prev.next = current_node.next
        else:
            duplicate_lookup[current_node.data] = True
            prev = current_node
        current_node = current_node.next


def remove_dups_space_efficient(head):
    if not head or not head.next:
        return
    current_node = head
    while current_node:
        prev = current_node
        runner_node = current_node
        while runner_node.next:
            if runner_node.next.data == current_node.data:
                runner_node.next = runner_node.next.next
            else:
                runner_node = runner_node.next
        current_node = current_node.next


ll = LinkedList()
ll.insert(1)
ll.insert(4)
ll.insert(1)
ll.insert(5)
ll.insert(5)
remove_dups_time_efficient(ll.head)
assert ll.get_as_a_list() == [1,4,5]
ll.insert(4)
ll.insert(1)
ll.insert(5)
remove_dups_space_efficient(ll.head)
assert ll.get_as_a_list() == [1,4,5]
