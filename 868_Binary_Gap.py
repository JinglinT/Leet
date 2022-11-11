class Solution:
    def binaryGap(self, n: int) -> int:

        bitString = f'{n:b}'
        prev = None
        maxDis = 0

        for i in range(len(bitString)):
            if bitString[i] == '1':
                if prev != None:
                    maxDis = max(maxDis, i - prev)
                prev = i

        return maxDis
