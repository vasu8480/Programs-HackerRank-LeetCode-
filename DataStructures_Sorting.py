# File: 1 Queue.py
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
# File: 2 Deque.py
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


# File: 3 Stack.py
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

# File: 4 stack using 2queues.py
#implement stack using two queues

class Stack:
    def __init__(self):
        self.q1 = [] #queue 1
        self.q2 = [] #queue 2
        self.size = 0
    def push(self, data):
        self.q1.append(data) #we append to q1
        self.size += 1 #we increase the size
    def pop(self):
        if self.size == 0:   #if the size is 0, we return None
            return None    #if the size is 1, we return the last element of q1
        while len(self.q1) > 1:  #we pop everything but the last element of q1 and append it to q2
            self.q2.append(self.q1.pop(0))  #we pop the last element of q1 and return it
        self.q1, self.q2 = self.q2, self.q1  #we swap q1 and q2
        self.size -= 1    #we decrease the size
        return self.q2.pop()  #we return the last element of q2
    def top(self): 
        if self.size == 0:   #if the size is 0, we return None
            return None   #if the size is 1, we return the last element of q1
        return self.q1[-1] #we return the last element of q1
    def __len__(self): 
        return self.size  #we return the size
    def __str__(self):
        return str(self.q1) #we return the queue
my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
print(my_stack)
print(my_stack.pop())
print(my_stack)
print(my_stack.top())
print(my_stack)


#--------------------------------------------------------------------------------------

from collections import deque
class MyStack:

    def __init__(self):
        self.q = deque() #we use a deque as a queue

    def push(self, x: int) -> None:
        self.q.append(x) #we just append the element to the queue

    def pop(self) -> int:
        for i in range(len(self.q)-1):
            self.q.append(self.q.popleft()) #we pop everything but the last one (and also we append them back)
        return self.q.popleft() #we pop the last one and not append it back

    def top(self) -> int:
        return self.q[-1] #we return the last element of the queue

    def empty(self) -> bool:
        return len(self.q) == 0 #if the length of the queue is 0, then it's empty
    def __repr__(self):
        return str(self.q) #to print the stack

my_stack = MyStack()
my_stack.push(1)
my_stack.push(2)
print(my_stack)
print(my_stack.top()) #2
print(my_stack.pop()) #2
print(my_stack.empty()) #False
print(my_stack.pop()) #1
print(my_stack.empty()) #True



# File: 5 LinkedLists.py
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

# File: 6 BinarySearchTree.py
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
    def __str__(self) -> str:
        return str(self.root.value)

myTree = BinarySearchTree()
myTree.insert(10)
myTree.insert(5)
myTree.insert(13)
myTree.insert(11)
myTree.insert(2)
myTree.insert(16)
myTree.insert(7)
print(myTree)
print(myTree.contains(7))
print(myTree.contains(8))
print(myTree.minOfNode(myTree.root).value)
print(myTree.maxOfNode(myTree.root).value)

# File: 7 BFS_DFS.py
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

