class Node:
    
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.root = None
    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            current = self.root
            while current.next != None:
                current = current.next
            current.next = Node(value)
    
    def NodeCount(self):
        current = self.root
        count = 0
        while current != None:
            count += 1
            current = current.next
        return count

    def indexValue(self, index):
        current = self.root
        for i in range(index):
            current = current.next
        return current.value

    def reverse(self, node):
        if node.next == None:
            self.root = node
            return
        self.reverse(node.next)
        q = node.next
        q.next = node
        node.next = None

    
    def deleteNode(self, position):
        if position == 0:
            self.root = self.root.next
        else:
            current = self.root
            for i in range(position-1):
                current = current.next
            current.next = current.next.next

    def printList(self):
        current = self.root
        while current != None:
            print(current.value, end="->")
            current = current.next


myTree = LinkedList()
myTree.insert(38)
myTree.insert(19)
myTree.insert(69)
myTree.insert(12)
myTree.insert(24)
myTree.insert(59)
myTree.insert(95)

print(myTree.printList())
print(myTree.NodeCount())

print(myTree.indexValue(3))

myTree.reverse(myTree.root)
print(myTree.printList())

print(myTree.deleteNode(3))
print(myTree.printList())