class Solution:
    def checkRecord(self, s: str) -> bool:

        count_L = 0
        count_A = 0

        for ch in s:
            if ch == 'A':
                count_A += 1
                count_L = 0
                if count_A >= 2:
                    return False
            elif ch == 'L':
                count_L += 1
                if count_L >= 3:
                    return False
            else:
                count_L = 0

        return True
