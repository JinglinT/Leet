class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:

        if len(s) != len(goal):
            return False

        diffCount = 0
        diffS = None
        diffGoal = None
        seen = set()
        dupCharCount = 0

        for i in range(len(s)):

            if s[i] != goal[i]:
                diffCount += 1

                if diffCount == 3:
                    return False
                if diffCount == 2:
                    if diffS != goal[i] or diffGoal != s[i]:
                        return False
                else:
                    diffS = s[i]
                    diffGoal = goal[i]

            if s[i] in seen:
                dupCharCount += 1
            else:
                seen.add(s[i])

        if diffCount == 1:
            return False
        if diffCount == 0 and dupCharCount == 0:
            return False
        return True
