class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        def helper(step):
            if step == 0 or step == 1:
                return 0
            if memo[step] != None:
                return memo[step]

            c1 = helper(step - 1)
            c2 = helper(step - 2)

            memo[step] = min(c1 + cost[step - 1], c2 + cost[step - 2])

            return memo[step]

        memo = [None] * (len(cost) + 1)

        return helper(len(cost))
