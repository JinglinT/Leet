class Solution:
    def isHappy(self, n: int) -> bool:
        def getNext(n):
            total = 0
            while n > 0:
                total += (n % 10) ** 2
                n //= 10
            return total

        if n == 1:
            return True

        slow = n
        fast = getNext(n)

        while slow != fast:
            if slow == 1 or fast == 1:
                return True
            slow = getNext(slow)
            fast = getNext(getNext(fast))
        return False
