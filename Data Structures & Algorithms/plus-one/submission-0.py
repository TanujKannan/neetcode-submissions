class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        res = []
        i = len(digits) - 1 

        while i >= 0:
            sumTwo = digits[i] + carry
            carry = sumTwo // 10
            res.append(sumTwo%10)
            i -= 1
        
        if carry:
            res.append(carry)
        
        return res[::-1]
        