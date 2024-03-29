class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for bracket in s:
            if bracket in hashmap:
                stack.append(bracket)
            elif not stack or hashmap[stack.pop()] != bracket:
                return False
        return not stack
