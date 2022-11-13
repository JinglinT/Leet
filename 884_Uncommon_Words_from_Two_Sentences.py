class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:

        counter1 = Counter(s1.split())
        counter2 = Counter(s2.split())

        res = []

        for k, v in counter1.items():
            if k not in counter2 and v == 1:
                res.append(k)

        for k, v in counter2.items():
            if k not in counter1 and v == 1:
                res.append(k)

        return res
