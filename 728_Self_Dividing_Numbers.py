class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:

        def isSelfDividing(n):
            for d in str(n):
                if d == '0' or n % int(d) != 0:
                    return False
            return True

        res = []

        for n in range(left, right + 1):
            if isSelfDividing(n):
                res.append(n)

        return res
