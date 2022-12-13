class Solution:
    root=None
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head== None:
            return None
        if head.next==None:
            self.root=head
            return head
        self.reverseList(head.next)
        head.next.next=head
        head.next=None
        return self.root

#------------------------------------------------------------
class Solution:
    root=None
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        while head:
            temp=head.next
            head.next=prev
            prev=head
            head=temp
        return prev