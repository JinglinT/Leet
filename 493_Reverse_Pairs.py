class Solution:
    def reversePairs(self, nums: List[int]) -> int:

        def sort(left, right):
            if right - left <= 1:
                return
            mid = (left + right) // 2
            sort(left, mid)
            sort(mid, right)
            merge(left, mid, right)

        def merge(left, mid, right):

            nonlocal count

            end = mid
            for i in range(left, mid):
                while end < right and nums[i] > 2 * nums[end]:
                    end += 1
                count += end - mid

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
                else:
                    temp.append(nums[j])
                    j += 1

            j = 0
            for i in range(left, right):
                nums[i] = temp[j]
                j += 1

        count = 0

        sort(0, len(nums))

        return count
