class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:

        minNum = min(nums)
        maxNum = max(nums)

        if maxNum - minNum <= k * 2:
            return 0

        return maxNum - minNum - k * 2
