class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            #Get last bit of n
            last_bit = n & 1

            #Shift res to the left to make room
            res = res << 1

            #Insert the last bit into res
            res = res | last_bit

            #Shift n to the right
            n = n >> 1
        return res

        