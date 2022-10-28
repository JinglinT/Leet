class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        res = total = sum(nums[:k])

        for i in range(k, len(nums)):
            total = total - nums[i - k] + nums[i]
            res = max(res, total)

        return res / k
