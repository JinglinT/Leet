class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n

        while left <= right:
            mid = (left + right) // 2
            if guess(mid) == 0:
                return mid
            if guess(mid) == -1:
                right = mid - 1
            else:
                left = mid + 1
