class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        counter = Counter(arr)

        if len(set(counter.values())) < len(counter):
            return False

        return True
