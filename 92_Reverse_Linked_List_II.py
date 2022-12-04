class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        successor = None

        def reverseN(head, n):
            nonlocal successor
            if n == 1:
                successor = head.next
                return head
            p = reverseN(head.next, n - 1)
            head.next.next = head
            head.next = successor
            return p

        def reverseBetween(head, m, n):
            if m == 1:
                return reverseN(head, n)
            head.next = reverseBetween(head.next, m - 1, n - 1)
            return head

        return reverseBetween(head, left, right)
