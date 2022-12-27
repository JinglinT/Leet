class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:

        def sort(left, right):
            if right - left <= 1:
                return
            mid = (left + right) // 2
            sort(left, mid)
            sort(mid, right)
            merge(left, mid, right)

        def merge(left, mid, right):

            nonlocal count

            start = end = mid

            for i in range(left, mid):
                while start < right and preSum[start] - preSum[i] < lower:
                    start += 1
                while end < right and preSum[end] - preSum[i] <= upper:
                    end += 1
                count += end - start

            temp = []

            i = left
            j = mid

            while i < mid or j < right:
                if i == mid:
                    temp.append(preSum[j])
                    j += 1
                elif j == right:
                    temp.append(preSum[i])
                    i += 1
                elif preSum[i] < preSum[j]:
                    temp.append(preSum[i])
                    i += 1
                else:
                    temp.append(preSum[j])
                    j += 1

            j = 0
            for i in range(left, right):
                preSum[i] = temp[j]
                j += 1

        preSum = [0] * (len(nums) + 1)

        for i in range(1, len(preSum)):
            preSum[i] = preSum[i - 1] + nums[i - 1]

        count = 0

        sort(0, len(preSum))

        return count
