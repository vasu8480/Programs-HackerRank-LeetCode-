class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l = headA
        r = headB
        while l != r:
            l = l.next if l != None else headB
            r = r.next if r != None else headA
        return l