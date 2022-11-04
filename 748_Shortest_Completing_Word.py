class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:

        dic = collections.defaultdict(int)

        for ch in licensePlate:
            if ch.isalpha():
                dic[ch.lower()] += 1

        shortest = float('inf')
        res = None

        for w in words:
            if len(w) < shortest:
                dic_copy = dic.copy()
                for ch in w:
                    if ch in dic_copy:
                        dic_copy[ch] -= 1
                        if dic_copy[ch] == 0:
                            dic_copy.pop(ch)
                        if not dic_copy:
                            shortest = len(w)
                            res = w
                            continue

        return res
