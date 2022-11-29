class Queue:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def __str__(self):
        return str(self.items)
    def __repr__(self):
        return str(self.items)
myqueue = Queue()
myqueue.enqueue(1)
myqueue.enqueue(2)
print(myqueue)
print(myqueue.dequeue())
print(myqueue.isEmpty())
myqueue.dequeue()
myqueue.enqueue(5)
print(myqueue.size())
print(myqueue)