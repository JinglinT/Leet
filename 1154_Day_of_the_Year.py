class Solution:
    def dayOfYear(self, date: str) -> int:

        year, month, day = [int(x) for x in date.split('-')]

        daysOfMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]

        res = day

        if month > 2:
            if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
                res += 1

        for i in range(month - 1):
            res += daysOfMonth[i]

        return res
