class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        need = Counter(s1)
        count_need = len(need)

        window = {}
        count_window = 0

        left = right = 0

        while right < len(s2):
            c = s2[right]
            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    count_window += 1

            right += 1

            if right - left == len(s1):
                if count_window == count_need:
                    return True

                c = s2[left]
                if c in need:
                    if window[c] == need[c]:
                        count_window -= 1
                    window[c] -= 1

                left += 1

        return False
