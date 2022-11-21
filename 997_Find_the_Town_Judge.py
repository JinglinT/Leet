class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        dic = defaultdict(set)

        for pair in trust:
            dic[pair[0]].add(pair[1])

        if len(dic) != n - 1:
            return -1

        judge = None

        for i in range(1, n + 1):
            if i not in dic:
                judge = i

        for v in dic.values():
            if judge not in v:
                return -1

        return judge
