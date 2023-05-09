class Solution:
    def constructRectangle(self, area: int) -> List[int]:

        sqrt_root = floor(math.sqrt(area))

        for divisor in range(sqrt_root, 0, -1):
            if area % divisor == 0:
                return [area // divisor, divisor]
