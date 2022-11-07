class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:

        morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
                 "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        letters = 'abcdefghijklmnopqrstuvwxyz'
        letter_morse = dict(zip(letters, morse))

        res = set()

        for w in words:
            code = []
            for ch in w:
                code.append(letter_morse[ch])
            res.add(''.join(code))

        return len(res)
