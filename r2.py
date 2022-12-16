class Node:
    
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.root = None
        
    def insert_end(self, value): #add to the end of the list - 38->19->69->12->24->59->95
        if self.root is None: #if the list is empty
            self.root = Node(value) #create a new node
        else: #if the list is not empty
            current = self.root #start at the root
            while current.next != None: #while the next node is not empty
                current = current.next #move to the next node
            current.next = Node(value) #create a new node at the end of the list
    
            current = current.next
    
    def printList(self):
        current = self.root
        while current is not None:
            print(current.value)
            current = current.next
    
    def sortList(self):
        current = self.root
        while current is not None:
            if current.next is not None:
                if current.value > current.next.value:
                    temp = current.value
                    current.value = current.next.value
                    current.next.value = temp
            current = current.next

myTree = LinkedList()
myTree.insert_end(1)
myTree.insert_end(25)
myTree.insert_end(5)
myTree.insert_end(3)


myTree.insert_end(45)
myTree.insert_end(2)
myTree.insert_end(4)
print(myTree.sortList())
print(myTree.printList())