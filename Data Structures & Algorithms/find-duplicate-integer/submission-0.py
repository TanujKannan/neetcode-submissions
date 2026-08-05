class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        Map each number to an index: num - 1
        Everrytime you see a new number, go to that index and make the value -ve
        If you go to the index and it's already -ve, then it's a duplicate
        and you can return the number.
        But return abs since the num itself may have been made negative.
        '''
        for num in nums:
            idx = abs(num) - 1
            if nums[idx] < 0:
                return abs(num)
            nums[idx] *= -1
        
        return -1
        

        