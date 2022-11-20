class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:

        number = 0

        for n in num:
            number = number * 10 + n

        number += k

        res = []

        while number > 0:
            res.append(number % 10)
            number //= 10

        res.reverse()

        return res
