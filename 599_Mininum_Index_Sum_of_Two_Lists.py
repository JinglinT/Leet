class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:

        res = []
        least = float('inf')
        word_index = {}

        for i, w in enumerate(list1):
            word_index[w] = i

        for i, w in enumerate(list2):
            if w in word_index:
                index_sum = i + word_index[w]
                if index_sum == least:
                    res.append(w)
                elif index_sum < least:
                    least = index_sum
                    res = [w]

        return res
