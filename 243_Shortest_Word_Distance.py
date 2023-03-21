class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        i1 = None
        i2 = None
        shortest = float('inf')

        for i in range(len(wordsDict)):
            if wordsDict[i] == word1 or wordsDict[i] == word2:
                if wordsDict[i] == word1:
                    i1 = i
                else:
                    i2 = i

                if i1 != None and i2 != None:
                    distance = abs(i1 - i2)
                    if distance < shortest:
                        shortest = distance

        return shortest
