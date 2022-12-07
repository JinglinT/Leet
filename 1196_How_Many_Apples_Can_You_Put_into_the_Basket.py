class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:

        weight.sort()

        total = 0
        count = 0

        for w in weight:
            total += w
            if total <= 5000:
                count += 1
            else:
                break

        return count
