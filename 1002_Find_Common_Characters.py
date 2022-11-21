class Solution:
    def commonChars(self, words: List[str]) -> List[str]:

        counter = Counter(words[0])

        for i in range(1, len(words)):
            counter = counter & Counter(words[i])
            if not counter:
                break

        res = []

        for k, v in counter.items():
            res.extend([k] * v)

        return res
