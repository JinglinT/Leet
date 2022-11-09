class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:

        for lst in image:
            for i in range((len(lst) + 1) // 2):
                lst[i], lst[~i] = lst[~i] ^ 1, lst[i] ^ 1

        return image
