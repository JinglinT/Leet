class Solution:
    def toHexspeak(self, num: str) -> str:

        hex_map = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D',
                   'e': 'E', 'f': 'F', '1': 'I', '0': 'O'}

        res = []

        for ch in hex(int(num))[2:]:
            if ch in hex_map:
                res.append(hex_map[ch])
            else:
                return 'ERROR'

        return ''.join(res)
