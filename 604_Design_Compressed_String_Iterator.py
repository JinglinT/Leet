class StringIterator:

    def __init__(self, compressedString: str):
        self.s = compressedString
        self.p = 0
        self.num = 0
        self.curr = None

    def next(self) -> str:
        if not self.hasNext():
            return ' '
        if self.num == 0:
            self.curr = self.s[self.p]
            self.p += 1
            while self.p < len(self.s) and self.s[self.p].isnumeric():
                self.num = self.num * 10 + int(self.s[self.p])
                self.p += 1
        self.num -= 1
        return self.curr

    def hasNext(self) -> bool:
        return not self.p == len(self.s) or not self.num == 0
