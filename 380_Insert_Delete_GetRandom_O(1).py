class RandomizedSet:

    def __init__(self):
        self.lst = []
        self.dic = {}

    def insert(self, val: int) -> bool:
        if val in self.dic:
            return False

        self.dic[val] = len(self.lst)
        self.lst.append(val)

        return True

    def remove(self, val: int) -> bool:
        if val not in self.dic:
            return False

        newIndexForlastElement, lastElement = self.dic[val], self.lst[-1]

        self.lst[newIndexForlastElement] = lastElement
        self.dic[lastElement] = newIndexForlastElement

        self.lst.pop()
        self.dic.pop(val)

        return True

    def getRandom(self) -> int:
        return random.choice(self.lst)
