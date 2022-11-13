class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:

        aSum = sum(aliceSizes)
        bSum = sum(bobSizes)
        average = (aSum + bSum) // 2

        bSet = set(bobSizes)

        for size in aliceSizes:
            exchange = average - (aSum - size)
            if exchange in bSet:
                return (size, exchange)
