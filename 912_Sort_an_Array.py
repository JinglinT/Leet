class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def sort(left, right):
            if right - left <= 1:
                return
            mid = (left + right) // 2
            sort(left, mid)
            sort(mid, right)
            merge(left, mid, right)

        def merge(left, mid, right):
            temp = []

            i = left
            j = mid

            while i < mid or j < right:
                if i == mid:
                    temp.append(nums[j])
                    j += 1
                elif j == right:
                    temp.append(nums[i])
                    i += 1
                elif nums[i] < nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:  # nums[j] <= nums[i]:
                    temp.append(nums[j])
                    j += 1

            m = 0
            for k in range(left, right):
                nums[k] = temp[m]
                m += 1

        sort(0, len(nums))

        return nums
