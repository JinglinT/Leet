class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:

        res = 0
        total = 0

        for i in range(k):
            total += calories[i]

        if total < lower:
            res -= 1
        if total > upper:
            res += 1

        for i in range(k, len(calories)):
            total += calories[i]
            total -= calories[i - k]
            if total < lower:
                res -= 1
            if total > upper:
                res += 1

        return res
