class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        for i in range(len(s) - 1, -1, -1):
            if not s[i].isspace():
                length = 0
                for j in range(i, -1, -1):
                    if not s[j].isspace():
                        length += 1
                    else:
                        break
                return length
        return 0
