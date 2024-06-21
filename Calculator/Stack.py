from CustomExceptions import EmptyStackException
import Entry

class Stack(Entry):
    # Constructor for new stack
    def __init__(self):
        self.items = []

    # Returns the size of the stack
    def sizeof(self):
        return len(self.items)

    # Adds a new item to top of stack
    def push(self, item):
        self.items.append(item)

    # Removes and returns the item at the top of the stack
    def pop(self):
        if self.is_empty():
            raise EmptyStackException("There is nothing to pop")
        return self.items.remove[self.sizeof - 1]
    
    # Returns the item at the top of the stack
    def top(self):
        if self.is_empty():
            raise EmptyStackException("There is nothing at the top of empty stack")
        return self.items[self.sizeof - 1]