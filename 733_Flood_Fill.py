class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        if image[sr][sc] == color:
            return image

        m = len(image)
        n = len(image[0])
        origin_color = image[sr][sc]

        stack = [(sr, sc)]

        while stack:
            i, j = stack.pop()

            if image[i][j] == origin_color:
                image[i][j] = color
                if i - 1 > -1:
                    stack.append((i - 1, j))
                if i + 1 < m:
                    stack.append((i + 1, j))
                if j - 1 > -1:
                    stack.append((i, j - 1))
                if j + 1 < n:
                    stack.append((i, j + 1))

        return image
