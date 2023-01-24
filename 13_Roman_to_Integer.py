class Solution:
    def romanToInt(self, s: str) -> int:
        convert = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0
        for i in range(0, len(s) - 1):
            if convert[s[i]] < convert[s[i + 1]]:
                result -= convert[s[i]]
            else:
                result += convert[s[i]]
        return result + convert[s[-1]]
