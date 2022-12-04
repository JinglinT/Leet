class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:

        charCounter = Counter(chars)

        res = 0

        for w in words:
            if Counter(w) <= charCounter:
                res += len(w)

        return res
