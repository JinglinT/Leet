class Solution:
    def validWordSquare(self, words: List[str]) -> bool:

        for i in range(len(words)):

            col = ''

            for s in words:
                if i < len(s):
                    col += s[i]
                else:
                    break

            if col != words[i]:
                return False

        return True
