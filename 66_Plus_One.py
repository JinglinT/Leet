class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] == 9:
            for i in (range(len(digits) - 1, -1, -1)):
                if digits[i] == 9:
                    digits[i] = 0
                    i -= 1
                else:
                    digits[i] += 1
                    return digits
            digits.insert(0, 1)
        else:
            digits[-1] += 1
        return digits
