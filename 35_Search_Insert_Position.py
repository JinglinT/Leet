class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        middle = None
        while low <= high:
            middle = (low + high) // 2
            if target == nums[middle]:
                return middle
            elif target < nums[middle]:
                high = middle - 1
            else:
                low = middle + 1
        if target > nums[middle]:
            return middle + 1
        return middle
