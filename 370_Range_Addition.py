class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:

        diff = [0] * length

        for update in updates:
            diff[update[0]] += update[2]
            if update[1] + 1 < length:
                diff[update[1] + 1] -= update[2]

        res = [0] * length

        res[0] = diff[0]

        for i in range(1, len(res)):
            res[i] = res[i - 1] + diff[i]

        return res
