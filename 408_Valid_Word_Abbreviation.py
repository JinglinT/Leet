class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:

        i = j = 0

        while i < len(word) and j < len(abbr):
            if word[i] == abbr[j]:
                i += 1
                j += 1
            else:
                if abbr[j].isnumeric() and abbr[j] != '0':
                    num = ''
                    while j < len(abbr) and abbr[j].isnumeric():
                        num += abbr[j]
                        j += 1
                    num = int(num)
                    i += num
                else:
                    return False

        return i == len(word) and j == len(abbr)
