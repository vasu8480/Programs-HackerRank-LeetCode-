class Node():
    def __init__(self,value):
        self.value = value
        self.nextNode = None
firstNode = Node(10)
secondNode = Node(20)
thirdNode = Node(30)
firstNode.nextNode = secondNode
secondNode.nextNode = thirdNode
print(firstNode.value)
print(firstNode.nextNode.value)
print(secondNode.nextNode.value)
print(firstNode.nextNode.nextNode.value)

#------------------------------------------------------------
#doubly linked list
class DoublyNode():
    
    def __init__(self,value):
        self.value = value
        self.nextNode = None
        self.prevNode = None
firstNode = DoublyNode(40)
secondNode = DoublyNode(50)
thirdNode = DoublyNode(60)
firstNode.nextNode = secondNode
secondNode.prevNode = firstNode
secondNode.nextNode = thirdNode
thirdNode.prevNode = secondNode
print(firstNode.value)
print(firstNode.nextNode.value)
