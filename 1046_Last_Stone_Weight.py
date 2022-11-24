import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        for i in range(len(stones)):
            stones[i] *= -1

        heapq.heapify(stones)

        while len(stones) > 1:
            y = heapq.heappop(stones)
            x = heapq.heappop(stones)

            if y - x < 0:
                heapq.heappush(stones, y - x)

        if stones:
            return abs(stones[0])
        return 0
