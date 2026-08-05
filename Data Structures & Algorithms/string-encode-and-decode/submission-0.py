class Solution:
    def encode(self, strs: List[str]) -> str:
        '''
        Maybe Length + # + Word
        Hello World = 5#Hello4#Word
        '''
        res = ""
        for word in strs:
            res += str(len(word)) + "#" + word
        return res
    def decode(self, s: str) -> List[str]:
        '''
        # tells me a new word is coming.
        the number right before the # tells me how long the word is after the #
        '''
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])

            i = j + 1

            word = s[i:i + length]
            res.append(word)

            i += length
        return res

        

