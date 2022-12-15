class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        window = {}

        left = right = 0

        res = 0

        while right < len(s):
            c = s[right]
            window[c] = window.get(c, 0) + 1

            right += 1

            while window[c] > 1:
                window[s[left]] -= 1
                left += 1

            res = max(res, right - left)

        return res
