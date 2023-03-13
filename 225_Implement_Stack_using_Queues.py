class MyStack:

    def __init__(self):
        self.q1 = collections.deque()
        self.q2 = collections.deque()
        self.topValue = None

    def push(self, x: int) -> None:
        self.q1.append(x)
        self.topValue = x

    def pop(self) -> int:
        while len(self.q1) > 1:
            self.topValue = self.q1.popleft()
            self.q2.append(self.topValue)

        res = self.q1.popleft()

        if len(self.q2) == 0:
            topValue = None

        self.q1, self.q2 = self.q2, self.q1

        return res

    def top(self) -> int:
        return self.topValue

    def empty(self) -> bool:
        return len(self.q1) == 0
