class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        words = []

        i = 0

        while i < len(paragraph):
            if paragraph[i].isalpha():
                for j in range(i + 1, len(paragraph) + 1):
                    if j == len(paragraph) or not paragraph[j].isalpha():
                        words.append(paragraph[i: j].lower())
                        i = j + 1
                        break
            else:
                i += 1

        wordsCount = collections.Counter(words)
        banSet = set(banned)
        count = 0
        res = None

        for k, v in wordsCount.items():
            if not k in banSet and v > count:
                count = v
                res = k

        return res
