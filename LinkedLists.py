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
    
    def insert_start(self, value):#add to the start of the list - 99->38->19->69->12->24->59->95
        current = self.root #start at the root
        self.root = Node(value) #create a new node
        self.root.next = current #point the new node to the current root
    
    def NodeCount(self): #count the number of nodes in the list
        current = self.root 
        count = 0
        while current != None:
            count += 1 #increment the count
            current = current.next #move to the next node
        return count #return the count

    def indexValue(self, index): #return the value of the node at the given index
        current = self.root 
        for i in range(index): #loop through the list until the index is reached
            current = current.next #move to the next node
        return current.value #return the value of the node at the given index

    def reverse(self, node): #reverse the list - 95->59->24->12->69->19->38->99
        if node.next == None: 
            self.root = node
            return
        self.reverse(node.next) #recursively call the reverse function
        q = node.next 
        q.next = node 
        node.next = None

    def deleteNode(self, position): #delete the node at the given position
        if position == 0: 
            self.root = self.root.next
        else:
            current = self.root 
            for i in range(position-1): #loop through the list until the position is reached
                current = current.next #move to the next node
            current.next = current.next.next #point the current node to the node after the node to be deleted

    def printList(self): #print the list
        current = self.root
        while current != None: 
            print(current.value, end="->")
            current = current.next

myTree = LinkedList()
myTree.insert_end(38)
myTree.insert_end(19)
myTree.insert_end(69)
myTree.insert_end(12)
myTree.insert_end(24)
myTree.insert_end(59)
myTree.insert_end(95)
myTree.insert_start(99)

print(myTree.printList())
print(myTree.NodeCount()) #8

print(myTree.indexValue(3)) #69

myTree.reverse(myTree.root) #95->59->24->12->69->19->38->99
print(myTree.printList())

print(myTree.deleteNode(3)) #95->59->24->69->19->38->99x
print(myTree.printList())