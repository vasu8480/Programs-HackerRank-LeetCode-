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


