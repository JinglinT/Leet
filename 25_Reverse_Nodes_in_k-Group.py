class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def reverse(a, b):
            prev = b
            curr = a
            while curr != b:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev

        def reverseK(head, k):
            b = head
            for i in range(k):
                if not b:
                    return head
                b = b.next
            newHead = reverse(head, b)
            head.next = reverseK(b, k)
            return newHead

        return reverseK(head, k)
