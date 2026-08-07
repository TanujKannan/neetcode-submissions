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
        tallest_to_left = [0]*len(height)
        tallest_to_right = [0]*len(height)

        tallest_to_left[0] = height[0]
        tallest_to_right[-1] = height[-1]

        for i in range(1, len(height)):
            tallest_to_left[i] = max(tallest_to_left[i-1], height[i-1])
        
        for i in range(len(height) - 2, -1, -1):
            tallest_to_right[i] = max(tallest_to_right[i+1], height[i+1])


        res = 0
        for i in range(len(height)):
            curHeight = height[i]
            minOfLeftRight = min(tallest_to_left[i], tallest_to_right[i])
            waterOnTop = max(0, minOfLeftRight - curHeight)
            res += waterOnTop
        
        return res
        