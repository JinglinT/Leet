class Solution:
    def fib(self, n: int) -> int:

        if n == 0:
            return 0
        if n == 1:
            return 1

        first = 0
        second = 1

        for i in range(n - 1):
            third = first + second
            first = second
            second = third

        return second
