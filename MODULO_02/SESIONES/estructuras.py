class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return None if self.is_empty() else self.stack.pop()

    def peek(self):
        return None if self.is_empty() else self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return None if self.is_empty() else self.queue.pop(0)

    def front(self):
        return None if self.is_empty() else self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


class Deque:
    def __init__(self):
        self.deque = []

    def add_front(self, item):
        self.deque.insert(0, item)

    def add_rear(self, item):
        self.deque.append(item)

    def remove_front(self):
        return None if self.is_empty() else self.deque.pop(0)

    def remove_rear(self):
        return None if self.is_empty() else self.deque.pop()

    def is_empty(self):
        return len(self.deque) == 0

    def size(self):
        return len(self.deque)


class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item, priority):
        self.queue.append((priority, item))
        self.queue.sort()

    def dequeue(self):
        return None if self.is_empty() else self.queue.pop(0)[1]

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)
