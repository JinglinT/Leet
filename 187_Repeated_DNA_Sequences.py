class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:

        dic = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        nums = [dic[x] for x in s]

        length = 10
        base = 4
        lb = base ** (length - 1)

        seen = set()
        res = set()

        windowHash = 0

        left = right = 0

        while right < len(nums):
            windowHash = windowHash * base + nums[right]

            right += 1

            if right - left == length:
                if windowHash in seen:
                    res.add(s[left:right])
                else:
                    seen.add(windowHash)

                windowHash = windowHash - nums[left] * lb

                left += 1

        return list(res)
