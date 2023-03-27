class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        chr_count = collections.Counter(s)

        middleChr = 0
        for v in chr_count.values():
            if v % 2 != 0:
                middleChr += 1
                if middleChr > 1:
                    return False

        return True
