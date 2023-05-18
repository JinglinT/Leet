class Solution:
    def checkPerfectNumber(self, num: int) -> bool:

        total = 0

        for n in range(1, ceil(math.sqrt(num))):
            if num % n == 0:
                total += n
                total += num // n

        return total - num == num
