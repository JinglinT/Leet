class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        s_list = s.split(' ')

        if len(pattern) != len(s_list):
            return False

        map_p_s = {}
        map_s_p = {}

        for i in range(len(pattern)):
            if pattern[i] not in map_p_s and s_list[i] not in map_s_p:
                map_p_s[pattern[i]] = s_list[i]
                map_s_p[s_list[i]] = pattern[i]
            elif map_p_s.get(pattern[i]) != s_list[i]:
                return False

        return True
