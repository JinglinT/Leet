class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.total = 0
        self.q = collections.deque()

    def next(self, val: int) -> float:
        self.q.append(val)
        self.total += val
        if len(self.q) > self.size:
            self.total -= self.q.popleft()
        return self.total / len(self.q)
