'''
How would you design a stack which, in addition to push and pop, has a function min
which returns the minimum element? Push, pop and min should all operate in 0(1) time.
'''
'''
We want to keep track of the minimum element. What are all of the scenarios to expect when keeping track
of the minimum element?
    1. We don't have a minimum element designated and the stack is empty and a new number gets pushed
    2. We have a minimum element and that number gets popped
    3. We have a minimum element and the number that gets pushed is smaller than current minimum element
    4. We have a minimum element and one number remains in the stack and that gets popped

Scenarios 1, 3, and 4 are simple to handle. Scenario 2 we would need to find out what the new minimum would be.

One solution is if the current minimum gets popped then we linearly search through the entire stack to find the
new minimum. Too long

A faster solution is to have each number also contain data that knows what the minimum number is based on
all of the numbers that came before that number in the stack i.e. the substack.

To optimize further, we can optimize the space of that solution by keeping a 2nd stack that tracks the mins only
and push on that stack when we have a new min and pop that stack when the min gets removed the first stack. This
solves the issue where each node keeps repeatedly having the same min information.
'''

class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        # min attribute tracks the min number of this node's substack including itself
        self.min = None


class StackMin:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = StackNode(data)
        if self.top:
            new_node.min = min(new_node.data, self.top.min)
        else:
            new_node.min = new_node.data
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.top:
            raise Exception("Stack is empty, you can't pop an empty stack.")
        node_to_be_popped = self.top
        self.top = self.top.next
        return node_to_be_popped.data

    def min(self):
        if not self.top:
            raise Exception("Stack is empty, there is not min value.")
        return self.top.min


stack = StackMin()
stack.push(5)
stack.push(2)
stack.push(11)
stack.push(-4)
assert stack.min() == -4
stack.pop()
assert stack.min() == 2
stack.pop()
stack.pop()
assert stack.min() == 5
stack.pop()
