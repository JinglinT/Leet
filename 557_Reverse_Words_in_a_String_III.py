class Solution:
    def reverseWords(self, s: str) -> str:

        s = list(s)

        i = 0
        j = 0

        while j < len(s) + 1:
            if j == len(s) or s[j] == ' ':
                s[i: j] = s[i: j][::-1]
                i = j + 1
            j += 1

        return ''.join(s)
