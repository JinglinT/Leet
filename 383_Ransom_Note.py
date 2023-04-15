class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        chr_count = collections.Counter(magazine)

        for n in ransomNote:
            if chr_count[n] > 0:
                chr_count[n] -= 1
            else:
                return False

        return True
