class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        result = strs[0]
        for i in range(1, len(strs)):
            for j in range(len(result)):
                if j >= len(strs[i]) or result[j] != strs[i][j]:
                    result = result[0: j]
                    break
            if not result:
                return result
        return result
