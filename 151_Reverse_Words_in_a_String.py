class Solution:
    def reverseWords(self, s: str) -> str:

        def trim_spaces(s):
            output = []
            left = 0
            right = len(s) - 1
            while left < len(s) and s[left] == ' ':
                left += 1
            while right > -1 and s[right] == ' ':
                right -= 1
            while left <= right:
                if s[left] != ' ':
                    output.append(s[left])
                elif output[-1] != ' ':
                    output.append(s[left])
                left += 1
            return output

        def reverse(lst, left, right):
            while left < right:
                lst[left], lst[right] = lst[right], lst[left]
                left += 1
                right -= 1

        def reverse_each_word(lst):
            start = end = 0
            while end < len(lst):
                while end < len(lst) and lst[end] != ' ':
                    end += 1
                reverse(lst, start, end - 1)
                start = end + 1
                end = start

        res = trim_spaces(s)
        reverse(res, 0, len(res) - 1)
        reverse_each_word(res)

        return ''.join(res)
