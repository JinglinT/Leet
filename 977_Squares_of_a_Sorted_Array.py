class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        i = 0
        j = k = len(nums) - 1
        res = [None] * len(nums)

        while i <= j:
            if abs(nums[i]) > abs(nums[j]):
                res[k] = nums[i] ** 2
                i += 1
            else:
                res[k] = nums[j] ** 2
                j -= 1
            k -= 1

        return res