# File: 8 Graph.py
class Graph:
    def __init__(self):
        self.adjDict = {}

    def addVertex(self, vertex):
        if vertex not in self.adjDict.keys():
            self.adjDict[vertex] = []
            return True
        return False

    def addEdge(self, v1, v2):
        if v1 in self.adjDict.keys() and v2 in self.adjDict.keys():
            self.adjDict[v1].append(v2)
            self.adjDict[v2].append(v1)
            return True
        return False

    def removeEdge(self, v1, v2):
        if v1 in self.adjDict.keys() and v2 in self.adjDict.keys():
            try:
                self.adjDict[v1].remove(v2)
                self.adjDict[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False

    def removeVertex(self, vertex):
        if vertex in self.adjDict.keys():
            for relatedVertex in self.adjDict[vertex]:
                self.adjDict[relatedVertex].remove(vertex)
            del self.adjDict[vertex]
            return True
        return False
    
    def printGraph(self):
        for vertex in self.adjDict:
            print(vertex, '->', self.adjDict[vertex]) 
myGraph = Graph()
myGraph.addVertex('A')
myGraph.addVertex('B')
myGraph.addVertex('C')
myGraph.addVertex('D')

myGraph.addEdge('A', 'B')   
myGraph.addEdge('A', 'C')
myGraph.addEdge('B', 'D')
myGraph.addEdge('C', 'D')
print(myGraph.adjDict)
myGraph.printGraph()

myGraph.removeEdge('A', 'B')
print(myGraph.adjDict)
myGraph.printGraph()

# File: fib_sum.py
#dynamic programming bottom up
cache = {}
def fibonacci(n):
    cache[0] = 0
    cache[1] = 1

    for i in range(2, n + 1):
        cache[i] = cache[i - 1] +  cache[i - 2]

    return cache[n]
print(fibonacci(10000))
#-----------------------------------------------------------------------------------------------------

def fibonacci(n):
  a = 0
  b = 1
  for i in range(2, n + 1):
      fi = b + a
      b, a = fi, b
  return fi

print(fibonacci(10000))
# File: seive.py
#seive of eratosthenes
def sieve(n):
		if n<=2: # if n is less than 2, return empty list
			return [] #no prime numbers
		is_prime = [True] * n #create a list of booleans
		is_prime[0] = False # 0 is not prime
		is_prime[1] = False # 1 is not prime

		for i in range(2, int(n**0.5)+1):
			x = i*i  #multuiples of i are not prime
			while x < n: 
				is_prime[x] = False 	
				x += i 

		return [i for i in range(n) if is_prime[i] ] 	

		

print(sieve(12554))  # runtime 0.0009970664978027344

# File: 1 Sorting_all.py
def mergeSort(arr):
    if len(arr) == 1:
        return arr
    midPoint = int(len(arr)/2)
    leftPart = arr[:midPoint]
    rightPart = arr[midPoint:]
    return merge(mergeSort(leftPart), mergeSort(rightPart))

def merge(arr1, arr2):
    firstPointer = 0
    secondPointer = 0
    mergedList = []

    while firstPointer < len(arr1) and secondPointer < len(arr2):
        if arr1[firstPointer] < arr2[secondPointer]:
            mergedList.append(arr1[firstPointer])
            firstPointer += 1
        else:
            mergedList.append(arr2[secondPointer])
            secondPointer += 1
    
    while firstPointer < len(arr1):
        mergedList.append(arr1[firstPointer])
        firstPointer += 1
    while secondPointer < len(arr2):
        mergedList.append(arr2[secondPointer])
        secondPointer += 1
    return mergedList

print(mergeSort([8,69,89,85,7885,146,98,464,678,648,875,47,845,8474,854,785,74,548,44,78,75]))

def quickSort(arr, left=0, right=None):
    if right == None:
        right = len(arr) - 1
    if left < right:
        pivotIndex = pivot(arr, left, right)
        quickSort(arr, left, pivotIndex-1)  
        quickSort(arr, pivotIndex+1, right)       
    return arr

def pivot(arr, pivotIndex, endIndex):
    swapIndex = pivotIndex
    for i in range(pivotIndex+1, endIndex+1):
        if arr[i] < arr[pivotIndex]:
            swapIndex += 1
            arr[swapIndex], arr[i] = arr[i], arr[swapIndex]
    arr[pivotIndex], arr[swapIndex] = arr[swapIndex], arr[pivotIndex]
    return swapIndex

print(quickSort([8,69,89,85,7885,146,98,464,678,648,875,47,845,8474,854,785,74,548,44,78,75]))

def heapSort(arr):
    n=len(arr)
    for i in range(n-1,-1,-1):
        heapify(arr,n,i)
    for i in range(n-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]
        heapify(arr,i,0)
    return arr

def heapify(arr,n,i):
    largest=i
    l=2*i+1
    r=2*i+2
    if l<n and arr[i]<arr[l]:
        largest=l
    if r<n and arr[largest]<arr[r]:
        largest=r
    if largest!=i:
        arr[i],arr[largest]=arr[largest],arr[i]
        heapify(arr,n,largest)

print(heapSort([8,69,89,85,7885,146,98,464,678,648,875,47,845,8474,854,785,74,548,44,78,75]))