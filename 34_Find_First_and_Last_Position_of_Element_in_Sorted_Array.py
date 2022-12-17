class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def findLeftBound():
            left = 0
            right = len(nums) - 1

            res = None

            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    res = mid
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return -1 if res == None else res

        def findRightBound():
            left = 0
            right = len(nums) - 1

            res = None

            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    res = mid
                    left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return -1 if res == None else res

        return [findLeftBound(), findRightBound()]
