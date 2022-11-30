class Deque():
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def addFront(self, item):
        self.items.append(item)
    def addRear(self, item):
        self.items.insert(0,item)
    def removeFront(self):
        return self.items.pop()
    def removeRear(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)
    def __str__(self):
        return str(self.items)


myDeque = Deque()
myDeque.addFront('hello')
print(myDeque)
myDeque.addRear('world')
print(myDeque)
print(myDeque.size())
myDeque.removeFront()
print(myDeque)
myDeque.removeRear()
print(myDeque)

