#Given a linked list, print reverse of it using a recursive function.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def reverse(self, node):
        if node.next is None:
            self.head = node
            return
        self.reverse(node.next)
        q = node.next
        q.next = node
        node.next = None
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next
if __name__=='__main__':
    llist = LinkedList()
    llist.push(20)
    llist.push(4)
    llist.push(15)
    llist.push(85)
    print("Given Linked List")
    llist.printList()
    llist.reverse(llist.head)
    print("Reversed Linked List")
    llist.printList()