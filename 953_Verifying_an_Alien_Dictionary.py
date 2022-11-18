class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        dic = {}

        for i in range(len(order)):
            dic[order[i]] = i

        def lessThanOrEqualTo(w1, w2):
            i = 0
            while i < len(w1) and i < len(w2):
                if dic[w1[i]] < dic[w2[i]]:
                    return True
                elif dic[w1[i]] > dic[w2[i]]:
                    return False
                i += 1
            return i == len(w1)

        for i in range(len(words) - 1):
            if not lessThanOrEqualTo(words[i], words[i + 1]):
                return False

        return True
