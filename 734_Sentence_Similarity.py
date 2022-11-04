class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:

        if len(sentence1) != len(sentence2):
            return False

        pairs = set((x, y) for x, y in similarPairs)

        for word1, word2 in zip(sentence1, sentence2):
            if (word1, word2) in pairs or (word2, word1) in pairs or word1 == word2:
                continue
            return False

        return True
