class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = []
        carry = 0
        i = len(num1) - 1
        j = len(num2) - 1

        while i > -1 or j > -1:
            d1 = 0 if i <= -1 else ord(num1[i]) - ord('0')
            d2 = 0 if j <= -1 else ord(num2[j]) - ord('0')

            carry = carry + d1 + d2

            res.append(carry % 10)

            carry //= 10

            i -= 1
            j -= 1

        if carry > 0:
            res.append(carry)

        res.reverse()

        return ''.join([str(x) for x in res])
