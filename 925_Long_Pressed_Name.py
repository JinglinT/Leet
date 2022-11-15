class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:

        i = j = 0
        curr = name[0]

        while i < len(name) or j < len(typed):
            if i < len(name) and j < len(typed) and typed[j] == name[i]:
                curr = name[i]
                i += 1
                j += 1
            elif j < len(typed) and typed[j] == curr:
                j += 1
            else:
                return False

        return True
