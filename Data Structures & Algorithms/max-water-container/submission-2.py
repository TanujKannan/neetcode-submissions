'''
Given array of integers, each representing the height of a bar.

We can choose two bars to form a container, basically some area of the rectangle
formed.

We want to return the maximum amount of water -> Max area of rectangle formed.

Logic is to use two pointers. We have to reduce width at any given moment, 
so it makes sense to move the pointer at a lower height in the hopes of finding
something higher.
'''
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1

        maxArea = 0

        while l < r:
            #minHeightxwidth
            curArea = min(heights[l], heights[r]) * (r - l)
            maxArea = max(curArea, maxArea)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return maxArea
        