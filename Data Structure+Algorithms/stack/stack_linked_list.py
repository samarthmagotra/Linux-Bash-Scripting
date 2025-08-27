#   Created by Elshad Karimov
#   Copyright © AppMillers. All rights reserved.
#   www.appmillers.com

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.length = 0

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.length += 1

    def pop(self):
        if self.top is None:
            return None
        popped_node = self.top
        self.top = self.top.next
        self.length -= 1
        return popped_node

    def peek(self):
        return self.top.value if self.top else None

    def is_empty(self):
        return self.top is None

    def clear(self):
        self.top = None
        self.length = 0

    def __len__(self):
        return self.length

    def __str__(self):
        current = self.top
        values = []
        while current:
            values.append(str(current.value))
            current = current.next
        return ' -> '.join(values)

# Example usage
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack)               # 3 -> 2 -> 1
print(stack.pop())         # 3
print(stack.peek())        # 2
print(stack.is_empty())    # False
print(len(stack))          # 2
