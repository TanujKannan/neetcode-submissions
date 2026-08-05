class Solution:
    def countBits(self, n: int) -> List[int]:
        def countOnes(num):
            count = 0
            while num:
                num = num & (num - 1)
                count += 1
            return count
        
        output = []
        for num in range(n+1):
            output.append(countOnes(num))
        
        return output
        