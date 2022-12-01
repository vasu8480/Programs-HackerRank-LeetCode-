class Solution:
    def removeNthFromEnd(self, head, n: int):
        
        leftPointer = head
        rightPointer = head
        
        while n > 0 and rightPointer: #there is n gap between two pointers
            rightPointer = rightPointer.next
            n -= 1
        
        while rightPointer and rightPointer.next:  # stop when rightPointer.next is None.
            leftPointer = leftPointer.next
            rightPointer = rightPointer.next
                
        if leftPointer == head and not rightPointer: #if we omit this, it won't work on the edge case of one node
            return head.next

        leftPointer.next = leftPointer.next.next #skip the leftPointer.next so it would be out of LinkedList
        
        return head
print(Solution().removeNthFromEnd([1,2,3,4,5], 2))