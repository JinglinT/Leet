class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:

        unique = len(set(candyType))
        half = len(candyType) // 2

        return min(unique, half)
