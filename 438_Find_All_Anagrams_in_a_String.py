class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        need = Counter(p)
        count_need = len(need)

        window = {}
        count_window = 0

        left = right = 0

        res = []

        while right < len(s):
            c = s[right]
            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    count_window += 1

            right += 1

            if right - left == len(p):
                if count_window == count_need:
                    res.append(left)

                c = s[left]
                if c in need:
                    if window[c] == need[c]:
                        count_window -= 1
                    window[c] -= 1

                left += 1

        return res
