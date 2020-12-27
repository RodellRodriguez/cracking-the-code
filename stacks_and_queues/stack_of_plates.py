'''
Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
threshold. Implement a data structure SetOfStacks that mimics this.

SetOfStacks should be composed of several stacks and should create a new stack once the previous one exceeds capacity.
SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single stack
(that is, pop() should return the same values as it would if there were just a single stack).

FOLLOW UP
Implement a function popAt ( int index) which performs a pop operation on a specific sub-stack.
'''
'''
Requirements:
    - Have a cap at num of nodes in a stack
    - Create a new stack when the cap is reached
    - Pop and push should behave the same as if there was one stack

If we set N = 3 for example then on the 4th node then a substack should be created where stack_1
has the first 3 numbers and then stack_2 has the 4'th number. The top most number should still be the 4th number.
When that 4'th number gets popped then stack_2 should get deleted and SetofStacks should then point to stack_1.
Then when stack_1's nodes all get popped then SetofStacks should be empty

So each sub stack needs to to know its top node as usual but also it needs to know the next substack after itself the same way
a node needs to know the next node after itself. When we say "next" we mean the sub stack that is came before the current substack.
Then SetofStacks needs to know what the current substack to point at.
Also SetofStack's push/pop operations should be delegated to the substack class's push/pop unless :
    - Push: check if the substack is full then SetofStacks creates a new stack, pushes a node onto that new stack, that new stack's next
    is pointed to SetofStack's current topstack, then set topstack == new_stack
    - Pop: check if the substack will be empty after the pop operation so the substack should perform the pop operation as normal
    and then SetofStack's current topstack should then point to current topstack's next sub stack

3 data structures:
    1. Node
        - data
        - next node
    2. Stack
        - top node
        - size (should never exceed max_size)
        - max_size
        - next stack
    3. SetofStacks
        - top stack
        - max_size (sets the size of the sub stacks. Cant change this max size once created)
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self, max_size):
        self.top_node = None
        self.size = 0
        self.max_size = max_size
        self.next_stack = None

    def push(self, data):
        if not self.top_node:
            self.top_node = Node(data)
            self.size = 1
            return
        assert self.size <= max_size
        new_node = Node(data)
        new_node.next = self.top_node
        self.top_node = new_node
        self.size += 1

    def pop(self):
        if not self.top_node:
            raise Exception("Cannot pop an empty stack")
        popped_node = self.top_node
        self.top_node = self.top_node.next
        self.size -= 1
        return popped_node.data

    def isFull(self):
        return self.size == self.max_size

    def isEmpty(self):
        return self.size == 0


class SetOfStacks:
    def __init__(self, max_size):
        assert max_size > 0
        # The max_size for each of the sub stacks
        self.max_size = max_size
        self.top_stack = None

    def push(self, data):
        if not self.top_stack:
            new_stack = Stack(self.max_size)
            new_stack.push(data)
            self.top_stack = new_stack
            return
        if self.top_stack.isFull():
            new_stack = Stack(self.max_size)
            new_stack.push(data)
            new_stack.next_stack = self.top_stack
            self.top_stack = new_stack
            return
        if self.top_stack.size <= self.top_stack.max_size:
            self.top_stack.push(data)

    def pop(self):
        assert self.top_stack is not None
        popped_node = self.top_stack.pop()
        if self.top_stack.isEmpty():
            self.top_stack = self.top_stack.next_stack
        return popped_node


max_size = 2
set_of_stacks = SetOfStacks(max_size)
set_of_stacks.push(5)
set_of_stacks.push(3)
set_of_stacks.push(11)
assert set_of_stacks.pop() == 11
assert set_of_stacks.pop() == 3
