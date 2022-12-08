class Node:
    
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    
    def __init__(self):
        self.root = None

    def insert(self, value):
        
        newNode = Node(value)
        
        if self.root is None:
            
            self.root = newNode
            return True
        
        tempNode = self.root
        
        while True:
            
            if newNode.value == tempNode.value:
                return False
            
            if newNode.value < tempNode.value:
                if tempNode.left is None:
                    tempNode.left = newNode
                    return True
                tempNode = tempNode.left
            
            else: 
                if tempNode.right is None:
                    tempNode.right = newNode
                    return True
                tempNode = tempNode.right

    def contains(self, value):
        tempNode = self.root
        
        while tempNode:
            if value < tempNode.value:
                tempNode = tempNode.left
            elif value > tempNode.value:
                tempNode = tempNode.right
            else:
                return True
        return False
        
    def minOfNode(self,currentNode):
        while currentNode.left:
            currentNode = currentNode.left
        return currentNode
    
    def maxOfNode(self,currentNode):
        while currentNode.right:
            currentNode = currentNode.right
        return currentNode
    def BFS(self):
        currentNode = self.root
        myQueue = []
        values = []
        myQueue.append(currentNode)

        while len(myQueue) > 0:
            currentNode = myQueue.pop(0)
            values.append(currentNode.value)
            if currentNode.left is not None:
                myQueue.append(currentNode.left)
            if currentNode.right is not None:
                myQueue.append(currentNode.right)
        return values
    
    def DFSPreOrder(self):#root, left, right
        values = []
        def traverse(currentNode):
            values.append(currentNode.value)
            if currentNode.left is not None:
                traverse(currentNode.left)
            if currentNode.right is not None:
                traverse(currentNode.right)
        traverse(self.root)
        
        return values

    def DFSPostOrder(self):
        values = []
        def traverse(currentNode):
            if currentNode.left is not None:
                traverse(currentNode.left)
            if currentNode.right is not None:
                traverse(currentNode.right)
            values.append(currentNode.value)
        traverse(self.root)
        return values
    
    def DFSInOrder(self):
        values = []
        def traverse(currentNode):
            if currentNode.left is not None:
                traverse(currentNode.left)
            values.append(currentNode.value) 
            if currentNode.right is not None:
                traverse(currentNode.right) 
        traverse(self.root)
        return values

myTree = BinarySearchTree()
myTree.insert(38)
myTree.insert(19)
myTree.insert(69)
myTree.insert(12)
myTree.insert(24)
myTree.insert(59)
myTree.insert(95)
print(myTree.BFS())
print(myTree.DFSPreOrder())
print(myTree.DFSPostOrder())
print(myTree.DFSInOrder())
