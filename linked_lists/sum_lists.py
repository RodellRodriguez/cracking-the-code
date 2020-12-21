'''
You have two numbers represented by a linked list, where each node contains a single
digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
function that adds the two numbers and returns the sum as a linked list.
EXAMPLE
Input: (7-> 1 -> 6) + (5 -> 9 -> 2). That is, 617 + 295.
Output: 2 -> 1 -> 9. That is, 912.
FOLLOW UP
Suppose the digits are stored in forward order. Repeat the above problem.
EXAMPLE
lnput:(6 -> 1 -> 7) + (2 -> 9 -> 5).That is, 617 + 295.
Output: 9 - > 1 -> 2. That is, 912.
'''
'''
A good example would be two linked lists with different number of digits and also where we would need to carry the 1
especially if this occurs in the most significant digit

REVERSE ORDER:
We could have 2 head pointers and traverse each linked list and add each node to each other.
    If carry_one == True then add plus 1 to the sum. Then set carry_one=False.
    If the sum is > 9 then subtract the sum by 10 then set carry_one=True and insert subtracted sum to new LL
    Keep going until both LL's reach the end
    If only one of the LL's end then insert the rest of the remaining values of the LL into the new LL
If at the very end that carry_one =True then we insert a 1 into the new LL
I'm going to assume that we won't get any 0's in the the most significant digit.

To-Do: Complete code
'''

from linked_list import LinkedList


def sum_lists_reverse_order(head_one, head_two, new_linked_list):
    carry_one = False
    current_one = head_one
    current_two = head_two
    while current_one and current_two:
        sum = current_one.data + current_two.data
        if carry_one:
            sum += 1
            carry_one = False
        if sum > 9:
            sum -= 10
            carry_one = True
        new_linked_list.insert(sum)
        current_one = current_one.next
        current_two = current_two.next
    # handle if only one of the ll's ended
    while current_one:
        if carry_one:
            sum += 1
            carry_one = False
        if sum > 9:
            sum -= 10
            carry_one = True
        new_linked_list.insert(current_one.data)
    while current_two:
        current_one = current_one.next
        if carry_one:
            sum += 1
            carry_one = False
        if sum > 9:
            sum -= 10
            carry_one = True
        new_linked_list.insert(current_two.data)
        current_two = current_two.next
    # handle if both ll's ended
    if carry_one:
        new_linked_list.insert(1)
        carry_one = False
    return new_linked_list
