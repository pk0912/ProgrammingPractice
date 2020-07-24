from collections import deque


class UnderflowError(Exception):
    def __init__(self, msg="Underflow Exception"):
        self.msg = msg

    def __str__(self):
        return self.msg


class Queue:
    def __init__(self, max_size):
        self.queue = deque()
        self.max_size = max_size

    def get_max_size(self):
        return self.max_size

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return self.size() == 0

    def enqueue(self, element):
        if self.size() == self.max_size:
            raise OverflowError("Queue overflow error")
        self.queue.append(element)

    def dequeue(self):
        if self.is_empty():
            raise UnderflowError("Queue underflow error")
        return self.queue.popleft()

    def front(self):
        if self.is_empty():
            return None
        return self.queue[0]

    def rear(self):
        if self.is_empty():
            return None
        return self.queue[-1]


q = Queue(3)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q)
print(q.get_max_size())
print(q.size())
# q.enqueue(4)  # Overflow exception
print(q.front())
print(q.rear())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.is_empty())
# print(q.dequeue())  # Underflow exception
