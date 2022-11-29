class stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def isEmpty(self):
        return self.items == []
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
    def __str__(self):
        return str(self.items)
    def __repr__(self):
        return str(self.items)
mystack = stack()
mystack.push(1)
mystack.push(2)
print(mystack)
print(mystack.pop())
print(mystack.isEmpty())
mystack.pop()
mystack.push(5)
print(mystack.size())
print(mystack)
