class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        
        return res

    def decode(self, s: str) -> List[str]:
        res = []

        i = 0
        '''
        "5#Hello5#World
        i = 0
        j = 1
        len = 5
        res.append(s[1: 6])
        i = 0 + 5
        '''
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            print(s[j])
            length = int(s[i:j])
            print(length)
            res.append(s[j+1:j+length+1])
            print(res)

            i = j + length + 1
            print(i)
        return res
