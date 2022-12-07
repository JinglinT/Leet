class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        dic1 = {'b': 0, 'a': 0, 'n': 0}
        dic2 = {'l': 0, 'o': 0}

        for ch in text:
            if ch in dic1:
                dic1[ch] += 1
            elif ch in dic2:
                dic2[ch] += 1

        return min(min(dic1.values()), min(dic2.values()) // 2)
