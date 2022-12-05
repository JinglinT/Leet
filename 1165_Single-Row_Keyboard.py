class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:

        dic = {}

        for i, v in enumerate(keyboard):
            dic[v] = i

        res = dic[word[0]]

        for i in range(len(word) - 1):
            res += abs(dic[word[i]] - dic[word[i + 1]])

        return res
