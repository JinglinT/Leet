class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:

        dic = Counter()

        for d in dominoes:
            dic[tuple(sorted(d))] += 1

        res = 0

        for v in dic.values():
            if v > 1:
                # res += math.factorial(v) // (math.factorial(v - 2) * math.factorial(2))
                res += (v - 1) * v // 2

        return res
