class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def backspaceDone(string):
            stack = []
            for ch in string:
                if ch != '#':
                    stack.append(ch)
                elif stack:
                    stack.pop()
            return stack

        return backspaceDone(s) == backspaceDone(t)
