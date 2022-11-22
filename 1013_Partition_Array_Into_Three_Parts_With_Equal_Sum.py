class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:

        total = sum(arr)

        if total % 3 != 0:
            return False

        partSum = total // 3
        part = 0
        count = 0
        i = 0

        for i in range(len(arr)):
            part += arr[i]
            if part == partSum:
                count += 1
                part = 0

        return count >= 3
