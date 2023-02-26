class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        copiedChars = 0
        readChars = 4
        buf4 = [0] * 4
        while readChars == 4:
            readChars = read4(buf4)
            for i in range(readChars):
                if copiedChars == n:
                    return copiedChars
                buf[copiedChars] = buf4[i]
                copiedChars += 1
        return copiedChars
