class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:

        counter = Counter(deck)

        minCount = min(counter.values())

        factors = []

        for n in range(2, minCount + 1):
            if minCount % n == 0:
                factors.append(n)

        for x in factors:
            if all(v % x == 0 for v in counter.values()):
                return True

        return False
