class Solution:
    def removeOuterParentheses(self, s: str) -> str:

        stack = []
        res = []

        for ch in s:
            if ch == '(':
                if len(stack) > 0:
                    res.append(ch)
                stack.append(ch)
            else:
                if len(stack) > 1:
                    res.append(ch)
                stack.pop()

        return ''.join(res)
