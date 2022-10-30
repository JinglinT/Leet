class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:

        dic = {}

        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = [1, i, i]
            else:
                dic[nums[i]][0] += 1
                dic[nums[i]][2] = i

        res = 0
        max_freq = 0

        for lst in dic.values():
            if lst[0] == max_freq:
                res = min(res, lst[2] - lst[1] + 1)
            elif lst[0] > max_freq:
                max_freq = lst[0]
                res = lst[2] - lst[1] + 1

        return res
