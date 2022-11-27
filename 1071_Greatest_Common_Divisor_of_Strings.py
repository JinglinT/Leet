class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        if len(str1) < len(str2):
            return self.gcdOfStrings(str2, str1)

        for i in range(len(str2), 0, -1):
            if len(str1) % i == 0 and len(str2) % i == 0 and \
                    len(str1) // i * str2[:i] == str1 and len(str2) // i * str2[:i] == str2:
                return str2[:i]

        return ''
