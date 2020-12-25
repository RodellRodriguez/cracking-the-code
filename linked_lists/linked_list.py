class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data=None, data_list=None): # inserts new node at the end of the LL
        def _insert(data):
            new_node = Node(data)
            if not self.head:
                self.head = new_node
            else:
                # never manipulate self.head directly since we always want access to the head of the LL
                current_node = self.head
                while current_node.next:
                    current_node = current_node.next
                current_node.next = new_node
        if data:
            _insert(data)
        elif data_list:
            for data in data_list:
                _insert(data)

    def print(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def delete(self, data):
        prev = None
        current = self.head
        while current:
            if current.data == data:
                if prev:
                    prev.next = current.next
                else:
                    # for when we need to delete the head
                    self.head = self.head.next
                return
            prev = current
            current = current.next
        raise LookupError('{} is not in the linked list'.format(data))

    def get_as_a_list(self):
        new_list = []
        current_node = self.head
        while current_node:
            new_list.append(current_node.data)
            current_node = current_node.next
        return new_list
