class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        length = len(needle)
        base = 255
        lb = base ** (length - 1)

        patHash = 0
        for ch in needle:
            patHash = patHash * base + ord(ch)

        windowHash = 0

        left = right = 0

        while right < len(haystack):
            windowHash = windowHash * base + ord(haystack[right])

            right += 1

            if right - left == length:
                if windowHash == patHash:
                    return left

                windowHash = windowHash - ord(haystack[left]) * lb

                left += 1

        return -1
