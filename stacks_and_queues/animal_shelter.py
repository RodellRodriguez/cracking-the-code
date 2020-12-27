'''
An animal shelter, which holds only dogs and cats, operates on a strictly "first in, first
out" basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter,
or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of
that type). They cannot select which specific animal they would like. Create the data structures to
maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog,
and dequeueCat. You may use the built-in Linked list data structure.
'''
'''
Person must adopt either the overall oldest of both dogs and cats or they can select
dog or cat and will receive the oldest in respect to the type of animal they choose

So how to keep track of the oldest overall and yet know the oldest if we want to filter by
category? If we want to find the oldest per category we could have a queue for each type.
So we we could have a cat queue and a dog queue where the oldest cat would be the first
node of that queue and the oldest dog would be the oldest dog of that queue.

Now how to select the oldest overall? We could attach a timestamp data to each of the nodes
and so if we want to return the oldest pet overall then we peek at the first nodes of both animal queues
and select the node with the older timestamp.


How many classes? Well we have a dog, cat, queue system.
    Node
      - Attributes
        - animal_type
        - next
        - timestamp
    Queue
      - Attributes
        - first
        - last
        - animal_type
      - Methods
        - enqueue
        - dequeue
    QueueSystem
      - Attributes
        - queues: hash_table where you supply the animal type and you get the queue for that animal type
      - Methods
        - enqueueCat
        - enqueueDog
        - dequeueCat
        - dequeueDog
        - dequeueAny
'''
import time


class Node:
    def __init__(self, type, name):
        self.type = type
        self.name = name
        self.next = None
        self.timestamp = time.time()

class Queue:
    def __init__(self, type):
        self.first = None
        self.last = None
        self.animal_type = type

    def enqueue(self, name):
        new_node = Node(self.animal_type, name)
        if not self.first:
            self.first = self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node

    def dequeue(self):
        assert self.first is not None
        dequeued_node = self.first
        self.first = self.first.next
        if self.first is None:
            self.last = None
        return dequeued_node

    def peek(self):
        assert self.first is not None
        return self.first


class AnimalQueue:
    def __init__(self):
        self.queues = {'cat': Queue('cat'), 'dog': Queue('dog')}

    def enqueueCat(self, name):
        self.queues.get('cat').enqueue(name)

    def dequeueCat(self):
        return self.queues.get('cat').dequeue()

    def enqueueDog(self, name):
        self.queues.get('dog').enqueue(name)

    def dequeueDog(self):
        return self.queues.get('dog').dequeue()

    def dequeueAny(self):
        # returns oldest animal regardles of type
        dog = self.queues.get('dog').peek()
        cat = self.queues.get('cat').peek()
        if dog.timestamp < cat.timestamp:
            return self.dequeueDog()
        else:
            return self.dequeueCat()


animal_adoption = AnimalQueue()
animal_adoption.enqueueCat('Garfield')
animal_adoption.enqueueCat('Cheshire')
animal_adoption.enqueueDog('Goofy')
animal_adoption.enqueueDog('Rufus')
animal = animal_adoption.dequeueAny()
assert animal.name == 'Garfield'
assert animal.type == 'cat'
animal = animal_adoption.dequeueDog()
assert animal.name == 'Goofy'
assert animal.type == 'dog'
animal = animal_adoption.dequeueCat()
assert animal.name == 'Cheshire'
assert animal.type == 'cat'
