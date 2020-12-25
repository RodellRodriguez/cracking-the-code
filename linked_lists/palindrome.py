'''
Implement a function to check if a linked list is a palindrome.
'''
'''
1 -> 2 -> 3 -> 3 -> 2 -> 1 - even
while runner_node. Stops when runner_node is None

1 -> 2 -> 3 - odd
while runner_node.next. Stops when runner_node is the last node

To check if a linked list is a palindrome it needs to read the same forwards and backwards.
We cant check backwards so we need to find a way to find the middle point of the palindrome
and then compare the first half and the second half of the linked list.

But the way we need to compare the first half and the second half we need to be careful of the order.
Specifically in the example above we know that we need to compare 1 -> 2 (first half) with 2 -> 1 (2nd half).
We can only go forwards and not backwards so how do we reverse that 2 -> 1 into 1 -> 2?

So this problem is broken down into 3 parts:
    1. Find the middle node(s)
        - Account for both even and odd number of nodes
    2. Reverse the second half of the linked list
        - If even nodes then include the half point node in the reversal
        - If odd nodes then don't include the half point node in the reversal
    3. Compare the first half of the linked list to the second half of the linked list

1.) We can find the middle node by doing the runner node technique by having pointer 1 move one node at a time
and then pointer 2 move 2 nodes at a time. When pointer 2's next is None then then point 1 will be at the middle node.

'''

from linked_list import LinkedList


def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev

def palindrome(head):
    # First find the middle node
    middle_node = head
    runner_node = head
    while runner_node and runner_node.next: # to account for both even and odd number nodes
        middle_node = middle_node.next
        runner_node = runner_node.next.next
    if runner_node: # we have odd number nodes
        # reverse LL starting AFTER the middle node
        second_half = reverse_linked_list(middle_node.next)
    else: # we have even number nodes
        # reverse LL starting WITH the middle node
        second_half = reverse_linked_list(middle_node)
    # compare first half of LL to second half of LL
    first_half = head
    while second_half:
        if first_half.data != second_half.data:
            return False
        first_half = first_half.next
        second_half = second_half.next
    return True


ll = LinkedList()
ll.insert(data_list=[1,2,3,3,2,1])
assert palindrome(ll.head) == True
ll = LinkedList()
ll.insert(data_list=[0,3,2,3,0])
assert palindrome(ll.head) == True
ll = LinkedList()
ll.insert(data_list=[0,3,2,3,0,2423])
assert palindrome(ll.head) == False
