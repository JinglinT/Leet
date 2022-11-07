class Solution:
    def rotateString(self, s: str, goal: str) -> bool:

        def computeLPS(pat):
            lps = [0] * len(pat)
            i = 0
            j = 1
            while j < len(pat):
                if pat[i] == pat[j]:
                    lps[j] = i + 1
                    i += 1
                    j += 1
                else:
                    if i == 0:
                        j += 1
                    else:
                        i = lps[i - 1]
            return lps

        def kmp(pat, text):
            lps = computeLPS(pat)
            i = 0
            j = 0
            while i < len(text) and j < len(pat):
                if text[i] == pat[j]:
                    i += 1
                    j += 1
                else:
                    if j == 0:
                        i += 1
                    else:
                        j = lps[j - 1]
            if j == len(pat):
                return True
            return False

        return len(s) == len(goal) and kmp(s, goal + goal)
