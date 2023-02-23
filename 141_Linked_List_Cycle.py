class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        fast = head.next
        while fast:
            if head == fast:
                return True
            if not fast.next:
                return False
            fast = fast.next.next
            head = head.next
        return False
