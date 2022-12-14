class Solution:
    def minWindow(self, s: str, t: str) -> str:

        need = Counter(t)
        count_need = len(need)

        window = {}
        count_window = 0

        left = 0
        right = 0
        res = (float('inf'), None, None)

        while right < len(s):
            if s[right] in need:
                window[s[right]] = window.get(s[right], 0) + 1
                if window[s[right]] == need[s[right]]:
                    count_window += 1

            right += 1

            while count_window == count_need:
                if right - left < res[0]:
                    res = (right - left, left, right)

                if s[left] in need:
                    window[s[left]] -= 1
                    if window[s[left]] < need[s[left]]:
                        count_window -= 1

                left += 1

        return s[res[1]:res[2]] if res[0] < float('inf') else ''
