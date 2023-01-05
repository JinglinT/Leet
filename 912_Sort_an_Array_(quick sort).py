class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def helper(start, end):
            if end - start <= 1:
                return
            p = partition(start, end)
            helper(start, p)
            helper(p + 1, end)

        def partition(start, end):
            pivot = nums[start]
            i = start + 1
            j = end - 1

            while True:
                while i < end and nums[i] <= pivot:
                    i += 1
                while j > start and nums[j] > pivot:
                    j -= 1

                if i > j:
                    break

                nums[i], nums[j] = nums[j], nums[i]

            nums[start], nums[j] = nums[j], nums[start]

            return j

        random.shuffle(nums)

        helper(0, len(nums))

        return nums
