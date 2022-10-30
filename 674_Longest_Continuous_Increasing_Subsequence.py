class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:

        res = 1
        count = 1

        for i in range(len(nums) - 1):
            if nums[i + 1] > nums[i]:
                count += 1
                res = max(res, count)
            else:
                count = 1

        return res
