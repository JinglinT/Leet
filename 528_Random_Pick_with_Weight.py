class Solution:

    def __init__(self, w: List[int]):
        self.preSum = [0] * (len(w) + 1)
        for i in range(1, len(self.preSum)):
            self.preSum[i] = self.preSum[i - 1] + w[i - 1]

    def pickIndex(self) -> int:
        target = randint(1, self.preSum[-1])
        return bisect_left(self.preSum, target) - 1
