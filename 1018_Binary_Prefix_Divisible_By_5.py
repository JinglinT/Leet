class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:

        res = []
        x = 0

        for n in nums:
            x = x * 2 + n
            if x % 5 == 0:
                res.append(True)
            else:
                res.append(False)

        return res
