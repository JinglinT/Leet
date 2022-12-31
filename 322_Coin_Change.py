class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [None] * (amount + 1)

        dp[0] = 0

        for i in range(1, len(dp)):
            minCount = float('inf')

            for c in coins:
                if i - c < 0:
                    continue

                if dp[i - c] == -1:
                    continue

                minCount = min(minCount, dp[i - c] + 1)

            dp[i] = minCount if minCount != float('inf') else -1

        return dp[-1]
