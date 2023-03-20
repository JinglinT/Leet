class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letter_count_s = collections.Counter(s)
        letter_count_t = collections.Counter(t)

        return letter_count_s == letter_count_t
