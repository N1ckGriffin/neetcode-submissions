class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for i in range(len(heights)):
            start = i
            while stack and heights[i] < stack[-1][1]:
                l, h = stack.pop()
                maxArea = max(maxArea, (i - l) * h)
                start = l
            stack.append((start, heights[i]))

        while stack:
            l, h = stack.pop()
            maxArea = max(maxArea, (len(heights) - l) * h)
        
        return maxArea