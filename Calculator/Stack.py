import EmptyStackException
import Entry

class Stack(Entry):
    def __init__(self):
        self.items = []

    def sizeof(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise EmptyStackException("There is nothing to pop")
        return self.items.remove[self.sizeof - 1]

    def top(self):
        if self.is_empty():
            raise EmptyStackException("There is nothing at the top of empty stack")
        return self.items[-1]