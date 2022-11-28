class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:

        minNum = min(nums)

        res = 0

        while minNum > 0:
            res += minNum % 10
            minNum //= 10

        return 0 if res % 2 == 1 else 1
