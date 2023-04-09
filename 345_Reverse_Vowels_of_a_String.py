class Solution:
    def reverseVowels(self, s: str) -> str:

        chrs = list(s)
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        i, j = 0, len(s) - 1

        while i < j:
            if chrs[i] in vowels and chrs[j] in vowels:
                chrs[i], chrs[j] = chrs[j], chrs[i]
                i += 1
                j -= 1
            while i < j and chrs[i] not in vowels:
                i += 1
            while i < j and chrs[j] not in vowels:
                j -= 1

        return ''.join(chrs)
