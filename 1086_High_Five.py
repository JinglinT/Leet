import heapq


class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:

        dic = dict()

        for item in items:
            if item[0] not in dic:
                dic[item[0]] = [item[1]]
            else:
                heapq.heappush(dic[item[0]], item[1])
                if len(dic[item[0]]) > 5:
                    heappop(dic[item[0]])

        res = []

        for k, v in dic.items():
            res.append([k, sum(v) // 5])

        res.sort()

        return res
