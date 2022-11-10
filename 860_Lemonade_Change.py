class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        changes = {5: 0, 10: 0}

        for pay in bills:

            if pay == 20:
                if changes[10] > 0:
                    changes[10] -= 1
                    if changes[5] < 1:
                        return False
                    changes[5] -= 1
                else:
                    if changes[5] < 3:
                        return False
                    changes[5] -= 3

            elif pay == 10:
                if changes[5] < 1:
                    return False
                changes[5] -= 1
                changes[10] += 1

            else:
                changes[5] += 1

        return True
