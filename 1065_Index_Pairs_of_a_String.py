class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:

        res = []

        for w in words:
            i = 0
            while True:
                i = text.find(w, i)
                if i > -1:
                    res.append([i, i + len(w) - 1])
                    i += 1
                else:
                    break

        res.sort()

        return res
