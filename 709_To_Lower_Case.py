class Solution:
    def toLowerCase(self, s: str) -> str:

        upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        lower = 'abcdefghijklmnopqrstuvwxyz'
        dic = dict(zip(upper, lower))

        res = []
        for ch in s:
            if ch in dic:
                res.append(dic[ch])
            else:
                res.append(ch)

        return ''.join(res)
