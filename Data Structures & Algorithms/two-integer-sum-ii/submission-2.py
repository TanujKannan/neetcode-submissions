class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1


        while l < r:
            sumTwo = numbers[l] + numbers[r]
            if sumTwo == target:
                return [l+1, r + 1]
            elif sumTwo < target:
                l += 1
            else:
                r -= 1
        
        return [-1, -1]
        