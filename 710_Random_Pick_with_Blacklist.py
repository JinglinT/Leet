class Solution:

    def __init__(self, n: int, blacklist: List[int]):

        self.dic = {}

        for b in blacklist:
            self.dic[b] = None

        self.startOfBlackListZone = n - len(blacklist)

        j = n - 1

        for b in blacklist:
            if b >= self.startOfBlackListZone:
                continue

            while j in self.dic:
                j -= 1

            self.dic[b] = j
            j -= 1

    def pick(self) -> int:
        r = random.randint(0, self.startOfBlackListZone - 1)

        if r in self.dic:
            return self.dic[r]

        return r
