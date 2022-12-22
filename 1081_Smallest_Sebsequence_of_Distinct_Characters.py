class Solution:
    def smallestSubsequence(self, s: str) -> str:

        lastIndexOfCh = {ch: i for i, ch in enumerate(s)}

        added = set()

        stack = []

        for i in range(len(s)):
            if s[i] not in added:

                while stack and stack[-1] > s[i] and lastIndexOfCh[stack[-1]] > i:
                    added.remove(stack[-1])
                    stack.pop()

                added.add(s[i])
                stack.append(s[i])

        return ''.join(stack)
