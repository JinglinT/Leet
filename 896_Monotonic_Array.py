class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:

        increase = decrease = False

        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                increase = True
            elif nums[i] > nums[i + 1]:
                decrease = True

        return not (decrease and increase)
