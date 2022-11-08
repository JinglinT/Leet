class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:

        lineCount = 1
        lineLen = 0

        for ch in s:
            newLen = widths[ord(ch) - ord('a')]
            if lineLen + newLen > 100:
                lineCount += 1
                lineLen = newLen
            else:
                lineLen += newLen

        return [lineCount, lineLen]
