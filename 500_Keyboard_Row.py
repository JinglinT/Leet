class Solution:
    def findWords(self, words: List[str]) -> List[str]:

        first = set("qwertyuiop")
        second = set("asdfghjkl")
        third = set("zxcvbnm")

        res = []

        for w in words:
            s = w.lower()
            i = 0
            if s[0] in first:
                while i < len(s):
                    if s[i] not in first:
                        break
                    i += 1
            elif s[0] in second:
                while i < len(s):
                    if s[i] not in second:
                        break
                    i += 1
            else:
                while i < len(s):
                    if s[i] not in third:
                        break
                    i += 1
            if i == len(s):
                res.append(w)

        return res
