'''
Given array of non-neg integers, which represent an elevation map.
Each value is a height of a bar, which have a width of 1.

Want to return the max area of water that can be trapped between the bars.

When can water sit on top of one bar?
    -> Only when there are two bars to left and right that are taller.

What's the amount of water that sits on top of one such bar?
    -> Diff between it's height and min(height of two tallest to left and right)
    -> sum over all amounts of water over each bar to get total area

Question is how to get tallest to left and right for each bar efficiently?
    -> Prefix Suffix arrays
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        '''
        Do I need these two extra arrays? 
        Can I just keep track of two variables? 
        One to represent max to left and one for right?
        '''
        tallest_to_left = height[0]
        tallest_to_right = height[-1]

        res = 0
        l = 0
        r = len(height) - 1

        while l < r:
            if tallest_to_left <= tallest_to_right:
                l += 1
                tallest_to_left = max(tallest_to_left, height[l])
                res += max(0, tallest_to_left - height[l])
            else:
                r -= 1
                tallest_to_right = max(tallest_to_right, height[r])
                res += max(0, tallest_to_right - height[r])
        
        return res
        