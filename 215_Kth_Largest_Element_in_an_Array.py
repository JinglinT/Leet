class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        def partition(start, end):
            pivot = nums[start]

            i = start + 1
            j = end

            while True:
                while i <= end and nums[i] <= pivot:
                    i += 1
                while j >= start and nums[j] > pivot:
                    j -= 1

                if i > j:
                    break

                nums[i], nums[j] = nums[j], nums[i]

            nums[start], nums[j] = nums[j], nums[start]

            return j

        random.shuffle(nums)

        left = 0
        right = len(nums) - 1

        while left <= right:
            p = partition(left, right)

            if len(nums) - p == k:
                return nums[p]
            elif len(nums) - p < k:
                right = p - 1
            elif len(nums) - p > k:
                left = p + 1

        return None
