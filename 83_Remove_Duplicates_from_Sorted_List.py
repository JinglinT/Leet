class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        while p:
            if p.next and p.val == p.next.val:
                p.next = p.next.next
            else:
                p = p.next
        return head
