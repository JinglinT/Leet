class Solution:
    def firstUniqChar(self, s: str) -> int:
        ch_count = collections.Counter(s)

        for i in range(len(s)):
            if ch_count[s[i]] == 1:
                return i

        return -1
