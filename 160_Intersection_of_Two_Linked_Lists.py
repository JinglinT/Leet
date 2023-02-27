class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pA = headA
        pB = headB

        while pA != pB:
            if not pA:
                pA = headB
            elif not pB:
                pB = headA
            else:
                pA = pA.next
                pB = pB.next

        return pA
